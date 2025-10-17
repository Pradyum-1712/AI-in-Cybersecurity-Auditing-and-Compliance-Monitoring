# AI in Cybersecurity Auditing and Compliance: A Systematic Literature Review

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)  
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## Project Description
This repository accompanies our **Survey Research Paper** titled *AI in Cybersecurity Auditing and Compliance*, prepared for the Cyber Security Management course (Fall 2025). The study synthesizes **40 peer-reviewed publications** (2022–2025) from IEEE, ACM, Elsevier, and Springer, analyzing trends, methodologies, challenges, and gaps in AI applications for cybersecurity auditing (e.g., threat detection, anomaly identification) and compliance (e.g., GDPR, EU AI Act, NIST alignment).

- **Research Objectives**:
  - Classify AI techniques across sub-themes (e.g., compliance frameworks, threat detection).
  - Evaluate performance metrics (e.g., accuracy, explainability).
  - Identify gaps (e.g., low focus on quantum-resilient auditing) and propose future directions.
- **Methodology**: Systematic Literature Review (SLR) following PRISMA guidelines, with automated analysis via Jupyter notebooks for reproducibility.
- **Baseline Extension**: Builds on Ref [9] (*A Comprehensive Survey of Explainable AI in Cybersecurity*, 2025, IEEE) by incorporating compliance and agentic AI—see [/baselines/comparison_to_baseline.md](baselines/comparison_to_baseline.md).
- **Novel Contribution**: A proposed taxonomy of 5 sub-themes, with visualizations highlighting post-2022 trends (e.g., 50% publications in 2025).

This work provides researchers, auditors, and practitioners with a roadmap for ethical, compliant AI deployment in cybersecurity ecosystems.

## Key Findings (50% Progress Snapshot)
As of October 19, 2025 (mid-implementation milestone), our analysis reveals:
- **Publication Trends**: Steady growth, with 50% of papers in 2025 (up 17.6% from 2024), driven by regulatory shifts like the EU AI Act. See [/data/timeline_analysis.csv](data/timeline_analysis.csv) and [/results/visualizations/timeline_trend.png](results/visualizations/timeline_trend.png).
- **Thematic Distribution**: Dominated by Compliance Frameworks (62.5%, 25 papers), followed by Threat Detection (30%, 12 papers). Emerging areas like Generative AI Risks remain underrepresented (2.5%, 1 paper). See [/data/categorization.csv](data/categorization.csv) and [/results/comparison_tables/table_iv_theme_summaries.csv](results/comparison_tables/table_iv_theme_summaries.csv).
- **Performance Metrics**: Average accuracy 91.3%; Threat Detection excels (92.9% avg.), while XAI & Ethics leads explainability (5.0/5). See [/data/comparison_metrics.csv](data/comparison_metrics.csv) and [/results/visualizations/performance_heatmap.png](results/visualizations/performance_heatmap.png).
- **Research Gaps**: High gaps in keywords like "quantum" (0% mentions) and "blockchain" (5%), signaling needs for resilient auditing tools. See [/results/statistics/gap_report.csv](results/statistics/gap_report.csv) and [/results/visualizations/gap_keywords.png](results/visualizations/gap_keywords.png).

Full paper draft and 100% analysis forthcoming.

## Repository Structure
```
AI-in-Cybersecurity-Auditing-and-Compliance-Monitoring/
├── README.md                          # This file: Overview & progress
├── requirements.txt                   # Dependencies: pandas, matplotlib, seaborn, numpy, wordcloud
├── baselines/                         # Baseline references
│   ├── baseline_paper_9.pdf           # Ref [9] PDF
│   └── comparison_to_baseline.md      # Detailed extensions/gaps
├── data/                              # Raw datasets from SLR
│   ├── papers_metadata.csv            # 40 papers: Titles, authors, years, sub-themes, etc.
│   ├── comparison_metrics.csv         # Metrics: Accuracy (91.3% avg.), explainability (3.5 med.)
│   ├── categorization.csv             # Sub-themes: Compliance (62.5%), Threat Detection (30%)
│   └── timeline_analysis.csv          # Trends: 2025 (50%), 2024 (42.5%)
├── analysis/                          # Jupyter notebooks (50% executed: 4/5)
│   ├── 01_paper_categorization.ipynb  # Theme grouping + pie chart
│   ├── 02_performance_comparison.ipynb # Metrics heatmap
│   ├── 03_trend_analysis.ipynb        # Timeline line/bar chart
│   └── 04_gap_identification.ipynb    # Keyword gaps bar chart
├── results/                           # Outputs: Tables & visualizations
│   ├── comparison_tables/             # Aggregated CSVs (e.g., table_i_frameworks.csv, table_iv_theme_summaries.csv)
│   ├── visualizations/                # PNGs: timeline_trend.png, performance_heatmap.png, gap_keywords.png
│   └── statistics/                    # Stats CSVs (e.g., gap_report.csv, trend_stats.csv)
├── summaries/                         # Literature synthesis
│   ├── paper_summaries.json           # Structured entries: Abstracts, findings, limitations (40 total)
│   └── key_findings.md                # Thematic insights (TBD)
└── docs/                              # Paper artifacts
    ├── evaluation_framework.pdf       # SLR criteria (accuracy, explainability, compliance focus)
    └── taxonomy_diagram.png           # Proposed sub-themes classification
```

## Setup and Reproduction
1. **Clone the Repo**:
   ```
   git clone https://github.com/[your-username]/AI-in-Cybersecurity-Auditing-and-Compliance-Monitoring.git
   cd AI-in-Cybersecurity-Auditing-and-Compliance-Monitoring
   ```

2. **Environment**:
   ```
   pip install -r requirements.txt
   # Or use conda: conda env create -f environment.yml (if provided)
   ```

3. **Run Analysis** (Jupyter recommended):
   ```
   jupyter notebook analysis/
   # Execute notebooks sequentially: 01 → 02 → 03 → 04
   # Outputs auto-save to /results/
   ```

4. **View Results**:
   - Trends: Open [/results/visualizations/timeline_trend.png](results/visualizations/timeline_trend.png) – 50% 2025 dominance.
   - Metrics: [/results/comparison_tables/table_i_frameworks.csv](results/comparison_tables/table_i_frameworks.csv) – Threat Detection: 90.9% accuracy.
   - Gaps: [/results/visualizations/gap_keywords.png](results/visualizations/gap_keywords.png) – Quantum: High gap (0%).

## Progress Video (4:32 min)
[Loom Video Link](https://www.loom.com/share/[your-loom-link])  
- **Overview** (Group Intro): Project scope, baseline extension, and 50% milestone.
- **[Your Name] (2 mins)**: Data pipeline (JSON → CSVs) and themes (e.g., "62.5% Compliance via categorization.csv").
- **[Partner Name] (2 mins)**: Notebook demos (trends viz, heatmap) + gaps (e.g., "Quantum 0%—future quantum audits!").
- **Q&A**: Open for Prof. Pakshad (@ppakshad) feedback.

## Group Information
- **Members**: [Jerusalem Mesfin Tasew] ([jtasew@hawk.illinoistech.edu]), [Partner Name] ([partner.email@university.edu])
- **Course**: Cyber Security Management – Fall 2025
- **Submission**: Pre-approved pair; all impl files (notebooks, data) uploaded for Oct 19 deadline.