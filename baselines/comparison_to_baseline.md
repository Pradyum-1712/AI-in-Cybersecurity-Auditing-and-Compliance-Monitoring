# Comparison to Baseline: Extending the XAI Survey in Cybersecurity

## Baseline Overview: Ref [9] - "A Comprehensive Survey of Explainable Artificial Intelligence in Cybersecurity" (2025, IEEE)
- **Core Focus**: Systematic review of XAI techniques (e.g., SHAP, LIME) for cyber applications like threat detection and anomaly identification. Covers ~100 studies, taxonomy of methods (average accuracy ~89%, high explainability), integration challenges (e.g., class imbalance), and benchmarks on datasets like CIC-IDS2018.
- **Strengths**: Deep emphasis on transparency for building trust in audits; combines qualitative/quantitative evaluations (e.g., SHAP outperforms LIME by 7% in cyber accuracy contexts).
- **Limitations**: Narrowly scoped to XAI—overlooks compliance frameworks (e.g., NIST/GDPR mapping), agentic/autonomous AI, generative risks, and hybrid tools (e.g., blockchain integration). Static pre-2025 trends; no sub-theme breakdowns or forward-looking gap analysis for ethics/SMEs.
- **PDF**: [baseline_paper_9.pdf](baseline_paper_9.pdf)

## Our Survey Extensions (40 Papers, 2022–2025)
Our work builds directly on [9]'s XAI foundation by synthesizing 40 peer-reviewed references (IEEE/ACM/Elsevier/Springer), broadening to holistic AI applications in auditing and compliance. Key expansions:
- **Broader Taxonomy**: Introduces 5 sub-themes (e.g., 62.5% Compliance Frameworks extends [9]'s detection focus; 30% Threat Detection builds on XAI subset). See [data/categorization.csv](data/categorization.csv) for ref lists (e.g., Refs [3],[5],[10]–[14],[18]–[20],[21]–[28],[32]–[35],[37],[39],[40] for Compliance).
- **Trends & Metrics**: 50% papers in 2025 (vs. [9]'s static snapshot)—surge in compliance/agentic themes (+17.6% growth from 2024). Avg accuracy 91.3% (up from [9]'s 89%); explainability median 3.5/5, with XAI & Ethics at 5.0. Compare via [results/comparison_tables/table_i_frameworks.csv](results/comparison_tables/table_i_frameworks.csv).
- **Gaps Bridged**: [9] omits blockchain for audits [30] and shadow AI risks [31],[36]; we quantify (e.g., 5% 'bias' mentions—High Gap in [results/statistics/gap_report.csv](results/statistics/gap_report.csv)). Adds SME/quantum focus [37] (0% mentions—High Gap).
- **Novelty**: Proposed taxonomy diagram [docs/taxonomy_diagram.png](docs/taxonomy_diagram.png) fuses XAI with compliance layers—first post-AI Act unified view.

## Key Gaps in Baseline & Our Contributions
| Aspect | Baseline [9] | Our Survey |
|--------|--------------|------------|
| **Scope** | XAI-only (detection emphasis) | 5 sub-themes incl. compliance/threat (40 refs; 62.5% Compliance) |
| **Trends** | Pre-2025 static | 2025 surge (50%); +17.6% growth from 2024 [results/visualizations/timeline_trend.png](results/visualizations/timeline_trend.png) |
| **Metrics** | 89% acc, high expl | 91.3% acc; sub-theme heatmaps [results/visualizations/performance_heatmap.png](results/visualizations/performance_heatmap.png) |
| **Gaps** | No ethics/SME/regs | Keyword analysis (e.g., 'quantum' 0%—High Gap) |
