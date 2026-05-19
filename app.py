import streamlit as st

st.set_page_config(
    page_title="Which Archives Are Next?",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Source+Serif+4:wght@300;400;600&family=JetBrains+Mono:wght@400;500&display=swap');

  /* ── Base ── */
  [data-testid="stAppViewContainer"] {
    background: #F0EAD6;
    font-family: 'Source Serif 4', Georgia, serif;
  }
  [data-testid="stSidebar"] {
    background: #F5F0EB;
    border-right: 1px solid #E0DED9;
  }
  [data-testid="stSidebar"] * { color: #3F3F3F !important; }
  [data-testid="stSidebar"] a { color: #D97706 !important; }

  /* ── Typography ── */
  h1 { font-family: 'Playfair Display', Georgia, serif !important;
       color: #1C1917 !important; }
  h2, h3 { font-family: 'Playfair Display', Georgia, serif !important;
            color: #292524 !important; }
  p, li { font-family: 'Source Serif 4', Georgia, serif;
          color: #44403C; font-size: 16px; line-height: 1.85; }

  /* ── Callout boxes ── */
  .fire-box {
    background: #FEF3C7;
    border-left: 5px solid #D97706;
    border-radius: 0 6px 6px 0;
    padding: 18px 22px; margin: 20px 0;
  }
  .fire-box p { color: #92400E; font-size: 15px; margin: 0; }
  .critical-box {
    background: #FEF2F2;
    border-left: 5px solid #DC2626;
    border-radius: 0 6px 6px 0;
    padding: 18px 22px; margin: 20px 0;
  }
  .critical-box p { color: #7F1D1D; font-size: 15px; margin: 0; }
  .source-box {
    background: #F0FDF4;
    border-left: 5px solid #16A34A;
    border-radius: 0 6px 6px 0;
    padding: 18px 22px; margin: 20px 0;
  }
  .source-box p { color: #14532D; font-size: 13.5px; margin: 0;
                  font-family: 'JetBrains Mono', monospace; }
  .info-box {
    background: #EFF6FF;
    border-left: 5px solid #2563EB;
    border-radius: 0 6px 6px 0;
    padding: 18px 22px; margin: 20px 0;
  }
  .info-box p { color: #1E3A5F; font-size: 15px; margin: 0; }

  /* ── Hero ── */
  .hero {
    /*background: linear-gradient(135deg, #1C1917 0%, #292524 60%, #3B2A1A 100%);*/
    background: #CFC2A8; /* muted sand background */
    border-radius: 12px;
    padding: 56px 48px 48px;
    margin-bottom: 36px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 300px; height: 100%;
    background: linear-gradient(135deg, transparent 0%, rgba(217,119,6,0.08) 100%);
    pointer-events: none;
  }
  .hero-date {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #D97706; margin-bottom: 16px;
  }
  .hero h1 {
    color: #FEF3C7 !important;
    font-size: 3em !important;
    line-height: 1.15 !important;
    margin-bottom: 20px !important;
  }
  .hero p {
    color: #D6D3D1 !important;
    font-size: 17px !important;
    line-height: 1.8 !important;
    max-width: 760px;
  }
  .hero .hero-sub {
    color: #A8A29E !important;
    font-size: 13px !important;
    margin-top: 20px !important;
    font-family: 'JetBrains Mono', monospace !important;
  }

  /* ── Section divider ── */
  .divider {
    border: none;
    border-top: 1px solid #D6D3D1;
    margin: 36px 0;
  }

  /* ── Stat cards ── */
  .stat-row { display: flex; gap: 16px; flex-wrap: wrap; margin: 24px 0; }
  .stat-card {
    background: white;
    border: 1px solid #E7E5E4;
    border-radius: 10px;
    padding: 22px 26px;
    flex: 1; min-width: 160px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }
  .stat-card .stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px; color: #78716C;
    text-transform: uppercase; letter-spacing: 0.1em;
    margin-bottom: 8px;
  }
  .stat-card .stat-value {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 32px; font-weight: 900; color: #1C1917;
  }
  .stat-card .stat-sub { font-size: 12px; color: #A8A29E; margin-top: 4px; }
  .stat-card.amber  { border-top: 3px solid #D97706; }
  .stat-card.red    { border-top: 3px solid #DC2626; }
  .stat-card.stone  { border-top: 3px solid #78716C; }
  .stat-card.green  { border-top: 3px solid #16A34A; }

  /* ── Finding cards ── */
  .finding-card {
    background: white;
    border: 1px solid #E7E5E4;
    border-radius: 10px;
    padding: 22px 24px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .finding-card .finding-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; color: #D97706;
    text-transform: uppercase; letter-spacing: 0.1em;
    margin-bottom: 6px;
  }
  .finding-card .finding-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 16px; font-weight: 700; color: #1C1917;
    margin-bottom: 8px;
  }
  .finding-card .finding-desc {
    font-size: 14px; color: #57534E; line-height: 1.65;
  }

  /* ── Methodology note ── */
  .method-note {
    background: #FAFAF9;
    border: 1px solid #E7E5E4;
    border-radius: 8px;
    padding: 16px 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px; color: #78716C;
    line-height: 1.7;
  }

  #MainMenu { visibility: hidden; }
  footer    { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏛️ Which Archives Are Next?")
    st.markdown("---")
    st.markdown("""
A public interest analysis of digitisation risk
across South Africa's 9 provincial archive repositories.

**Navigate:**
- **Risk Dashboard** — Province-by-province scores
- **Priority Score** — Weighted risk ranking
- **Policy Recommendations** — Action plan
    """)
    st.markdown("---")
    st.markdown("**Sources**")
    st.markdown("""
- [NARSSA](https://www.nationalarchives.gov.za)
- [AtoM](https://www.accesstomemory.org)
- [Wits Research Archives](https://researcharchives.wits.ac.za)
- [SA Society of Archivists](https://saarchivist.co.za)
- [PMG Parliamentary Records](https://pmg.org.za)
    """)
    st.markdown("---")
    st.caption("Analysis by Lindiwe Songelwa · 2026")

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-date">📍 Mthatha, Eastern Cape · 24 March 2026</div>
  <h1>Which Archives<br>Are Next?</h1>
  <p>
    Fire gutted the Botha Sigcau Building — a 13-storey landmark housing
    11 government departments and irreplaceable Eastern Cape records dating back
    to the pre-colonial era. It was the eleventh prominent building in Mthatha
    gutted by fire since 2021. This was not bad luck. It was the predictable
    consequence of a national failure to digitise South Africa's archival heritage.
    <br><br>
    <strong style="color:#FEF3C7;">This dashboard maps that failure across all nine provinces —
    and asks which archives are next.</strong>
  </p>
  <p class="hero-sub">
    SA Provincial Archives Digitisation Risk Analysis · Public Interest Data Science · 2026
  </p>
</div>
""", unsafe_allow_html=True)

# ── The building ───────────────────────────────────────────────────────────────
st.markdown("## The Botha Sigcau Building — What Was Lost")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
The Botha Sigcau Building was not merely an office block. Named after **Botha Manzowandle
Sigcau**, King of the Mpondo people, it was the administrative heart of the former Transkei
government — one of apartheid's most consequential Bantustans. It was a 13-storey, 50-year-old
building belonging to the Department of Public Works and Infrastructure, housing 1,330 officials
across 11 departments including Health, Education, Social Development, Agriculture, Land Affairs,
Transport, Human Settlements, the Deeds Office, and SAPS.
""")

    st.markdown("""
<div class="fire-box">
<p>
  <strong>UDM President Bantu Holomisa:</strong> "The Botha Sigcau Building is a cornerstone
  of our country's political and administrative history. It was in this very building that,
  upon my assumption of leadership in 1987, we received many delegations from across the world.
  This is not merely a structure of bricks and mortar, but a living symbol of governance,
  transition and the resilience of the people of the Transkei."
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
It was also the site of one of South Africa's most consequential acts of political courage.
On **30 December 1987**, General Bantu Holomisa led the Transkei Defence Force in a bloodless
coup from this building, overthrowing Bantustan Prime Minister Stella Sigcau — ending a corrupt,
apartheid-compliant administration that had lost R45 million of state funds under the Matanzima
brothers. The transition that followed helped pave the path toward democratic negotiations.

The basement of the building housed a vast archive documenting the history and lived experiences
of Black communities in the Eastern Cape, with records dating back to the pre-colonial era.
When it burned, **those records burned with it.**
    """)

with col2:
    st.markdown("""
<div style="background:white; border:1px solid #E7E5E4; border-radius:10px; padding:24px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#78716C;
              text-transform:uppercase; letter-spacing:0.1em; margin-bottom:16px;">
    Building Facts
  </div>
  <table style="width:100%; font-size:13.5px; border-collapse:collapse;
                font-family:'Source Serif 4',Georgia,serif;">
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:8px 0;">Storeys</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">13</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:8px 0;">Departments housed</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">11</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:8px 0;">Officials displaced</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">1,330</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:8px 0;">Building age</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">~50 years</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:8px 0;">Custodian</td>
      <td style="font-weight:600; color:#1C1917; text-align:right; font-size:12px;">DPWI</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:8px 0;">Fire date</td>
      <td style="font-weight:600; color:#DC2626; text-align:right;">24 Mar 2026</td>
    </tr>
    <tr>
      <td style="color:#78716C; padding:8px 0;">Mthatha fires since 2021</td>
      <td style="font-weight:700; color:#DC2626; text-align:right;">11</td>
    </tr>
  </table>
</div>

<div style="background:white; border:1px solid #E7E5E4; border-radius:10px;
            padding:20px; margin-top:14px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#78716C;
              text-transform:uppercase; letter-spacing:0.1em; margin-bottom:12px;">
    Departments in the Building
  </div>
  <div style="font-size:13px; color:#57534E; line-height:2.1;
              font-family:'Source Serif 4',Georgia,serif;">
    Health · Education · Social Development<br>
    Agriculture · Land Affairs · Transport<br>
    Human Settlements · Deeds Office · SAPS<br>
    Co-operative Governance & Traditional Affairs<br>
    Public Works & Infrastructure
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Why archives matter ────────────────────────────────────────────────────────
st.markdown("## Why National Archives Matter")

st.markdown("""
The National Archives and Records Service of South Africa (NARSSA) operates under a
dual constitutional mandate. The **first** is to preserve a national archival heritage
for use by the government and people of South Africa — acquiring and managing records
of national importance, including both public and non-public records. The **second** is
to create the conditions for efficient, accountable and transparent government through
the proper management and care of records in the possession of governmental bodies.
""")

st.markdown("""
<div class="info-box">
<p>
  These are not administrative abstractions. In a country where land ownership disputes,
  pension records, birth certificates and court documents determine people's access to
  rights and services, the physical vulnerability of paper-based archives is a
  <strong>direct threat to citizens' lives.</strong> The communities who most need these
  records — those dispossessed by apartheid land policy — are the least likely to have
  digital alternatives.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── National digitisation status ──────────────────────────────────────────────
st.markdown("## The National Digitisation Crisis")
st.markdown("*What the data — sourced directly from NARSSA — confirms.*")

st.markdown("""
<div class="stat-row">
  <div class="stat-card red">
    <div class="stat-label">Archival Holdings in NAAIRS</div>
    <div class="stat-value">&lt;50%</div>
    <div class="stat-sub">More than half of SA's archives are not yet catalogued digitally</div>
  </div>
  <div class="stat-card amber">
    <div class="stat-label">Records Mid-Migration</div>
    <div class="stat-value">8.3M</div>
    <div class="stat-sub">NAAIRS entries being migrated to new system — incomplete</div>
  </div>
  <div class="stat-card red">
    <div class="stat-label">Provinces at Critical Risk</div>
    <div class="stat-value">5 of 9</div>
    <div class="stat-sub">Eastern Cape, Limpopo, North West, Mpumalanga, KZN</div>
  </div>
  <div class="stat-card stone">
    <div class="stat-label">Former Bantustan Archives</div>
    <div class="stat-value">10</div>
    <div class="stat-sub">Scattered, under-resourced, largely undigitised</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="source-box">
<p>
  Sources: national.archives.gov.za/naairsintro.htm · nationalarchives.gov.za/node/737 ·
  UCT Archive &amp; Public Culture Research Initiative (2013) · saarchivist.co.za (March 2026)
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Key findings ──────────────────────────────────────────────────────────────
st.markdown("## Seven Key Findings")
st.markdown("*Use the sidebar to explore each finding in detail.*")

findings = [
    ("Finding 01", "5 of 9 provinces are at Critical Risk",
     "Eastern Cape (10/10), Limpopo (9.5/10), North West (7.0/10), Mpumalanga (6.7/10) and KwaZulu-Natal (6.6/10) all score in the Critical Risk tier."),
    ("Finding 02", "The digital preservation gap follows the apartheid map",
     "Provinces carrying the most Bantustan archive burden face the highest risk. Bantustan burden correlates with risk score at r = 0.835."),
    ("Finding 03", "Nationally, more than half of all archives are not digitally catalogued",
     "NARSSA confirms that a significant part of archival holdings — probably more than half — are not yet reflected in NAAIRS."),
    ("Finding 04", "The Lebowa archives are an undocumented heap in a basement",
     "UCT researchers documented the Lebowa archives in Lebowakgomo as spread across 4 rooms, partially catalogued, and at times a random heap of papers. Not digitised."),
    ("Finding 05", "The Ciskei archives have been in private hands for 30 years",
     "Unlike every other Bantustan archive, the Ciskei records are held privately and are very difficult to access. Who holds them, and why, has not been publicly established."),
    ("Finding 06", "The solution exists, is proven in SA, and is free",
     "AtoM (Access to Memory) is open-source, ICA-compliant, and already deployed at Wits Historical Papers and the Western Cape Archives. There is no technology barrier."),
    ("Finding 07", "Apartheid records were not destroyed",
     "A persistent myth holds that apartheid state records were destroyed. Open Secrets (Wits HPRA) confirms a vast collection remains in public and private archives — much of it undigitised and at risk."),
]

col1, col2 = st.columns(2)
for i, (num, title, desc) in enumerate(findings):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
<div class="finding-card">
  <div class="finding-num">{num}</div>
  <div class="finding-title">{title}</div>
  <div class="finding-desc">{desc}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Methodology ───────────────────────────────────────────────────────────────
st.markdown("## Methodology & Data Transparency")

st.markdown("""
<div class="method-note">
  Risk scores are composite indices across 5 weighted dimensions:<br>
  Physical vulnerability (30%) · Digitisation progress (25%) · Undigitised volume (20%)<br>
  Budget adequacy (15%) · Staff capacity (10%) · Bantustan burden bonus (10%)<br><br>
  DATA TRANSPARENCY: 49% of data points are directly sourced from public records.<br>
  51% are informed estimates anchored to the confirmed national NAAIRS baseline (&lt;50% digitised).<br>
  Province-level digitisation data is not publicly available — PAIA requests recommended.<br>
  Contact: naairs@dac.gov.za · Every score includes a source column in the underlying CSV.
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:20px 0 8px; color:#A8A29E;
            font-size:12px; font-family:'JetBrains Mono',monospace;">
  Analysis: Lindiwe Songelwa · 2026 · Public Interest Data Science<br>
  Sources: NARSSA · DSAC · UCT APC Research Initiative · Wits HPRA ·
  SA Society of Archivists · PMG
</div>
""", unsafe_allow_html=True)