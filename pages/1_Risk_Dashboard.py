import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Risk Dashboard",
    page_icon="📊",
    layout="wide",
)

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
  #MainMenu { visibility: hidden; } footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Load data ──────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('data/provincial_archives.csv')
    return df

df = load_data()

TIER_COLORS = {
    'Critical Risk': '#DC2626',
    'Moderate Risk': '#D97706',
    'Lower Risk':    '#16A34A',
}
TIER_BG = {
    'Critical Risk': '#FEF2F2',
    'Moderate Risk': '#FEF3C7',
    'Lower Risk':    '#F0FDF4',
}
TIER_BORDER = {
    'Critical Risk': '#DC2626',
    'Moderate Risk': '#D97706',
    'Lower Risk':    '#16A34A',
}

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("# 📊 Risk Dashboard")
st.markdown("### Province-by-province digitisation risk across South Africa's 9 archive repositories")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("""
<div class="critical-box">
<p>
  <strong>5 of 9 provinces are at Critical Risk.</strong> The risk scoring combines
  physical vulnerability, digitisation progress, undigitised volume, budget adequacy,
  staff capacity and Bantustan archive burden — each weighted by policy relevance.
  A score of 10/10 means maximum risk across all dimensions. Eastern Cape scores 10/10.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Main risk chart ────────────────────────────────────────────────────────────
st.markdown("## Overall Risk Score by Province")
st.markdown("*Higher score = greater risk of irreversible archival loss. Threshold lines show tier boundaries.*")

df_sorted = df.sort_values('risk_score_10', ascending=True)
bar_colors = [TIER_COLORS[t] for t in df_sorted['risk_tier']]

fig_main = go.Figure()
fig_main.add_trace(go.Bar(
    y=df_sorted['province'],
    x=df_sorted['risk_score_10'],
    orientation='h',
    marker_color=bar_colors,
    marker_opacity=0.85,
    text=[f"{v}/10 — {t}" for v, t in
          zip(df_sorted['risk_score_10'], df_sorted['risk_tier'])],
    textposition='outside',
    textfont=dict(size=11, color='#44403C'),
    hovertemplate=(
        '<b>%{y}</b><br>'
        'Risk Score: %{x}/10<extra></extra>'
    ),
))
fig_main.add_vline(x=6.5, line_dash='dash', line_color='#DC2626',
                   line_width=1.5,
                   annotation_text='Critical threshold',
                   annotation_position='top',
                   annotation_font=dict(color='#DC2626', size=10))
fig_main.add_vline(x=3.5, line_dash='dash', line_color='#D97706',
                   line_width=1.5,
                   annotation_text='Moderate threshold',
                   annotation_position='top',
                   annotation_font=dict(color='#D97706', size=10))
fig_main.update_layout(
    plot_bgcolor='white', paper_bgcolor='#F7F3EE',
    font=dict(family='Source Serif 4, Georgia, serif', color='#44403C'),
    xaxis=dict(title='Composite Risk Score (0–10)', gridcolor='#E7E5E4',
               range=[0, 13.5]),
    yaxis=dict(title=''),
    margin=dict(t=30, b=20, l=20, r=160),
    height=400,
    showlegend=False,
)
st.plotly_chart(fig_main, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Dimension breakdown ────────────────────────────────────────────────────────
st.markdown("## Risk Dimensions by Province")
st.markdown("*What drives risk in each province — broken down across all five scoring dimensions.*")

st.markdown("""
<div class="fire-box">
<p>
  <strong>Reading this chart:</strong> For Physical Vulnerability and Undigitised Volume,
  a higher bar means higher risk. For Digitisation Progress, Budget and Staff Capacity,
  a <em>lower</em> bar means higher risk — these dimensions are inverted in the composite score.
</p>
</div>
""", unsafe_allow_html=True)

dims = [
    ('physical_vulnerability_score', 'Physical Vulnerability', '#DC2626'),
    ('digitisation_score',           'Digitisation Progress',  '#2563EB'),
    ('budget_score',                 'Budget Adequacy',        '#D97706'),
    ('staff_capacity_score',         'Staff Capacity',         '#16A34A'),
    ('undigitised_volume_score',     'Undigitised Volume',     '#7C3AED'),
]

df_dim = df.sort_values('risk_score_10', ascending=False)

fig_dim = go.Figure()
for col, label, color in dims:
    fig_dim.add_trace(go.Bar(
        name=label,
        x=df_dim['province'],
        y=df_dim[col],
        marker_color=color,
        opacity=0.82,
        hovertemplate=f'<b>%{{x}}</b><br>{label}: %{{y}}/5<extra></extra>',
    ))
fig_dim.update_layout(
    barmode='group',
    plot_bgcolor='white', paper_bgcolor='#F7F3EE',
    font=dict(family='Source Serif 4, Georgia, serif', color='#44403C'),
    xaxis=dict(title='', tickangle=-20, gridcolor='#E7E5E4'),
    yaxis=dict(title='Score (1–5)', gridcolor='#E7E5E4', range=[0, 6.2]),
    legend=dict(orientation='h', yanchor='bottom', y=1.02,
                xanchor='right', x=1, font=dict(size=11)),
    margin=dict(t=40, b=60, l=20, r=20),
    height=420,
)
st.plotly_chart(fig_dim, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Province cards ─────────────────────────────────────────────────────────────
st.markdown("## Province-by-Province Detail")
st.markdown("*Click a province to expand its full risk profile.*")

for _, row in df.iterrows():
    tier   = row['risk_tier']
    color  = TIER_COLORS[tier]
    bg     = TIER_BG[tier]
    border = TIER_BORDER[tier]

    with st.expander(
        f"{row['province']} — {row['risk_score_10']}/10 · {tier}",
        expanded=False
    ):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
<div style="background:{bg}; border:1px solid {border}; border-radius:8px; padding:16px 18px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#78716C;
              text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">
    Overall Risk
  </div>
  <div style="font-family:'Playfair Display',serif; font-size:40px;
              font-weight:900; color:{color};">
    {row['risk_score_10']}<span style="font-size:18px; color:#78716C;">/10</span>
  </div>
  <div style="font-size:13px; font-weight:600; color:{color}; margin-top:4px;">
    {tier}
  </div>
</div>
""", unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
<div style="background:white; border:1px solid #E7E5E4; border-radius:8px; padding:16px 18px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#78716C;
              text-transform:uppercase; letter-spacing:0.1em; margin-bottom:12px;">
    Score Breakdown
  </div>
  <table style="width:100%; font-size:13px; border-collapse:collapse;
                font-family:'Source Serif 4',serif;">
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:5px 0;">Physical Vulnerability</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">
        {row['physical_vulnerability_score']}/5</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:5px 0;">Digitisation Progress</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">
        {row['digitisation_score']}/5</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:5px 0;">Undigitised Volume</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">
        {row['undigitised_volume_score']}/5</td>
    </tr>
    <tr style="border-bottom:1px solid #F5F5F4;">
      <td style="color:#78716C; padding:5px 0;">Budget Adequacy</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">
        {row['budget_score']}/5</td>
    </tr>
    <tr>
      <td style="color:#78716C; padding:5px 0;">Staff Capacity</td>
      <td style="font-weight:600; color:#1C1917; text-align:right;">
        {row['staff_capacity_score']}/5</td>
    </tr>
  </table>
</div>
""", unsafe_allow_html=True)

        with col3:
            special = row.get('special_risk_flag', 'None')
            special_html = f"""
<div style="background:#FEF3C7; border:1px solid #D97706; border-radius:8px;
            padding:14px 16px; margin-top:10px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#92400E;
              text-transform:uppercase; margin-bottom:6px;">⚠ Special Risk Flag</div>
  <div style="font-size:12.5px; color:#92400E;">{special}</div>
</div>""" if special != 'None' else ''

            bantustan_html = ''
            if row['bantustan_burden'] > 0:
                bantustan_html = f"""
<div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:8px;
            padding:14px 16px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#1E40AF;
              text-transform:uppercase; margin-bottom:6px;">
    Bantustan Archives ({row['bantustan_burden']})</div>
  <div style="font-size:12.5px; color:#1E40AF;">{row['bantustan_names']}</div>
</div>"""
            else:
                bantustan_html = """
<div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:8px;
            padding:14px 16px;">
  <div style="font-size:12.5px; color:#14532D;">No former Bantustan archive burden</div>
</div>"""

            st.markdown(f"""
{bantustan_html}
{special_html}
""", unsafe_allow_html=True)

        # Repository and source note
        st.markdown(f"""
<div style="background:#FAFAF9; border:1px solid #E7E5E4; border-radius:6px;
            padding:12px 16px; margin-top:10px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px;
              color:#78716C; margin-bottom:4px;">REPOSITORY</div>
  <div style="font-size:13px; color:#57534E;">{row['main_repository']}</div>
  <div style="font-family:'JetBrains Mono',monospace; font-size:10px;
              color:#78716C; margin-top:10px; margin-bottom:4px;">
    DIGITISATION SOURCE NOTE</div>
  <div style="font-size:12px; color:#78716C;">{row['digitisation_source']}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── The apartheid map finding ──────────────────────────────────────────────────
st.markdown("## The Apartheid Map Finding")
st.markdown("*Provinces with more Bantustan archives face significantly higher digitisation risk.*")

corr = df['bantustan_burden'].corr(df['risk_score_10'])

fig_corr = go.Figure()
tier_color_list = [TIER_COLORS[t] for t in df['risk_tier']]

fig_corr.add_trace(go.Scatter(
    x=df['bantustan_burden'],
    y=df['risk_score_10'],
    mode='markers+text',
    marker=dict(
        color=tier_color_list, size=18, opacity=0.85,
        line=dict(color='white', width=1.5)
    ),
    text=df['province'],
    textposition='top right',
    textfont=dict(size=10, color='#44403C'),
    hovertemplate=(
        '<b>%{text}</b><br>'
        'Bantustan archives: %{x}<br>'
        'Risk score: %{y}/10<extra></extra>'
    ),
))

# OLS line
m, b = np.polyfit(df['bantustan_burden'], df['risk_score_10'], 1)
x_line = np.linspace(-0.2, 3.4, 100)
fig_corr.add_trace(go.Scatter(
    x=x_line, y=m * x_line + b,
    mode='lines',
    line=dict(color='#D97706', dash='dash', width=2),
    name=f'OLS fit (r = {corr:.3f})',
    hoverinfo='skip',
))
fig_corr.update_layout(
    plot_bgcolor='white', paper_bgcolor='#F7F3EE',
    font=dict(family='Source Serif 4, Georgia, serif', color='#44403C'),
    xaxis=dict(title='Number of Former Bantustan Archives Absorbed',
               gridcolor='#E7E5E4', dtick=1),
    yaxis=dict(title='Composite Risk Score (0–10)', gridcolor='#E7E5E4'),
    legend=dict(font=dict(size=11)),
    margin=dict(t=20, b=20, l=20, r=20),
    height=420,
    showlegend=True,
)
st.plotly_chart(fig_corr, use_container_width=True)

st.markdown(f"""
<div class="fire-box">
<p>
  <strong>r = {corr:.3f} · R² = {corr**2:.3f}</strong> — The digital preservation gap
  in South Africa follows the apartheid map. Provinces that absorbed the most Bantustan
  archives after 1994 face the highest risk today — and received the least capacity to
  preserve them. This is not a coincidence. It is the compound consequence of a colonial
  and apartheid administrative legacy that was never adequately remediated.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="source-box">
<p>
  Sources: Wits People's Guide to Archives (Bantustan locations) ·
  UCT Archive &amp; Public Culture Research Initiative (2013) ·
  national.archives.gov.za/naairsintro.htm (NAAIRS baseline)
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:20px 0 8px; color:#A8A29E;
            font-size:12px; font-family:'JetBrains Mono',monospace;">
  Data: provincial_archives.csv · Analysis: Lindiwe Songelwa · 2026
</div>
""", unsafe_allow_html=True)
