#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_pptx_structure.py  —  Strict Validator (gamma-1) STRUCTURAL gate.

Catches OOXML schema violations that PowerPoint rejects with a Repair dialog but
LibreOffice silently tolerates (false-green). The validator the deck pipeline had
checked element *order* but NOT *duplication* — so a doubled singleton child slipped
through. Root cause of the DSL CRM V01R03 Repair dialog: two <a:effectLst/> in one
<p:spPr> (a no-shadow effectLst applied twice by rect()+_noshadow()).

RULE: certain children are singletons (maxOccurs=1) inside their parent. If any parent
element contains >1 of a singleton child, that is a FAIL.

Singletons enforced here (the ones the deck builder can realistically duplicate):
  in a:spPr / pic:spPr / cxnSp spPr (CT_ShapeProperties):
      xfrm, custGeom, prstGeom (geometry is a choice → at most one of the two),
      noFill/solidFill/gradFill/blipFill/pattFill/grpFill (fill is a choice → <=1 total),
      ln, effectLst, effectDag (effect is a choice → <=1 total), scene3d, sp3d, extLst
  in a:bodyPr's owner txBody (CT_TextBody): bodyPr, lstStyle  (each <=1)
  in a:rPr / a:defRPr / a:endParaRPr (CT_TextCharacterProperties):
      ln, fill-choice, effect-choice, latin, ea, cs, sym, highlight, uFill, uLn   (each <=1)

Usage:  python3 validate_pptx_structure.py FILE.pptx
Exit 0 + "PASS ..." on clean; exit 1 + "FAIL ..." listing each violation.
"""
import sys, zipfile, re
from collections import Counter
import xml.etree.ElementTree as ET

# Harden against XXE / billion-laughs. Prefer defusedxml; otherwise parse with a
# stdlib parser that has DTD/entity handling disabled (PPTX parts never use DTDs).
try:
    from defusedxml.ElementTree import fromstring as _safe_fromstring
except ImportError:
    def _safe_fromstring(xmlbytes):
        from xml.parsers import expat
        p = ET.XMLParser()
        # neutralise entity expansion at the expat level
        try:
            p.parser.DefaultHandler = lambda data: None
            p.parser.EntityDeclHandler = None
            p.entity = {}
        except Exception:
            pass
        p.feed(xmlbytes if isinstance(xmlbytes, (bytes, bytearray)) else xmlbytes.encode())
        return p.close()

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"


def _local(tag):
    return tag.rsplit("}", 1)[-1]


# choice groups: at most ONE member total may appear in the parent
FILL_CHOICE = {"noFill", "solidFill", "gradFill", "blipFill", "pattFill", "grpFill"}
GEOM_CHOICE = {"custGeom", "prstGeom"}
EFFECT_CHOICE = {"effectLst", "effectDag"}

# plain singletons: each may appear at most once
SPPR_SINGLETONS = {"xfrm", "ln", "scene3d", "sp3d", "extLst"}
TXBODY_SINGLETONS = {"bodyPr", "lstStyle"}
RPR_SINGLETONS = {"ln", "latin", "ea", "cs", "sym", "highlight", "uFill", "uLn",
                  "uFillTx", "uLnTx"}

# parents we inspect (local names). spPr appears in p:sp, p:pic, p:cxnSp, etc.
SHAPE_PROPS = {"spPr", "grpSpPr"}
RPR_TAGS = {"rPr", "defRPr", "endParaRPr"}


def _check_parent(parent, singletons, choices):
    """Return list of violation strings for one parent element."""
    counts = Counter(_local(c.tag) for c in list(parent))
    out = []
    for name, n in counts.items():
        if name in singletons and n > 1:
            out.append(f"<a:{name}> x{n} (singleton, max 1)")
    for label, group in choices:
        total = sum(counts.get(g, 0) for g in group)
        if total > 1:
            present = ", ".join(f"{g}x{counts[g]}" for g in group if counts.get(g))
            out.append(f"{label} choice has {total} members [{present}] (max 1)")
    return out


def scan_xml(xmlbytes, partname):
    """Yield violation strings for one slide/layout/master XML part."""
    viol = []
    try:
        root = _safe_fromstring(xmlbytes)
    except ET.ParseError as e:
        return [f"{partname}: XML parse error: {e}"]
    for el in root.iter():
        ln = _local(el.tag)
        if ln in SHAPE_PROPS:
            for v in _check_parent(el, SPPR_SINGLETONS,
                                   [("fill", FILL_CHOICE), ("geometry", GEOM_CHOICE),
                                    ("effect", EFFECT_CHOICE)]):
                viol.append(f"{partname}: <{ln}> {v}")
        elif ln == "txBody" or ln.endswith("txBody"):
            for v in _check_parent(el, TXBODY_SINGLETONS, []):
                viol.append(f"{partname}: <txBody> {v}")
        elif ln in RPR_TAGS:
            for v in _check_parent(el, RPR_SINGLETONS,
                                   [("fill", FILL_CHOICE), ("effect", EFFECT_CHOICE)]):
                viol.append(f"{partname}: <{ln}> {v}")
    return viol


def validate(path):
    viol = []
    with zipfile.ZipFile(path) as z:
        targets = [n for n in z.namelist()
                   if re.match(r"ppt/(slides|slideLayouts|slideMasters|notesSlides)/[^/]+\.xml$", n)]
        for n in sorted(targets):
            viol.extend(scan_xml(z.read(n), n.split("/")[-1]))
    return viol


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: validate_pptx_structure.py FILE.pptx"); sys.exit(2)
    v = validate(sys.argv[1])
    if v:
        print(f"FAIL — {len(v)} structural violation(s):")
        for x in v:
            print("  -", x)
        sys.exit(1)
    print("PASS — no duplicate singleton children in spPr/txBody/rPr across all slides")
    sys.exit(0)
