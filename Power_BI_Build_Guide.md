# Phase 8 — Power BI build guide

**Status: import-ready dashboard package and verified reference previews. Native Power BI Desktop assembly and acceptance testing remain to be completed.** No `.pbix` file is supplied or claimed to have been tested. This fulfills the project's Power BI structure/instructions option while making the remaining Desktop work explicit.

The report answers: which historical market profiles deserve investigation, how do the six focus markets differ, where does Pakistan stand, and how sensitive are the scores? Use four pages and eight main visuals. `Dashboard_Reference_Preview.html` shows the intended appearance using actual approved data. Those images are reference renders, not screenshots from Power BI.

## Start here

1. Extract `Power_BI_Build_Package.zip` into a stable folder on your computer. The `data` folder contains all seven ready-to-import CSVs. You do not need to run Python for the first build.
2. Open Power BI Desktop and create a blank report. Open **Transform data**. Create a Text parameter named **DataFolder**, containing the full path to the extracted `data` folder, without a trailing slash. For example: `C:/Users/Umair/Documents/Rice_Dashboard/data`.
3. Create a blank query called **DashboardData**, open **Advanced Editor**, and paste the complete `Power_Query.m` file. This staging query returns a record of typed tables; turn off **Enable load** for it.
4. Create seven blank queries, with the exact names and one-line formulas below. Use the **formula bar** for these expressions (enable it under View if needed). If using Advanced Editor instead, omit the leading `=`. Only these seven queries should load to the model. Select **Close & Apply**.

| Query name | Formula | Expected rows |
|---|---|---:|
| Markets | `= DashboardData[Markets]` | 181 |
| AnnualImports | `= DashboardData[AnnualImports]` | 1,013 |
| Scenarios | `= DashboardData[Scenarios]` | 7 |
| Screening | `= DashboardData[Screening]` | 546 |
| SupplierShares | `= DashboardData[SupplierShares]` | 262 |
| MirrorComparison | `= DashboardData[MirrorComparison]` | 18 |
| PBSBasmati | `= DashboardData[PBSBasmati]` | 12 |

Empty CSV cells are converted to `null`, then columns receive explicit types with `en-US` numeric parsing. A missing expected column should produce an error; do not replace it with invented data. The full schemas and field provenance are in `data_dictionary.csv`.

## Build the model

In **Model view**, remove any automatically detected relationships that conflict with this list. Create these six active relationships, all **one-to-many**, with **single-direction filtering from the first table to the second**:

| One side | Many side | Match |
|---|---|---|
| Markets | AnnualImports | EconomyID → EconomyID |
| Markets | Screening | EconomyID → EconomyID |
| Markets | SupplierShares | EconomyID → EconomyID |
| Markets | MirrorComparison | EconomyID → EconomyID |
| Markets | PBSBasmati | EconomyID → EconomyID |
| Scenarios | Screening | ScenarioID → ScenarioID |

**Plain-language explanation:** Markets supplies one identity per economy. Each detailed table contains repeated observations for that economy. This lets one market selection filter its details without joining supplier rows directly to annual imports and multiplying values.

Do not create relationships between the detailed tables, between their year columns, or between `FiscalYear` and calendar year. There is deliberately no global year slicer: the score is fixed at 2023, trends use 2018–2023, supplier snapshots use 2018/2023, and PBS uses fiscal-year labels.

Use `Markets[Market]` for market names in visuals and slicers, not a name from a detailed table. `EconomyID` is the stable join key. The only display alias is **USA → United States**; the source name and Comtrade code 842 are retained. Other source identities are preserved.

Set:

- `Markets[Market]`: sort by `FocusOrder` for the focus comparison; explicit measure sorting overrides it in ranking visuals.
- `Scenarios[Scenario]`: sort by `ScenarioOrder`.
- Numeric identifiers and year fields: **Don't summarize**.
- Raw metric columns in Markets: **Don't summarize**; prefer the supplied measures in visuals.
- Turn off automatic date hierarchies for this report if enabled. Use the numeric year fields directly.

## Add measures and formatting

Create each definition in `DAX_measures.dax` separately using **Modeling → New measure**. Keep their home table as Markets. Do not paste all definitions into a single measure editor.

| Measure group | Format |
|---|---|
| Selected score | Decimal, 1 place |
| Original universe rank, universe size, visible markets, strict/extended ranks | Whole number |
| Market size USD m, annual import value USD m, both mirror values | Decimal, 1–2 places; label the visual USD m |
| Quantity CAGR, Pakistan shares, Supplier share | Percentage, 1–2 places; values are stored as fractions |
| Growth variability pp, Pakistan share change pp | Decimal, 1–2 places; label **percentage points**, not percentage |
| Pooled unit value USD t | Decimal, 0–2 places; label USD/tonne |
| Annual quantity thousand t | Decimal, 1 place; label thousand tonnes |
| PBS Basmati value USD m | Whole number; source values are rounded |
| PBS Basmati tonnes | Whole number |
| Notes and rank range | Text |

**Why the guards?** A score or share across several unrelated markets is not a meaningful card value. `HASONEVALUE` permits single-market displays; multiple selections return blank where aggregation would mislead. `DIVIDE` preserves unavailable ratios as blank. No numeric `COALESCE(...,0)` is used.

The imported `OriginalRank` values remain tied to their approved universe. There is no `RANKX` and no dynamic re-normalization. Filtering to Oman must not turn rank 6 into rank 1.

Import `Rice_Export_Theme.json` through **View → Themes → Browse for themes**. Use a 16:9 page, white/light-grey backgrounds, readable 11–12 point visual text, and restrained teal/blue/amber colors. Label Panel A, Panel B and contextual status in text as well as color.

## Page 1 — Historical market screen

**Question:** which strict-panel profiles score highly, and how do size and physical growth differ?

Set page filters: `Markets[StrictPanel] = true`; `Scenarios[ScenarioID] = strict_base`. Do not use report-level scenario filters or synchronize them to other pages.

Use four simple cards/text labels: original reference size 69; base weights 40/30/20/10; common year 2023; “Historical research screen”. If you add a market slicer, show **Visible scored markets** separately from **Original universe size**.

| Visual | Fields and setup |
|---|---|
| Horizontal bar: strict base top 15 | Category: `Markets[Market]`; value: **Selected score**. Visual filter: `Markets[StrictBaseRank] ≤ 15`. Sort score descending. Axis 0–100. Tooltip: **Original universe rank**, four raw metrics, `ReviewNote`. Equal scores retain equal ranks; bar order does not break a tie. |
| Scatter: size versus physical growth | Point/category field (Values/Details): `Markets[Market]`; X: **Quantity CAGR**; Y: **Market size USD m**. Use a logarithmic Y scale and label it. Keep the full X range, including negative growth and small-base extremes. Do not trim or exclude outliers. Tooltip: panel, unit value, variability and review note. |

Always show: **Common year 2023; size 2021–2023; quantity 2018–2023; HS 100630 is broader than Basmati.** Keep the strict reference at 69 even if fewer markets are displayed.

## Page 2 — Six-market comparison

**Question:** how do the commercially relevant markets compare, including those outside the main score?

Set page filter `Markets[IsFocus] = true`. No strict-panel or scenario page filter. Add a single-select `Markets[Market]` slicer, default Oman.

| Visual | Fields and setup |
|---|---|
| Six-market comparison table | Market, Panel, **Market size USD m**, **Quantity CAGR**, **Growth variability pp**, **Pakistan share 2023**, **Strict base rank**, **Extended base rank**, ResearchGroup. Headers must distinguish ranks **/69** and **/134**. Show all six, in FocusOrder. Turn totals off. Use **Edit interactions** so the market slicer and lower charts do **not** filter this comparison table. |
| Annual value line | Axis: `AnnualImports[Year]`; value: **Annual import value USD m**. Single selected market, 2018–2023, year ascending. Start Y at zero. Tooltip: Year, WorldSourceFile and annual Pakistan share where present. |
| Separate quantity line | Axis: `AnnualImports[Year]`; value: **Annual quantity thousand t**. Separate axis/visual from value. Tooltip: QuantityQuality, AnyQuantityEstimated and QuantityFieldReview. The measure intentionally suppresses the entire line when the six-year quantity panel is incomplete. |

Add **Market status** as a text/card visual and **Pooled unit value USD t** as a tooltip or small card. For the UK, show “Contextual market — excluded from quantity-based scoring due to missing World net weights.” Its value line stays available, while quantity CAGR, variability, pooled full-window unit value, score, ranks and quantity line remain blank.

The broader rank includes 69 strict plus 65 estimated additions and uses its own percentiles. Do not color the strict and extended rank columns as though they were a single ranking. ResearchGroup is a separate qualitative Phase 6 judgment.

## Page 3 — Pakistan and supplier countries

**Question:** who supplies the market, and do Pakistan-related reporting perspectives agree?

Set page filter `Markets[IsFocus] = true`. Use an independent single-select market slicer, default Kenya. Do not synchronize it with Page 2. Show Pakistan share 2023, share change in percentage points, and panel status as cards.

| Visual | Fields and setup |
|---|---|
| Stacked supplier columns | Axis: `SupplierShares[Year]`; legend: `SupplierDisplay`; value: **Supplier share**. Use an ordinary stacked column chart, Y axis 0–100%, not a 100% chart that silently rescales a filtered subset. Keep both 2018 and 2023. Assign Pakistan teal and India amber consistently. |
| Clustered mirror columns | Axis: `MirrorComparison[Year]`; values: **Importer mirror USD m** and **Pakistan exporter mirror USD m**. Keep the distinct years 2018, 2021 and 2023. Label reporting sides explicitly. Do not average them or calculate shares from exporter data. |

Keep legend clicks/other visual selections from filtering the mirror chart: **Edit interactions → None** where appropriate. A supplier selection must not change the source denominator or relabel the selected subset as the whole market. The supplied shares already use destination World totals.

`SupplierDisplay` keeps the union of each snapshot's five largest suppliers plus Pakistan. Remaining ordinary source rows are grouped as “Other supplier countries/areas”. Special categories retain explicit source labels, including “Other Asia, nes”. All 262 detailed component rows remain in the data; no World row is present in this table. This is not company competition.

For supporting PBS context, use a single-select `PBSBasmati[FiscalYear]` slicer (default FY2024), **PBS Basmati value USD m**, **PBS Basmati tonnes** and **PBS context note**. These fiscal-year cards must not filter the calendar-year charts. Keep supplier/mirror interactions from changing the PBS cards.

The dashboard projection retains the six reviewed destinations actually listed in the PBS table: Oman, Kenya, UK, USA, South Africa and Australia, with two fiscal years each. The full original 40-row table remains in the main project. For Azerbaijan, Kazakhstan, Uzbekistan, Malaysia and Türkiye, display the note about absence from the top-20 evidence—not zero.

## Page 4 — Sensitivity and limitations

**Question:** do historical positions survive changes in the assumed weights?

Do not apply a scenario page filter. Use a matrix:

- Rows: `Markets[Market]`.
- Columns: `Scenarios[Scenario]`, sorted by ScenarioOrder.
- Values: **Original universe rank**.
- Visual filters: `Scenarios[Family] = Strict weights`; `Markets[StrictBaseRank] ≤ 15`.
- Sort rows by the Base rank column, ascending. Turn row/column totals off.
- Optional background rule: ranks 1–10 pale teal, others neutral. Explain that this highlights the five tested cases, not success probability.

Keep a concise note beside the matrix:

> Azerbaijan ranges from 6–10; Oman from 6–25. The 67-market quality sensitivity excludes Malawi and Mauritius only for that case and preserves the same base top-10 membership. The 134-market extension includes official estimates and has separate normalization. Kenya is 10th there; Kazakhstan 75th and Uzbekistan 89th. The UK remains unscored.

The quality and extended scenarios are supplied in Screening for inspection, but do not put their scores into the five-column strict matrix. Page 2 already displays the extended focus ranks separately.

Include the Phase 7 decision: **Forecasting was intentionally excluded because the short annual series do not support robust validation in this project.** Do not turn on Power BI's automatic forecasting or trend-extrapolation features.

## Desktop acceptance checks

These are required before claiming that a native Power BI dashboard is complete. The CSV calculations and reference renders were checked here; Power Query, DAX execution and interactions have not been run inside Power BI Desktop.

| Check | Expected behavior |
|---|---|
| Seven tables load | Row counts match the import table above; no conversion errors |
| Strict base result | USA score 81.764706, rank 1; Azerbaijan and Oman score 67.352941, both rank 6 |
| Filter to Oman | Original rank remains 6; original universe size remains 69 |
| Two weight-sensitive cases | Azerbaijan 6–10; Oman 6–25; no-unit-value ranks are 6 and 8 respectively |
| Extended focus results | Kenya 10, Kazakhstan 75, Uzbekistan 89; UK blank; universe 134 |
| UK selection on Page 2 | All six comparison rows remain; UK value line appears; quantity line and quantity metrics are blank |
| Kenya estimation | Panel B throughout; Year 2021 quantity marked estimated; Year 2023 unestimated |
| Missing bilateral record | Pakistan share stays blank, not zero |
| Uzbekistan 2018 mirror | Exporter value stays blank, not zero |
| Kazakhstan 2023 mirror | Importer about USD 0.847m versus exporter USD 32.553m; never averaged |
| Supplier share totals | Each focus market/year sums to approximately 100%; no World component |
| PBS context | Oman FY2024 USD 71m / 58,249 t; UK USD 45m / 37,395 t; Azerbaijan no observation |
| Year and forecast boundary | No 2024/2025 ranking inputs; no forecast line |

Save the resulting Desktop report as `Rice_Export_Market_Selection.pbix`. Capture screenshots only after these checks; use those real screenshots for later portfolio claims. The current preview images must remain labelled as references.

## Refresh and reproducibility

For the initial Desktop build, use the included CSV snapshot. **Refresh** reloads those files; it does not call Comtrade or update the analysis to 2026.

From the full project, reproduce the presentation tables with:

```bash
python dashboard/build_powerbi_inputs.py
```

Optional: recreate the reference images with `python dashboard/render_reference_pages.py`.

The notebook's Phase 8 cell runs the same short export helper. It copies/reshapes approved outputs, preserves missingness and verifies input hashes. Do not edit scores in the CSVs or derive replacements in DAX. New trade data, new weights or a new common year require a separately reviewed analysis refresh.

The dashboard uses the Phase 6 research groups unchanged and records the Phase 7 no-forecast decision. Stop here for dashboard review before Phase 9 report/README and Phase 10 public/CV material.

## Official implementation references

Checked 28 September 2026; the project's statistical choices come from the approved notebook, not these software documents.

- [Microsoft: star-schema guidance](https://learn.microsoft.com/power-bi/guidance/star-schema)
- [Microsoft: create/manage relationships](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships)
- [Microsoft: Csv.Document](https://learn.microsoft.com/en-us/powerquery-m/csv-document)
- [Microsoft: Table.TransformColumnTypes](https://learn.microsoft.com/en-us/powerquery-m/table-transformcolumntypes)
- [Microsoft: HASONEVALUE](https://learn.microsoft.com/en-us/dax/hasonevalue-function-dax)
- [Microsoft: SELECTEDVALUE](https://learn.microsoft.com/en-us/dax/selectedvalue-function-dax)
- [Microsoft: DIVIDE](https://learn.microsoft.com/en-us/dax/divide-function-dax)
- [Microsoft: custom report themes](https://learn.microsoft.com/en-us/power-bi/create-reports/report-themes-create-custom)
