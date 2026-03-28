import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from itr_catalog import ITR_CATALOG

# Load and clean nav block (remove duplicate Resources link)
with open(os.path.join(BASE, '_nav_block.txt'), 'r', encoding='utf-8') as f:
    nav_raw = f.read()

# Remove the plain /resources.html link (keep the bold one)
nav_raw = nav_raw.replace(
    '<a href="/resources.html" class="button is-text is-nav w-button">Resources</a>',
    ''
)
# Fix resources link to use full path
nav_raw = nav_raw.replace(
    '<a href="resources.html" class="button is-text is-nav w-button" style="font-weight:700;">Resources</a>',
    '<a href="/resources.html" class="button is-text is-nav w-button" style="font-weight:700;">Resources</a>'
)

# ---- ITP CATALOG -------------------------------------------------------
# fmt: xlsx / pdf / docx / doc
# cat: civil / structural / piping / mechanical / conveyors / electrical / coatings / multidiscipline
# stages: list of ints 1-7
# roles: list from PM / Engineer / Quality / Estimator / Scheduler / HSE

CATALOG = [
  # ── CIVIL ──────────────────────────────────────────────────────────────
  {"file":"ITP-Bulk-Landform.doc","title":"Bulk Landform","cat":"civil","fmt":"doc",
   "stages":[5],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Civil-Concrete-Works.xlsx","title":"Civil Concrete Works","cat":"civil","fmt":"xlsx",
   "stages":[5],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Civil-General.xlsx","title":"Civil General","cat":"civil","fmt":"xlsx",
   "stages":[5],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Civil-Works-Master.xlsx","title":"Civil Works Master","cat":"civil","fmt":"xlsx",
   "stages":[3,4,5],"roles":["PM","Engineer","Quality","Estimator","Scheduler"]},
  {"file":"ITP-Earthworks-Concrete-Civil.xlsx","title":"Earthworks & Concrete Civil","cat":"civil","fmt":"xlsx",
   "stages":[5],"roles":["PM","Engineer","Quality"]},
  {"file":"ITP-Fuel-Lubricant-Storage-Facility.xlsx","title":"Fuel & Lubricant Storage Facility","cat":"civil","fmt":"xlsx",
   "stages":[4,5],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Seeding.doc","title":"Seeding","cat":"civil","fmt":"doc",
   "stages":[5,7],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Topsoil-Spread.doc","title":"Topsoil Spread","cat":"civil","fmt":"doc",
   "stages":[5,7],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Underground-Services-Installation.pdf","title":"Underground Services Installation","cat":"civil","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},

  # ── STRUCTURAL ─────────────────────────────────────────────────────────
  {"file":"ITP-Structural-Steel-Erection.docx","title":"Structural Steel Erection","cat":"structural","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality","Scheduler"]},
  {"file":"ITP-Structural-Steel-Fabrication.docx","title":"Structural Steel Fabrication","cat":"structural","fmt":"docx",
   "stages":[4,5],"roles":["Engineer","Quality","Estimator"]},
  {"file":"ITP-Structural-Steel-Supply-Fabrication.xlsx","title":"Structural Steel Supply & Fabrication","cat":"structural","fmt":"xlsx",
   "stages":[3,4,5],"roles":["PM","Engineer","Quality","Estimator"]},

  # ── PIPING ─────────────────────────────────────────────────────────────
  {"file":"ITP-Carbon-Steel-Piping-Installation.pdf","title":"Carbon Steel Piping Installation","cat":"piping","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Chute-Drain.doc","title":"Chute & Drain Piping","cat":"piping","fmt":"doc",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-HDPE-Piping-Installation.pdf","title":"HDPE Piping Installation","cat":"piping","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Lubrication-Hydraulics-Piping.pdf","title":"Lubrication & Hydraulics Piping","cat":"piping","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Multi-Site-Piping-Works.xlsx","title":"Multi-Site Piping Works","cat":"piping","fmt":"xlsx",
   "stages":[5],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Piping-Supply-Fabrication-Assembly-A.xlsx","title":"Piping Supply, Fabrication & Assembly (A)","cat":"piping","fmt":"xlsx",
   "stages":[4,5],"roles":["Engineer","Quality","Estimator"]},
  {"file":"ITP-Piping-Supply-Fabrication-Assembly-B.xlsx","title":"Piping Supply, Fabrication & Assembly (B)","cat":"piping","fmt":"xlsx",
   "stages":[4,5],"roles":["Engineer","Quality","Estimator"]},
  {"file":"ITP-Piping-Supply-Fabrication-Offsite.xlsx","title":"Piping Supply & Fabrication – Offsite","cat":"piping","fmt":"xlsx",
   "stages":[4],"roles":["Engineer","Quality","Estimator"]},
  {"file":"ITP-Piping-Works-General.xlsx","title":"Piping Works General","cat":"piping","fmt":"xlsx",
   "stages":[3,4,5],"roles":["PM","Engineer","Quality","Estimator","Scheduler"]},
  {"file":"ITP-Polyethylene-Piping-Installation.docx","title":"Polyethylene Piping Installation","cat":"piping","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Pressure-Vessel-Fabrication.xlsx","title":"Pressure Vessel Fabrication","cat":"piping","fmt":"xlsx",
   "stages":[4,5],"roles":["Engineer","Quality","Estimator"]},
  {"file":"ITP-Steel-Piping-Fabrication-Template.docx","title":"Steel Piping Fabrication Template","cat":"piping","fmt":"docx",
   "stages":[4,5],"roles":["Engineer","Quality","Estimator"]},
  {"file":"ITP-Steel-Piping-Installation-Template.docx","title":"Steel Piping Installation Template","cat":"piping","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Steel-Piping-Installation.xlsx","title":"Steel Piping Installation","cat":"piping","fmt":"xlsx",
   "stages":[5],"roles":["PM","Engineer","Quality","Scheduler"]},

  # ── MECHANICAL ─────────────────────────────────────────────────────────
  {"file":"ITP-Apron-Feeder-Installation.pdf","title":"Apron Feeder Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Bin-Chute-Installation.pdf","title":"Bin & Chute Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Cone-Crusher-Installation.pdf","title":"Cone Crusher Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Dry-Vibrating-Screen-Installation.pdf","title":"Dry Vibrating Screen Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Gyratory-Crusher-Installation.pdf","title":"Gyratory Crusher Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-HPGR-Installation.pdf","title":"HPGR Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Isolation-Gate-Installation.pdf","title":"Isolation Gate Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Low-Profile-Feeder-Installation.pdf","title":"Low Profile Feeder Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Mechanical-Equipment-Installation-A.xlsx","title":"Mechanical Equipment Installation (A)","cat":"mechanical","fmt":"xlsx",
   "stages":[5],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Mechanical-Equipment-Installation-B.xlsx","title":"Mechanical Equipment Installation (B)","cat":"mechanical","fmt":"xlsx",
   "stages":[5],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Mechanical-Equipment-Installation-Template.docx","title":"Mechanical Equipment Installation Template","cat":"mechanical","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Mechanical-Installation-General.pdf","title":"Mechanical Installation General","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Metal-Detector.pdf","title":"Metal Detector Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Pump-Installation.pdf","title":"Pump Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Rock-Breaker-Installation.pdf","title":"Rock Breaker Installation","cat":"mechanical","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},

  # ── CONVEYORS ──────────────────────────────────────────────────────────
  {"file":"ITP-Air-Classifier-Installation.pdf","title":"Air Classifier Installation","cat":"conveyors","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Baghouse-Installation.pdf","title":"Baghouse Installation","cat":"conveyors","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Belt-Feeder-Installation.pdf","title":"Belt Feeder Installation","cat":"conveyors","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Belt-Scraper.pdf","title":"Belt Scraper","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-Belt-Weigher.pdf","title":"Belt Weigher","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-Conveyor-Installation.pdf","title":"Conveyor Installation","cat":"conveyors","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality","Scheduler"]},
  {"file":"ITP-EI-Air-Classification-A.pdf","title":"Equipment Installation: Air Classification (A)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Air-Classification-B.pdf","title":"Equipment Installation: Air Classification (B)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Coarse-Ore-Stockpile.pdf","title":"Equipment Installation: Coarse Ore Stockpile","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Dry-Magnetic-Separation-A.pdf","title":"Equipment Installation: Dry Magnetic Separation (A)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Dry-Magnetic-Separation-B.pdf","title":"Equipment Installation: Dry Magnetic Separation (B)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Dry-Tailings.pdf","title":"Equipment Installation: Dry Tailings","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Primary-Crusher-A.pdf","title":"Equipment Installation: Primary Crusher (A)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Primary-Crusher-B.pdf","title":"Equipment Installation: Primary Crusher (B)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Primary-Grinding-A.pdf","title":"Equipment Installation: Primary Grinding (A)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Primary-Grinding-B.pdf","title":"Equipment Installation: Primary Grinding (B)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Secondary-Crusher-A.pdf","title":"Equipment Installation: Secondary Crusher (A)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Secondary-Crusher-B.pdf","title":"Equipment Installation: Secondary Crusher (B)","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-EI-Tertiary-Crushing.pdf","title":"Equipment Installation: Tertiary Crushing","cat":"conveyors","fmt":"pdf",
   "stages":[5,6],"roles":["Engineer","Quality"]},
  {"file":"ITP-Fabric-Conveyor-Belt-Installation.pdf","title":"Fabric Conveyor Belt Installation","cat":"conveyors","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Steel-Cord-Conveyor-Belt-Installation.pdf","title":"Steel Cord Conveyor Belt Installation","cat":"conveyors","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality"]},

  # ── ELECTRICAL ─────────────────────────────────────────────────────────
  {"file":"ITP-Cable-Ladder-Tray-Conduit.docx","title":"Cable Ladder, Tray & Conduit","cat":"electrical","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Earthing-Installation-Termination.docx","title":"Earthing Installation & Termination","cat":"electrical","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Electrical-Equipment-Installation.docx","title":"Electrical Equipment Installation","cat":"electrical","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality"]},
  {"file":"ITP-Electrical-Instrumentation-A.xlsx","title":"Electrical & Instrumentation (A)","cat":"electrical","fmt":"xlsx",
   "stages":[5,6],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Electrical-Instrumentation-B.xlsx","title":"Electrical & Instrumentation (B)","cat":"electrical","fmt":"xlsx",
   "stages":[5,6],"roles":["PM","Engineer","Quality","Scheduler"]},
  {"file":"ITP-Electrical-Instrumentation-Hazardous-Area.xlsx","title":"Electrical & Instrumentation – Hazardous Area","cat":"electrical","fmt":"xlsx",
   "stages":[5,6],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Lighting-Small-Power-Installation.docx","title":"Lighting & Small Power Installation","cat":"electrical","fmt":"docx",
   "stages":[5],"roles":["Engineer","Quality"]},

  # ── COATINGS ───────────────────────────────────────────────────────────
  {"file":"ITP-Grouting-Cementitious-Epoxy.pdf","title":"Grouting – Cementitious & Epoxy","cat":"coatings","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-High-Build-Epoxy-Coating.xlsx","title":"High-Build Epoxy Coating","cat":"coatings","fmt":"xlsx",
   "stages":[5],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Protective-Coatings-Treatment.xlsx","title":"Protective Coatings & Treatment","cat":"coatings","fmt":"xlsx",
   "stages":[5],"roles":["Engineer","Quality","HSE"]},
  {"file":"ITP-Surface-Treatment-Repair.pdf","title":"Surface Treatment & Repair","cat":"coatings","fmt":"pdf",
   "stages":[5],"roles":["Engineer","Quality","HSE"]},

  # ── MULTI-DISCIPLINE ───────────────────────────────────────────────────
  {"file":"ITP-Civil-Structural-Mechanical-Site-Installation.xlsx","title":"Civil, Structural & Mechanical Site Installation","cat":"multidiscipline","fmt":"xlsx",
   "stages":[4,5],"roles":["PM","Engineer","Quality","Estimator","Scheduler"]},
  {"file":"ITP-Industrial-Facility-Master.xlsx","title":"Industrial Facility Master ITP","cat":"multidiscipline","fmt":"xlsx",
   "stages":[3,4,5],"roles":["PM","Engineer","Quality","Estimator","Scheduler"]},
  {"file":"ITP-Piping-Mechanical-Structural-Civil-Matrix.xlsx","title":"Piping, Mechanical, Structural & Civil Matrix","cat":"multidiscipline","fmt":"xlsx",
   "stages":[3,4,5],"roles":["PM","Engineer","Quality","Estimator","Scheduler"]},
  {"file":"ITP-Sustaining-Works-Multi-Discipline.xlsx","title":"Sustaining Works – Multi-Discipline","cat":"multidiscipline","fmt":"xlsx",
   "stages":[5,6],"roles":["PM","Engineer","Quality","Scheduler","HSE"]},
]

# ---- Helper to build a card ----------------------------------------

STAGE_LABELS = {
    1: "S1: Initiation", 2: "S2: Design", 3: "S3: Preconstruction",
    4: "S4: Procurement", 5: "S5: Construction", 6: "S6: Closeout",
    7: "S7: Post-Construction"
}
STAGE_SHORT = {1:"S1",2:"S2",3:"S3",4:"S4",5:"S5",6:"S6",7:"S7"}

FORMAT_ICON = {
    "xlsx": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9l6 6M15 9l-6 6"/></svg>',
    "pdf":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    "docx": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
    "doc":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
}

def card(item):
    stage_tags = "".join(f'<span class="tag tag-s{s}">{STAGE_SHORT[s]}</span>' for s in item["stages"])
    role_tags  = "".join(f'<span class="tag tag-role tag-{r.lower()}">{r}</span>' for r in item["roles"])
    fmt        = item["fmt"]
    fmt_label  = fmt.upper()
    icon       = FORMAT_ICON.get(fmt, FORMAT_ICON["docx"])
    stages_data = ",".join(str(s) for s in item["stages"])
    roles_data  = ",".join(r.lower() for r in item["roles"])
    return f'''<div class="lib-card"
      data-cat="{item["cat"]}"
      data-fmt="{fmt}"
      data-stages="{stages_data}"
      data-roles="{roles_data}"
      data-title="{item["title"].lower()}">
  <div class="lib-card-icon">{icon}</div>
  <div class="lib-card-body">
    <p class="lib-card-title">{item["title"]}</p>
    <div class="lib-card-tags">{stage_tags}{role_tags}</div>
  </div>
  <a href="resources/itps/{item["file"]}" download class="lib-card-dl" title="Download">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
  </a>
</div>'''

# Group by category
CAT_ORDER = [
    ("multidiscipline","Multi-Discipline"),
    ("civil","Civil"),
    ("structural","Structural"),
    ("piping","Piping"),
    ("mechanical","Mechanical"),
    ("conveyors","Conveyors & Material Handling"),
    ("electrical","Electrical & Instrumentation"),
    ("coatings","Coatings & Surface Treatment"),
]

def build_grid():
    sections = []
    for cat_key, cat_label in CAT_ORDER:
        items = [x for x in CATALOG if x["cat"] == cat_key]
        if not items:
            continue
        cards = "\n".join(card(i) for i in items)
        sections.append(f'''<div class="lib-section" data-section="{cat_key}">
  <h3 class="lib-section-heading">{cat_label}</h3>
  <div class="lib-grid">{cards}</div>
</div>''')
    return "\n".join(sections)

# ---- PODCAST EPISODES --------------------------------------------------
PODCAST_EPISODES = [
    {
        "num": 1,
        "title": "Why Most Punchlists Fail",
        "desc": "We break down the root causes behind incomplete close-out punchlists — poor ownership, late generation, and the handover rush that kills quality.",
        "duration": "34 min",
        "tags": ["Closeout", "Quality"],
    },
    {
        "num": 2,
        "title": "Hold Points vs Witness Points — What's the Difference?",
        "desc": "Engineers and inspectors often confuse these two. We explain when each applies, who owns them, and how to enforce them without killing progress.",
        "duration": "28 min",
        "tags": ["Quality", "Engineer"],
    },
    {
        "num": 3,
        "title": "The Hidden Cost of Poor ITP Compliance",
        "desc": "Non-conformances caught late cost 10x more to fix. We look at real rework scenarios and how consistent ITP sign-off prevents them.",
        "duration": "41 min",
        "tags": ["Quality", "PM"],
    },
    {
        "num": 4,
        "title": "How to Run a Pre-Construction Quality Kickoff",
        "desc": "A well-run quality kickoff sets the tone for the entire job. We walk through what to cover, who should attend, and the documents you need in the room.",
        "duration": "36 min",
        "tags": ["Preconstruction", "PM"],
    },
    {
        "num": 5,
        "title": "Writing NCRs That Actually Get Closed",
        "desc": "Most non-conformance reports sit open for weeks. We cover how to write an NCR with enough specificity that contractors can't stall on resolution.",
        "duration": "29 min",
        "tags": ["Quality", "Engineer"],
    },
    {
        "num": 6,
        "title": "Scope Creep and How to Stop It Before It Starts",
        "desc": "Scope creep rarely arrives all at once. We explore the early warning signs, how to document scope boundaries, and when to push back.",
        "duration": "45 min",
        "tags": ["PM", "Estimator"],
    },
    {
        "num": 7,
        "title": "The Scheduler's Role in Quality Management",
        "desc": "Quality milestones that aren't in the schedule don't get hit. We discuss how schedulers and QA teams need to collaborate from week one.",
        "duration": "33 min",
        "tags": ["Scheduler", "Quality"],
    },
    {
        "num": 8,
        "title": "What Great Commissioning Actually Looks Like",
        "desc": "Commissioning is where all the upstream quality problems surface at once. We look at what separates a smooth handover from a three-month battle.",
        "duration": "52 min",
        "tags": ["Closeout", "Engineer"],
    },
    {
        "num": 9,
        "title": "Building a QA Culture on Large Infrastructure Projects",
        "desc": "Culture eats process for breakfast. We talk to project leaders about what it takes to get site teams genuinely invested in quality outcomes.",
        "duration": "48 min",
        "tags": ["PM", "Quality", "HSE"],
    },
]

# Gradient pairs for thumbnail backgrounds (index → [from, to])
THUMB_GRADIENTS = [
    ("#1a1a2e", "#16213e"),
    ("#0d1b2a", "#1b4332"),
    ("#1a1a2e", "#4a1942"),
    ("#0d1b2a", "#023e8a"),
    ("#1b2838", "#3d1c02"),
    ("#0d1b2a", "#1b4332"),
    ("#1a1a2e", "#2d3561"),
    ("#0f0c29", "#302b63"),
    ("#1a1a2e", "#16213e"),
]

def podcast_card(ep):
    i = ep["num"] - 1
    g_from, g_to = THUMB_GRADIENTS[i % len(THUMB_GRADIENTS)]
    tag_html = "".join(f'<span class="pod-tag">{t}</span>' for t in ep["tags"])
    return f'''<div class="pod-card">
  <div class="pod-thumb" style="background:linear-gradient(135deg,{g_from},{g_to})">
    <div class="pod-play">
      <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="5,3 19,12 5,21"/></svg>
    </div>
    <div class="pod-ep-num">EP {ep["num"]:02d}</div>
    <div class="pod-duration">{ep["duration"]}</div>
    <div class="pod-coming-overlay">
      <span>Coming Soon</span>
    </div>
  </div>
  <div class="pod-body">
    <div class="pod-tags">{tag_html}</div>
    <p class="pod-title">{ep["title"]}</p>
    <p class="pod-desc">{ep["desc"]}</p>
  </div>
</div>'''

def build_podcast_grid():
    return "\n".join(podcast_card(ep) for ep in PODCAST_EPISODES)

# ---- ITR CHECKLIST CATALOG ---------------------------------------------

ITR_CAT_ORDER = [
    ("civil",           "Civil"),
    ("structural",      "Structural"),
    ("mechanical",      "Mechanical"),
    ("piping",          "Piping"),
    ("electrical",      "Electrical & Instrumentation"),
    ("instrumentation", "Instrumentation"),
    ("fire_gas",        "Fire & Gas"),
    ("telecoms",        "Telecoms"),
    ("architectural",   "Architectural"),
]

def itr_card(item):
    stage_tags = "".join(f'<span class="tag tag-s{s}">{STAGE_SHORT[s]}</span>' for s in item["stages"])
    role_tags  = "".join(f'<span class="tag tag-role tag-{r.lower()}">{r}</span>' for r in item["roles"])
    fmt        = item["fmt"]
    icon       = FORMAT_ICON.get(fmt, FORMAT_ICON["docx"])
    stages_data = ",".join(str(s) for s in item["stages"])
    roles_data  = ",".join(r.lower() for r in item["roles"])
    return f'''<div class="lib-card"
      data-cat="{item["cat"]}"
      data-fmt="{fmt}"
      data-stages="{stages_data}"
      data-roles="{roles_data}"
      data-title="{item["title"].lower()}">
  <div class="lib-card-icon">{icon}</div>
  <div class="lib-card-body">
    <p class="lib-card-title">{item["title"]}</p>
    <div class="lib-card-tags">{stage_tags}{role_tags}</div>
  </div>
  <a href="resources/itrs/{item["file"]}" download class="lib-card-dl" title="Download">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
  </a>
</div>'''

def build_itr_grid():
    sections = []
    for cat_key, cat_label in ITR_CAT_ORDER:
        items = [x for x in ITR_CATALOG if x["cat"] == cat_key]
        if not items:
            continue
        cards = "\n".join(itr_card(i) for i in items)
        sections.append(f'''<div class="lib-section" data-section="{cat_key}">
  <h3 class="lib-section-heading">{cat_label}</h3>
  <div class="lib-grid">{cards}</div>
</div>''')
    return "\n".join(sections)

# ---- Build full HTML ---------------------------------------------------
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Resource Library — ITP Templates &amp; More | Piksort</title>
  <meta name="description" content="Free construction resource library: Inspection &amp; Test Plan templates, checklists, forms, and guides for project teams."/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <link rel="stylesheet" href="styles.css"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js"></script>
  <script>WebFont.load({{ google: {{ families: ["Montserrat:300,400,500,600,700,800"] }} }});</script>
  <link href="https://cdn.prod.website-files.com/691a64dbefbb704b5550e811/6942965bf5e1b2e432924775_Favicon%2032.png" rel="shortcut icon" type="image/x-icon"/>

  <style>
    :root {{
      --blue: #476CFF;
      --blue-dark: #2d4fd4;
      --black: #0d0d0d;
      --gray-50: #fafafa;
      --gray-100: #f3f3f6;
      --gray-200: #e4e4ec;
      --gray-500: #6b6b75;
      --gray-700: #2c2c35;
      --white: #ffffff;
      --radius: 0.75rem;

      /* Discipline colours */
      --cat-civil:           #22863a;
      --cat-structural:      #7c3aed;
      --cat-piping:          #0369a1;
      --cat-mechanical:      #b45309;
      --cat-conveyors:       #be185d;
      --cat-electrical:      #d97706;
      --cat-coatings:        #6b7280;
      --cat-multidiscipline: #476CFF;

      /* Stage colours */
      --s1: #64748b; --s2: #0ea5e9; --s3: #8b5cf6;
      --s4: #f59e0b; --s5: #22c55e; --s6: #ef4444; --s7: #14b8a6;

      /* Role colours */
      --r-pm:        #476CFF;
      --r-engineer:  #0369a1;
      --r-quality:   #22863a;
      --r-estimator: #b45309;
      --r-scheduler: #7c3aed;
      --r-hse:       #dc2626;
    }}

    /* Nav integration */
    .nav_fixed {{ position: sticky; top: 0; z-index: 200; }}
    .page-wrapper {{ display: contents; }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Montserrat', sans-serif; background: var(--gray-100); color: var(--black); }}

    /* ── Library Layout ─────────────────────────────────────────── */
    .lib-page {{ max-width: 1400px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }}

    /* Breadcrumb */
    .lib-breadcrumb {{ display: flex; align-items: center; gap: 0.5rem;
      font-size: 0.75rem; color: var(--gray-500); margin-bottom: 1.5rem; }}
    .lib-breadcrumb a {{ color: var(--gray-500); text-decoration: none; }}
    .lib-breadcrumb a:hover {{ color: var(--blue); }}
    .lib-breadcrumb span {{ color: var(--gray-700); font-weight: 600; }}

    /* Hero */
    .lib-hero {{ margin-bottom: 2.5rem; }}
    .lib-hero h1 {{ font-size: clamp(1.75rem, 3vw, 2.5rem); font-weight: 800;
      color: var(--black); line-height: 1.15; }}
    .lib-hero p {{ margin-top: 0.5rem; color: var(--gray-500); font-size: 1rem;
      max-width: 56ch; }}

    /* Collections row */
    .lib-collections {{ display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2.5rem; }}
    .lib-coll {{ display: flex; flex-direction: column; gap: 0.35rem;
      padding: 1rem 1.25rem; border-radius: var(--radius);
      border: 1.5px solid var(--gray-200); background: var(--white);
      cursor: pointer; transition: border-color .15s, box-shadow .15s;
      min-width: 160px; text-decoration: none; position: relative; }}
    .lib-coll:hover {{ border-color: var(--blue); box-shadow: 0 2px 12px rgba(71,108,255,.12); }}
    .lib-coll.active {{ border-color: var(--blue); background: #eef1ff; box-shadow: 0 2px 12px rgba(71,108,255,.15); }}
    .lib-coll-label {{ font-size: 0.8rem; font-weight: 700; color: var(--black); }}
    .lib-coll-count {{ font-size: 0.7rem; color: var(--gray-500); font-weight: 500; }}
    .lib-coll-badge {{ position: absolute; top: 0.5rem; right: 0.6rem;
      font-size: 0.6rem; font-weight: 700; letter-spacing: .04em; text-transform: uppercase;
      color: var(--gray-500); background: var(--gray-200); border-radius: 99px;
      padding: 0.15rem 0.45rem; }}

    /* Two-col layout: sidebar + content */
    .lib-body {{ display: grid; grid-template-columns: 240px 1fr; gap: 2rem; align-items: start; }}
    @media (max-width: 900px) {{ .lib-body {{ grid-template-columns: 1fr; }} }}

    /* Sidebar */
    .lib-sidebar {{ position: sticky; top: 80px; }}
    .lib-sidebar-card {{ background: var(--white); border-radius: var(--radius);
      border: 1.5px solid var(--gray-200); padding: 1.25rem; }}
    .lib-sidebar-section {{ margin-bottom: 1.25rem; }}
    .lib-sidebar-section:last-child {{ margin-bottom: 0; }}
    .lib-sidebar-label {{ font-size: 0.65rem; font-weight: 800; letter-spacing: .08em;
      text-transform: uppercase; color: var(--gray-500); margin-bottom: 0.6rem; }}

    /* Search */
    .lib-search {{ width: 100%; border: 1.5px solid var(--gray-200); border-radius: 0.5rem;
      padding: 0.55rem 0.75rem; font-size: 0.8rem; font-family: inherit;
      color: var(--black); outline: none; transition: border-color .15s; }}
    .lib-search:focus {{ border-color: var(--blue); }}

    /* Pills */
    .pill-group {{ display: flex; flex-wrap: wrap; gap: 0.4rem; }}
    .pill {{ font-size: 0.7rem; font-weight: 600; padding: 0.25rem 0.6rem;
      border-radius: 99px; border: 1.5px solid var(--gray-200);
      background: var(--gray-50); cursor: pointer; transition: all .15s;
      user-select: none; color: var(--gray-700); }}
    .pill:hover {{ border-color: var(--blue); color: var(--blue); }}
    .pill.active {{ background: var(--blue); border-color: var(--blue); color: #fff; }}

    /* Stage pills — coloured when active */
    .pill[data-stage="1"].active  {{ background: var(--s1); border-color: var(--s1); }}
    .pill[data-stage="2"].active  {{ background: var(--s2); border-color: var(--s2); }}
    .pill[data-stage="3"].active  {{ background: var(--s3); border-color: var(--s3); }}
    .pill[data-stage="4"].active  {{ background: var(--s4); border-color: var(--s4); }}
    .pill[data-stage="5"].active  {{ background: var(--s5); border-color: var(--s5); }}
    .pill[data-stage="6"].active  {{ background: var(--s6); border-color: var(--s6); }}
    .pill[data-stage="7"].active  {{ background: var(--s7); border-color: var(--s7); }}

    /* Role pills */
    .pill[data-role="pm"].active        {{ background: var(--r-pm);        border-color: var(--r-pm); }}
    .pill[data-role="engineer"].active  {{ background: var(--r-engineer);  border-color: var(--r-engineer); }}
    .pill[data-role="quality"].active   {{ background: var(--r-quality);   border-color: var(--r-quality); }}
    .pill[data-role="estimator"].active {{ background: var(--r-estimator); border-color: var(--r-estimator); }}
    .pill[data-role="scheduler"].active {{ background: var(--r-scheduler); border-color: var(--r-scheduler); }}
    .pill[data-role="hse"].active       {{ background: var(--r-hse);       border-color: var(--r-hse); }}

    /* Discipline pills (sidebar) */
    .disc-list {{ display: flex; flex-direction: column; gap: 0.3rem; }}
    .disc-item {{ display: flex; align-items: center; gap: 0.5rem; padding: 0.3rem 0.5rem;
      border-radius: 0.4rem; cursor: pointer; transition: background .12s;
      font-size: 0.75rem; font-weight: 600; color: var(--gray-700); }}
    .disc-item:hover {{ background: var(--gray-100); }}
    .disc-item.active {{ background: var(--gray-100); color: var(--black); }}
    .disc-dot {{ width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }}

    /* Format pills */
    .fmt-pill {{ font-size: 0.65rem; }}

    /* Clear button */
    .lib-clear {{ display: none; margin-top: 0.75rem; width: 100%;
      font-size: 0.75rem; font-weight: 600; color: var(--gray-500);
      background: none; border: 1.5px solid var(--gray-200); border-radius: 0.5rem;
      padding: 0.45rem; cursor: pointer; transition: all .15s; }}
    .lib-clear:hover {{ border-color: var(--blue); color: var(--blue); }}
    .lib-clear.visible {{ display: block; }}

    /* Sidebar CTA */
    .lib-sidebar-cta {{ margin-top: 1.25rem; background: var(--blue); border-radius: var(--radius);
      padding: 1.25rem; color: #fff; text-align: center; }}
    .lib-sidebar-cta p {{ font-size: 0.8rem; font-weight: 600; line-height: 1.4; margin-bottom: 0.75rem; }}
    .lib-sidebar-cta a {{ display: inline-block; background: #fff; color: var(--blue);
      font-size: 0.75rem; font-weight: 700; padding: 0.5rem 1rem; border-radius: 0.5rem;
      text-decoration: none; transition: opacity .15s; }}
    .lib-sidebar-cta a:hover {{ opacity: 0.9; }}

    /* Active filter chips */
    .lib-chips {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.25rem; min-height: 0; }}
    .lib-chip {{ display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.2rem 0.55rem;
      border-radius: 99px; font-size: 0.7rem; font-weight: 600;
      background: var(--gray-200); color: var(--gray-700); cursor: pointer;
      border: none; transition: background .12s; }}
    .lib-chip:hover {{ background: var(--gray-300, #d1d1db); }}
    .lib-chip svg {{ width: 10px; height: 10px; }}

    /* Content header */
    .lib-content-header {{ display: flex; align-items: flex-start; gap: 1rem;
      margin-bottom: 1.5rem; padding-bottom: 1.25rem;
      border-bottom: 1.5px solid var(--gray-200); }}
    .lib-content-icon {{ width: 48px; height: 48px; border-radius: 0.75rem;
      background: #eef1ff; display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; }}
    .lib-content-icon svg {{ width: 24px; height: 24px; color: var(--blue); }}
    .lib-content-meta h2 {{ font-size: 1.2rem; font-weight: 800; color: var(--black); }}
    .lib-content-meta p {{ font-size: 0.8rem; color: var(--gray-500); margin-top: 0.25rem; }}
    .lib-count {{ font-size: 0.75rem; font-weight: 600; color: var(--gray-500);
      margin-left: auto; align-self: center; white-space: nowrap; }}

    /* Section headings */
    .lib-section {{ margin-bottom: 2rem; }}
    .lib-section-heading {{ font-size: 0.7rem; font-weight: 800; letter-spacing: .08em;
      text-transform: uppercase; color: var(--gray-500); margin-bottom: 0.75rem;
      padding-bottom: 0.4rem; border-bottom: 1px solid var(--gray-200); }}

    /* Grid */
    .lib-grid {{ display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 0.75rem; }}

    /* Card */
    .lib-card {{ background: var(--white); border: 1.5px solid var(--gray-200);
      border-radius: var(--radius); padding: 1rem;
      display: flex; align-items: flex-start; gap: 0.75rem;
      transition: border-color .15s, box-shadow .15s; position: relative; }}
    .lib-card:hover {{ border-color: var(--blue); box-shadow: 0 2px 12px rgba(71,108,255,.1); }}
    .lib-card[hidden] {{ display: none; }}
    .lib-card-icon {{ width: 36px; height: 36px; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center;
      border-radius: 0.5rem; background: var(--gray-100); }}
    .lib-card-icon svg {{ width: 18px; height: 18px; color: var(--gray-500); }}
    .lib-card-body {{ flex: 1; min-width: 0; }}
    .lib-card-title {{ font-size: 0.8rem; font-weight: 700; color: var(--black);
      line-height: 1.35; margin-bottom: 0.5rem; }}
    .lib-card-tags {{ display: flex; flex-wrap: wrap; gap: 0.3rem; }}
    .lib-card-dl {{ flex-shrink: 0; width: 28px; height: 28px; border-radius: 0.4rem;
      display: flex; align-items: center; justify-content: center;
      background: var(--gray-100); color: var(--gray-500);
      text-decoration: none; transition: background .15s, color .15s;
      align-self: flex-start; margin-top: 2px; }}
    .lib-card-dl:hover {{ background: var(--blue); color: #fff; }}
    .lib-card-dl svg {{ width: 14px; height: 14px; }}

    /* Tags */
    .tag {{ display: inline-flex; align-items: center; font-size: 0.6rem; font-weight: 700;
      padding: 0.15rem 0.45rem; border-radius: 99px; letter-spacing: .02em;
      white-space: nowrap; }}
    .tag-s1 {{ background: color-mix(in srgb, var(--s1) 12%, white); color: var(--s1); }}
    .tag-s2 {{ background: color-mix(in srgb, var(--s2) 12%, white); color: var(--s2); }}
    .tag-s3 {{ background: color-mix(in srgb, var(--s3) 12%, white); color: var(--s3); }}
    .tag-s4 {{ background: color-mix(in srgb, var(--s4) 12%, white); color: var(--s4); }}
    .tag-s5 {{ background: color-mix(in srgb, var(--s5) 12%, white); color: var(--s5); }}
    .tag-s6 {{ background: color-mix(in srgb, var(--s6) 12%, white); color: var(--s6); }}
    .tag-s7 {{ background: color-mix(in srgb, var(--s7) 12%, white); color: var(--s7); }}
    .tag-role {{ background: var(--gray-100); color: var(--gray-700); }}
    .tag-pm        {{ background: color-mix(in srgb, var(--r-pm)        12%, white); color: var(--r-pm); }}
    .tag-engineer  {{ background: color-mix(in srgb, var(--r-engineer)  12%, white); color: var(--r-engineer); }}
    .tag-quality   {{ background: color-mix(in srgb, var(--r-quality)   12%, white); color: var(--r-quality); }}
    .tag-estimator {{ background: color-mix(in srgb, var(--r-estimator) 12%, white); color: var(--r-estimator); }}
    .tag-scheduler {{ background: color-mix(in srgb, var(--r-scheduler) 12%, white); color: var(--r-scheduler); }}
    .tag-hse       {{ background: color-mix(in srgb, var(--r-hse)       12%, white); color: var(--r-hse); }}

    /* No results */
    .lib-noresults {{ display: none; text-align: center; padding: 3rem;
      color: var(--gray-500); font-size: 0.875rem; font-weight: 500; }}
    .lib-noresults.visible {{ display: block; }}

    /* ── Podcast ────────────────────────────────────────────────────── */
    #podcastView {{ display: none; }}
    #podcastView.active {{ display: block; }}

    .pod-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.25rem;
    }}

    .pod-card {{
      background: var(--white);
      border: 1.5px solid var(--gray-200);
      border-radius: var(--radius);
      overflow: hidden;
      transition: border-color .15s, box-shadow .15s;
    }}
    .pod-card:hover {{
      border-color: var(--blue);
      box-shadow: 0 4px 20px rgba(71,108,255,.12);
    }}

    .pod-thumb {{
      position: relative;
      aspect-ratio: 16/9;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    .pod-play {{
      width: 52px; height: 52px;
      border-radius: 50%;
      background: rgba(255,255,255,.15);
      backdrop-filter: blur(4px);
      border: 2px solid rgba(255,255,255,.3);
      display: flex; align-items: center; justify-content: center;
      color: #fff;
      transition: background .2s, transform .2s;
      position: relative; z-index: 1;
    }}
    .pod-play svg {{ width: 20px; height: 20px; margin-left: 3px; }}
    .pod-card:hover .pod-play {{
      background: rgba(71,108,255,.7);
      transform: scale(1.08);
    }}

    .pod-ep-num {{
      position: absolute; top: 0.75rem; left: 0.75rem;
      font-size: 0.65rem; font-weight: 800; letter-spacing: .08em;
      color: rgba(255,255,255,.7); text-transform: uppercase;
    }}
    .pod-duration {{
      position: absolute; bottom: 0.6rem; right: 0.75rem;
      font-size: 0.65rem; font-weight: 700;
      background: rgba(0,0,0,.45); color: #fff;
      padding: 0.15rem 0.45rem; border-radius: 4px;
    }}

    .pod-coming-overlay {{
      position: absolute; inset: 0;
      background: rgba(0,0,0,.42);
      display: flex; align-items: center; justify-content: center;
      z-index: 2;
    }}
    .pod-coming-overlay span {{
      font-size: 0.7rem; font-weight: 800; letter-spacing: .1em;
      text-transform: uppercase; color: rgba(255,255,255,.85);
      border: 1.5px solid rgba(255,255,255,.4);
      padding: 0.3rem 0.8rem; border-radius: 99px;
      backdrop-filter: blur(4px);
    }}

    .pod-body {{ padding: 1rem 1rem 1.1rem; }}
    .pod-tags {{ display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 0.5rem; }}
    .pod-tag {{
      font-size: 0.6rem; font-weight: 700; padding: 0.15rem 0.5rem;
      border-radius: 99px; background: var(--gray-100); color: var(--gray-700);
    }}
    .pod-title {{
      font-size: 0.875rem; font-weight: 800; color: var(--black);
      line-height: 1.3; margin-bottom: 0.5rem;
    }}
    .pod-desc {{
      font-size: 0.75rem; color: var(--gray-500); line-height: 1.55;
    }}

    /* Podcast content header */
    #podcastView .lib-content-header {{ margin-bottom: 1.5rem; }}
  </style>
</head>
<body>
<div class="page-wrapper">

{nav_raw}

<!-- Gate -->
<script>
(function(){{
  if(localStorage.getItem('piksort_subscribed')!=='true'){{
    document.body.style.visibility='hidden';
    window.location.replace('subscribe.html');
  }}else{{
    document.body.style.visibility='visible';
  }}
}})();
</script>

<div class="lib-page">

  <!-- Breadcrumb -->
  <nav class="lib-breadcrumb" aria-label="Breadcrumb">
    <a href="/">Piksort</a>
    <svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="M6 4l4 4-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/></svg>
    <span>Resource Library</span>
  </nav>

  <!-- Hero -->
  <div class="lib-hero">
    <h1>Resource Library</h1>
    <p>Free, anonymised construction templates and tools — ready to adapt for your next project.</p>
  </div>

  <!-- Collections -->
  <div class="lib-collections">
    <div class="lib-coll active" data-collection="itp">
      <span class="lib-coll-label">ITP Templates</span>
      <span class="lib-coll-count">77 templates</span>
    </div>
    <div class="lib-coll" data-collection="podcast">
      <span class="lib-coll-label">Podcast</span>
      <span class="lib-coll-count">9 episodes</span>
    </div>
    <div class="lib-coll" data-collection="checklists">
      <span class="lib-coll-label">ITR Checklists</span>
      <span class="lib-coll-count">365 checklists</span>
    </div>
    <div class="lib-coll" data-collection="forms" style="opacity:.65;pointer-events:none;">
      <span class="lib-coll-badge">Coming Soon</span>
      <span class="lib-coll-label">Forms &amp; Registers</span>
      <span class="lib-coll-count">NCR, RFI, punch lists</span>
    </div>
    <div class="lib-coll" data-collection="guides" style="opacity:.65;pointer-events:none;">
      <span class="lib-coll-badge">Coming Soon</span>
      <span class="lib-coll-label">Guides &amp; Procedures</span>
      <span class="lib-coll-count">QA/QC how-to guides</span>
    </div>
    <div class="lib-coll" data-collection="schedules" style="opacity:.65;pointer-events:none;">
      <span class="lib-coll-badge">Coming Soon</span>
      <span class="lib-coll-label">Schedule Templates</span>
      <span class="lib-coll-count">Baseline &amp; reporting</span>
    </div>
  </div>

  <!-- Body: sidebar + content -->
  <div class="lib-body">

    <!-- Sidebar -->
    <aside class="lib-sidebar">
      <div class="lib-sidebar-card">

        <div class="lib-sidebar-section">
          <div class="lib-sidebar-label">Search</div>
          <input type="search" id="libSearch" class="lib-search" placeholder="Search templates&hellip;" autocomplete="off"/>
        </div>

        <div class="lib-sidebar-section">
          <div class="lib-sidebar-label">Project Stage</div>
          <div class="pill-group" id="stagePills">
            <button class="pill" data-stage="1">S1 Initiation</button>
            <button class="pill" data-stage="2">S2 Design</button>
            <button class="pill" data-stage="3">S3 Preconstruction</button>
            <button class="pill" data-stage="4">S4 Procurement</button>
            <button class="pill" data-stage="5">S5 Construction</button>
            <button class="pill" data-stage="6">S6 Closeout</button>
            <button class="pill" data-stage="7">S7 Post-Construction</button>
          </div>
        </div>

        <div class="lib-sidebar-section">
          <div class="lib-sidebar-label">Role</div>
          <div class="pill-group" id="rolePills">
            <button class="pill" data-role="pm">PM</button>
            <button class="pill" data-role="engineer">Engineer</button>
            <button class="pill" data-role="quality">Quality</button>
            <button class="pill" data-role="estimator">Estimator</button>
            <button class="pill" data-role="scheduler">Scheduler</button>
            <button class="pill" data-role="hse">HSE</button>
          </div>
        </div>

        <div class="lib-sidebar-section">
          <div class="lib-sidebar-label">Discipline</div>
          <div class="disc-list" id="discList">
            <div class="disc-item" data-disc="all">
              <span class="disc-dot" style="background:var(--gray-500)"></span>All Disciplines
            </div>
            <div class="disc-item" data-disc="multidiscipline">
              <span class="disc-dot" style="background:var(--cat-multidiscipline)"></span>Multi-Discipline
            </div>
            <div class="disc-item" data-disc="civil">
              <span class="disc-dot" style="background:var(--cat-civil)"></span>Civil
            </div>
            <div class="disc-item" data-disc="structural">
              <span class="disc-dot" style="background:var(--cat-structural)"></span>Structural
            </div>
            <div class="disc-item" data-disc="piping">
              <span class="disc-dot" style="background:var(--cat-piping)"></span>Piping
            </div>
            <div class="disc-item" data-disc="mechanical">
              <span class="disc-dot" style="background:var(--cat-mechanical)"></span>Mechanical
            </div>
            <div class="disc-item" data-disc="conveyors">
              <span class="disc-dot" style="background:var(--cat-conveyors)"></span>Conveyors &amp; Material Handling
            </div>
            <div class="disc-item" data-disc="electrical">
              <span class="disc-dot" style="background:var(--cat-electrical)"></span>Electrical &amp; Instrumentation
            </div>
            <div class="disc-item" data-disc="coatings">
              <span class="disc-dot" style="background:var(--cat-coatings)"></span>Coatings &amp; Surface Treatment
            </div>
          </div>
        </div>

        <div class="lib-sidebar-section">
          <div class="lib-sidebar-label">Format</div>
          <div class="pill-group" id="fmtPills">
            <button class="pill fmt-pill" data-fmt="all">All</button>
            <button class="pill fmt-pill" data-fmt="xlsx">Excel</button>
            <button class="pill fmt-pill" data-fmt="pdf">PDF</button>
            <button class="pill fmt-pill" data-fmt="docx">Word</button>
          </div>
        </div>

        <button class="lib-clear" id="libClear">Clear all filters</button>
      </div>

      <div class="lib-sidebar-cta">
        <p>Get notified when new templates drop</p>
        <a href="subscribe.html">Subscribe free</a>
      </div>
    </aside>

    <!-- Content -->
    <main>
      <!-- Collection header -->
      <div class="lib-content-header">
        <div class="lib-content-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"/>
            <rect x="9" y="3" width="6" height="4" rx="1"/>
            <path d="M9 12h6M9 16h4"/>
          </svg>
        </div>
        <div class="lib-content-meta">
          <h2>ITP Templates</h2>
          <p>Anonymised Inspection &amp; Test Plan templates covering civil, structural, mechanical, piping, E&amp;I and coatings works.</p>
        </div>
        <span class="lib-count" id="libCount">77 templates</span>
      </div>

      <!-- Active filter chips -->
      <div class="lib-chips" id="libChips"></div>

      <!-- ITP grid sections -->
      <div id="libContent">
{build_grid()}
      </div>
      <div class="lib-noresults" id="libNoResults">No templates match your filters. Try clearing some filters.</div>
    </main>
  </div>

  <!-- ── CHECKLIST VIEW ── -->
  <div id="checklistView" style="display:none">
    <div class="lib-content-header">
      <div class="lib-content-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2"/>
          <rect x="9" y="3" width="6" height="4" rx="1"/>
          <polyline points="9,12 11,14 15,10"/>
        </svg>
      </div>
      <div class="lib-content-meta">
        <h2>ITR Checklists</h2>
        <p>Inspection &amp; Test Record checklists covering civil, structural, mechanical, piping, E&amp;I, fire &amp; gas, and telecoms works.</p>
      </div>
      <span class="lib-count" id="checklistCount">365 checklists</span>
    </div>
    <!-- Active filter chips for checklist view -->
    <div class="lib-chips" id="checklistChips"></div>
    <div id="checklistContent">
{build_itr_grid()}
    </div>
    <div class="lib-noresults" id="checklistNoResults">No checklists match your filters. Try clearing some filters.</div>
  </div>

  <!-- ── PODCAST VIEW (hidden until collection selected) ── -->
  <div id="podcastView">
    <div class="lib-content-header">
      <div class="lib-content-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/>
          <polygon points="10,8 16,12 10,16" fill="currentColor" stroke="none"/>
        </svg>
      </div>
      <div class="lib-content-meta">
        <h2>Podcast</h2>
        <p>Straight talk on construction quality, project controls, and what it actually takes to deliver on time.</p>
      </div>
      <span class="lib-count">9 episodes</span>
    </div>
    <div class="pod-grid">
{build_podcast_grid()}
    </div>
  </div>

</div>

<script src="piksort.js"></script>
<script>
(function(){{
  // ── State ──────────────────────────────────────────────────────────
  let activeStages = new Set();
  let activeRoles  = new Set();
  let activeDisc   = 'all';
  let activeFmt    = 'all';
  let searchQ      = '';

  const allCards = Array.from(document.querySelectorAll('.lib-card'));
  const countEl  = document.getElementById('libCount');
  const chipsEl  = document.getElementById('libChips');
  const clearBtn = document.getElementById('libClear');

  const STAGE_NAMES = {{
    '1':'S1: Initiation','2':'S2: Design','3':'S3: Preconstruction',
    '4':'S4: Procurement','5':'S5: Construction','6':'S6: Closeout','7':'S7: Post-Construction'
  }};

  // ── Filter ─────────────────────────────────────────────────────────
  function applyFilters() {{
    let visible = 0;
    const sectionsVisible = {{}};

    allCards.forEach(card => {{
      const stages = card.dataset.stages.split(',');
      const roles  = card.dataset.roles.split(',');
      const disc   = card.dataset.cat;
      const fmt    = card.dataset.fmt;
      const title  = card.dataset.title;

      const stageOk = activeStages.size === 0 || [...activeStages].some(s => stages.includes(s));
      const roleOk  = activeRoles.size === 0  || [...activeRoles].some(r => roles.includes(r));
      const discOk  = activeDisc === 'all'    || disc === activeDisc;
      const fmtOk   = activeFmt === 'all'     || fmt === activeFmt;
      const searchOk = searchQ === ''         || title.includes(searchQ.toLowerCase());

      const show = stageOk && roleOk && discOk && fmtOk && searchOk;
      card.hidden = !show;
      if (show) {{ visible++; sectionsVisible[disc] = true; }}
    }});

    // Show/hide section headings
    document.querySelectorAll('.lib-section').forEach(sec => {{
      const d = sec.dataset.section;
      const hasVisible = sec.querySelectorAll('.lib-card:not([hidden])').length > 0;
      sec.style.display = hasVisible ? '' : 'none';
    }});

    countEl.textContent = visible + ' template' + (visible===1?'':'s');
    document.getElementById('libNoResults').classList.toggle('visible', visible===0);
    renderChips();
    updateClearBtn();
  }}

  // ── Chips ──────────────────────────────────────────────────────────
  function renderChips() {{
    chipsEl.innerHTML = '';
    activeStages.forEach(s => chipsEl.appendChild(makeChip(STAGE_NAMES[s], ()=>{{ activeStages.delete(s); document.querySelector('.pill[data-stage="'+s+'"]').classList.remove('active'); applyFilters(); }})));
    activeRoles.forEach(r => chipsEl.appendChild(makeChip(r.charAt(0).toUpperCase()+r.slice(1), ()=>{{ activeRoles.delete(r); document.querySelector('.pill[data-role="'+r+'"]').classList.remove('active'); applyFilters(); }})));
    if (activeDisc !== 'all') chipsEl.appendChild(makeChip(activeDisc.charAt(0).toUpperCase()+activeDisc.slice(1), ()=>{{ activeDisc='all'; document.querySelectorAll('.disc-item').forEach(d=>d.classList.remove('active')); applyFilters(); }}));
    if (activeFmt !== 'all')  chipsEl.appendChild(makeChip(activeFmt.toUpperCase(), ()=>{{ activeFmt='all'; document.querySelector('.pill[data-fmt="all"]').classList.add('active'); document.querySelectorAll('.pill[data-fmt]:not([data-fmt="all"])').forEach(p=>p.classList.remove('active')); applyFilters(); }}));
    if (searchQ) chipsEl.appendChild(makeChip('"'+searchQ+'"', ()=>{{ searchQ=''; document.getElementById('libSearch').value=''; applyFilters(); }}));
  }}

  function makeChip(label, onRemove) {{
    const btn = document.createElement('button');
    btn.className = 'lib-chip';
    btn.innerHTML = label + '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="4" x2="12" y2="12"/><line x1="12" y1="4" x2="4" y2="12"/></svg>';
    btn.addEventListener('click', onRemove);
    return btn;
  }}

  function updateClearBtn() {{
    const hasFilter = activeStages.size || activeRoles.size || activeDisc!=='all' || activeFmt!=='all' || searchQ;
    clearBtn.classList.toggle('visible', !!hasFilter);
  }}

  // ── Stage pills ────────────────────────────────────────────────────
  document.getElementById('stagePills').addEventListener('click', e => {{
    const pill = e.target.closest('.pill[data-stage]');
    if (!pill) return;
    const s = pill.dataset.stage;
    if (activeStages.has(s)) {{ activeStages.delete(s); pill.classList.remove('active'); }}
    else {{ activeStages.add(s); pill.classList.add('active'); }}
    applyFilters();
  }});

  // ── Role pills ─────────────────────────────────────────────────────
  document.getElementById('rolePills').addEventListener('click', e => {{
    const pill = e.target.closest('.pill[data-role]');
    if (!pill) return;
    const r = pill.dataset.role;
    if (activeRoles.has(r)) {{ activeRoles.delete(r); pill.classList.remove('active'); }}
    else {{ activeRoles.add(r); pill.classList.add('active'); }}
    applyFilters();
  }});

  // ── Discipline list ────────────────────────────────────────────────
  document.getElementById('discList').addEventListener('click', e => {{
    const item = e.target.closest('.disc-item');
    if (!item) return;
    document.querySelectorAll('.disc-item').forEach(d => d.classList.remove('active'));
    item.classList.add('active');
    activeDisc = item.dataset.disc;
    applyFilters();
  }});

  // ── Format pills ───────────────────────────────────────────────────
  document.getElementById('fmtPills').addEventListener('click', e => {{
    const pill = e.target.closest('.pill[data-fmt]');
    if (!pill) return;
    document.querySelectorAll('.pill[data-fmt]').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    activeFmt = pill.dataset.fmt;
    applyFilters();
  }});
  // default fmt: all
  document.querySelector('.pill[data-fmt="all"]').classList.add('active');

  // ── Search ─────────────────────────────────────────────────────────
  document.getElementById('libSearch').addEventListener('input', e => {{
    searchQ = e.target.value.trim();
    applyFilters();
  }});

  // ── Clear ──────────────────────────────────────────────────────────
  clearBtn.addEventListener('click', () => {{
    activeStages.clear(); activeRoles.clear(); activeDisc='all'; activeFmt='all'; searchQ='';
    document.querySelectorAll('.pill').forEach(p=>p.classList.remove('active'));
    document.querySelector('.pill[data-fmt="all"]').classList.add('active');
    document.querySelectorAll('.disc-item').forEach(d=>d.classList.remove('active'));
    document.getElementById('libSearch').value='';
    applyFilters();
  }});

}})();
</script>

<script>
// ── Collection switcher ─────────────────────────────────────────────
(function(){{
  const colls         = document.querySelectorAll('.lib-coll[data-collection]');
  const itpView       = document.querySelector('.lib-body');
  const podView       = document.getElementById('podcastView');
  const checkView     = document.getElementById('checklistView');

  function showView(key) {{
    itpView.style.display   = key === 'itp'        ? '' : 'none';
    podView.classList.toggle('active', key === 'podcast');
    checkView.style.display = key === 'checklists' ? ''  : 'none';
  }}

  colls.forEach(coll => {{
    if (coll.style.pointerEvents === 'none') return;
    coll.addEventListener('click', () => {{
      colls.forEach(c => c.classList.remove('active'));
      coll.classList.add('active');
      showView(coll.dataset.collection);
    }});
  }});

  // ── Checklist filtering (mirrors ITP filter logic) ────────────────
  (function(){{
    let cStages = new Set(), cRoles = new Set(), cDisc = 'all', cFmt = 'all', cQ = '';
    const cards     = Array.from(document.querySelectorAll('#checklistContent .lib-card'));
    const countEl   = document.getElementById('checklistCount');
    const chipsEl   = document.getElementById('checklistChips');
    const clearBtn  = document.getElementById('libClear'); // shared clear button

    const STAGE_NAMES = {{
      '1':'S1: Initiation','2':'S2: Design','3':'S3: Preconstruction',
      '4':'S4: Procurement','5':'S5: Construction','6':'S6: Closeout','7':'S7: Post-Construction'
    }};

    function applyC() {{
      let visible = 0;
      cards.forEach(card => {{
        const stages = card.dataset.stages.split(',');
        const roles  = card.dataset.roles.split(',');
        const show   = (cStages.size===0 || [...cStages].some(s=>stages.includes(s)))
                    && (cRoles.size===0  || [...cRoles].some(r=>roles.includes(r)))
                    && (cDisc==='all'    || card.dataset.cat===cDisc)
                    && (cFmt==='all'     || card.dataset.fmt===cFmt)
                    && (cQ===''         || card.dataset.title.includes(cQ.toLowerCase()));
        card.hidden = !show;
        if(show) visible++;
      }});
      document.querySelectorAll('#checklistContent .lib-section').forEach(sec=>{{
        sec.style.display = sec.querySelectorAll('.lib-card:not([hidden])').length>0 ? '' : 'none';
      }});
      countEl.textContent = visible+' checklist'+(visible===1?'':'s');
      document.getElementById('checklistNoResults').classList.toggle('visible', visible===0);
      renderCChips();
      updateClearC();
    }}

    function makeChip(label, onRemove) {{
      const btn = document.createElement('button');
      btn.className = 'lib-chip';
      btn.innerHTML = label+'<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="4" x2="12" y2="12"/><line x1="12" y1="4" x2="4" y2="12"/></svg>';
      btn.addEventListener('click', onRemove);
      return btn;
    }}
    function renderCChips() {{
      chipsEl.innerHTML = '';
      cStages.forEach(s=>chipsEl.appendChild(makeChip(STAGE_NAMES[s],()=>{{cStages.delete(s);document.querySelector('.pill[data-stage="'+s+'"]').classList.remove('active');applyC();}})));
      cRoles.forEach(r=>chipsEl.appendChild(makeChip(r.charAt(0).toUpperCase()+r.slice(1),()=>{{cRoles.delete(r);document.querySelector('.pill[data-role="'+r+'"]').classList.remove('active');applyC();}})));
      if(cDisc!=='all') chipsEl.appendChild(makeChip(cDisc,()=>{{cDisc='all';document.querySelectorAll('.disc-item').forEach(d=>d.classList.remove('active'));applyC();}}));
      if(cFmt!=='all')  chipsEl.appendChild(makeChip(cFmt.toUpperCase(),()=>{{cFmt='all';document.querySelector('.pill[data-fmt="all"]').classList.add('active');document.querySelectorAll('.pill[data-fmt]:not([data-fmt="all"])').forEach(p=>p.classList.remove('active'));applyC();}}));
      if(cQ) chipsEl.appendChild(makeChip('"'+cQ+'"',()=>{{cQ='';document.getElementById('libSearch').value='';applyC();}}));
    }}
    function updateClearC(){{
      clearBtn.classList.toggle('visible', !!(cStages.size||cRoles.size||cDisc!=='all'||cFmt!=='all'||cQ));
    }}

    // Listen to the same sidebar controls, but only apply when checklist view is active
    function isChecklistActive(){{ return checkView.style.display !== 'none'; }}

    document.getElementById('stagePills').addEventListener('click', e=>{{
      if(!isChecklistActive()) return;
      const pill = e.target.closest('.pill[data-stage]'); if(!pill) return;
      const s=pill.dataset.stage;
      if(cStages.has(s)){{cStages.delete(s);pill.classList.remove('active');}}
      else{{cStages.add(s);pill.classList.add('active');}}
      applyC();
    }});
    document.getElementById('rolePills').addEventListener('click', e=>{{
      if(!isChecklistActive()) return;
      const pill=e.target.closest('.pill[data-role]'); if(!pill) return;
      const r=pill.dataset.role;
      if(cRoles.has(r)){{cRoles.delete(r);pill.classList.remove('active');}}
      else{{cRoles.add(r);pill.classList.add('active');}}
      applyC();
    }});
    document.getElementById('discList').addEventListener('click', e=>{{
      if(!isChecklistActive()) return;
      const item=e.target.closest('.disc-item'); if(!item) return;
      document.querySelectorAll('.disc-item').forEach(d=>d.classList.remove('active'));
      item.classList.add('active'); cDisc=item.dataset.disc; applyC();
    }});
    document.getElementById('fmtPills').addEventListener('click', e=>{{
      if(!isChecklistActive()) return;
      const pill=e.target.closest('.pill[data-fmt]'); if(!pill) return;
      document.querySelectorAll('.pill[data-fmt]').forEach(p=>p.classList.remove('active'));
      pill.classList.add('active'); cFmt=pill.dataset.fmt; applyC();
    }});
    document.getElementById('libSearch').addEventListener('input', e=>{{
      if(!isChecklistActive()) return;
      cQ=e.target.value.trim(); applyC();
    }});
    document.getElementById('libClear').addEventListener('click', ()=>{{
      if(!isChecklistActive()) return;
      cStages.clear();cRoles.clear();cDisc='all';cFmt='all';cQ='';
      document.querySelectorAll('.pill').forEach(p=>p.classList.remove('active'));
      document.querySelector('.pill[data-fmt="all"]').classList.add('active');
      document.querySelectorAll('.disc-item').forEach(d=>d.classList.remove('active'));
      document.getElementById('libSearch').value=''; applyC();
    }});
  }})();
}})();
</script>

</div>
</body>
</html>'''

out_path = os.path.join(BASE, 'resources.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written {len(html):,} chars to resources.html")
print(f"Total ITP entries: {len(CATALOG)}")
