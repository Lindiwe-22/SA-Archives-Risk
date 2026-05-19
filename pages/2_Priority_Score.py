import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Priority Score", page_icon="🎯", layout="wide")

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

@st.cache_data
def load_data():
    return pd.read_csv('data/provincial_archives.csv')

df = load_data()

TIER_COLORS = {
    'Critical Risk': '#DC2626',
    'Moderate Risk': '#D97706',
    'Lower Risk':    '#16A34A',
}

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("# 🎯 Digitisation Priority Score")
st.markdown("### Which archives need urgent intervention — and in what order?")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("""
The risk score tells us how dangerous the situation is. The priority score answers the
operational question: **if resources are limited, where should they go first?**

Priority scoring adds two additional dimensions to the risk score:
- **Urgency multiplier** — provinces with recent fire incidents score higher
- **Intervention feasibility** — provinces with existing AtoM infrastructure score lower
  (quicker wins possible elsewhere first)
""")

# ── Compute priority score ─────────────────────────────────────────────────────
df_p = df.copy()

# Urgency multiplier: fire incidents add weight
df_p['urgency_multiplier'] = 1.0 + (df_p['fire_incidents_since_2020'] * 0.15)

# Feasibility: WC already has AtoM — lower priority for emergency spend
# Gauteng has NAAIRS — moderate feasibility advantage
df_p['feasibility_adjustment'] = df_p['province'].map({
    'Western Cape':   -1.5,  # already advanced — deprioritise emergency spend
    'Gauteng':        -0.5,  # NAAIRS infrastructure exists
    'Eastern Cape':    0.0,
    'Limpopo':         0.0,
    'North West':      0.0,
    'KwaZulu-Natal':   0.0,
    'Mpumalanga':      0.0,
    'Free State':      0.0,
    'Northern Cape':   0.0,
})

df_p['priority_raw'] = (df_p['risk_score_10'] * df_p['urgency_multiplier']
                         + df_p['feasibility_adjustment'])
df_p['priority_raw'] = df_p['priority_raw'].clip(lower=0)

# Normalise to 0–10
p_min = df_p['priority_raw'].min()
p_max = df_p['priority_raw'].max()
df_p['priority_score'] = ((df_p['priority_raw'] - p_min) /
                           (p_max - p_min) * 10).round(1)

df_p = df_p.sort_values('priority_score', ascending=False).reset_index(drop=True)
df_p['priority_rank'] = range(1, len(df_p) + 1)

# ── Priority ranking chart ─────────────────────────────────────────────────────
st.markdown("## Priority Ranking — Where to Act First")
st.markdown("*Combines risk score + fire incident urgency + intervention feasibility.*")

bar_colors = [TIER_COLORS[t] for t in df_p['risk_tier']]

fig_priority = go.Figure()
fig_priority.add_trace(go.Bar(
    y=df_p['province'],
    x=df_p['priority_score'],
    orientation='h',
    marker_color=bar_colors,
    marker_opacity=0.85,
    text=[f"Priority #{r} · {s}/10"
          for r, s in zip(df_p['priority_rank'], df_p['priority_score'])],
    textposition='outside',
    textfont=dict(size=11, color='#44403C'),
    hovertemplate='<b>%{y}</b><br>Priority Score: %{x}/10<extra></extra>',
))
fig_priority.update_layout(
    plot_bgcolor='white', paper_bgcolor='#F7F3EE',
    font=dict(family='Source Serif 4, Georgia, serif', color='#44403C'),
    xaxis=dict(title='Priority Score (0–10)', gridcolor='#E7E5E4', range=[0, 13]),
    yaxis=dict(title='', categoryorder='total ascending'),
    margin=dict(t=20, b=20, l=20, r=180),
    height=380,
    showlegend=False,
)
st.plotly_chart(fig_priority, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Priority cards ─────────────────────────────────────────────────────────────
st.markdown("## Priority Intervention Summary")

for _, row in df_p.iterrows():
    rank  = row['priority_rank']
    tier  = row['risk_tier']
    color = TIER_COLORS[tier]

    rank_bg = '#FEF2F2' if rank <= 2 else '#FEF3C7' if rank <= 5 else '#F0FDF4'
    rank_border = '#DC2626' if rank <= 2 else '#D97706' if rank <= 5 else '#16A34A'

    urgency_note = (
        f"🔥 {int(row['fire_incidents_since_2020'])} fire incident(s) since 2020 — urgency elevated"
        if row['fire_incidents_since_2020'] > 0
        else "No confirmed fire incidents since 2020"
    )
    feasibility_note = {
        'Western Cape': '✅ AtoM + ECM active — lower emergency priority, knowledge transfer role',
        'Gauteng':      '⚡ NAAIRS infrastructure exists — mid-priority, system migration focus',
    }.get(row['province'], '⚠️ No confirmed digitisation infrastructure — maximum intervention needed')

    special = row.get('special_risk_flag', 'None')

    st.markdown(f"""
<div style="background:white; border:1px solid #E7E5E4; border-radius:10px;
            padding:22px 26px; margin-bottom:14px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="min-width:80px;">
      <div style="background:{rank_bg}; border:2px solid {rank_border};
                  border-radius:50%; width:60px; height:60px;
                  display:flex; align-items:center; justify-content:center;
                  font-family:'Playfair Display',serif;
                  font-size:24px; font-weight:900; color:{rank_border};">
        #{rank}
      </div>
    </div>
    <div style="flex:1; min-width:220px;">
      <div style="font-family:'Playfair Display',serif; font-size:18px;
                  font-weight:700; color:#1C1917; margin-bottom:4px;">
        {row['province']}
      </div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:11px;
                  color:{color}; margin-bottom:10px;">
        {tier} · Risk {row['risk_score_10']}/10 · Priority {row['priority_score']}/10
      </div>
      <div style="font-size:13.5px; color:#57534E; margin-bottom:6px;">
        📦 {row['main_repository']}
      </div>
      <div style="font-size:13px; color:#DC2626; margin-bottom:4px;">{urgency_note}</div>
      <div style="font-size:13px; color:#44403C;">{feasibility_note}</div>
      {'<div style="font-size:12.5px; color:#92400E; margin-top:8px; background:#FEF3C7; padding:8px 12px; border-radius:4px;">⚠️ ' + special + '</div>' if special != 'None' else ''}
    </div>
    <div style="min-width:120px; text-align:right;">
      <div style="font-family:'JetBrains Mono',monospace; font-size:10px;
                  color:#78716C; margin-bottom:4px;">BANTUSTAN BURDEN</div>
      <div style="font-family:'Playfair Display',serif; font-size:28px;
                  font-weight:900; color:#1C1917;">{row['bantustan_burden']}</div>
      <div style="font-size:11px; color:#A8A29E;">former archives</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Risk vs Priority scatter ───────────────────────────────────────────────────
st.markdown("## Risk Score vs Priority Score")
st.markdown("*Provinces above the diagonal line have higher priority than their raw risk score suggests — driven by fire incident urgency.*")

fig_scatter = go.Figure()
fig_scatter.add_trace(go.Scatter(
    x=[0, 10], y=[0, 10],
    mode='lines',
    line=dict(color='#D6D3D1', dash='dash', width=1.5),
    name='Risk = Priority (baseline)',
    hoverinfo='skip',
))
fig_scatter.add_trace(go.Scatter(
    x=df_p['risk_score_10'],
    y=df_p['priority_score'],
    mode='markers+text',
    marker=dict(
        color=[TIER_COLORS[t] for t in df_p['risk_tier']],
        size=16, opacity=0.85,
        line=dict(color='white', width=1.5)
    ),
    text=df_p['province'],
    textposition='top right',
    textfont=dict(size=10, color='#44403C'),
    hovertemplate=(
        '<b>%{text}</b><br>'
        'Risk: %{x}/10<br>'
        'Priority: %{y}/10<extra></extra>'
    ),
    name='Provinces',
))
fig_scatter.update_layout(
    plot_bgcolor='white', paper_bgcolor='#F7F3EE',
    font=dict(family='Source Serif 4, Georgia, serif', color='#44403C'),
    xaxis=dict(title='Risk Score (0–10)', gridcolor='#E7E5E4', range=[-0.5, 11]),
    yaxis=dict(title='Priority Score (0–10)', gridcolor='#E7E5E4', range=[-0.5, 11]),
    legend=dict(font=dict(size=11)),
    margin=dict(t=20, b=20, l=20, r=20),
    height=420,
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("""
<div class="fire-box">
<p>
  <strong>Eastern Cape sits furthest above the diagonal</strong> — its priority score
  exceeds even its already-maximum risk score, driven by 3 fire incidents since 2020
  including the Botha Sigcau Building. This province requires emergency intervention,
  not a place in a queue.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:20px 0 8px; color:#A8A29E;
            font-size:12px; font-family:'JetBrains Mono',monospace;">
  Priority scoring: risk score × urgency multiplier + feasibility adjustment ·
  Analysis: Lindiwe Songelwa · 2026
</div>
""", unsafe_allow_html=True)
