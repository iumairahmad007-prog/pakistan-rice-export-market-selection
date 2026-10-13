# **Data-Driven Export Market Selection for Pakistani Rice Exporters: A Market Attractiveness and Demand Analysis** 

#### **Umair Ahmad** 

Data-driven international trade / market-selection project 

28 September 2026 

### **Purpose** 

Which foreign rice markets should a resource-constrained Pakistani exporter investigate first based on observable trade data and commercially relevant evidence? 

This report presents a historical market screen, sensitivity checks and a separate commercial interpretation for a Basmati-focused export business. It is intended to support the allocation of research effort. 

### **Evidence boundaries** 

Common historical year: **2023** . Physical quantity window: **2018-2023** . Market-size and unit-value window: **2021-2023** . 

The main quantitative reference is **69 strict-panel markets** . A separately normalized extension contains **134 quantity-complete markets** , including **65 officially estimated additions** . 

Trade snapshot acquired 25-26 September 2026. Commercial evidence reviewed 26-28 September 2026. No 2024-2025 observation enters the ranking. 

**HS 100630 is not Basmati-specific. No sales or profitability forecast is made.** 

1 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **1. Executive summary** 

A Pakistani rice exporter with limited time and resources needs a disciplined way to decide which foreign markets deserve further investigation. Import volume alone cannot answer that question: a large market may have slow physical growth, established suppliers, unsuitable product demand or difficult access. A sharp one-year increase may instead reflect a small starting base, exceptional shipments or reporting gaps. 

This project combines preserved UN Comtrade records with World Bank economic context and separate Pakistan Bureau of Statistics (PBS) Basmati evidence. The common historical year is 2023. Quantity analysis covers 2018-2023; market size and pooled unit value use 2021-2023. A conservative main panel contains 69 markets with complete positive, unestimated quantities. Another 65 markets enter a separately labelled 134-market sensitivity universe. Missing observations remain missing, and importer and exporter reports are kept separate. 

The transparent base screen assigns 40% to market size, 30% to physical growth, 20% to stability and 10% to pooled import unit value. Percentile normalization limits the influence of highly skewed raw magnitudes. These weights express business judgment. The United States scores highest. Azerbaijan and Oman genuinely tie at rank 6, but their ranges across five weighting scenarios differ: 6-10 for Azerbaijan and 6-25 for Oman. 

Commercial research priorities are a separate interpretation of the screen, supplier structure, Pakistan's position, Basmati evidence, dated access research and practical uncertainties. Tier 1 comprises Oman and Azerbaijan. Tier 2 comprises Kenya, the United Kingdom, the United States and Australia. Kazakhstan and Uzbekistan form a data-limited watchlist; Malaysia, South Africa and Türkiye remain reserves. There is no numerical ordering within these groups. Oman's stronger direct Basmati evidence can matter more to the business case than Azerbaijan's narrower rank range. 

HS 100630 measures broad semi-/wholly milled rice, not exact demand for 1121 or 1509 Basmati. Unit values are not selling prices or margins; supplier countries are not buyer companies. Kenya demonstrates that growing total imports can coexist with a falling Pakistan share, while Kazakhstan's large mirror-data gap limits bilateral confidence. The UK remains commercially visible despite missing World quantities. Forecasting is deliberately excluded because the short annual series cannot support robust validation here. The result is a reproducible research framework, not a prediction of sales, profitability or successful entry. 

### **2. Business problem** 

The motivation comes from international business development around Pakistani rice exports. Time spent contacting buyers, investigating compliance or arranging market visits has an opportunity cost. Headline import value, a single year's growth or Pakistan's existing share is insufficient on its own. Physical trends, volatility, supplier competition, product fit, access, logistics and data confidence all affect the next research decision. This project makes the initial screen explicit and reproducible while leaving buyer qualification and shipment economics for subsequent commercial work. 

2 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **3. Data, product scope and quality** 

**Table 1. Source and panel overview** 

|**Source / dataset**|**Observation**<br>**window**|**Role in the project**|
|---|---|---|
|UN Comtrade: World imports and<br>imports from Pakistan|Annual<br>2015-2025|Historical size, quantities and importer-based<br>Pakistan shares; ranking uses only approved<br>windows.|
|UN Comtrade: supplier-country<br>snapshots|2018 and 2023|Six focus markets; World totals distinguished<br>from country/area components.|
|UN Comtrade: Pakistan-reported<br>exports|Annual<br>2015-2025|Separate mirror comparison; never<br>substituted into importer-based shares.|
|World Bank: population and GDP<br>percapita|2015-2025, where<br>available|Individual-economy context; aggregates<br>excluded; outside the score.|
|PBS: Basmati destination table|FY2023 and<br>FY2024|Supporting evidence for the 20 listed<br>destinations; absence is not zero.|



Sources: UN Comtrade [1], World Bank [2] and PBS [3]. Original raw files were preserved. The 49 original Phase 2 source files were verified, followed by five retained official HS reference files. Exact URLs, retrieval timestamps and checksums are recorded in the source manifest. 

### **Product and time boundaries** 

HS 100630 covers semi-/wholly milled rice. It cannot isolate 1121 or 1509 Basmati, buyer specifications, achievable selling prices or margins. Brown/husked Basmati may fall outside this code. PBS Basmati observations therefore remain separate fiscal-year commercial evidence. 

The predeclared continuity gate required at least 90% of the previous year's positive-import reporters and 95% of their previous-year import value. **2023 retained 98.19% of reporters and represented 98.03% of prior value; 2024 and 2025 failed the gate.** This assesses continuity of the retrieved product rows, not complete global coverage. The main analysis uses 2018-2023 quantities and 2021-2023 size/unit values. Later observations are recent context only. 

### **Panel and cleaning discipline** 

**Panel A has 69 markets:** six positive quantity observations and no officially estimated quantity flags. **Panel B adds 65 markets:** six positive quantities with at least one official estimate. The 134-market extension has separate normalization; the 69-market ranking remains the main reference. Kenya's 2023 row is unestimated, but its estimated 2021 row keeps the full-window panel at B. 

Primary trade values were retained. Quantity is net weight divided by 1,000; supplementary quantities did not replace it. Source flags and explicit country/economy identifiers were preserved, including "Other Asia, nes" under its source identity. World Bank aggregates were removed from country analysis. H2-H6 reference definitions showed no material break in the broad six-digit rice concept; this does not guarantee unchanged product mix. 

Duplicate keys, years, units, values, supplier totals and panel counts were checked. Missing fields and absent rows were not changed to zero; there was no interpolation, imputation or automatic outlier deletion. Questionable records remain flagged. Importer and exporter mirror values were never averaged. 

3 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **4. Market-screening framework** 

**Size (40%)** uses mean annual import value in 2021-2023. It receives the largest weight because the screen should recognize meaningful market scale. **Physical growth (30%)** uses five-year quantity CAGR: ( Q 2 0 2 3 / Q 2 0 1 8 ) ^ ( 1 / 5 ) - 1 , only for the appropriate complete-quantity panel. It separates physical change from nominal value movements. 

**Stability (20%)** reverses the sample standard deviation of the five annual quantity-growth rates from 2019 through 2023. It moderates profiles dominated by sharp annual changes. **Pooled unit value (10%)** divides the sum of matched import values by matched tonnes in 2021-2023. It receives the lowest weight because product mix, valuation and shipment characteristics weaken its interpretation as value potential. It is not a market price. 

Each component uses an average-rank percentile on a 0-100 scale: 1 0 0  x  ( a v e r a g e  r a n k  - 1 ) / ( n - 1 ) . Variability is reversed; a constant metric receives 50. The weighted average produces the screen score. Percentiles reduce domination by raw outlier magnitudes but also discard economic distances. Weights remain subjective. Pakistan penetration, supplier structure and income context stay outside the composite; a low Pakistan share is not automatically an opportunity gap. 

**Figure 1. Market size versus physical import growth - strict reference** 



<!-- Start of picture text -->
United States<br>Z 1000 7<br>S oman<br>-e<br>3100<br>z * ; Tanzania<br>2 ‘Azerbaijan °<br>3 10<br>v<br>=<br>S$ 1.<br>5aMalawi iigane<br>Eol<br>c<br>G<br>o<br>=<br>0.01<br>-50 0 50 100 150 200<br>Quantity CAGR, 2018-2023 (%)<br><!-- End of picture text -->

Source: approved exploratory metrics; 69 strict markets. Import value uses a logarithmic axis. All observations and extreme values are retained; highlighted labels are examples, not recommendations. 

### **What exploration changed in the interpretation** 

Size is heavily skewed: the strict-panel median is about USD 21.56m, against a maximum of USD 1.385bn. Guyana's approximately 195% CAGR starts from only 391 kg, with a mean market value of about USD 0.21m. Tanzania's variability is dominated by the recorded movement from 25.99 tonnes in 2022 to 139,351 tonnes in 2023; its economic or reporting explanation remains unresolved. Strict eligibility is therefore not a guarantee of perfect source quality. Botswana, Malawi and Mauritius retain their quantity-review flags. These findings support percentile normalization and explicit sensitivity checks, not deleting inconvenient observations. 

4 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **5. Historical results and robustness** 

**Table 2. Top 10 under the strict base screen** 

|**Rank**|**Market**|**Base score / 100**|
|---|---|---|
|1|UnitedStates|81.76|
|2|Malaysia|80.00|
|3|South Africa|72.50|
|4|Türkiye|70.15|
|5|Australia|67.94|
|6|Azerbaijan|67.35|
|6|Oman|67.35|
|8|NewZealand|66.18|
|9|Italy|65.44|
|10|Norway|65.00|



Source: s t r i c t _ m a r k e t _ s c r e e n i n g . c s v . Scores are displayed to two decimals. Equal model totals share competition ranks; Azerbaijan and Oman are both sixth. The ranking uses unrounded results, with a 12-decimal numerical tolerance for ties, rather than displayed values. 

The United States has the strongest base historical profile under the selected assumptions. This result does not establish that it is the easiest or most profitable first market for this exporter. Import scale, growth, stability and aggregate unit value answer a narrower question than access to an appropriate buyer and product segment. 

### **Weight sensitivity** 

Five strict-panel scenarios were tested: base 40/30/20/10; growth emphasis 25/50/15/10; stability emphasis 35/15/40/10; equal weights; and removal of unit value, redistributing the remaining weights proportionately as 4/9, 1/3 and 2/9. The 69-market component percentiles stay fixed across these weight tests. 

**Table 3. Same base position can imply different robustness** 

|**Market**|**Base rank**|**Range across five weights**|
|---|---|---|
|UnitedStates|1|1-2|
|Malaysia|2|1-5|
|Azerbaijan|6|6-10|
|Oman|6|6-25|



Azerbaijan's narrower rank range indicates greater stability to the five tested weight choices. It does not establish stronger Basmati demand than Oman. The ranges are sensitivity outcomes, not confidence intervals or probabilities of sales success. 

A separate 67-market quality check excludes only Malawi and Mauritius and recalculates percentiles. **Base top-10 membership is unchanged.** This does not resolve those countries' source problems. The 134-market extension separately admits the 65 estimated-quantity additions and applies base weights only. Its scores and ranks use a different reference population; the five strict weight scenarios were not repeated for Panel B. 

5 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **6. Six focus markets** 

**Table 4. Raw metrics and clearly separated ranking universes** 

|**Market**|**Panel**|**Mean**<br>**value USD**<br>**m**|**Quantity**<br>**CAGR %**|**Growth SD**<br>**pp**|**Pakistan**<br>**share %**|**Rank /**<br>**universe**|
|---|---|---|---|---|---|---|
|Azerbaijan|A|41.82|10.03|16.58|4.07|6/69|
|Oman|A|240.03|2.01|14.11|18.42|6/69|
|Kazakhstan|B|10.02|25.31|103.92|4.46|75/134|
|Uzbekistan|B|13.38|39.45|764.91|35.48|89/134|
|Kenya|B|303.88|8.34|12.86|29.06|10/134|
|United Kingdom|Context|309.19|Unavailable|Unavailable|13.46|Unscored|



Mean value: 2021-2023. Quantity CAGR: 2018-2023. Growth SD: sample standard deviation of five annual changes, in percentage points. Pakistan share: destination-reported value share in 2023. A ranks are out of 69; B ranks are from the separate 134-market extension. Rows follow the business focus list, not a new ranking. "Unavailable" is not zero. 

### **Oman** 

Mean broad-rice imports are approximately USD 240m. PBS lists Pakistani Basmati exports of **USD 71m and 58,249 tonnes in FY2024** , providing direct product-related evidence for further research [3]. Pakistan held 18.42% of Oman's HS 100630 import value in 2023, down from 27.27% in 2018; India held 71.55% in 2023. This is an established but competitive market, not assured entry. 

The reviewed Oman Customs 2026 schedule shows **0% general customs duty** for line 10 06 30 00 00 00 [5]. This is not a Pakistan-only preference and does not remove other taxes, permits or costs. Importer requirements, exact rice specification and a current carrier route still need confirmation. Oman's stronger Basmati evidence and larger scale support Tier 1 research despite its wider quantitative rank range. 

### **Azerbaijan** 

Mean imports are approximately USD 42m, with 10.03% physical CAGR and a strict rank range of 6-10. Pakistan's April 2024 government announcement reports an exemption for Pakistani rice through December 2027 [6]. The operative origin procedure and consignment treatment still require confirmation; an announcement is not a shipment-level ruling. 

India supplied 84.79% of reported 2023 import value, while Pakistan held 4.07%. The retained PBS top-20 table does not list Azerbaijan, which means no listed observation rather than zero Basmati exports. Current route availability and the 1121/1509 product segment remain open questions. Robust broad-rice statistics support investigation, not a Basmati-specific conclusion. 

### **Kenya** 

The market averages about USD 304m, with 8.34% physical CAGR, and ranks tenth in the extended universe. Yet Pakistan's value share fell from **53.96% to 29.06%** , while India's rose from **5.45% to 67.32%** . Aggregate 2023 unit values were approximately USD 408/t for India and USD 389/t for Pakistan. These mixed products and shipment conditions do not support a causal claim that India gained share because it was cheaper. Kenya remains Tier 2; explaining the sourcing shift needs buyer- and product-level evidence. 

6 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **7. Commercial interpretation** 

Commercial groups combine the historical screen with Pakistan's position, supplier competition, Basmati evidence, dated access findings, logistics practicality and data confidence. Logistics remain qualitative questions or route hypotheses, without a freight-cost or transit-time model. The groups preserve the Phase 6 judgment; no additional score is introduced. 

**Table 5. Commercial research-priority matrix** 

|**Research group**|**Markets - no ordering within**<br>**group**|**Basis and unresolved work**|
|---|---|---|
|Tier1|Oman; Azerbaijan|Existing business relevance plus<br>complementary scale/Basmati and<br>rank/access evidence. Verify buyer<br>specification, importer requirements and<br>current routes.|
|Tier2|Kenya; United Kingdom; United<br>States; Australia|Substantial or product-relevant markets with<br>sourcing, compliance or channel questions<br>that need further investigation.|
|Data-limited<br>watchlist|Kazakhstan; Uzbekistan|Recorded trade is relevant, but mirror<br>discrepancies or irregular quantity paths<br>materially reduce confidence.|
|Additional reserves|Malaysia; South Africa; Türkiye|Strong quantitative comparators; channel,<br>segment or policy questions are not<br>sufficiently resolved for the immediate<br>research group.|



Source: approved Phase 6 commercial evidence matrix and dated source register. These are research groups, not an ordering of guaranteed opportunities. 

### **United Kingdom: commercial relevance despite missing quantities** 

Mean import value is approximately USD 309m; Pakistan's 2023 share is 13.46%. PBS records **USD 45m and 37,395 tonnes** of Pakistani Basmati exports in FY2024 [3]. Missing World net weights for 2022 and 2023 prevent quantity CAGR, variability and composite ranking. Value, supplier and Basmati evidence remain usable. Reviewed government guidance lists Pakistani rice for pesticide-residue and mycotoxin controls [7]. Exact tariffs and jurisdiction/port requirements still need importer confirmation. 

### **Kazakhstan: unresolved mirror evidence** 

For 2023, Kazakhstan reports approximately **USD 0.847m** of imports from Pakistan, while Pakistan reports **USD 32.553m** of exports to Kazakhstan - about 38.42 times as much. Neither value is reconciled or averaged. Valuation, timing, routing, classification and partner attribution are possible contributors, not a diagnosis [4]. This limits Pakistan-specific conclusions and supports watchlist treatment. Its extended rank remains 75. 

### **Uzbekistan: endpoint growth hides an irregular path** 

The 39.45% quantity CAGR masks sharp reversals, three annual declines and a **1,704.05% increase in 2023** . Annual-growth variability is 764.91 percentage points; extended rank is 89. The high endpoint rate should not be presented as steady demand expansion or extrapolated into a forecast. The estimated-quantity flag, rebound and route/access questions keep it on the watchlist. 

7 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **8. Forecasting decision and dashboard** 

### **Forecasting was intentionally excluded** 

The preserved project data are annual only. The common quantity window supplies six annual levels and five growth rates. Longer focus-market histories provide at most nine annual observations through 2023 and eleven through 2025, with fewer usable observations for some markets and incomplete recent global reporting. 

The agreed preference for approximately **60 consistent monthly observations or 24 quarterly observations** was not met. These would be feasibility gates rather than guarantees of forecast quality. Even the longest annual series leaves little room for repeated out-of-sample validation in this project. No ARIMA, machine learning, artificial monthly series, interpolation or CAGR extrapolation was added. Historical trends and sensitivity analysis are used without presenting them as forecasts. This is a methodological decision, not unfinished analysis. 

### **Power BI presentation** 

The project includes seven Power BI-ready import tables, DAX measures, Power Query transformations, a theme, build instructions and four reference layouts. The page architecture is: 

1. **Global rice market screen:** main 69-market reference and size versus physical growth. 

2. **Focus market comparison:** all six markets, with the UK's quantity limitations visible. 

3. **Pakistan's competitive position:** supplier shares, separate mirror reports and PBS context. 

4. **Ranking robustness / sensitivity:** five weight scenarios, separate quality/extended checks and limitations. 

**Native Power BI Desktop assembly and acceptance testing remain pending. No tested** . p b i x **is claimed.** Reference layouts were rendered from the approved tables and visually inspected. Static/data checks do not replace executing M/DAX and checking slicer interactions in Desktop. The imported ranks retain their approved universe when countries are filtered. 

**Exhibit 7. Final dashboard screenshots - pending Desktop completion** 



<!-- Start of picture text -->
B69 Se 40/30/20/10 2023<br>————= i<br>'<br><!-- End of picture text -->



<!-- Start of picture text -->
gm a aen<br>'<br><!-- End of picture text -->





<!-- Start of picture text -->
ey ne Say —<br><!-- End of picture text -->

8 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **9. Limitations and conclusion** 

**Product scope and commercial measurement.** HS 100630 includes non-Basmati rice and cannot measure exact 1121/1509 demand or buyer specifications. Import values are nominal, and pooled unit values reflect product mix and valuation rather than achievable prices, quality grades or margins. Total imports are not unmet demand or a sales pipeline. 

**Historical coverage and selection.** The common year remains 2023 because 2024/2025 global reporting continuity was incomplete. A 2026 source review does not make 2023 demand current. The strict panel favors markets with complete, unestimated quantity reporting and is not a representative sample of all importing economies. Official estimates remain explicit in the extension. 

**Quantity reliability and missingness.** Missing UK World net weights prevent quantity-based scoring. A missing row is not zero trade. No imputation was performed, and unusual source observations were retained with flags. Botswana, Malawi, Mauritius, Tanzania and other review cases show that satisfying the strict rule does not establish error-free demand measurement. Percentiles bound numerical influence but do not repair source reliability. 

**Supplier and mirror interpretation.** Supplier-country data identify economies and reporting areas, not companies, brands or buyers. World totals and special categories require explicit treatment. Importer/exporter differences can be material; no averaging, reconciliation or substitution was used. No causal explanation is established for Kenya's supplier shift or Kazakhstan's mirror gap. 

**Model assumptions.** The 40/30/20/10 weights are subjective. A high relative score is not a measured probability of success. Rank robustness covers the specified scenarios only, not every possible weight choice. Scores normalized over 69, 67 and 134 markets are not interchangeable. Economic context and Pakistan's position are interpreted separately rather than forced into an additional composite. 

**Commercial execution.** No buyer-level demand evidence, freight-cost model, payment-risk verification, achievable-margin calculation or sales/profit forecast was produced. Tariffs and regulations can change; exact product classification, origin entitlement, documentation and port-specific requirements need current verification. Commercial research priorities require buyer qualification and consignment-level due diligence. No generated sales, company strategy change or business impact is claimed. 

### **What the project contributes** 

A useful selection process asks more than which country imports the most rice. It examines market scale, changes in physical demand, the stability of those changes, existing suppliers, Pakistan's position, direct Basmati evidence, practical access and the reliability of the supporting observations. Here, the historical screen narrows the statistical comparison, while commercial interpretation directs the next research effort. Keeping those two stages separate makes both the assumptions and the unresolved questions visible. 

9 / 10 

Umair Ahmad | Rice market selection | September 2026 

Data-Driven Export Market Selection for Pakistani Rice Exporters 

## **10. Reproducibility and source notes** 

### **Reproduce the approved calculations** 

Retain the repository structure and work in the project root. Python 3.12.14 was used for the verification run. Install the pinned analytical dependencies and a Jupyter interface, then open the notebook: 

p y t h o n - m p i p i n s t a l l  - r r e q u i r e m e n t s . t x t j u p y t e r j u p y t e r n o t e b o o k n o t e b o o k s / r i c e _ m a r k e t _ a n a l y s i s . i p y n b 

Run all cells from top to bottom. The notebook verifies raw hashes, rebuilds the six clean tables and crosswalk, recreates exploration and screening, reproduces Phase 6 supplier-concentration checks and selected mirror comparisons, then prepares dashboard inputs. It needs no live API connection once dependencies and the preserved files are available. The separate dashboard export is p y t h o n d a s h b o a r d / b u i l d _ p o w e r b i _ i n p u t s . p y . 

The verification run executed all **37 original code cells sequentially in a fresh Python process** , in an isolated copy rather than a Jupyter kernel. The canonical notebook was not overwritten. All 54 manifested raw sources verified successfully. The 23 calculated CSV outputs reproduced byte-for-byte; the manually maintained commercial matrix also remained identical. Detailed checks are in d o c s / P h a s e _ 9 _ I n t e g r i t y _ C h e c k . j s o n . 

Historical calculations are reproducible from the saved snapshot. The commercial evidence matrix and d o c s / p h a s e 6 _ s o u r c e _ r e g i s t e r . c s v are dated manual research inputs, not automatically refreshed outputs. PBS transcription is explicit in the notebook and traceable to the preserved PDF. A new trade snapshot or current regulatory update needs separate verification; clicking Power BI Refresh only reloads local CSVs. 

### **Selected primary references** 

[1] **UN Comtrade.** Annual HS 100630 trade, preserved snapshot downloaded 25-26 September 2026. Exact per-file API queries and SHA-256 checksums: d a t a / r a w / d o w n l o a d _ m a n i f e s t . j s o n . Comtrade data portal. 

[2] **World Bank.** World Development Indicators: population, SP.POP.TOTL and GDP per capita, NY.GDP.PCAP.CD. Individual-economy observations; source query URLs retained in the manifest. 

[3] **Pakistan Bureau of Statistics.** Annual Analytical Report on Trade Statistics, FY2023-24, Table 16, PDF page 36. Listed Basmati destinations, FY2024 with FY2023 comparison; USD million values rounded. 

[4] **UN Comtrade.** Bilateral asymmetries. General measurement explanations, not diagnoses of individual gaps. 

[5] **Oman Customs.** 2026 integrated customs tariff, PDF page 24, line 10 06 30 00 00 00. General duty evidence documented in the approved 28 September 2026 review; other consignment costs and requirements remain separate. 

[6] **Pakistan Press Information Department.** Pakistan-Azerbaijan economic ties announcement, 4 April 2024. Reported Pakistani rice exemption through December 2027; operative implementation remains to be verified. 

[7] **UK Government.** Foodstuffs with GB import restrictions, updated 10 July 2026, Pakistan section; page applies to England and Wales. Other UK jurisdictions and exact consignment requirements require separate checks. 

The complete dated commercial source register, including the other comparison markets, is retained in d o c s / p h a s e 6 _ s o u r c e _ r e g i s t e r . c s v . Definitions, transformations and limitations are in d o c s / d a t a _ d i c t i o n a r y . j s o n ; the shorter guide is d o c s / M e t h o d s _ a n d _ S o u r c e s . m d . Older phase reviews are preserved checkpoints, not statements of current project status. 

10 / 10 

Umair Ahmad | Rice market selection | September 2026 

