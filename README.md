# SA Provincial Archives Digitisation Risk Dashboard
### Which Archives Are Next?

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://sa-archives-risk.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

> *On 24 March 2026, fire gutted the Botha Sigcau Building in Mthatha — a 13-storey
> landmark that housed 11 government departments and irreplaceable Eastern Cape records
> dating back to the pre-colonial era. It was the eleventh prominent building in Mthatha
> gutted by fire since 2021. This was not bad luck. It was the predictable consequence
> of a national failure to digitise South Africa's archival heritage.
> **This dashboard maps that failure across all nine provinces — and asks which archives
> are next.***

---

## 📋 Project Overview

This is a **public interest data science project** mapping digitisation risk across
South Africa's 9 provincial archive repositories — inspired by the March 2026 fire
at the historic Botha Sigcau Building in Mthatha, Eastern Cape.

| Layer | Audience | File |
|-------|----------|------|
| 📓 Analytical notebook | Data scientists, policy analysts, archivists | `analysis.ipynb` |
| 🌐 Public Streamlit app | Journalists, civic advocates, policymakers, general public | `app.py` + `pages/` |

---

## 🏛️ The Botha Sigcau Building — Why This Project Exists

The Botha Sigcau Building was not merely an office block. Named after **Botha Sigcau**,
King of the Mpondo people, it was the administrative heart of the former Transkei
government — housing 11 departments including Health, Education, Social Development,
Agriculture, Land Affairs, Transport, Human Settlements, the Deeds Office and SAPS.

It was also the site of one of South Africa's most consequential acts of political
courage. On **30 December 1987**, General Bantu Holomisa led the Transkei Defence
Force in a bloodless coup from this building, overthrowing Bantustan Prime Minister
Stella Sigcau — ending a corrupt, apartheid-compliant administration.

> *"The Botha Sigcau Building is a cornerstone of our country's political and
> administrative history. This is not merely a structure of bricks and mortar,
> but a living symbol of governance, transition and the resilience of the people
> of the Transkei."* — UDM President Bantu Holomisa

When it burned, irreplaceable Eastern Cape records dating back to the pre-colonial
era burned with it.

---

## 🔍 Seven Key Findings

### 1. Five of Nine Provinces Are at Critical Risk
Eastern Cape (10/10), Limpopo (9.5/10), North West (7.0/10), Mpumalanga (6.7/10)
and KwaZulu-Natal (6.6/10) all score in the Critical Risk tier.

### 2. The Digital Preservation Gap Follows the Apartheid Map
Bantustan archive burden correlates with risk score at **r = 0.835**. Provinces
that absorbed the most Bantustan archives after 1994 face the highest risk today —
and received the least capacity to preserve them.

### 3. Nationally, More Than Half of All Archives Are Not Digitally Catalogued
NARSSA confirms that a significant part of archival holdings — probably more than
half — are not yet reflected in NAAIRS. 8.3 million records are currently
mid-migration to a new database.

### 4. The Lebowa Archives Are an Undocumented Heap in a Basement
UCT researchers documented the Lebowa archives in Lebowakgomo as spread across
4 rooms, partially catalogued, and at times a random heap of papers. Not digitised.
Documented since at least 2013. Nothing has changed.

### 5. The Ciskei Archives Have Been in Private Hands for 30 Years
Unlike every other former Bantustan, the Ciskei records are held privately and
are very difficult to access. Who holds them — and why — has not been
publicly established.

### 6. The Solution Exists, Is Proven in SA, and Is Free
AtoM (Access to Memory — accesstomemory.org) is open-source, ICA-compliant,
and already deployed at Wits Historical Papers and the Western Cape Archives.
There is no technology barrier to adoption.

### 7. Apartheid Records Were Not Destroyed
A persistent myth holds that apartheid state records were destroyed. Open Secrets
(Wits HPRA) confirms a vast collection remains in public and private archives —
much of it undigitised and at risk.

---

## 📊 Data Sources

| Source | URL | What it provides |
|--------|-----|-----------------|
| NARSSA NAAIRS Introduction | national.archives.gov.za/naairsintro.htm | National digitisation baseline <50% |
| NARSSA NAAIRS Migration | nationalarchives.gov.za/node/737 | 8.3M records mid-migration |
| UCT Archive & Public Culture Research Initiative (2013) | humanities.uct.ac.za/apc | Lebowa archive condition |
| Wits People's Guide to Archives | wits.ac.za/history-workshop/archives-guide/ | All Bantustan archive locations |
| SA Society of Archivists | saarchivist.co.za | Botha Sigcau fire + records at risk |
| AtoM — Access to Memory | accesstomemory.org | Open-source archival platform |
| Wits Research Archives | researcharchives.wits.ac.za | AtoM adoption confirmed in SA |
| Open Secrets Collection, Wits HPRA | historicalpapers-atom.wits.ac.za/al3450 | Apartheid records not destroyed |
| PMG Parliamentary Records | pmg.org.za/committee-meeting/22093/ | Limpopo/NW underfunding |
| EWN / Daily Maverick / SowetanLive | Various | Fire incident timeline |

> **Data transparency note:** 49% of risk scores are directly sourced from public
> records. 51% are informed estimates anchored to the confirmed national NAAIRS
> baseline of <50% digitisation completion. Province-level digitisation data is
> not publicly available. Every score includes a `_source` column in the CSV.
> PAIA requests to provincial DSAC offices are recommended to close this gap.
> Contact: naairs@dac.gov.za

---

## 🗂️ Repository Structure

```
sa-archives-risk/
│
├── app.py                          # Streamlit landing page — Botha Sigcau narrative
├── analysis.ipynb                  # Full analytical notebook (professional audience)
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Risk_Dashboard.py         # Province risk scores + dimension breakdown
│   ├── 2_Priority_Score.py         # Weighted intervention priority ranking
│   └── 3_Policy_Recommendations.py # 6 national recs + Lebowa action plan
│
└── data/
    └── provincial_archives.csv     # 9 provinces, 23 columns, source-documented
```

---

## 🚀 Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/Lindiwe-22/sa-archives-risk.git
cd sa-archives-risk

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py

# 4. Or open the notebook
jupyter notebook analysis.ipynb
```

---

## 🧪 Analytical Notebook — `analysis.ipynb`

Linear narrative with headings per analytical lens, for data science and
policy professionals. Documents all working, assumptions and findings before
they are delivered to the Streamlit app.

| Section | What it covers |
|---------|---------------|
| Source Register | 11 primary sources with URLs and data contribution |
| Data Loading | Load CSV + print source transparency summary |
| Risk Overview | Province risk score bar chart |
| Apartheid Map Finding | Bantustan burden vs risk score — r = 0.835 |
| Dimension Analysis | Grouped bar chart across all 5 risk dimensions |
| Lebowa Case Study | Documented condition + 4-phase digitisation plan |
| Fire Timeline | Incident chart 2021–2026 |
| Findings & Recommendations | 7 findings + 8 policy recommendations |
| Attribution | All sources cited |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `pandas` | Data wrangling and risk score computation |
| `numpy` | Statistical calculations (correlation, OLS) |
| `matplotlib` | Notebook visualisations (light theme) |
| `plotly` | Interactive Streamlit charts |
| `streamlit` | Public-facing web application |

---

## 🌐 Deployment

Deployed on **Streamlit Cloud**. To deploy your own instance:

1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repo and set **Main file** to `app.py`
5. Click **Deploy**

---

## ⚠️ Limitations & Caveats

- **51% of risk scores are informed estimates** — not directly measured figures.
  Province-level digitisation data is not publicly available from NARSSA or DSAC.
- Risk scoring is a **composite index**, not an audit. Weights are based on policy
  relevance judgement — reasonable people may weight dimensions differently.
- The dataset contains **9 rows** (one per province). Statistical findings such
  as the r = 0.835 correlation should be interpreted as directional, not as
  statistically significant in the formal sense.
- **Fire incident data** is sourced from news archives — incidents not covered
  by mainstream media may be missing.
- The **Ciskei archive** situation is documented from a single source (Wits
  People's Guide to Archives). Independent verification was not possible.

---

## 🙏 Acknowledgements

This project was inspired by the March 2026 fire at the Botha Sigcau Building,
Mthatha — a building that served as the administrative heart of the Transkei
government, the site of Bantu Holomisa's 1987 coup, and a cornerstone of South
Africa's political and administrative history.

Research was made possible by the publicly available work of:
- The **UCT Archive and Public Culture Research Initiative**
- The **Wits Historical Papers Research Archive**
- The **SA Society of Archivists**
- **Parliamentary Monitoring Group (PMG)**
- **NARSSA** — for publishing what data is available

---

## 📁 Portfolio Series

| Project | Title | Status |
|---------|-------|--------|
| This project | SA Provincial Archives Digitisation Risk | ✅ Live |
| Related | Who Really Gets the Money? (SA DFI Inequality) | ✅ Live |
| Related | SA Crime Intelligence Report | ✅ Live |

---

## 📜 License

MIT License.
Data sourced from South African public records.
Analysis and code © 2026 Lindiwe Songelwa.

---

*Public interest data science. Built with Python · Streamlit · Plotly.*
*For policymakers, archivists, journalists and anyone who believes
South Africa's history is worth preserving.*