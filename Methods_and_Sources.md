# Methods, sources and concise data dictionary

The final report summarizes approved analysis through Phase 8. This document is a compact guide to the full field-level `data_dictionary.json`, not a replacement for it. No analytical definition was changed during Phase 9.

## Source inventory

Trade inputs and economic context were downloaded on 25-26 September 2026. Official HS reference lists were added in Phase 3. `data/raw/download_manifest.json` contains exact per-file URLs, UTC retrieval times and SHA-256 hashes: 49 original source files plus five HS references. The PBS PDF is preserved; its separate manifest records the original document.

| Clean table | Rows | Grain and coverage | Primary source |
|---|---:|---|---|
| market_imports_clean.csv | 1,792 | Reporter economy/year, World partner, 2015-2025; includes 11 Pakistan reference rows excluded from foreign screening | [UN Comtrade](https://comtradeplus.un.org/) |
| imports_from_pakistan_clean.csv | 1,231 | Destination/year, importer-reported Pakistan partner, 2015-2025 | [UN Comtrade](https://comtradeplus.un.org/) |
| suppliers_clean.csv | 274 | Focus market/year/supplier, 2018 and 2023; 262 components plus 12 World totals | [UN Comtrade](https://comtradeplus.un.org/) |
| pakistan_exports_clean.csv | 1,255 | Pakistan-reported destination/year, 2015-2025; includes 11 World totals | [UN Comtrade](https://comtradeplus.un.org/) |
| economic_context_clean.csv | 2,387 | Individual economy/year, 2015-2025; missing GDP values remain missing | [World Bank population](https://data.worldbank.org/indicator/SP.POP.TOTL), [GDP per capita](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD) |
| pbs_basmati_supporting.csv | 40 | Twenty listed destinations x FY2023/FY2024 | [PBS annual trade report](https://www.pbs.gov.pk/wp-content/uploads/2020/07/Annual-Analytical-Report-on-Trade-Statistics-of-Pakistan-FY2023-24-3.pdf), Table 16, PDF page 36 |
| country_economy_crosswalk.csv | 223 | Source identities, codes, entity types and documented mappings | Comtrade and World Bank metadata; explicit manual mappings |

Counts are rows, not unique foreign markets. World totals must not be added to their own components. The notebook reads these sources locally and explicitly transcribes the PBS table. It does not scrape a fresh Basmati series.

## Main clean-table fields

Comtrade fields below retain source dates in `source_downloaded_at_utc` and provenance in `source_file`. Original units and flag meanings are recorded in the full dictionary. All trade measures concern HS 100630, not exact Basmati varieties.

| Field | Unit / definition | Transformation and limitation |
|---|---|---|
| country_economy_id | Source-prefixed text identifier, such as CT:031 | Stable joins; source territories are not silently renamed |
| country_comtrade_code | Comtrade source code | Not interchangeable with ISO numeric codes; USA is 842, India is 699 |
| year; hs_code; hs_revision | Calendar year; product code; reported HS revision | HS H2-H6 reviewed; no material broad-code break found, but product mix can change |
| import_value_usd | Primary import trade value, nominal USD | Retained directly; CIF/FOB metadata do not silently replace primary value |
| net_weight_kg | Reported physical net weight, kg | Missing/nonpositive quantities remain explicit; no interpolation or supplementary substitution |
| import_quantity_tonnes | Net weight in metric tonnes | net_weight_kg / 1,000; never Pakistan bilateral weight substituted for World weight |
| is_net_weight_estimated; any_quantity_estimated | Source net-weight flag; combined source quantity flag | Row-level information, distinct from full-window panel membership |
| quantity_quality | observed_unestimated, observed_estimated, missing, nonpositive or unusable | Mechanical quality classification; observed does not prove correctness |
| valid_value_quantity_pair | Usable positive matched value and weight | Ratios require valid pairs; blanks are not zero |
| strict_panel_2018_2023 | Boolean; strict six-year eligibility | 69 foreign markets; no officially estimated quantity years |
| broader_panel_addition_2018_2023 | Boolean; complete but estimated addition | 65 additional markets; not the entire 134-market extension |
| quantity_complete_2018_2023 | Boolean; complete positive matched window | 134 total; does not imply strict eligibility |
| estimated_quantity_years_2018_2023 | Number of flagged years | Kenya remains B because 2021 is estimated, even though 2023 is unestimated |
| contextual_only | Boolean | Includes UK; retain value/supplier context without inventing quantity metrics |
| review_quantity_field_difference | Boolean review flag | Preserves supplementary/net-weight discrepancies; does not replace either source field |

World Bank population is persons; GDP per capita is current USD/person, not household income or measured Basmati affordability. Aggregates are excluded. PBS values are rounded USD million in the source, converted to USD in the clean table; quantities are tonnes. Fiscal years remain fiscal years, and absent top-20 destinations receive no synthetic rows.

## Approved metrics and scoring

Market size is the mean of three annual primary values in 2021-2023. Quantity CAGR is `(Q2023/Q2018)^(1/5)-1`. Variability is sample SD (`ddof=1`) across five annual quantity-growth rates. Pooled unit value is matched value sum divided by matched tonnes sum, not an average of annual ratios. The UK partial one-year ratio is flagged in exploratory output and excluded from full-window/dashboard comparisons.

Pakistan share uses a destination's imports from Pakistan divided by the same destination's World value. Missing Pakistan-partner rows remain missing. Mirror exports never enter that denominator calculation. Supplier shares likewise use the destination World total. Country/area HHI is descriptive and includes labelled non-World components; it does not measure company competition.

For each universe, percentiles equal `100*(average rank-1)/(n-1)`; stability reverses the variability percentile. A constant metric receives 50. Base weights are size/growth/stability/unit value = 40/30/20/10. All are subjective assumptions. Ranking applies 12-decimal rounding for numerical tie tolerance and competition ranks (`method='min'`); presentation rounding does not break ties.

Strict weight scenarios keep the same 69-market component percentiles. Growth emphasis is 25/50/15/10; stability emphasis 35/15/40/10; equal weights 25 each; no-unit-value weights are exactly 4/9, 1/3, 2/9 and zero. Quality sensitivity re-normalizes 67 cases excluding Malawi and Mauritius. The extension re-normalizes 134 cases with base weights only. Do not compare scores across universes as a fixed common scale.

## Commercial interpretation and references

Research groups are unchanged qualitative judgments recorded in `reports/tables/commercial_evidence_matrix.csv` and the Phase 6 review. Market access and route practicality are dated, qualified evidence; no new numerical commercial score or freight model exists. `phase6_source_register.csv` contains agency, URL, date, supported claim and limitation for each source. It includes official tariffs, regulations, public statistical sources and clearly labelled primary operator/transport evidence.

The model is an historical research screen. No causal result, market selling price, margin, buyer demand, sales conversion or forecast is established.
