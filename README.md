# AI in Cybersecurity Auditing and Compliance: Systematic Literature Review

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)  
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## Overview
Survey of 40 peer-reviewed papers (2022–2025, IEEE/ACM/Elsevier/Springer) on AI for cybersecurity auditing/compliance. Analyzes trends, metrics, and gaps via SLR (PRISMA). Extends baseline Ref [9] (*XAI in Cybersecurity Survey*, 2025, IEEE) with compliance focus. See [/baselines/comparison_to_baseline.md](baselines/comparison_to_baseline.md).

**Objectives**: Classify sub-themes (e.g., 62.5% Compliance), evaluate performance (avg 91.3% accuracy), identify gaps (e.g., 0% quantum mentions).

## Key Insights
- **Trends**: 50% papers in 2025 (+17.6% growth). [/results/visualizations/timeline_trend.png](results/visualizations/timeline_trend.png)
- **Themes**: Compliance 62.5% (25 papers), Threat Detection 30% (12). [/data/categorization.csv](data/categorization.csv)
- **Gaps**: High in "quantum" (0%), "blockchain" (5%). [/results/visualizations/gap_keywords.png](results/visualizations/gap_keywords.png)

## Structure
```
AI-in-Cybersecurity-Auditing-and-Compliance-Monitoring/
├── README.md
├── requirements.txt
├── baselines/          # Ref [9] PDF + comparison MD
├── data/               # CSVs: metadata, categorization, timeline
├── analysis/           # Notebooks (3/3 run: categorization, trends, gaps)
├── results/            # Tables/viz: comparison_tables/, visualizations/, statistics/
├── summaries/          # paper_summaries.json (40 entries)
└── docs/               # evaluation_framework.pdf, taxonomy_diagram.png
```

## Setup & Run
1. Clone: `git clone https://github.com/Pradyum-1712/AI-in-Cybersecurity-Auditing-and-Compliance-Monitoring.git`
2. Install: `pip install -r requirements.txt`
3. Run: `python scripts/populate_data.py` to populate the data/ directory
4. Run: `jupyter notebook analysis/` to run the analysis notebooks

## Progress Video
[Loom Link](https://www.loom.com/share/[your-link]) – Group demo of pipeline, themes, gaps.

## Group
- **Members**: [Jerusalem Mesfin Tasew] ([jtasew@hawk.illinoistech.edu]), [Partner Name] ([email])
- **Course**: Cyber Security Management, Fall 2025