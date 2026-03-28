"""
Extract ITR/Checklist templates from ITRs zip, deduplicate, anonymize,
copy to resources/itrs/, and output a catalog for the library.

Sources:
  - RTIO ITRs (primary): Civil, Structural, Mechanical, Piping, Electrical,
    Instrumentation, Fire/Gas, Telecoms, Architectural
  - Daruosh's Misc ITRs (supplement): QU-ITR-XXXX items unique to this set
  - Pilgangoora (supplement for any remaining unique types)

Dedup strategy:
  - Within RTIO, M1/E1/P1/J1/S1/C1 are primary; M2-M4 etc. are duplicates → skip them
    unless a title in M2/M3/M4 doesn't appear in M1
  - Skip "Contractor ITR Place Holder" / "Vendor ITR Place Holder"
  - Skip desktop.ini, FIC Register etc.
  - From Daruosh: only QU-ITR docx, only items not already covered by RTIO
  - Keep .docx over .doc where both exist
"""

import os, zipfile, re, shutil
from pathlib import Path

BASE    = Path(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = BASE / "resources" / "itrs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ZIP = Path(r"C:\Users\M. Gustave\Dropbox\My PC (DESKTOP-IECVDML)\Downloads\ITRs-20260328T040414Z-1-001.zip")

def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9 \-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-{2,}", "-", s)
    return s

# --------------------------------------------------------------------------
# 1. Parse the zip and build a manifest of useful files
# --------------------------------------------------------------------------
z = zipfile.ZipFile(ZIP)
all_names = [n for n in z.namelist() if not n.endswith("/")]

SKIP_KEYWORDS = [
    "placeholder", "place holder", "desktop.ini", "fic register", "wps-", "wqr-", "wps_",
    "scope of works", "appendix", "commissioning plan", "itr procedure",
    "vendor coversheet", "~$",
]

def should_skip(fname):
    fl = fname.lower()
    return any(kw in fl for kw in SKIP_KEYWORDS)

# We'll collect records as: {clean_title: (zip_path, extension)}
# Preference order for same title: docx > doc > pdf

catalog = {}  # key = (discipline, clean_title), val = (zip_path, ext)

EXT_RANK = {"docx": 0, "doc": 1, "pdf": 2}

def add_entry(discipline, clean_title, zip_path):
    ext = zip_path.rsplit(".", 1)[-1].lower()
    if ext not in EXT_RANK:
        return
    key = (discipline, clean_title.lower())
    existing = catalog.get(key)
    if existing is None:
        catalog[key] = (zip_path, ext)
    else:
        # prefer better extension
        if EXT_RANK[ext] < EXT_RANK[existing[1]]:
            catalog[key] = (zip_path, ext)

# ---- Helper: extract description from RTIO filename ---------------------
# e.g. "000001 - M1.001 - Mechanical - Cable Supports Protection.docx"
#   → discipline="electrical", clean_title="Cable Supports Protection"
# e.g. "000001 - C1.001 - Civil - Clear Grub Topsoil Removal.docx"
#   → discipline="civil", clean_title="Clear Grub Topsoil Removal"

RTIO_DISC_MAP = {
    "Civil": "civil",
    "Structural": "structural",
    "Mechanical": "mechanical",
    "Piping": "piping",
    "Electrical": "electrical",
    "Instrument": "instrumentation",
    "Fire Gas": "fire_gas",
    "Telecomms": "telecoms",
    "Architectural": "architectural",
}

def parse_rtio(fname):
    """Returns (discipline, clean_title) or None."""
    # Pattern: "000001 - X1.001 - Discipline - Description.ext"
    base = fname.rsplit(".", 1)[0]
    m = re.match(r"\d+ - [A-Z]\d+\.\d+ - (.+?) - (.+)$", base)
    if not m:
        # Try without area code e.g. "P1.097 - Flange Pack Cover Page"
        m = re.match(r"[A-Z]\d+\.\d+ - (.+?) - (.+)$", base)
    if m:
        disc_raw, desc = m.group(1).strip(), m.group(2).strip()
        disc = RTIO_DISC_MAP.get(disc_raw, disc_raw.lower().replace(" ", "_"))
        return disc, desc
    return None

# ---- RTIO: primary areas only (M1, P1, E1, J1, S1, C1, H1, T1, A1) ----
# We collect primary-area items first, then add secondary-area unique items

primary_rtio = {}  # (disc, desc_lower) → zip_path

for n in all_names:
    if "RTIO" not in n:
        continue
    fname = n.split("/")[-1]
    if should_skip(fname.lower()):
        continue
    ext = fname.rsplit(".", 1)[-1].lower()
    if ext not in ("docx", "doc", "pdf"):
        continue
    r = parse_rtio(fname)
    if not r:
        continue
    disc, desc = r
    key = (disc, desc.lower())
    # Determine area priority from code number (M1 < M2 < M3)
    code_m = re.search(r"[A-Z](\d+)\.\d+", fname)
    area_num = int(code_m.group(1)) if code_m else 99
    existing = primary_rtio.get(key)
    if existing is None:
        primary_rtio[key] = (n, ext, area_num)
    else:
        _, _, ex_area = existing
        if area_num < ex_area:
            primary_rtio[key] = (n, ext, area_num)

for (disc, desc_lower), (zip_path, ext, _) in primary_rtio.items():
    fname = zip_path.split("/")[-1]
    r = parse_rtio(fname)
    if r:
        _, desc = r
        add_entry(disc, desc, zip_path)

# ---- Daruosh QU-ITR: supplement with items not already in catalog -------
DARUOSH_DISC_MAP = {
    "000": "civil",
    "001": "civil",   # 0001-0010: civil
    "002": "civil",
    "003": "civil",
    "004": "civil",
    "005": "civil",
    "006": "civil",
    "007": "civil",
    "008": "civil",
    "009": "civil",
    "010": "civil",
    "101": "structural",  # 0101-0111: structural
    "102": "structural",
    "103": "structural",
    "104": "structural",
    "105": "structural",
    "106": "structural",
    "107": "structural",
    "108": "structural",
    "109": "structural",
    "110": "structural",
    "111": "structural",
    "201": "mechanical",
    "202": "mechanical",
    "203": "mechanical",
    "204": "mechanical",
    "205": "mechanical",
    "206": "mechanical",
    "207": "mechanical",
    "208": "mechanical",
    "209": "mechanical",
    "210": "mechanical",
    "211": "mechanical",
    "212": "mechanical",
    "213": "mechanical",
    "214": "mechanical",
    "215": "mechanical",
    "216": "mechanical",
    "217": "mechanical",
    "218": "mechanical",
    "219": "mechanical",
    "220": "mechanical",
    "221": "mechanical",
    "222": "mechanical",
    "223": "mechanical",
    "224": "mechanical",
    "225": "mechanical",
    "226": "mechanical",
    "227": "mechanical",
    "228": "mechanical",
    "229": "mechanical",
    "230": "mechanical",
    "231": "mechanical",
    "232": "mechanical",
    "233": "mechanical",
    "234": "mechanical",
    "235": "mechanical",
    "236": "mechanical",
    "237": "mechanical",
    "238": "mechanical",
    "239": "mechanical",
    "240": "mechanical",
    "241": "mechanical",
    "242": "mechanical",
    "243": "mechanical",
    "244": "mechanical",
    "245": "mechanical",
    "246": "mechanical",
    "247": "mechanical",
    "248": "mechanical",
    "250": "mechanical",
    "251": "mechanical",
    "301": "piping",
    "302": "piping",
    "303": "piping",
    "304": "piping",
    "305": "piping",
    "306": "piping",
    "307": "piping",
    "308": "piping",
    "309": "piping",
    "310": "piping",
    "311": "piping",
    "312": "piping",
    "313": "piping",
    "314": "piping",
    "315": "piping",
    "316": "piping",
    "317": "piping",
    "318": "piping",
    "319": "piping",
    "320": "piping",
    "321": "piping",
    "322": "piping",
    "323": "piping",
    "324": "piping",
}

for n in all_names:
    if "Daruosh" not in n:
        continue
    fname = n.split("/")[-1]
    if should_skip(fname.lower()):
        continue
    # Only QU-ITR files (not QU-FIC)
    if "QU-ITR" not in fname:
        continue
    ext = fname.rsplit(".", 1)[-1].lower()
    if ext not in ("docx",):  # prefer docx only from Daruosh ITRs
        continue
    # Parse: "0000_QU-ITR-0001_A Earthworks.docx"
    m = re.match(r"\d+_QU-ITR-(\d+)_[A-Z]?\s*(.+)\.docx", fname, re.IGNORECASE)
    if not m:
        # Try without rev letter: "0000_QU-ITR-0004_Compaction.docx"
        m = re.match(r"\d+_QU-ITR-(\d+)_(.+)\.docx", fname, re.IGNORECASE)
    if not m:
        continue
    num_str, desc = m.group(1), m.group(2).strip()
    disc = DARUOSH_DISC_MAP.get(num_str.lstrip("0") or "0", "mechanical")
    # Only add if not already covered by RTIO
    key = (disc, desc.lower())
    if key not in catalog:
        add_entry(disc, desc, n)

print(f"Total unique ITRs catalogued: {len(catalog)}")

# --------------------------------------------------------------------------
# 2. Extract files to resources/itrs/
# --------------------------------------------------------------------------

DISC_PREFIX = {
    "civil":          "Civil",
    "structural":     "Structural",
    "mechanical":     "Mechanical",
    "piping":         "Piping",
    "electrical":     "Electrical",
    "instrumentation":"Instrument",
    "fire_gas":       "FireGas",
    "telecoms":       "Telecoms",
    "architectural":  "Architectural",
}

extracted = []

for (disc, _), (zip_path, ext) in sorted(catalog.items()):
    # Re-get the clean desc
    fname = zip_path.split("/")[-1]
    r = parse_rtio(fname)
    if r:
        _, desc = r
    else:
        # Daruosh
        m = re.match(r"\d+_QU-ITR-\d+_[A-Z]?\s*(.+)\.(docx|doc)", fname, re.IGNORECASE)
        if not m:
            m = re.match(r"\d+_QU-ITR-\d+_(.+)\.(docx|doc)", fname, re.IGNORECASE)
        desc = m.group(1).strip() if m else fname.rsplit(".", 1)[0]

    prefix = DISC_PREFIX.get(disc, disc.title())
    clean_name = f"ITR-{prefix}-{slugify(desc)}.{ext}"

    dest = OUT_DIR / clean_name
    # Extract
    data = z.read(zip_path)
    with open(dest, "wb") as f:
        f.write(data)
    extracted.append({
        "file": clean_name,
        "title": desc,
        "disc": disc,
        "fmt": ext,
    })

print(f"Extracted {len(extracted)} files to {OUT_DIR}")

# --------------------------------------------------------------------------
# 3. Print catalog summary by discipline
# --------------------------------------------------------------------------
from collections import Counter
counts = Counter(e["disc"] for e in extracted)
for disc, cnt in sorted(counts.items()):
    print(f"  {disc:20s}: {cnt}")

# --------------------------------------------------------------------------
# 4. Write catalog to itr_catalog.py for import by build_resources.py
# --------------------------------------------------------------------------
from collections import defaultdict

DISC_STAGE_ROLE = {
    "architectural":  {"stages": [5],    "roles": ["Engineer","Quality"]},
    "civil":          {"stages": [5],    "roles": ["PM","Engineer","Quality","Scheduler"]},
    "structural":     {"stages": [5],    "roles": ["Engineer","Quality","Scheduler"]},
    "mechanical":     {"stages": [5,6],  "roles": ["Engineer","Quality"]},
    "piping":         {"stages": [5,6],  "roles": ["Engineer","Quality"]},
    "electrical":     {"stages": [5,6],  "roles": ["Engineer","Quality","HSE"]},
    "instrumentation":{"stages": [5,6],  "roles": ["Engineer","Quality"]},
    "fire_gas":       {"stages": [5,6],  "roles": ["Engineer","Quality","HSE"]},
    "telecoms":       {"stages": [5,6],  "roles": ["Engineer","Quality"]},
}

by_disc = defaultdict(list)
for e in extracted:
    by_disc[e["disc"]].append(e)

lines = ["ITR_CATALOG = [\n"]
for disc in ["civil","structural","mechanical","piping","electrical","instrumentation",
             "fire_gas","telecoms","architectural"]:
    items = sorted(by_disc.get(disc, []), key=lambda x: x["title"])
    if not items:
        continue
    sr = DISC_STAGE_ROLE.get(disc, {"stages":[5],"roles":["Engineer","Quality"]})
    lines.append(f"  # {disc.upper()}\n")
    for e in items:
        lines.append(
            f'  {{"file":{repr(e["file"])},"title":{repr(e["title"])},'
            f'"cat":{repr(disc)},"fmt":{repr(e["fmt"])},'
            f'"stages":{sr["stages"]!r},"roles":{sr["roles"]!r}}},\n'
        )
lines.append("]\n")

catalog_path = BASE / "itr_catalog.py"
with open(catalog_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"\nWrote catalog to {catalog_path}")
print(f"Total entries: {len(extracted)}")
