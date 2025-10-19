# Comparison to Baseline: Extending the XAI Survey in Cybersecurity

## Baseline Overview: Ref [9] - "A Comprehensive Survey of Explainable Artificial Intelligence in Cybersecurity" (2025, IEEE)
- **Core Focus**: Systematic review of XAI techniques (e.g., SHAP, LIME) for cyber applications like threat detection and anomaly identification. Covers ~100 studies, taxonomy of methods, integration challenges (e.g., class imbalance), and benchmarks on datasets like CIC-IDS2018.
- **Strengths**: Emphasizes transparency for trust in audits; qualitative/quantitative evaluations (e.g., SHAP outperforms LIME by 7% in accuracy).
- **Limitations**: Narrow XAI scope—overlooks compliance (e.g., NIST/GDPR), agentic AI, generative risks, and hybrids (e.g., blockchain). Static pre-2025 trends; no sub-theme breakdowns or ethics/SME gaps.
- **PDF**: [baseline_paper_9.pdf](docs/Paper_9(baseline)_Summary.pdf)

## Our Survey Extensions (40 Papers, 2022–2025)
Builds on [9]'s XAI foundation with 40 peer-reviewed refs (IEEE/ACM/Elsevier/Springer), expanding to auditing/compliance:
- **Taxonomy**: 5 sub-themes (62.5% Compliance Frameworks; 30% Threat Detection). See [data/categorization.csv](data/categorization.csv).
- **Trends**: 50% papers in 2025 (+17.6% growth from 2024). See [results/visualizations/timeline_trend.png](results/visualizations/timeline_trend.png).
- **Gaps Bridged**: Adds blockchain [30], shadow AI [31],[36]; quantifies e.g., 0% 'quantum' mentions (High Gap in [results/statistics/gap_report.csv](results/statistics/gap_report.csv)).
- **Novelty**: Taxonomy diagram [docs/taxonomy_diagram.png](docs/taxonomy_diagram.png) fuses XAI with compliance—post-AI Act view.

## Key Gaps in Baseline & Our Contributions
| Aspect | Baseline [9] | Our Survey |
|--------|--------------|------------|
| **Scope** | XAI-only (detection) | 5 sub-themes incl. compliance (40 refs; 62.5% Compliance) |
| **Trends** | Pre-2025 static | 2025 surge (50%); +17.6% growth [timeline_trend.png](results/visualizations/timeline_trend.png) |
| **Gaps** | No ethics/SME/regs | Keyword analysis (e.g., 'quantum' 0%—High Gap) [gap_report.csv](results/statistics/gap_report.csv) |

This extends [9]'s XAI into a compliance roadmap, forecasting e.g., quantum-resilient audits.

*Generated Oct 19, 2025 – For 50% progress: See README.md for video demo.*