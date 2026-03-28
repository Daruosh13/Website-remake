"""
build_itps.py  —  Copy and classify ITP files into piksort/resources/itps/
Run once: python build_itps.py
"""
import shutil, os

SRC_BASE = r"C:\Users\M. Gustave\Downloads\ITPs-extracted\ITPs"
SRC_LOOSE = r"C:\Users\M. Gustave\Downloads"
DEST = r"C:\Users\M. Gustave\piksort\resources\itps"

os.makedirs(DEST, exist_ok=True)

# (source_rel_to_SRC_BASE, dest_filename, category, title, description)
# If source starts with "LOOSE:", it comes from SRC_LOOSE instead
CATALOG = [
  # ── CIVIL & EARTHWORKS ────────────────────────────────────────────────
  ("CIVIL ITP MASTER_G.xlsx",
   "ITP-Civil-Works-Master.xlsx", "civil",
   "Civil Works Master ITP",
   "Comprehensive ITP covering earthworks, concrete, and general civil construction activities."),

  ("Civil ITP.xlsx",
   "ITP-Civil-General.xlsx", "civil",
   "Civil Works ITP",
   "General civil works inspection and test plan."),

  ("06705-ITP-CC-001_A ITP Civil Concrete Works.xlsx",
   "ITP-Civil-Concrete-Works.xlsx", "civil",
   "Civil Concrete Works ITP",
   "ITP for civil concrete construction including formwork, reinforcement, placement and curing."),

  ("LOOSE:NCP-NC-1507-BL-ITP-0015 Rev5 - S4 Bulk Landform.doc",
   "ITP-Bulk-Landform.doc", "civil",
   "Bulk Landform ITP",
   "ITP for bulk earthworks landform construction including compaction and surveying."),

  ("LOOSE:NCP-NC-1510-CV-ITP-0031 Rev2 - S5 Topsoil spread.doc",
   "ITP-Topsoil-Spread.doc", "civil",
   "Topsoil Spread ITP",
   "ITP for topsoil spreading and placement operations."),

  ("LOOSE:NCP-NC-1510-SD-ITP-0004 Rev2 - S6 Seeding.doc",
   "ITP-Seeding.doc", "civil",
   "Seeding and Revegetation ITP",
   "ITP for seeding and revegetation works following earthworks completion."),

  ("LOOSE:NCP-NC-1510-CV-ITP-0022 Rev1 - S5 Chute Drain.doc",
   "ITP-Chute-Drain.doc", "civil",
   "Chute Drain ITP",
   "ITP for chute drain civil construction works."),

  ("01708-ITP-QM-000_C.xlsx",
   "ITP-Earthworks-Concrete-Civil.xlsx", "civil",
   "Earthworks, Concrete and Civil Works ITP",
   "Multi-tab ITP covering earthworks, concrete works, concrete patching and repair."),

  ("Civmec/662NSC2002-2000-IT-QA-0001_0_IFU_01.pdf",
   "ITP-Underground-Services-Installation.pdf", "civil",
   "Underground Services Installation ITP",
   "ITP for underground services installation including trenching, bedding, and backfill."),

  # ── STRUCTURAL STEEL ──────────────────────────────────────────────────
  ("06702-ITP-ST-001_B ITP Structural Steel Supply and Fabrication.xlsx",
   "ITP-Structural-Steel-Supply-Fabrication.xlsx", "structural",
   "Structural Steel Supply and Fabrication ITP",
   "ITP for structural steel supply, incoming inspection, and fabrication quality control."),

  ("BGER/BGER-QA-ITP-xxxx Structural Steel Fabrication ITP Template.docx",
   "ITP-Structural-Steel-Fabrication.docx", "structural",
   "Structural Steel Fabrication ITP Template",
   "Template ITP for structural steel fabrication covering material, welding, and dimensional checks."),

  ("BGER/BGER-QA-ITP-0002 Structural Steel - Erection ITP Template.docx",
   "ITP-Structural-Steel-Erection.docx", "structural",
   "Structural Steel Erection ITP Template",
   "Template ITP for structural steel erection covering alignment, connections, and final inspection."),

  # ── PIPING ────────────────────────────────────────────────────────────
  ("06702-ITP-PP-001_B ITP Piping Supply, Fabrication and Assembly.xlsx",
   "ITP-Piping-Supply-Fabrication-Assembly-A.xlsx", "piping",
   "Piping Supply, Fabrication and Assembly ITP (Type A)",
   "ITP for full piping lifecycle: supply inspection, fabrication, assembly and hydrotesting."),

  ("06705-ITP-PP-002_A ITP Piping Supply, Fabrication and Assembly.xlsx",
   "ITP-Piping-Supply-Fabrication-Assembly-B.xlsx", "piping",
   "Piping Supply, Fabrication and Assembly ITP (Type B)",
   "Alternative ITP format for piping supply, fabrication and assembly."),

  ("03404-ITP-QA-001_ Piping Supply & Fabrication Off Site.xlsx",
   "ITP-Piping-Supply-Fabrication-Offsite.xlsx", "piping",
   "Piping Supply and Fabrication (Offsite) ITP",
   "ITP for offsite piping fabrication covering material traceability, NDE and dimensional checks."),

  ("06705-ITP-PP-001_A ITP Steel Piping Installation.xlsx",
   "ITP-Steel-Piping-Installation.xlsx", "piping",
   "Steel Piping Installation ITP",
   "ITP for steel piping installation covering fit-up, welding, supports and pressure testing."),

  ("BGER/BGER-QA-ITP-0004 Steel Piping Installation ITP Template.docx",
   "ITP-Steel-Piping-Installation-Template.docx", "piping",
   "Steel Piping Installation ITP Template",
   "Template ITP for steel piping installation on construction sites."),

  ("BGER/BGER-QA-ITP-xxxx Steel Piping Fabrication ITP Template.docx",
   "ITP-Steel-Piping-Fabrication-Template.docx", "piping",
   "Steel Piping Fabrication ITP Template",
   "Template ITP for steel piping fabrication in workshop or field settings."),

  ("BGER/BGER-QA-ITP-xxxx Polyethylene Piping Installation ITP Template.docx",
   "ITP-Polyethylene-Piping-Installation.docx", "piping",
   "Polyethylene Piping Installation ITP Template",
   "Template ITP for polyethylene (HDPE/MDPE) piping installation."),

  ("Civmec/662NSC2002-2000-IT-QA-0006_1_IFU_01.pdf",
   "ITP-Carbon-Steel-Piping-Installation.pdf", "piping",
   "Carbon Steel Piping Installation ITP",
   "ITP for carbon steel piping installation including fit-up, NDE, pressure testing and reinstatement."),

  ("Civmec/662NSC2002-2000-IT-QA-0008_1_IFU_01.pdf",
   "ITP-HDPE-Piping-Installation.pdf", "piping",
   "HDPE Piping Installation ITP",
   "ITP for HDPE piping installation including butt-fusion, electrofusion and leak testing."),

  ("Civmec/662NSC2002-2000-IT-QA-0037_0_IFU_01.pdf",
   "ITP-Lubrication-Hydraulics-Piping.pdf", "piping",
   "Lubrication and Hydraulics Piping ITP",
   "ITP for lubrication and hydraulic piping installation by subcontractor."),

  ("01743-ITP-PLN-001.xlsx",
   "ITP-Piping-Works-General.xlsx", "piping",
   "Piping Works ITP",
   "General piping works ITP covering fabrication, installation and testing activities."),

  # ── MECHANICAL EQUIPMENT ──────────────────────────────────────────────
  ("06702-ITP-ME-001_B ITP Mechanical Equipment Installation.xlsx",
   "ITP-Mechanical-Equipment-Installation-A.xlsx", "mechanical",
   "Mechanical Equipment Installation ITP (Type A)",
   "ITP for mechanical equipment installation including receipt, alignment, grouting and commissioning readiness."),

  ("06705-ITP-ME-001_A ITP Mechanical Equipment Installation.xlsx",
   "ITP-Mechanical-Equipment-Installation-B.xlsx", "mechanical",
   "Mechanical Equipment Installation ITP (Type B)",
   "Alternative ITP format for mechanical equipment installation."),

  ("BGER/BGER-QA-ITP-xxxx Mechanical Equipment Installation ITP Template.docx",
   "ITP-Mechanical-Equipment-Installation-Template.docx", "mechanical",
   "Mechanical Equipment Installation ITP Template",
   "Template ITP for static and rotating mechanical equipment installation."),

  ("Civmec/662NSC2002-2000-IT-QA-0004_1_IFU_01.pdf",
   "ITP-Mechanical-Installation-General.pdf", "mechanical",
   "Mechanical Installation (General) ITP",
   "General mechanical installation ITP applicable to standard equipment items."),

  ("06702-ITP-ME-002_0 ITP Pressure Vessel Fabrication.xlsx",
   "ITP-Pressure-Vessel-Fabrication.xlsx", "mechanical",
   "Pressure Vessel Fabrication ITP",
   "ITP for pressure vessel fabrication covering material, welding, NDE, PWHT and hydrotesting."),

  ("Civmec/662NSC2002-2000-IT-QA-0010_3_IFU_01.pdf",
   "ITP-Pump-Installation.pdf", "mechanical",
   "Pump Installation ITP",
   "ITP for pump installation covering base preparation, alignment, shaft coupling and mechanical seal."),

  ("Civmec/662NSC2002-2000-IT-QA-0011_1_IFU_01.pdf",
   "ITP-Gyratory-Crusher-Installation.pdf", "mechanical",
   "Gyratory Crusher Installation ITP",
   "ITP for gyratory crusher installation including foundation, mainframe erection, and final alignment."),

  ("Civmec/662NSC2002-2000-IT-QA-0014_2_IFU_01.pdf",
   "ITP-Cone-Crusher-Installation.pdf", "mechanical",
   "Cone Crusher Installation ITP",
   "ITP for cone crusher installation covering assembly, lubrication and pre-commissioning checks."),

  ("Civmec/662NSC2002-2000-IT-QA-0013_1_IFU_01.pdf",
   "ITP-Rock-Breaker-Installation.pdf", "mechanical",
   "Rock Breaker Installation ITP",
   "ITP for rock breaker installation including boom, hydraulic lines and operational checks."),

  ("Civmec/662NSC2002-2000-IT-QA-0012_1_IFU_01.pdf",
   "ITP-Low-Profile-Feeder-Installation.pdf", "mechanical",
   "Low Profile Feeder Installation ITP",
   "ITP for low profile feeder installation covering support structure, drive, and belt tracking."),

  ("Civmec/662NSC2002-2000-IT-QA-0016_0_IFU_01.pdf",
   "ITP-Belt-Feeder-Installation.pdf", "mechanical",
   "Belt Feeder Installation ITP",
   "ITP for belt feeder installation including structure, conveyor belt, drive and idlers."),

  ("Civmec/662NSC2002-2000-IT-QA-0017_1_IFU_01.pdf",
   "ITP-Apron-Feeder-Installation.pdf", "mechanical",
   "Apron Feeder Installation ITP",
   "ITP for apron feeder installation covering pan chain assembly, drive, and alignment."),

  ("Civmec/662NSC2002-2000-IT-QA-0024_1_IFU_01.pdf",
   "ITP-HPGR-Installation.pdf", "mechanical",
   "HPGR Installation ITP",
   "ITP for High Pressure Grinding Roll (HPGR) installation including frame, rolls, and drive assembly."),

  ("Civmec/662NSC2002-2000-IT-QA-0022_1_IFU_01.pdf",
   "ITP-Dry-Vibrating-Screen-Installation.pdf", "mechanical",
   "Dry Vibrating Screen Installation ITP",
   "ITP for dry vibrating screen installation including structure, exciter, and screen media."),

  ("Civmec/662NSC2002-2000-IT-QA-0027_0_IFU_01.pdf",
   "ITP-Air-Classifier-Installation.pdf", "mechanical",
   "Air Classifier Installation ITP",
   "ITP for air classifier installation covering structural support, fan, and process ductwork."),

  ("Civmec/662NSC2002-2000-IT-QA-0028_1_IFU_01.pdf",
   "ITP-Baghouse-Installation.pdf", "mechanical",
   "Baghouse Installation ITP",
   "ITP for product baghouse installation including structure, filter bags, and fan assembly."),

  ("Civmec/662NSC2002-2000-IT-QA-0003_2_IFU_01.pdf",
   "ITP-Bin-Chute-Installation.pdf", "mechanical",
   "Bin and Chute Installation ITP",
   "ITP for bin and chute installation covering structural assembly, liner installation and weld inspection."),

  ("Civmec/662NSC2002-2000-IT-QA-0015_1_IFU_01.pdf",
   "ITP-Isolation-Gate-Installation.pdf", "mechanical",
   "Isolation Gate Installation ITP",
   "ITP for isolation gate installation including frame, gate blade, actuator and leak test."),

  # ── CONVEYORS & MATERIAL HANDLING ─────────────────────────────────────
  ("Civmec/662NSC2002-2000-IT-QA-0005_1_IFU_01.pdf",
   "ITP-Conveyor-Installation.pdf", "conveyors",
   "Conveyor Installation ITP",
   "ITP for belt conveyor installation including structure, idlers, drive, belt and tensioning."),

  ("Civmec/662NSC2002-2000-IT-QA-0038_0_IFU_01.pdf",
   "ITP-Steel-Cord-Conveyor-Belt-Installation.pdf", "conveyors",
   "Steel Cord Conveyor Belt Installation ITP",
   "ITP for steel cord conveyor belt installation including splice procedures and load testing."),

  ("Civmec/662NSC2002-2000-IT-QA-0039_0_IFU_01.pdf",
   "ITP-Fabric-Conveyor-Belt-Installation.pdf", "conveyors",
   "Fabric Conveyor Belt Installation ITP",
   "ITP for fabric conveyor belt installation including vulcanised and mechanical splicing."),

  ("P1000-V2325-G01-001_C_Belt Weigher.pdf",
   "ITP-Belt-Weigher.pdf", "conveyors",
   "Belt Weigher ITP",
   "ITP for belt weigher installation, calibration and commissioning verification."),

  ("P1000-V2334-G01-200_A_Belt Scraper.pdf",
   "ITP-Belt-Scraper.pdf", "conveyors",
   "Belt Scraper ITP",
   "ITP for belt scraper installation and adjustment."),

  ("P1000-V2395-G01-001_B_Metal Detector.pdf",
   "ITP-Metal-Detector.pdf", "conveyors",
   "Metal Detector ITP",
   "ITP for metal detector installation, sensitivity testing and functional verification."),

  # ── ELECTRICAL & INSTRUMENTATION ──────────────────────────────────────
  ("06702-ITP-EL-001_C ITP Electrical & Instrumentation.xlsx",
   "ITP-Electrical-Instrumentation-A.xlsx", "electrical",
   "Electrical and Instrumentation ITP (Type A)",
   "Comprehensive ITP for E&I installation including cable installation, termination, and loop testing."),

  ("06705-ITP-EL-001_C ITP Electrical  Instrumentation.xlsx",
   "ITP-Electrical-Instrumentation-B.xlsx", "electrical",
   "Electrical and Instrumentation ITP (Type B)",
   "Alternative E&I ITP covering installation, continuity testing, IR testing and functional checks."),

  ("05503-ITP-QA-003_B.xlsx",
   "ITP-Electrical-Instrumentation-Hazardous-Area.xlsx", "electrical",
   "Electrical and Instrumentation ITP (Hazardous Areas)",
   "ITP for E&I installation in hazardous areas per AS/NZS 3000 and AS60079 requirements."),

  ("BGER/BGER-QA-ITP-xxxx_A Aboveground cable ladder, tray and conduit installation.docx",
   "ITP-Cable-Ladder-Tray-Conduit.docx", "electrical",
   "Cable Ladder, Tray and Conduit Installation ITP",
   "ITP for aboveground cable ladder, cable tray and conduit installation."),

  ("BGER/BGER-QA-ITP-xxxx_A Earthing installation and termination.docx",
   "ITP-Earthing-Installation-Termination.docx", "electrical",
   "Earthing Installation and Termination ITP",
   "ITP for earthing system installation and termination activities."),

  ("BGER/BGER-QA-ITP-xxxx_A Electrical equipment installation.docx",
   "ITP-Electrical-Equipment-Installation.docx", "electrical",
   "Electrical Equipment Installation ITP",
   "ITP for electrical equipment installation including switchgear, MCC, and distribution boards."),

  ("BGER/BGER-QA-ITP-xxxx_A Lighting and small power equipment installation.docx",
   "ITP-Lighting-Small-Power-Installation.docx", "electrical",
   "Lighting and Small Power Equipment ITP",
   "ITP for lighting and small power equipment installation and testing."),

  ("Civmec/662NSC2002-2000-IT-QA-0029_1_IFU_01.pdf",
   "ITP-EI-Primary-Crusher-A.pdf", "electrical",
   "E&I Installation ITP — Primary Crusher Area A",
   "Area-specific E&I ITP for primary crusher area A installation and commissioning."),

  ("Civmec/662NSC2002-2000-IT-QA-0030_1_IFU_01.pdf",
   "ITP-EI-Primary-Crusher-B.pdf", "electrical",
   "E&I Installation ITP — Primary Crusher Area B",
   "Area-specific E&I ITP for primary crusher area B installation and commissioning."),

  ("Civmec/662NSC2002-2000-IT-QA-0031_1_IFU_01.pdf",
   "ITP-EI-Secondary-Crusher-A.pdf", "electrical",
   "E&I Installation ITP — Secondary Crusher Area A",
   "Area-specific E&I ITP for secondary crusher area A."),

  ("Civmec/662NSC2002-2000-IT-QA-0032_1_IFU_01.pdf",
   "ITP-EI-Secondary-Crusher-B.pdf", "electrical",
   "E&I Installation ITP — Secondary Crusher Area B",
   "Area-specific E&I ITP for secondary crusher area B."),

  ("Civmec/662NSC2002-2000-IT-QA-0033_1_IFU_01.pdf",
   "ITP-EI-Coarse-Ore-Stockpile.pdf", "electrical",
   "E&I Installation ITP — Coarse Ore Stockpile",
   "Area-specific E&I ITP for coarse ore stockpile area."),

  ("Civmec/662NSC2002-2000-IT-QA-0034_1_IFU_01.pdf",
   "ITP-EI-Tertiary-Crushing.pdf", "electrical",
   "E&I Installation ITP — Tertiary Crushing",
   "Area-specific E&I ITP for tertiary crushing circuit."),

  ("Civmec/662NSC2002-2000-IT-QA-0035_1_IFU_01.pdf",
   "ITP-EI-Dry-Magnetic-Separation-A.pdf", "electrical",
   "E&I Installation ITP — Dry Magnetic Separation A",
   "Area-specific E&I ITP for dry magnetic separation circuit A."),

  ("Civmec/662NSC2002-2000-IT-QA-0036_1_IFU_01.pdf",
   "ITP-EI-Dry-Magnetic-Separation-B.pdf", "electrical",
   "E&I Installation ITP — Dry Magnetic Separation B",
   "Area-specific E&I ITP for dry magnetic separation circuit B."),

  ("Civmec/662NSC2002-2000-IT-QA-0040_1_IFU_01.pdf",
   "ITP-EI-Air-Classification-A.pdf", "electrical",
   "E&I Installation ITP — Air Classification A",
   "Area-specific E&I ITP for air classification circuit A."),

  ("Civmec/662NSC2002-2000-IT-QA-0041_1_IFU_01.pdf",
   "ITP-EI-Air-Classification-B.pdf", "electrical",
   "E&I Installation ITP — Air Classification B",
   "Area-specific E&I ITP for air classification circuit B."),

  ("Civmec/662NSC2002-2000-IT-QA-0042_1_IFU_01.pdf",
   "ITP-EI-Primary-Grinding-A.pdf", "electrical",
   "E&I Installation ITP — Primary Grinding A",
   "Area-specific E&I ITP for primary grinding circuit A."),

  ("Civmec/662NSC2002-2000-IT-QA-0043_1_IFU_01.pdf",
   "ITP-EI-Primary-Grinding-B.pdf", "electrical",
   "E&I Installation ITP — Primary Grinding B",
   "Area-specific E&I ITP for primary grinding circuit B."),

  ("Civmec/662NSC2002-2000-IT-QA-0044_1_IFU_01.pdf",
   "ITP-EI-Dry-Tailings.pdf", "electrical",
   "E&I Installation ITP — Dry Tailings",
   "Area-specific E&I ITP for dry tailings handling area."),

  # ── COATINGS & SURFACE TREATMENT ──────────────────────────────────────
  ("Civmec/662NSC2002-2000-IT-QA-0009_2_IFU_01.pdf",
   "ITP-Surface-Treatment-Repair.pdf", "coatings",
   "Surface Treatment Repair ITP",
   "ITP for surface treatment and coating repair works in field."),

  ("Civmec/662NSC2002-2000-IT-QA-0007_2_IFU_01.pdf",
   "ITP-Grouting-Cementitious-Epoxy.pdf", "coatings",
   "Grouting ITP (Cementitious and Epoxy)",
   "ITP for cementitious and epoxy grouting of equipment bases and structural foundations."),

  ("06705-ITP-ME-002_A ITP High Build Epoxy Coating.xlsx",
   "ITP-High-Build-Epoxy-Coating.xlsx", "coatings",
   "High Build Epoxy Coating ITP",
   "ITP for high build epoxy coating application covering surface preparation, application and DFT checks."),

  ("FMG Treatment ITP.xlsx",
   "ITP-Protective-Coatings-Treatment.xlsx", "coatings",
   "Protective Coatings Treatment ITP",
   "ITP for protective coatings and surface treatment works."),

  # ── MULTI-DISCIPLINE ──────────────────────────────────────────────────
  ("02707-ITP-QA-001_A.xlsx",
   "ITP-Civil-Structural-Mechanical-Site-Installation.xlsx", "multidiscipline",
   "Civil, Structural and Mechanical Site Installation ITP",
   "Combined ITP for civil, structural and mechanical works on a single site installation package."),

  ("04204-ITP-QA-000_A.xlsx",
   "ITP-Fuel-Lubricant-Storage-Facility.xlsx", "multidiscipline",
   "Fuel and Lubricant Storage Facility ITP",
   "ITP for construction of fuel and lubricant storage infrastructure including civil, piping and mechanical."),

  ("02704-ITP-QA-MASTER_E.xlsx",
   "ITP-Industrial-Facility-Master.xlsx", "multidiscipline",
   "Industrial Facility Construction — Master ITP",
   "Master ITP covering all disciplines for industrial facility construction."),

  ("02704-ITP-MATRIX_A.xlsx",
   "ITP-Piping-Mechanical-Structural-Civil-Matrix.xlsx", "multidiscipline",
   "ITP Matrix — Piping, Mechanical, Structural and Civil",
   "ITP matrix document integrating piping, mechanical, structural and civil inspection hold points."),

  ("01707-ITP-QA-000_B.xlsx",
   "ITP-Sustaining-Works-Multi-Discipline.xlsx", "multidiscipline",
   "Sustaining Works Multi-Discipline ITP",
   "Multi-discipline ITP register for sustaining capital works across civil, piping and structural scopes."),

  ("01709-ITP-QA-000_A.xlsx",
   "ITP-Multi-Site-Piping-Works.xlsx", "multidiscipline",
   "Multi-Site Piping Works ITP",
   "ITP for piping works executed across multiple site locations."),
]

ok, fail = 0, 0
for entry in CATALOG:
    src_rel, dest_name, cat, title, desc = entry
    if src_rel.startswith("LOOSE:"):
        src = os.path.join(SRC_LOOSE, src_rel[6:])
    else:
        src = os.path.join(SRC_BASE, src_rel)
    dest = os.path.join(DEST, dest_name)
    if os.path.exists(src):
        shutil.copy2(src, dest)
        ok += 1
    else:
        print(f"MISSING: {src}")
        fail += 1

print(f"\nDone. Copied: {ok}  |  Missing: {fail}")
