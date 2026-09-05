"""Validator: checks PPTX font-embedding is PowerPoint-safe (ECMA-376 CT_Presentation order)."""
import zipfile, re, sys

# ECMA-376 CT_Presentation canonical child order
ORDER = ["sldMasterIdLst","notesMasterIdLst","handoutMasterIdLst","sldIdLst",
         "sldSz","notesSz","smartTags","embeddedFontLst","custShowLst","photoAlbum",
         "custDataLst","kinsoku","defaultTextStyle","modifyVerifier","extLst"]

def validate(path):
    errs=[]
    with zipfile.ZipFile(path) as z:
        names=z.namelist()
        pres=z.read("ppt/presentation.xml").decode()
        ct=z.read("[Content_Types].xml").decode()
        rels=z.read("ppt/_rels/presentation.xml.rels").decode()
    # 1. element order
    found=[t for t in re.findall(r'<p:(\w+)', pres) if t in ORDER]
    idx=[ORDER.index(t) for t in found]
    if idx != sorted(idx):
        errs.append(f"CT_Presentation child order WRONG: {found} (must follow {[ORDER[i] for i in sorted(set(idx))]})")
    # 2. if embeddedFontLst present, fonts must exist + content type + rels + flag
    if "embeddedFontLst" in found:
        if 'embedTrueTypeFonts="1"' not in pres:
            errs.append('embeddedFontLst present but embedTrueTypeFonts="1" missing')
        if "fntdata" not in ct:
            errs.append("fntdata content-type not registered in [Content_Types].xml")
        if 'application/x-fontdata' not in ct:
            errs.append("font content-type must be application/x-fontdata for PowerPoint")
        nfonts_xml = pres.count("<p:font ")
        nfonts_files = sum(1 for n in names if n.startswith("ppt/fonts/") and n.endswith(".fntdata"))
        nfonts_rels = rels.count("/font\"")  # relationship type ending /font
        if nfonts_files==0:
            errs.append("embeddedFontLst declared but no ppt/fonts/*.fntdata files")
    return errs

if __name__=="__main__":
    for p in sys.argv[1:]:
        e=validate(p)
        if e:
            print(f"FAIL  {p}")
            for x in e: print(f"      - {x}")
        else:
            print(f"PASS  {p}")
