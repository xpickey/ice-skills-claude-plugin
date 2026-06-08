#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
embed_fonts_pptx.py — PowerPoint-SAFE font embedding for .pptx (TH+EN decks)

WHY THIS EXISTS
  python-pptx cannot embed fonts. The naive manual approach (inject ppt/fonts/*.fntdata +
  <p:embeddedFontLst> into presentation.xml) opens fine in LibreOffice but makes PowerPoint
  show "found a problem with content … Repair" because PowerPoint STRICTLY validates the
  ECMA-376 CT_Presentation child-element ORDER, while LibreOffice is lenient.

ROOT CAUSE of the bug we hit (2026.06.03):
  <p:embeddedFontLst> was inserted BEFORE <p:sldSz>. ECMA-376 CT_Presentation requires:
      sldMasterIdLst? notesMasterIdLst? handoutMasterIdLst? sldIdLst?
      sldSz? notesSz? smartTags? embeddedFontLst? custShowLst? photoAlbum?
      custDataLst? kinsoku? defaultTextStyle? modifyVerifier? extLst?
  => embeddedFontLst MUST come AFTER notesSz and BEFORE custShowLst/defaultTextStyle.

WHAT POWERPOINT WANTS (verified against MS-OE376):
  - content type  : application/x-fontdata   (NOT x-font-ttf; NOT obfuscatedFont — that's Word only)
  - font binary   : RAW TrueType/OpenType .ttf bytes, NOT obfuscated (only Word obfuscates)
  - extension     : .fntdata
  - relationship  : type .../officeDocument/2006/relationships/font
  - presentation  : embedTrueTypeFonts="1" on <p:presentation>, plus <p:embeddedFontLst> in
                    the CORRECT schema slot (after notesSz).
  - <p:embeddedFont> entries support <p:regular> <p:bold> <p:italic> <p:boldItalic> r:id refs.

USAGE
  python3 embed_fonts_pptx.py INPUT.pptx OUTPUT.pptx \
      --font "Open Sans:regular=/path/OpenSans-Regular.ttf,bold=/path/OpenSans-Bold.ttf" \
      --font "Sarabun:regular=/path/Sarabun-Regular.ttf,bold=/path/Sarabun-Bold.ttf"
  Then validate:
  python3 validate_pptx_fonts.py OUTPUT.pptx
"""
import zipfile, shutil, os, re, sys, argparse, tempfile

REL_FONT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"
# CT_Presentation canonical order; embeddedFontLst sits right after notesSz/smartTags.
# We insert it before the FIRST of these (whichever exists), else before </p:presentation>.
AFTER_ELEMENTS_PRIORITY = ["smartTags","notesSz","sldSz","sldIdLst"]  # insert AFTER the first found (search in this order)
BEFORE_ELEMENTS = ["custShowLst","photoAlbum","custDataLst","kinsoku","defaultTextStyle","modifyVerifier","extLst"]

def parse_font_arg(s):
    """'Family:regular=/p/a.ttf,bold=/p/b.ttf' -> ('Family', {'regular':..,'bold':..})"""
    fam, rest = s.split(":",1)
    styles={}
    for kv in rest.split(","):
        k,v=kv.split("=",1); styles[k.strip()]=v.strip()
    return fam.strip(), styles

def normalize_font(src, dst):
    """
    CRITICAL FIX (PrimeZone 2026.06.03): PowerPoint rejects some otherwise-valid TTFs at
    embed time with 'Install Embedded Fonts: <Family> — General Failure', then strips them.
    Observed with a Sarabun static TTF whose fsType was Installable and name table clean.
    A fontTools round-trip re-save NORMALIZES the sfnt (rebuilds table directory + checksums,
    drops embedder-hostile remnants) and makes PowerPoint accept it.
    Also instances Variable fonts to a static default (Variable fonts cannot be embedded).
    Returns dst path. Requires: pip install fonttools
    """
    from fontTools.ttLib import TTFont
    f = TTFont(src)
    # If Variable, instance to default (PowerPoint cannot embed variable fonts)
    if "fvar" in f:
        try:
            from fontTools.varLib.instancer import instantiateVariableFont
            axes = {a.axisTag: a.defaultValue for a in f["fvar"].axes}
            instantiateVariableFont(f, axes, inplace=True)
        except Exception as e:
            print(f"  WARN: variable-font instancing failed for {src}: {e}", file=sys.stderr)
    f.save(dst)   # fontTools rebuilds a clean sfnt
    f.close()
    return dst

def embed(input_pptx, output_pptx, fonts, normalize=True):
    work=tempfile.mkdtemp(prefix="pptx_embed_")
    normdir=tempfile.mkdtemp(prefix="pptx_fontnorm_")
    try:
        with zipfile.ZipFile(input_pptx) as z: z.extractall(work)

        # 0) NORMALIZE fonts via fontTools round-trip (fixes PowerPoint "General Failure")
        if normalize:
            for fam, styles in fonts.items():
                for style, src in list(styles.items()):
                    if src and os.path.exists(src):
                        base=f"{fam}-{style}".replace(" ","_")+".ttf"
                        dst=os.path.join(normdir, base)
                        try:
                            normalize_font(src, dst); styles[style]=dst
                        except Exception as e:
                            print(f"  WARN: normalize failed {fam} {style}: {e} (using original)", file=sys.stderr)

        # 1) copy font binaries -> ppt/fonts/fontN.fntdata
        fdir=os.path.join(work,"ppt","fonts"); os.makedirs(fdir,exist_ok=True)
        idx=1; fontmap={}; font_files=[]
        for fam,styles in fonts.items():
            fontmap[fam]={}
            for style,src in styles.items():
                if not (src and os.path.exists(src)):
                    print(f"  WARN: {fam} {style}: file not found -> {src}", file=sys.stderr); continue
                fn=f"font{idx}.fntdata"; idx+=1
                shutil.copy(src, os.path.join(fdir,fn))
                fontmap[fam][style]=fn; font_files.append((fn,fam,style))
        if not font_files:
            raise SystemExit("No valid font files found — nothing embedded.")

        # 2) [Content_Types].xml — register fntdata default (PowerPoint: application/x-fontdata)
        ctp=os.path.join(work,"[Content_Types].xml"); ct=open(ctp,encoding="utf-8").read()
        if 'Extension="fntdata"' not in ct:
            ct=ct.replace("</Types>",'<Default Extension="fntdata" ContentType="application/x-fontdata"/></Types>')
            open(ctp,"w",encoding="utf-8").write(ct)

        # 3) ppt/_rels/presentation.xml.rels — add font relationships
        relp=os.path.join(work,"ppt","_rels","presentation.xml.rels"); rs=open(relp,encoding="utf-8").read()
        used=[int(m) for m in re.findall(r'Id="rId(\d+)"',rs)]; nid=(max(used)+1) if used else 1
        rid_for={}; addrel=""
        for fn,fam,style in font_files:
            rid=f"rId{nid}"; nid+=1; rid_for[(fam,style)]=rid
            addrel+=f'<Relationship Id="{rid}" Type="{REL_FONT}" Target="fonts/{fn}"/>'
        rs=rs.replace("</Relationships>",addrel+"</Relationships>"); open(relp,"w",encoding="utf-8").write(rs)

        # 4) ppt/presentation.xml — set embedTrueTypeFonts + insert embeddedFontLst IN CORRECT SLOT
        pp=os.path.join(work,"ppt","presentation.xml"); ps=open(pp,encoding="utf-8").read()
        # 4a. flag on opening tag: embedTrueTypeFonts="1"; and force saveSubsetFonts="0"
        #     (we embed FULL fonts; leaving saveSubsetFonts="1" claims subset → mismatch)
        m=re.search(r'<p:presentation\b[^>]*>', ps); open_tag=m.group(0)
        new_tag=open_tag
        if "embedTrueTypeFonts" not in new_tag:
            new_tag=new_tag[:-1]+' embedTrueTypeFonts="1">'
        if 'saveSubsetFonts="1"' in new_tag:
            new_tag=new_tag.replace('saveSubsetFonts="1"','saveSubsetFonts="0"')
        if new_tag!=open_tag:
            ps=ps.replace(open_tag, new_tag, 1)
        # 4b. build the block
        STYLE_TAG={"regular":"p:regular","bold":"p:bold","italic":"p:italic","boldItalic":"p:boldItalic"}
        def font_block(fam):
            fm=fontmap[fam]; e=f'<p:embeddedFont><p:font typeface="{fam}"/>'
            for style in ("regular","bold","italic","boldItalic"):
                if style in fm: e+=f'<{STYLE_TAG[style]} r:id="{rid_for[(fam,style)]}"/>'
            return e+"</p:embeddedFont>"
        efl="<p:embeddedFontLst>"+"".join(font_block(f) for f in fonts)+"</p:embeddedFontLst>"
        # 4c. remove any pre-existing (possibly mis-placed) embeddedFontLst
        ps=re.sub(r'<p:embeddedFontLst>.*?</p:embeddedFontLst>','',ps,flags=re.DOTALL)
        # 4d. INSERT in correct position: AFTER the close tag of the latest of {smartTags,notesSz,sldSz,sldIdLst}
        inserted=False
        for el in AFTER_ELEMENTS_PRIORITY:
            # match either <p:el .../> self-closing or <p:el ...>...</p:el>
            pat=re.compile(r'(<p:%s\b[^>]*/>)|(<p:%s\b[^>]*>.*?</p:%s>)' % (el,el,el), re.DOTALL)
            matches=list(pat.finditer(ps))
            if matches:
                end=matches[-1].end()
                ps=ps[:end]+efl+ps[end:]
                inserted=True; break
        if not inserted:
            # fallback: before the first BEFORE_ELEMENTS, else before </p:presentation>
            pos=None
            for el in BEFORE_ELEMENTS:
                m=re.search(r'<p:%s\b'%el, ps)
                if m: pos=m.start(); break
            if pos is None: pos=ps.rfind("</p:presentation>")
            ps=ps[:pos]+efl+ps[pos:]
        open(pp,"w",encoding="utf-8").write(ps)

        # 5) repackage ([Content_Types].xml first is best practice)
        if os.path.exists(output_pptx): os.remove(output_pptx)
        with zipfile.ZipFile(output_pptx,"w",zipfile.ZIP_DEFLATED) as z:
            z.write(ctp,"[Content_Types].xml")
            for root,_,files in os.walk(work):
                for fn in files:
                    arc=os.path.relpath(os.path.join(root,fn),work)
                    if arc=="[Content_Types].xml": continue
                    z.write(os.path.join(root,fn),arc)
        print(f"Embedded {len(font_files)} font part(s) into {output_pptx}")
        for fn,fam,style in font_files: print(f"  + {fam} ({style}) -> ppt/fonts/{fn}")
    finally:
        shutil.rmtree(work, ignore_errors=True)
        shutil.rmtree(normdir, ignore_errors=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("input"); ap.add_argument("output")
    ap.add_argument("--font",action="append",required=True,
                    help='Family:style=path[,style=path]  e.g. "Sarabun:regular=/p/S.ttf,bold=/p/Sb.ttf"')
    a=ap.parse_args()
    fonts={}
    for f in a.font:
        fam,styles=parse_font_arg(f); fonts[fam]=styles
    embed(a.input,a.output,fonts)
