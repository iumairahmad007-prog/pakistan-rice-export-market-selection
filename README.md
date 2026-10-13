# Data-Driven Export Market Selection for Pakistani Rice Exporters: A Market Attractiveness and Demand Analysis

**Umair Ahmad**

A market-screening and decision-support project motivated by international business development around Pakistani rice exports. It combines reproducible historical trade analysis with a separate commercial research judgment for a Basmati-focused exporter. It does not predict sales, profitability, buyer conversion or successful entry.

Read the [final report (PDF)](reports/Final_Report.pdf), [HTML report](reports/Final_Report.html) or [Markdown report](reports/Final_Report.md).

## Business question

Which foreign rice markets should a resource-constrained Pakistani exporter investigate first based on observable trade data and commercially relevant evidence?

The business focus is Basmati, including 1121 and 1509. **HS 100630 covers broader semi-/wholly milled rice and cannot isolate those varieties.** PBS Basmati evidence is a separate supporting layer.

## Key findings

- **United States ranks first** under the base historical screen. Azerbaijan and Oman genuinely tie at rank 6, with weight-sensitivity ranges of 6-10 and 6-25 respectively.
- **Quantitative robustness and product fit differ.** Oman has a much larger broad-rice market and direct PBS Basmati evidence, while Azerbaijan's strict ranking is less sensitive to the tested weights.
- **Kenya's market growth and Pakistan's position diverge.** Quantity CAGR is 8.34%, but Pakistan's importer-reported share falls from 53.96% to 29.06%. Aggregate unit values do not establish why suppliers gained or lost share.
- **Mirror evidence can materially disagree.** Kazakhstan's 2023 importer-reported Pakistan trade is about USD 0.847m versus Pakistan-reported exports of USD 32.553m. The values remain separate and unresolved.
- **The UK stays visible without a quantity score.** Missing World weights are not repaired with zero, bilateral weights or interpolation. Forecasting is deliberately excluded because the annual series lack sufficient depth for robust validation here.
- **Commercial research groups differ from the numerical ranking.** Tier 1: Oman and Azerbaijan. Tier 2: Kenya, UK, United States and Australia. Data-limited watchlist: Kazakhstan and Uzbekistan. Reserves: Malaysia, South Africa and Türkiye. There is no numerical ordering within a group.

## Methodology

The common year is **2023**, selected by a predeclared reporting-continuity gate. Quantity growth and variability use **2018-2023**; size and pooled unit value use **2021-2023**. Available 2024-2025 observations are separate recent context, not ranking inputs.

The main reference contains **69 strict markets** with six positive unestimated quantities. **65 estimated-quantity additions** enter a separately normalized **134-market extension**. A further 67-market quality sensitivity excludes Malawi and Mauritius only for that case; main membership stays unchanged.

The base weights are **40% size, 30% physical quantity growth, 20% stability and 10% pooled unit value**. Average-rank percentiles address highly skewed distributions; five weight scenarios test sensitivity. Weights are assumptions, not objective market truths. Pakistan share, supplier structure, population/income and commercial evidence remain outside the score.

Primary values and source flags are retained. Quantity is net weight / 1,000. Missing is not zero; no imputation or automatic outlier deletion is used. Pakistan shares use destination-reported numerator and denominator. Exporter mirror values and PBS fiscal years stay separate. See [methods, sources and concise dictionary](docs/Methods_and_Sources.md).

## Data sources

| Source | Use |
|---|---|
| [UN Comtrade](https://comtradeplus.un.org/) | Annual World imports, imports from Pakistan, Pakistan-reported exports and 2018/2023 supplier snapshots |
| [World Bank](https://data.worldbank.org/) | Individual-economy population and GDP per capita context |
| [Pakistan Bureau of Statistics](https://www.pbs.gov.pk/wp-content/uploads/2020/07/Annual-Analytical-Report-on-Trade-Statistics-of-Pakistan-FY2023-24-3.pdf) | FY2023/FY2024 Basmati evidence for listed top-20 destinations |
| Official customs, government and sector sources | Dated access/product evidence in the [Phase 6 source register](docs/phase6_source_register.csv) |

Trade/source snapshot: 25-26 September 2026. Commercial review: 26-28 September 2026. Exact query URLs, timestamps and hashes are in [the download manifest](data/raw/download_manifest.json). The full [data dictionary](docs/data_dictionary.json) records definitions, transformations, units and limitations.

## Project workflow

The single notebook covers acquisition checks, cleaning, exploratory metrics, scoring, sensitivity, supplier/mirror checks and dashboard-input preparation. Commercial interpretation is documented separately. Forecasting was excluded after a feasibility review. This final report packages the approved work without adding analysis; earlier phase audits remain dated checkpoints.

## Dashboard

Four pages cover the global screen, six-market comparison, Pakistan's competitive position and ranking robustness. Open the [reference layouts](dashboard/Dashboard_Reference_Preview.html) and [Power BI build guide](dashboard/Power_BI_Build_Guide.md).

**Status:** import-ready tables, DAX, Power Query, theme and validated reference layouts are supplied. Native Power BI Desktop assembly, M/DAX execution and acceptance checks remain pending. No tested `.pbix` is claimed. Dashboard styling was not changed during Phase 9.

Final screenshot slots, to be replaced only after Desktop checks:

- [FINAL DASHBOARD SCREENSHOT - PAGE 1]
- [FINAL DASHBOARD SCREENSHOT - PAGE 2]
- [FINAL DASHBOARD SCREENSHOT - PAGE 3]
- [FINAL DASHBOARD SCREENSHOT - PAGE 4]

## Repository structure

```text
rice-export-market-selection/
  README.md
  requirements.txt
  requirements-report.txt
  data/
    raw/                    Preserved source files and manifest
    processed/              Six clean tables and one crosswalk
  notebooks/
    rice_market_analysis.ipynb
  dashboard/                Import tables, M/DAX, theme and build materials
  reports/
    Final_Report.md
    Final_Report.html
    Final_Report.pdf
    figures/                Approved figures and report presentation figure
    tables/                 Approved analytical and commercial outputs
  docs/                     Methods, dictionary, reproduction guide and audits
```

Existing `reports/tables` and `reports/figures` paths are retained so the notebook and its references remain reproducible. No duplicate `outputs` tree is added. See the [complete project file tree](docs/PROJECT_FILE_TREE.txt).

## How to reproduce

Use Python 3.12 and a virtual environment. From the extracted project root:

```bash
python -m pip install -r requirements.txt jupyter
jupyter notebook notebooks/rice_market_analysis.ipynb
```

Run all cells in order. The notebook works from the project or `notebooks` directory and uses saved local data; no API key or live acquisition is needed. The final cell prepares dashboard inputs. They can also be rebuilt with `python dashboard/build_powerbi_inputs.py`.

**Verification:** all 37 code cells executed sequentially in a fresh Python process in an isolated copy. All 54 manifested source hashes passed. The 23 calculated CSV outputs reproduced byte-for-byte; the manual commercial matrix also stayed identical. This was not a Jupyter-kernel or Power BI Desktop execution. The canonical notebook and approved results were not overwritten.

See [detailed reproduction instructions and report exhibit register](docs/Reproducibility.md) and [Phase 9 integrity checks](docs/Phase_9_Integrity_Check.json). Historical calculations reproduce from the snapshot; dated commercial/web research does not automatically refresh.

## Limitations

The product code is not Basmati-specific and the ranking is historical. Reporting gaps, official estimates and unusual source observations qualify quantity interpretation. The UK's missing World weights prevent a quantity score. Supplier economies do not identify companies; mirrors may disagree substantially. Unit values are not prices or margins. Subjective scores, research groups and sensitivity ranges are not success probabilities.

No buyer-level demand verification, freight-cost model, payment-risk assessment or sales/profit forecast is included. Tariffs and regulations can change. Buyer qualification, exact specifications and current shipment requirements must be verified before commercial commitment. No realized business impact is claimed.

## Tools used

Python, pandas, NumPy and Matplotlib; a Jupyter notebook as the analytical deliverable; DAX and Power Query build materials for Power BI, with Desktop validation pending. Pandoc and ReportLab produce the final report. SQL, machine learning and forecasting models were not used.

## Author

Umair Ahmad - BBA Finance, with minors in Mathematics and Data Analytics, Lahore School of Economics.
