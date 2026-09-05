#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pali_translit.py — ถอดอักษรบาลีระหว่างอักษรไทย (อักขรวิธีบาลี: พินทุ ฺ นิคหิต ํ) กับอักษรโรมัน (IAST / ISO 15919 / Velthuis)

ใช้:
  python3 ~/.claude/skills/pali-language/scripts/pali_translit.py --from thai --to iast "ภิกฺขุ มนฺตํ สชฺฌายติ"
  python3 ~/.claude/skills/pali-language/scripts/pali_translit.py --from iast --to thai "bhikkhu mantaṃ sajjhāyati"
  python3 ~/.claude/skills/pali-language/scripts/pali_translit.py --from velthuis --to iast "bhikkhu manta.m sajjhaayati"
  python3 ~/.claude/skills/pali-language/scripts/pali_translit.py --from iast --to iso "saṅghaṃ"        # ṃ → ṁ
  python3 ~/.claude/skills/pali-language/scripts/pali_translit.py --from thai --to iast -f in.md -o out.md   # ทั้งไฟล์
  python3 ~/.claude/skills/pali-language/scripts/pali_translit.py --sort "saṅgha kāya ñāṇa aṅga"           # เรียงตามลำดับอักษรบาลี
  python3 ~/.claude/skills/pali-language/scripts/pali_translit.py --selftest                                 # ทดสอบไป-กลับ

รูปแบบที่รับ (--from): thai · iast · iso · velthuis · pts (ŋ = นิคหิต)   |   รูปแบบที่ให้ (--to): thai · iast · iso · velthuis
กติกาอักขรวิธีไทยที่ใช้ (references/11-roman-pali.md §3):
  · พยัญชนะที่ไม่มีสระกำกับและไม่มีพินทุ = มีเสียง a ในตัว (ก = ka)   · พินทุ ฺ ใต้ตัว = ไม่มีสระ (กฺ = k)
  · นิคหิต ํ = ṃ   · ึ = iṃ (อักขรวิธีไทยเขียน ิ+ํ เป็น ึ เช่น กรึสุ = kariṃsu)   · ุํ = uṃ   · ํ หลังพยัญชนะเปล่า = aṃ
  · สระหน้า เ/โ ออกเสียงที่พยัญชนะตัวสุดท้ายของกลุ่ม: กลุ่มต้นคำเขียนสระหน้าทั้งกลุ่ม (เสฺนห = sneha) · กลุ่มกลางคำ
    ตัวแรกปิดพยางค์ก่อนหน้าแล้วสระอยู่หน้าตัวที่เหลือ (ภนฺเต = bhante · พุทฺโธ = buddho · เสฏฺฐี = seṭṭhī)
  · สระลอยใช้ อ นำ (อิติ = iti · เอวํ = evaṃ · โอ = o)   · ฬ = ḷ · ญ = ñ · ง = ṅ · ฏ ฐ ฑ ฒ ณ = ṭ ṭh ḍ ḍh ṇ
  · ฎ ไม่ใช่อักขระบาลีมาตรฐาน (ตำราใช้ ฑ = ḍ) — รับเข้าเป็น ḍ แต่แจ้งเตือน · ำ (สระอำไทย) รับเป็น aṃ แต่แจ้งเตือน
ข้อจำกัด: ไม่แยกเสียง ṅ กับนิคหิตในต้นฉบับที่เขียนนิคหิตด้วย ง (บางสำนักพิมพ์) · ไม่ตัดคำ · อักขระที่ไม่ใช่ไทย (ละติน ตัวเลข
  เครื่องหมาย) ส่งผ่านตามเดิม · อักขระไทยนอกอักขรวิธีบาลี (ั ็ ่ ้ ์ ะ แ ไ ใ ฯลฯ = คำไทย) ส่งผ่านและ **เตือน** — ผลที่ได้ใช้ไม่ได้
  · PTS รับเฉพาะ ŋ → ṃ (ฉบับที่พิมพ์ n แทน ṅ ต้องแก้มือ)
script V01R02 · skill pali-language V01R05 · 2026.09.05 (R02 ตาม QA อริส PALI-019: +คำเตือนอักขระไทยนอกบาลี · พินทุท้ายคำ) · ที่มาของกติกา: ตำราอบรมบาลี น.5-9 + Access to Insight (Velthuis) + ISO 15919/IAST (ดู 11 §1)
"""
import sys, re, argparse, unicodedata

# ---------- ตารางพยัญชนะ ----------
TH2ROM = {
    'ก':'k','ข':'kh','ค':'g','ฆ':'gh','ง':'ṅ',
    'จ':'c','ฉ':'ch','ช':'j','ฌ':'jh','ญ':'ñ',
    'ฏ':'ṭ','ฐ':'ṭh','ฑ':'ḍ','ฒ':'ḍh','ณ':'ṇ',
    'ต':'t','ถ':'th','ท':'d','ธ':'dh','น':'n',
    'ป':'p','ผ':'ph','พ':'b','ภ':'bh','ม':'m',
    'ย':'y','ร':'r','ล':'l','ว':'v','ส':'s','ห':'h','ฬ':'ḷ',
    'ฎ':'ḍ',   # ไม่มาตรฐาน — เตือน
}
ROM2TH = {v:k for k,v in TH2ROM.items() if k != 'ฎ'}
VOWEL_CARRIER = 'อ'
PINTHU  = 'ฺ'   # ฺ
NIKHAHIT= 'ํ'   # ํ
AFTER_VOWELS = {'า':'ā','ิ':'i','ี':'ī','ุ':'u','ู':'ū'}   # า ิ ี ุ ู
PREFIX_VOWELS = {'เ':'e','โ':'o'}   # เ โ
SARA_UE  = 'ึ'   # ึ  = iṃ
SARA_AM  = 'ำ'   # ำ  = aṃ (ไม่มาตรฐานในบาลี)
ROM_VOWELS = ['ā','ī','ū','a','i','u','e','o']
ROM_CONS_ORDER = ['kh','gh','ch','jh','ṭh','ḍh','th','dh','ph','bh',   # ทวิอักษรก่อน
                  'k','g','ṅ','c','j','ñ','ṭ','ḍ','ṇ','t','d','n','p','b','m','y','r','l','v','s','h','ḷ']

# ---------- ลำดับอักษรบาลี (พจนานุกรม PED / DPD) ----------
PALI_ORDER = ['a','ā','i','ī','u','ū','e','o','ṃ',
              'k','kh','g','gh','ṅ','c','ch','j','jh','ñ','ṭ','ṭh','ḍ','ḍh','ṇ',
              't','th','d','dh','n','p','ph','b','bh','m','y','r','l','ḷ','v','s','h']
ORDER_RANK = {t:i for i,t in enumerate(PALI_ORDER)}

def nfc(s): return unicodedata.normalize('NFC', s)

# ---------- ทำให้เป็น IAST ก่อน (จาก iso / velthuis / pts) ----------
def velthuis_to_iast(s):
    rep = [('aa','ā'),('ii','ī'),('uu','ū'),('.m','ṃ'),('.t','ṭ'),('.d','ḍ'),('.n','ṇ'),('.l','ḷ'),('~n','ñ'),('"n','ṅ'),
           ('AA','Ā'),('II','Ī'),('UU','Ū'),('.M','Ṃ'),('.T','Ṭ'),('.D','Ḍ'),('.N','Ṇ'),('.L','Ḷ'),('~N','Ñ'),('"N','Ṅ')]
    for a,b in rep: s = s.replace(a,b)
    return s
def iso_to_iast(s):  return s.replace('ṁ','ṃ').replace('Ṁ','Ṃ')
def pts_to_iast(s):  return s.replace('ŋ','ṃ').replace('Ŋ','Ṃ')
def iast_to_iso(s):  return s.replace('ṃ','ṁ').replace('Ṃ','Ṁ')
def iast_to_velthuis(s):
    rep = [('ā','aa'),('ī','ii'),('ū','uu'),('ṃ','.m'),('ṭ','.t'),('ḍ','.d'),('ṇ','.n'),('ḷ','.l'),('ñ','~n'),('ṅ','"n'),
           ('Ā','AA'),('Ī','II'),('Ū','UU'),('Ṃ','.M'),('Ṭ','.T'),('Ḍ','.D'),('Ṇ','.N'),('Ḷ','.L'),('Ñ','~N'),('Ṅ','"N')]
    for a,b in rep: s = s.replace(a,b)
    return s

# ---------- ไทย → IAST ----------
def thai_to_iast(text, warnings=None):
    text = nfc(text)
    out = []
    i = 0; n = len(text)
    pend = None      # พยัญชนะที่รอสระ (สตริงโรมัน)
    prefix = None    # สระหน้า เ/โ ที่รอพยัญชนะ
    def flush(vowel=None):
        nonlocal pend
        if pend is None: return
        out.append(pend + (vowel if vowel is not None else 'a'))
        pend = None
    while i < n:
        ch = text[i]
        if ch in TH2ROM:
            if ch == 'ฎ' and warnings is not None: warnings.append('พบ ฎ (ไม่ใช่อักขระบาลีมาตรฐาน — ถอดเป็น ḍ ตรวจต้นฉบับ)')
            nxt = text[i+1] if i+1 < n else ''
            if nxt == PINTHU:                 # พยัญชนะไม่มีสระ
                after = text[i+2] if i+2 < n else ''
                if warnings is not None and not (after in TH2ROM or after == VOWEL_CARRIER or after in PREFIX_VOWELS):
                    warnings.append(f'พินทุท้ายคำหรือหน้าอักขระที่ไม่ใช่พยัญชนะ ("{ch}ฺ") — ตรวจต้นฉบับ')
                flush(); out.append(TH2ROM[ch]); i += 2; continue
            flush()                           # พยัญชนะก่อนหน้าที่ยังไม่มีสระ = a
            if prefix is not None:            # สระหน้ารออยู่ → ออกเสียงที่ตัวนี้
                # ตรวจนิคหิตต่อท้าย (เอวํ = evaṃ)
                if nxt == NIKHAHIT: out.append(TH2ROM[ch] + prefix + 'ṃ'); i += 2
                else: out.append(TH2ROM[ch] + prefix); i += 1
                prefix = None; continue
            pend = TH2ROM[ch]; i += 1; continue
        if ch == VOWEL_CARRIER:               # สระลอย
            flush()
            nxt = text[i+1] if i+1 < n else ''
            if prefix is not None:
                if nxt == NIKHAHIT: out.append(prefix + 'ṃ'); i += 2
                else: out.append(prefix); i += 1
                prefix = None; continue
            if nxt in AFTER_VOWELS:
                v = AFTER_VOWELS[nxt]; i += 2
                if i < n and text[i] == NIKHAHIT: v += 'ṃ'; i += 1
                out.append(v); continue
            if nxt == SARA_UE: out.append('iṃ'); i += 2; continue
            if nxt == NIKHAHIT: out.append('aṃ'); i += 2; continue
            if nxt == SARA_AM:
                if warnings is not None: warnings.append('พบ ำ (สระอำไทย) — ถอดเป็น aṃ ตรวจต้นฉบับ')
                out.append('aṃ'); i += 2; continue
            out.append('a'); i += 1; continue
        if ch in PREFIX_VOWELS:
            flush(); prefix = PREFIX_VOWELS[ch]; i += 1; continue
        if ch in AFTER_VOWELS:
            v = AFTER_VOWELS[ch]; i += 1
            if i < n and text[i] == NIKHAHIT: v += 'ṃ'; i += 1
            if pend is not None: flush(v)
            else: out.append(v)               # สระไม่มีพยัญชนะนำ (ผิดอักขรวิธี) — ส่งผ่าน
            continue
        if ch == SARA_UE:
            i += 1
            if pend is not None: flush('iṃ')
            else: out.append('iṃ')
            continue
        if ch == SARA_AM:
            if warnings is not None: warnings.append('พบ ำ (สระอำไทย) — ถอดเป็น aṃ ตรวจต้นฉบับ')
            i += 1
            if pend is not None: flush('aṃ')
            else: out.append('aṃ')
            continue
        if ch == NIKHAHIT:                    # นิคหิตหลังพยัญชนะเปล่า = aṃ
            i += 1
            if pend is not None: flush('aṃ')
            else: out.append('ṃ')
            continue
        if ch == PINTHU:                      # พินทุกำพร้า
            if warnings is not None: warnings.append('พบพินทุที่ไม่มีพยัญชนะนำ (ข้อความอาจเสียหาย — ดู 09 P7)')
            i += 1; continue
        # อักขระอื่น (ช่องว่าง เครื่องหมาย ตัวเลข ละติน) — ปิดพยางค์ค้างแล้วส่งผ่าน
        if '\u0e00' <= ch <= '\u0e7f' and warnings is not None:   # อักขระไทยที่ไม่อยู่ในอักขรวิธีบาลี
            warnings.append(f'พบอักขระไทยนอกอักขรวิธีบาลี "{ch}" — ข้อความเป็นคำไทย ไม่ใช่รูปบาลี ต้องหารูปบาลีก่อน (11 §3.1 ข้อ 6)')
        flush()
        if prefix is not None:
            if warnings is not None: warnings.append('สระหน้า เ/โ ไม่มีพยัญชนะตาม')
            out.append(prefix); prefix = None
        out.append(ch); i += 1
    flush()
    if prefix is not None: out.append(prefix)
    return ''.join(out)

# ---------- IAST → ไทย ----------
def tokenize_iast(word):
    toks = []; i = 0; n = len(word)
    while i < n:
        matched = False
        for c in ROM_CONS_ORDER:
            if word.startswith(c, i): toks.append(('C', c)); i += len(c); matched = True; break
        if matched: continue
        ch = word[i]
        if ch in ROM_VOWELS: toks.append(('V', ch)); i += 1; continue
        if ch == 'ṃ': toks.append(('M', ch)); i += 1; continue
        toks.append(('X', ch)); i += 1
    return toks

VOWEL_MARK = {'a':'', 'ā':'า', 'i':'ิ', 'ī':'ี', 'u':'ุ', 'ū':'ู'}
def iast_to_thai(text, warnings=None):
    text = nfc(text).replace('ṁ','ṃ').replace('ŋ','ṃ')
    out = []
    for piece in re.split(r'(\s+)', text):
        if piece.isspace() or piece == '': out.append(piece); continue
        # แยกเครื่องหมายหัวท้ายที่ไม่ใช่อักษร (วงเล็บ จุลภาค) ให้คงไว้
        m = re.match(r'^([^\wāīūṃṅñṭḍṇḷ]*)(.*?)([^\wāīūṃṅñṭḍṇḷ]*)$', piece)
        head, core, tail = m.group(1), m.group(2), m.group(3)
        out.append(head + _word_to_thai(core.lower(), warnings) + tail)
    return ''.join(out)

def _word_to_thai(word, warnings):
    toks = tokenize_iast(word)
    res = []; cluster = []   # cluster = พยัญชนะที่ยังไม่มีสระ (โรมัน)
    def emit_cluster_with_vowel(v):
        # พยัญชนะทุกตัวยกเว้นตัวสุดท้ายได้พินทุ
        # สระหน้า เ/โ: กลุ่มต้นคำ → วางหน้าทั้งกลุ่ม (sneha = เสฺนห) · กลุ่มกลางคำ → ตัวแรกปิดพยางค์ก่อนหน้า
        # แล้วสระหน้าอยู่หน้าตัวที่เหลือ (bhante = ภนฺเต · buddho = พุทฺโธ) — กติกาแบ่งพยางค์ของบาลี
        if v in ('e','o'):
            pre = 'เ' if v == 'e' else 'โ'
            if len(cluster) >= 2 and res:      # กลางคำ: ปิดพยางค์ก่อนด้วยตัวแรก
                head = ROM2TH[cluster[0]] + PINTHU
                rest = cluster[1:]
                return head + pre + ''.join(ROM2TH[c] + PINTHU for c in rest[:-1]) + ROM2TH[rest[-1]]
            return pre + ''.join(ROM2TH[c] + PINTHU for c in cluster[:-1]) + ROM2TH[cluster[-1]]
        th = ''.join(ROM2TH[c] + PINTHU for c in cluster[:-1]) + ROM2TH[cluster[-1]]
        return th + VOWEL_MARK[v]
    i = 0
    while i < len(toks):
        kind, val = toks[i]
        if kind == 'C':
            cluster.append(val); i += 1; continue
        if kind == 'V':
            if cluster: res.append(emit_cluster_with_vowel(val)); cluster = []
            else:
                res.append({'a':'อ','ā':'อา','i':'อิ','ī':'อี','u':'อุ','ū':'อู','e':'เอ','o':'โอ'}[val])
            i += 1
            # นิคหิตตามสระ
            if i < len(toks) and toks[i][0] == 'M':
                if val == 'i' and res[-1].endswith('ิ'): res[-1] = res[-1][:-1] + SARA_UE   # ิ+ํ → ึ
                else: res.append(NIKHAHIT)
                i += 1
            continue
        if kind == 'M':          # ṃ ที่ไม่มีสระนำ (ผิดอักขรวิธี) — ใส่นิคหิตหลังกลุ่ม
            if cluster: res.append(''.join(ROM2TH[c] + PINTHU for c in cluster)); cluster = []
            res.append(NIKHAHIT); i += 1
            if warnings is not None: warnings.append(f'ṃ ไม่มีสระนำใน "{word}"')
            continue
        # อักขระอื่น (ขีด อะพอสทรอฟี ตัวเลข) — ปิดกลุ่มพยัญชนะด้วยพินทุ
        if cluster: res.append(''.join(ROM2TH[c] + PINTHU for c in cluster)); cluster = []
        if val not in "-'’" and warnings is not None and val.isalpha():
            warnings.append(f'อักษร "{val}" ไม่อยู่ในชุดอักขระบาลี (คำ "{word}")')
        res.append(val); i += 1
    if cluster: res.append(''.join(ROM2TH[c] + PINTHU for c in cluster))   # พยัญชนะท้ายคำไม่มีสระ
    return ''.join(res)

# ---------- เรียงลำดับอักษรบาลี ----------
def pali_sort_key(word):
    key = []
    for kind, val in tokenize_iast(nfc(word).lower().replace('ṁ','ṃ')):
        key.append(ORDER_RANK.get(val, 99))
    return key

def convert(text, src, dst, warnings=None):
    if src == 'velthuis': text = velthuis_to_iast(text)
    elif src == 'iso': text = iso_to_iast(text)
    elif src == 'pts': text = pts_to_iast(text)
    # ตอนนี้ text เป็น thai หรือ iast
    if src == 'thai' and dst == 'thai': return nfc(text)
    if src == 'thai': text = thai_to_iast(text, warnings)
    if dst == 'thai': return nfc(iast_to_thai(text, warnings))
    if dst == 'iso': return nfc(iast_to_iso(text))
    if dst == 'velthuis': return iast_to_velthuis(text)
    return nfc(text)

SELFTEST = [   # (ไทย, IAST) — คำจากตำราอบรม/paradigm ในไฟล์ 02 04 06 ของ skill นี้
    ('ภิกฺขุ มนฺตํ สชฺฌายติ', 'bhikkhu mantaṃ sajjhāyati'),
    ('เสฏฺฐี', 'seṭṭhī'), ('ครุํ', 'garuṃ'), ('ครูนํ', 'garūnaṃ'), ('กรึสุ', 'kariṃsu'), ('เอยฺยุํ', 'eyyuṃ'),
    ('อตฺตา หิ อตฺตโน นาโถ', 'attā hi attano nātho'), ('สงฺคหวตฺถุ', 'saṅgahavatthu'), ('ปญฺญา', 'paññā'),
    ('โยนิโสมนสิการ', 'yonisomanasikāra'), ('เอวํ', 'evaṃ'), ('อิติ', 'iti'), ('โอวาท', 'ovāda'), ('เสฺนห', 'sneha'),
    ('วฏฺฏ', 'vaṭṭa'), ('ฐาน', 'ṭhāna'), ('ทฬฺห', 'daḷha'), ('อุโปสถาคาเร', 'uposathāgāre'), ('ภนฺเต', 'bhante'),
    ('พุทฺโธ', 'buddho'), ('ธมฺมํ', 'dhammaṃ'), ('สนฺโต', 'santo'), ('อคฺเค', 'agge'), ('โยฺห', 'yho'), ('ตสฺเสว', 'tasseva'), ('สรณํ คจฺฉามิ', 'saraṇaṃ gacchāmi'),
]
def selftest():
    bad = 0
    for th, ro in SELFTEST:
        w = []
        got_ro = thai_to_iast(th, w); got_th = iast_to_thai(ro, w)
        ok = (got_ro == ro) and (got_th == nfc(th))
        print(('✓' if ok else '✗'), th, '→', got_ro, '|', ro, '→', got_th, ('' if not w else ' ⚠ '+'; '.join(w)))
        bad += (not ok)
    print(f'selftest: {len(SELFTEST)-bad}/{len(SELFTEST)} ผ่าน')
    return 0 if bad == 0 else 1

def main():
    ap = argparse.ArgumentParser(description='ถอดอักษรบาลี ไทย ↔ โรมัน (IAST/ISO 15919/Velthuis)')
    ap.add_argument('text', nargs='?', help='ข้อความ (หรือใช้ -f)')
    ap.add_argument('--from', dest='src', choices=['thai','iast','iso','velthuis','pts'], default='thai')
    ap.add_argument('--to', dest='dst', choices=['thai','iast','iso','velthuis'], default='iast')
    ap.add_argument('-f','--file', help='อ่านจากไฟล์')
    ap.add_argument('-o','--out', help='เขียนผลลงไฟล์')
    ap.add_argument('--sort', action='store_true', help='เรียงคำ (คั่นด้วยช่องว่าง) ตามลำดับอักษรบาลี — รับ IAST')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest: sys.exit(selftest())
    text = open(a.file, encoding='utf-8').read() if a.file else (a.text or '')
    if not text: ap.print_help(); sys.exit(1)
    if a.sort:
        words = text.split()
        print('\n'.join(sorted(words, key=pali_sort_key))); return
    warnings = []
    res = convert(text, a.src, a.dst, warnings)
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(res); print(f'เขียน {a.out} ({len(res):,} อักขระ)')
    else:
        print(res)
    for w in sorted(set(warnings)): print('⚠', w, file=sys.stderr)

if __name__ == '__main__':
    main()
