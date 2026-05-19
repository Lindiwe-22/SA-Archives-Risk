import streamlit as st
import pandas as pd

st.set_page_config(page_title="Policy Recommendations", page_icon="📋", layout="wide")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Source+Serif+4:wght@300;400;600&family=JetBrains+Mono:wght@400;500&display=swap');
  [data-testid="stAppViewContainer"] { background: #F7F3EE; font-family: 'Source Serif 4', Georgia, serif; }
  [data-testid="stSidebar"] { background: #1C1917; border-right: 1px solid #292524; }
  [data-testid="stSidebar"] * { color: #D6D3D1 !important; }
  h1, h2, h3 { font-family: 'Playfair Display', Georgia, serif !important; color: #1C1917 !important; }
  p, li { font-family: 'Source Serif 4', Georgia, serif; color: #44403C; font-size: 15px; line-height: 1.8; }
  .divider { border: none; border-top: 1px solid #D6D3D1; margin: 32px 0; }
  .fire-box { background: #FEF3C7; border-left: 5px solid #D97706; border-radius: 0 6px 6px 0; padding: 16px 20px; margin: 18px 0; }
  .fire-box p { color: #92400E; font-size: 14.5px; margin: 0; }
  .critical-box { background: #FEF2F2; border-left: 5px solid #DC2626; border-radius: 0 6px 6px 0; padding: 16px 20px; margin: 18px 0; }
  .critical-box p { color: #7F1D1D; font-size: 14.5px; margin: 0; }
  .source-box { background: #F0FDF4; border-left: 5px solid #16A34A; border-radius: 0 6px 6px 0; padding: 14px 18px; margin: 14px 0; }
  .source-box p { color: #14532D; font-size: 12px; margin: 0; font-family: 'JetBrains Mono', monospace; }
  .info-box { background: #EFF6FF; border-left: 5px solid #2563EB; border-radius: 0 6px 6px 0; padding: 16px 20px; margin: 18px 0; }
  .info-box p { color: #1E3A5F; font-size: 14.5px; margin: 0; }
  #MainMenu { visibility: hidden; } footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("# 📋 Policy Recommendations")
st.markdown("### Eight evidence-based actions South Africa must take — now")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("""
The risk dashboard identifies the problem. The priority score orders the interventions.
This page provides the concrete, actionable recommendations — each tied to a specific
finding, a responsible institution, and a funding pathway where one exists.
""")

st.markdown("""
<div class="critical-box">
<p>
  <strong>The window is closing.</strong> The Botha Sigcau Building was flagged as unsafe
  before it burned. The Lebowa archives have been documented as a deteriorating heap
  since at least 2013. The Ciskei archives have been in private hands for 30 years.
  Each of these situations was known. None was acted upon. The question is not whether
  South Africa can afford to digitise its archives. It is whether it can afford not to.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── National recommendations ───────────────────────────────────────────────────
st.markdown("## National Recommendations")

national_recs = [
    {
        "num": "01",
        "title": "Declare Eastern Cape and Limpopo Archives a National Emergency",
        "urgency": "Immediate",
        "responsible": "DSAC + NARSSA + DPWI",
        "finding": "EC scores 10/10 risk. 3 fire incidents since 2021. Limpopo carries 3 Bantustan archives.",
        "action": """Activate NARSSA emergency protocols. Commission an immediate physical condition
assessment of all EC and Limpopo repositories. Install fire suppression and humidity
monitoring in the Lebowakgomo basement within 90 days. Declare the Transkei Archives
(Mthatha) a protected site under the National Heritage Resources Act.""",
        "funding": "Emergency DPWI infrastructure allocation. DSAC discretionary budget.",
        "source": "saarchivist.co.za · UCT APC Research Initiative (2013)",
        "color": "#DC2626",
    },
    {
        "num": "02",
        "title": "Adopt AtoM as the National Digitisation Standard",
        "urgency": "Within 6 months",
        "responsible": "NARSSA + DSAC + All Provincial Archives",
        "finding": "AtoM is free, open-source, ICA-compliant and already deployed in SA at Wits and WC.",
        "action": """Mandate AtoM (Access to Memory — accesstomemory.org) as the national standard
for archival description and digital access. The Western Cape and Wits Historical Papers
have already proven the implementation. This eliminates the technology barrier entirely —
the only remaining barriers are political will and capacity.""",
        "funding": "Zero licensing cost. Implementation cost only — covered by existing DSAC ICT budget.",
        "source": "accesstomemory.org · researcharchives.wits.ac.za",
        "color": "#2563EB",
    },
    {
        "num": "03",
        "title": "Complete the NAAIRS Migration as a National Priority",
        "urgency": "Within 12 months",
        "responsible": "NARSSA + SITA",
        "finding": "8.3 million records mid-migration. More than half of all holdings not yet in NAAIRS.",
        "action": """Treat the NAAIRS-to-new-database migration as a critical national infrastructure
project. Assign dedicated SITA capacity. Set a public completion target with parliamentary
reporting. Every month of delay is a month during which a fire, flood or infrastructure
failure could destroy records that are not yet catalogued.""",
        "funding": "Existing NARSSA + SITA operational budgets. No new spend required.",
        "source": "nationalarchives.gov.za/node/737 · national.archives.gov.za/naairsintro.htm",
        "color": "#7C3AED",
    },
    {
        "num": "04",
        "title": "Establish a Bantustan Archives Recovery Programme",
        "urgency": "Within 12 months",
        "responsible": "DSAC + NARSSA + Presidency",
        "finding": "10 former homeland archives. Under-resourced for 30 years. Correlation with risk r=0.835.",
        "action": """Create a dedicated, ring-fenced funding programme specifically for the digitisation
and cataloguing of former Bantustan archives — Transkei, KwaZulu, Lebowa, Gazankulu,
Venda, Bophuthatswana, Qwaqwa, KaNgwane, KwaNdebele, and Ciskei. These records document
the lives of millions of South Africans dispossessed by apartheid. Their digitisation
is not an archival matter. It is a justice matter.""",
        "funding": "Presidential Employment Stimulus — R30M precedent from 2020/21 (453 youth deployed).",
        "source": "Wits People's Guide to Archives · DSAC Parliamentary Q 2020/21",
        "color": "#D97706",
    },
    {
        "num": "05",
        "title": "Submit PAIA Requests for Province-Level Digitisation Data",
        "urgency": "Within 30 days",
        "responsible": "Civil society + Journalists + Researchers",
        "finding": "Province-level digitisation progress is not publicly available. 51% of this analysis is estimated.",
        "action": """Lodge Promotion of Access to Information Act (PAIA) requests with each provincial
Department of Sport, Arts and Culture asking for: total records held, total records
digitised, active digitisation programme status, and digitisation budget for the last
3 financial years. Contact NARSSA directly at naairs@dac.gov.za for national breakdowns.
Publish all responses publicly.""",
        "funding": "No cost. PAIA requests are free to submit.",
        "source": "PAIA Act 2 of 2000 · naairs@dac.gov.za",
        "color": "#16A34A",
    },
    {
        "num": "06",
        "title": "Western Cape Knowledge Transfer Programme",
        "urgency": "Within 6 months",
        "responsible": "WC Provincial Archives + NARSSA + Critical Risk Provinces",
        "finding": "WC scores 0/10 risk — the same outcome is possible elsewhere with investment.",
        "action": """Commission the Western Cape Archives to lead a formal knowledge transfer programme
to Critical Risk provinces — sharing AtoM implementation methodology, staff training
protocols, digitisation workflows and ECM system configuration. This costs a fraction
of building new capacity from scratch in each province.""",
        "funding": "DSAC intergovernmental relations budget. WC capacity-sharing allocation.",
        "source": "WC Govt ICT Annual Report · accesstomemory.org",
        "color": "#16A34A",
    },
]

for rec in national_recs:
    with st.expander(
        f"Recommendation {rec['num']} — {rec['title']} · {rec['urgency']}",
        expanded=False
    ):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
<div style="margin-bottom:12px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10.5px;
              color:{rec['color']}; margin-bottom:6px;">
    ⏱ {rec['urgency']} &nbsp;·&nbsp; 🏛️ {rec['responsible']}
  </div>
  <div style="font-size:14px; color:#57534E; margin-bottom:14px;
              font-style:italic;">
    Finding: {rec['finding']}
  </div>
  <div style="font-size:14.5px; color:#1C1917; line-height:1.8;">
    {rec['action']}
  </div>
</div>
""", unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
<div style="background:#FAFAF9; border:1px solid #E7E5E4; border-radius:8px; padding:14px 16px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#78716C;
              text-transform:uppercase; margin-bottom:6px;">Funding Pathway</div>
  <div style="font-size:12.5px; color:#44403C; line-height:1.6;">{rec['funding']}</div>
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#78716C;
              text-transform:uppercase; margin-top:10px; margin-bottom:6px;">Source</div>
  <div style="font-size:11.5px; color:#78716C;">{rec['source']}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Lebowa case study ──────────────────────────────────────────────────────────
st.markdown("## Case Study — The Lebowa Archive Action Plan")
st.markdown("*The most documented example of archival neglect in South Africa — and a concrete roadmap to fix it.*")

st.markdown("""
<div class="fire-box">
<p>
  <strong>The situation (sourced):</strong> The Lebowa archives are housed in the basement
  of the old legislative buildings in Lebowakgomo — the former capital of the Lebowa
  Bantustan. They are spread across four rooms and along the walls of a passage. They
  are only partially catalogued, not digitised, and at times described as a random heap
  of papers. This was documented by UCT researchers in 2013. Nothing has changed since.
</p>
</div>
""", unsafe_allow_html=True)

phases = [
    {
        "phase": "Phase 1",
        "timeline": "0–3 months",
        "title": "Physical Stabilisation",
        "color": "#DC2626",
        "actions": [
            "Install fire suppression system in Lebowakgomo basement",
            "Install humidity and temperature monitoring",
            "Conduct pest control assessment and treatment",
            "Prevent any further physical deterioration before records are moved",
            "Commission structural safety assessment of the building",
        ],
        "responsible": "DPWI + DSAC",
        "funding": "Emergency DPWI infrastructure allocation",
    },
    {
        "phase": "Phase 2",
        "timeline": "3–6 months",
        "title": "Rapid Cataloguing",
        "color": "#D97706",
        "actions": [
            "Deploy qualified archivists to create a basic inventory of all records",
            "Box and label all loose records before any digitisation begins",
            "Document record type, approximate date, department of origin",
            "Partner with Unisa and University of Limpopo archivist programmes",
            "Produce a publicly available catalogue of what the Lebowa archives contain",
        ],
        "responsible": "NARSSA + Limpopo Provincial Archives",
        "funding": "NARSSA operational budget + university partnership",
    },
    {
        "phase": "Phase 3",
        "timeline": "6–18 months",
        "title": "Digitisation",
        "color": "#2563EB",
        "actions": [
            "Deploy high-volume scanners from NARSSA 2020/21 stimulus equipment",
            "Recruit youth via Presidential Employment Stimulus — 453 youth precedent",
            "Prioritise records most at physical risk — deteriorating paper, water damage",
            "Upload to AtoM (Access to Memory) for structured, searchable access",
            "Back up to both local server and cloud storage simultaneously",
        ],
        "responsible": "NARSSA + DSAC + Presidency (Employment Stimulus)",
        "funding": "Presidential Employment Stimulus — R30M precedent from 2020/21",
    },
    {
        "phase": "Phase 4",
        "timeline": "18–24 months",
        "title": "Public Access",
        "color": "#16A34A",
        "actions": [
            "Migrate digitised records to NAAIRS for national public access",
            "Index by record type, date range, department, subject and geographic area",
            "Notify communities in former Lebowa areas that records are accessible",
            "Publish a public completion report — what was preserved and what was lost",
            "Establish ongoing maintenance and digitisation protocol for future records",
        ],
        "responsible": "NARSSA",
        "funding": "NARSSA operational budget — no new spend required at this stage",
    },
]

for phase in phases:
    st.markdown(f"""
<div style="background:white; border:1px solid #E7E5E4; border-left:4px solid {phase['color']};
            border-radius:0 10px 10px 0; padding:22px 26px; margin-bottom:14px;">
  <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">
    <div style="min-width:120px;">
      <div style="font-family:'JetBrains Mono',monospace; font-size:11px;
                  color:{phase['color']}; font-weight:600;">{phase['phase']}</div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:11px;
                  color:#78716C;">{phase['timeline']}</div>
      <div style="font-family:'Playfair Display',serif; font-size:16px;
                  font-weight:700; color:#1C1917; margin-top:6px;">{phase['title']}</div>
    </div>
    <div style="flex:1; min-width:280px;">
      <ul style="margin:0; padding-left:18px; font-size:13.5px;
                 color:#44403C; line-height:2.0;">
        {''.join(f'<li>{a}</li>' for a in phase['actions'])}
      </ul>
      <div style="margin-top:12px; font-size:12.5px; color:#78716C;
                  font-family:'JetBrains Mono',monospace;">
        Responsible: {phase['responsible']} &nbsp;·&nbsp; Funding: {phase['funding']}
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="source-box">
<p>
  Lebowa archive condition: UCT Archive &amp; Public Culture Research Initiative (2013) ·
  Funding precedent: DSAC Parliamentary Q 2020/21 (R30M, 453 youth) ·
  AtoM platform: accesstomemory.org · NAAIRS: nationalarchives.gov.za
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Accountability gaps ────────────────────────────────────────────────────────
st.markdown("## Unresolved Accountability Gaps")
st.markdown("*Two situations that require parliamentary and legal intervention, not just digitisation budgets.*")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
<div style="background:white; border:1px solid #E7E5E4; border-top:4px solid #DC2626;
            border-radius:10px; padding:22px 24px; height:100%;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:11px;
              color:#DC2626; margin-bottom:10px;">ACCOUNTABILITY GAP 01</div>
  <div style="font-family:'Playfair Display',serif; font-size:17px;
              font-weight:700; color:#1C1917; margin-bottom:12px;">
    The Ciskei Archives — 30 Years in Private Hands
  </div>
  <p style="font-size:13.5px; color:#44403C; line-height:1.8;">
    Unlike every other former Bantustan, the Ciskei archives are held privately
    and are very difficult to access. The identity of the custodian is not publicly
    known. These records document the lives of millions of Xhosa-speaking South Africans
    assigned Ciskeian citizenship under apartheid — including land records, identity
    documents and administrative files critical to resolving present-day claims.
  </p>
  <div style="margin-top:14px; font-size:13px; color:#7F1D1D; font-weight:600;">
    Required action:
  </div>
  <ul style="font-size:13px; color:#44403C; line-height:2.0; padding-left:18px;">
    <li>Parliamentary question to Minister of DSAC</li>
    <li>PAIA request to Eastern Cape Provincial Archives</li>
    <li>NARSSA investigation under the National Archives Act</li>
    <li>Public naming of custodian and legal basis for private retention</li>
  </ul>
  <div style="font-family:'JetBrains Mono',monospace; font-size:11px;
              color:#78716C; margin-top:12px;">
    Source: Wits People's Guide to Archives
  </div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div style="background:white; border:1px solid #E7E5E4; border-top:4px solid #D97706;
            border-radius:10px; padding:22px 24px; height:100%;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:11px;
              color:#D97706; margin-bottom:10px;">ACCOUNTABILITY GAP 02</div>
  <div style="font-family:'Playfair Display',serif; font-size:17px;
              font-weight:700; color:#1C1917; margin-bottom:12px;">
    The KwaNdebele Archives — Location Unknown
  </div>
  <p style="font-size:13.5px; color:#44403C; line-height:1.8;">
    The archives of the former KwaNdebele Bantustan cannot be definitively located.
    They may be partially deposited in Nelspruit (Mpumalanga), but this has not been
    confirmed. A Bantustan whose records cannot be found is a distinct category of
    risk — loss may already have occurred. The communities of the former KwaNdebele
    deserve to know what happened to their administrative history.
  </p>
  <div style="margin-top:14px; font-size:13px; color:#92400E; font-weight:600;">
    Required action:
  </div>
  <ul style="font-size:13px; color:#44403C; line-height:2.0; padding-left:18px;">
    <li>Parliamentary question to DSAC on KwaNdebele archive location</li>
    <li>NARSSA investigation mandate — locate and assess condition</li>
    <li>Mpumalanga Provincial Archives formal inventory request</li>
    <li>Public report on findings within 6 months</li>
  </ul>
  <div style="font-family:'JetBrains Mono',monospace; font-size:11px;
              color:#78716C; margin-top:12px;">
    Source: Wits People's Guide to Archives (location unconfirmed)
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Closing ────────────────────────────────────────────────────────────────────
st.markdown("## A Final Note")

st.markdown("""
<div class="info-box">
<p>
  <strong>This analysis was built from public data — parliamentary questions, academic
  research, news archives and NARSSA's own website.</strong> If a data scientist working
  alone can identify five Critical Risk provinces, an undocumented heap of records in
  Lebowakgomo, a 30-year-old private custody situation in the Eastern Cape, and a missing
  Bantustan archive — imagine what a properly resourced parliamentary inquiry could find.
  <br><br>
  The data exists. The solutions exist. The funding mechanisms exist. What is required now
  is the political will to treat South Africa's archival heritage as what it is:
  <strong>a non-renewable national asset.</strong>
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:20px 0 8px; color:#A8A29E;
            font-size:12px; font-family:'JetBrains Mono',monospace;">
  Analysis: Lindiwe Songelwa · 2026 · Public Interest Data Science<br>
  Sources: NARSSA · DSAC · UCT APC Research Initiative · Wits HPRA ·
  SA Society of Archivists · accesstomemory.org · PMG
</div>
""", unsafe_allow_html=True)
