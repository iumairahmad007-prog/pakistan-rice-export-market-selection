"""Export presentation tables from approved outputs. No new scores or imputation.
Run: python dashboard/build_powerbi_inputs.py (from any working directory).
"""
from pathlib import Path
import json
import hashlib
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dashboard/data'
OUT.mkdir(exist_ok=True)
TABLES = ROOT / 'reports/tables'
CLEAN = ROOT / 'data/processed'
inputs = [TABLES / x for x in [
    'market_metrics_exploratory.csv', 'strict_market_screening.csv',
    'quality_review_sensitivity.csv', 'extended_market_screening.csv',
    'focus_market_screening_comparison.csv', 'focus_supplier_shares_exploratory.csv',
    'focus_mirror_comparison.csv']]
inputs += [CLEAN / x for x in ['market_imports_clean.csv', 'imports_from_pakistan_clean.csv', 'pbs_basmati_supporting.csv']]
original_hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
metrics, strict, quality, extended, focus, suppliers, mirrors, world, pakistan, pbs = [pd.read_csv(p) for p in inputs]
assert len(strict) == 69 and len(quality) == 67 and len(extended) == 134
assert metrics.broader_panel_addition_2018_2023.sum() == 65
focus_codes = [31, 512, 404, 398, 860, 826]
reviewed_codes = focus_codes + [842, 458, 710, 792, 36]

# 1. One row per market. All raw metrics are copied from the approved notebook.
market_mapping = {
 'country_economy_id':'EconomyID', 'country_comtrade_code':'ComtradeCode',
 'country_name':'SourceMarketName', 'country_source_iso':'SourceISO',
 'panel_membership':'PanelCode', 'strict_panel_2018_2023':'StrictPanel',
 'broader_panel_addition_2018_2023':'EstimatedAddition',
 'estimated_quantity_years_2018_2023':'EstimatedYears',
 'average_import_value_usd_2021_2023':'MeanImportValueUSD',
 'quantity_cagr_2018_2023':'QuantityCAGR',
 'annual_quantity_growth_sd_2019_2023':'GrowthSD',
 'pooled_unit_value_usd_per_tonne_2021_2023':'PooledUnitValueUSDt',
 'pooled_unit_value_full_window':'FullUnitValueWindow',
 'pakistan_value_share_2018':'PakistanShare2018',
 'pakistan_value_share_2023':'PakistanShare2023',
 'pakistan_share_change_pp_2018_2023':'PakistanShareChangePP',
 'world_import_value_usd_2023':'WorldValue2023USD',
 'source_files':'MetricSourceFiles',
}
markets = metrics[list(market_mapping)].rename(columns=market_mapping).copy()
markets['Market'] = markets.SourceMarketName.replace({'USA':'United States'})
markets['IsFocus'] = markets.ComtradeCode.isin(focus_codes)
markets['FocusOrder'] = markets.ComtradeCode.map({code:i+1 for i,code in enumerate(focus_codes)}).fillna(99).astype(int)
markets['QuantityComplete'] = markets.StrictPanel | markets.EstimatedAddition
markets['Panel'] = markets.PanelCode.map({
 'A_strict':'A - strict / main reference',
 'B_estimated_addition':'B - estimated-quantity addition',
 'contextual_only':'Contextual / not quantity-score eligible'})
# Suppress partial pooled ratios in the dashboard, preserving the original metric file.
markets.loc[~markets.FullUnitValueWindow, 'PooledUnitValueUSDt'] = np.nan
for source, mapping in [
 (strict, {'base_score':'StrictBaseScore','base_rank':'StrictBaseRank','best_rank':'BestStrictRank','worst_rank':'WorstStrictRank','top10_appearances':'Top10Scenarios'}),
 (extended, {'extended_score':'ExtendedBaseScore','extended_rank':'ExtendedBaseRank','review_flags':'ReviewNote'}),
 (focus, {'population_2023':'Population2023','gdp_per_capita_usd_2023':'GDPPerCapita2023USD'}),
]:
 extra=source[['country_economy_id']+list(mapping)].rename(columns={'country_economy_id':'EconomyID',**mapping})
 markets=markets.merge(extra,on='EconomyID',how='left',validate='one_to_one')
# Manual carry-forward of approved Phase 6 research groups, not a new model.
tiers={31:'Tier 1 - immediate research',512:'Tier 1 - immediate research',404:'Tier 2 - secondary',826:'Tier 2 - secondary',842:'Tier 2 - secondary',36:'Tier 2 - secondary',398:'Data-limited watchlist',860:'Data-limited watchlist',458:'Channel / segment reserve',710:'Channel / segment reserve',792:'Channel / segment reserve'}
markets['ResearchGroup']=markets.ComtradeCode.map(tiers).fillna('Not commercially reviewed')
markets['Status']=markets.Panel
markets.loc[markets.ComtradeCode.eq(826),'Status']='Contextual market - excluded from quantity-based scoring due to missing World net weights.'
markets.loc[markets.ComtradeCode.eq(826),'ReviewNote']='World net weights missing in 2022 and 2023; no quantity CAGR, volatility or score.'
assert markets.EconomyID.is_unique and len(markets)==181
market_ids=set(markets.EconomyID)

# 2. Actual annual records only. No new rows are made to balance the panel.
world = world.loc[world.year.between(2018,2023) & world.country_economy_id.isin(market_ids)].copy()
annual_map={'country_economy_id':'EconomyID','year':'Year','import_value_usd':'WorldImportValueUSD','import_quantity_tonnes':'WorldQuantityTonnes','quantity_quality':'QuantityQuality','any_quantity_estimated':'AnyQuantityEstimated','is_net_weight_estimated':'NetWeightEstimated','review_quantity_field_difference':'QuantityFieldReview','source_file':'WorldSourceFile'}
annual=world[list(annual_map)].rename(columns=annual_map)
pk_map={'destination_economy_id':'EconomyID','year':'Year','import_value_from_pakistan_usd':'PakistanImportValueUSD','source_file':'PakistanSourceFile'}
pk=pakistan.loc[pakistan.year.between(2018,2023),list(pk_map)].rename(columns=pk_map)
annual=annual.merge(pk,on=['EconomyID','Year'],how='left',validate='one_to_one')
annual['PakistanObservationPresent']=annual.PakistanSourceFile.notna()
assert not annual.duplicated(['EconomyID','Year']).any()
assert annual.loc[~annual.PakistanObservationPresent,'PakistanImportValueUSD'].isna().all()

# 3. Reshape the seven approved scenarios. Values, ranks and reference populations are copied.
scenario_specs=[
 ('strict_base','Strict - base 40/30/20/10','Strict weights',1,69,strict,'base',[40,30,20,10]),
 ('strict_growth','Strict - growth emphasis','Strict weights',2,69,strict,'growth_emphasis',[25,50,15,10]),
 ('strict_stability','Strict - stability emphasis','Strict weights',3,69,strict,'stability_emphasis',[35,15,40,10]),
 ('strict_equal','Strict - equal weights','Strict weights',4,69,strict,'equal_weights',[25,25,25,25]),
 ('strict_no_uv','Strict - no unit value','Strict weights',5,69,strict,'no_unit_value',[400/9,100/3,200/9,0]),
 ('quality_base','Quality sensitivity - 67 markets','Quality sensitivity',6,67,quality,'quality',[40,30,20,10]),
 ('extended_base','Extended sensitivity - 134 markets','Estimated-quantity extension',7,134,extended,'extended',[40,30,20,10]),
]
scenario_rows=[];score_parts=[]
for sid,label,family,order,count,frame,prefix,weights in scenario_specs:
 note='Fixed 69-market reference; ranks do not change when markets are filtered.'
 if sid=='quality_base':note='Separate 67-market normalization excluding Malawi and Mauritius; main membership unchanged.'
 if sid=='extended_base':note='Separate 134-market normalization: 69 strict plus 65 estimated additions. Not the main ranking.'
 scenario_rows.append(dict(ScenarioID=sid,Scenario=label,Family=family,ScenarioOrder=order,UniverseN=count,SizeWeight=weights[0]/100,GrowthWeight=weights[1]/100,StabilityWeight=weights[2]/100,UnitValueWeight=weights[3]/100,Interpretation=note))
 mapping={'country_economy_id':'EconomyID',prefix+'_score':'Score',prefix+'_rank':'OriginalRank','size_percentile':'SizePercentile','growth_percentile':'GrowthPercentile','stability_percentile':'StabilityPercentile','unit_value_percentile':'UnitValuePercentile'}
 part=frame[list(mapping)].rename(columns=mapping).copy();part['ScenarioID']=sid
 score_parts.append(part)
scenarios=pd.DataFrame(scenario_rows);screening=pd.concat(score_parts,ignore_index=True)
assert len(screening)==546 and not screening.duplicated(['EconomyID','ScenarioID']).any()
assert 'CT:826' not in set(screening.EconomyID)

# 4. Supplier components only. Retain special categories and their exact source identity.
sup_map={'market_economy_id':'EconomyID','year':'Year','supplier_economy_id':'SupplierID','supplier_name':'Supplier','supplier_entity_type':'SupplierType','import_value_usd':'ImportValueUSD','supplier_value_share':'ValueShare','source_file':'SourceFile'}
supplier_view=suppliers[list(sup_map)].rename(columns=sup_map).copy()
assert supplier_view.SupplierType.ne('world_total').all()
# The display group is a chart convenience: union of each year's five leaders plus Pakistan.
# Source rows are not dropped; all other ordinary suppliers combine under an explicit label.
for eid,group in supplier_view.groupby('EconomyID'):
 leaders=set(group.groupby('Year',group_keys=False).apply(lambda x:x.nlargest(5,'ValueShare'),include_groups=False).SupplierID)
 leaders.add('CT:586')
 for index,row in group.iterrows():
  if row.SupplierType!='country_or_area':display=row.Supplier+' (special category)'
  elif row.SupplierID in leaders:display=row.Supplier
  else:display='Other supplier countries/areas'
  supplier_view.loc[index,'SupplierDisplay']=display
assert len(supplier_view)==262
assert np.allclose(supplier_view.groupby(['EconomyID','Year']).ValueShare.sum(),1,atol=1e-6,rtol=0)

# 5. Mirror reports stay separate. Missing exports stay missing.
mirror_map={'destination_economy_id':'EconomyID','year':'Year','import_value_from_pakistan_usd':'ImporterValueUSD','export_value_usd':'PakistanExporterValueUSD','quantity_from_pakistan_tonnes':'ImporterQuantityTonnes','export_quantity_tonnes':'ExporterQuantityTonnes','importer_source_file':'ImporterSourceFile','exporter_source_file':'ExporterSourceFile'}
mirror_view=mirrors[list(mirror_map)].rename(columns=mirror_map)

# 6. PBS context: only the eleven commercially reviewed markets, and only listed destinations.
# Afghanistan and Somalia lie outside this dashboard market universe; full original PBS data remain intact.
pbs=pbs.loc[pbs.destination_comtrade_code.isin(reviewed_codes)].copy()
pbs_map={'destination_economy_id':'EconomyID','fiscal_year':'FiscalYear','export_value_usd_rounded':'ExportValueUSDRounded','export_quantity_tonnes':'ExportQuantityTonnes','source_file':'SourceFile','source_note':'SourceNote'}
pbs_view=pbs[list(pbs_map)].rename(columns=pbs_map)
assert len(pbs_view)==12 and set(pbs_view.EconomyID)<=market_ids
assert set(pbs_view.EconomyID)=={'CT:036','CT:404','CT:512','CT:710','CT:826','CT:842'}

# Write a small presentation model. Missing CSV cells remain blank; numbers are not rounded.
frames={'Markets':markets,'AnnualImports':annual,'Scenarios':scenarios,'Screening':screening,'SupplierShares':supplier_view,'MirrorComparison':mirror_view,'PBSBasmati':pbs_view}
schema={}
for name,frame in frames.items():
 types={}
 for col in frame:
  if pd.api.types.is_bool_dtype(frame[col]):types[col]='logical'
  elif pd.api.types.is_integer_dtype(frame[col]):types[col]='whole'
  elif pd.api.types.is_numeric_dtype(frame[col]):types[col]='decimal'
  else:types[col]='text'
 schema[name]=dict(rows=len(frame),columns=types)
 export=frame.copy()
 for col,type_name in types.items():
  if type_name=='logical':export[col]=export[col].map({True:'true',False:'false'})
 export.to_csv(OUT/(name+'.csv'),index=False)
for relative,digest in original_hashes.items():assert hashlib.sha256((ROOT/relative).read_bytes()).hexdigest()==digest,relative
manifest={'created_date':'2026-09-28','scope':'2018–2023 history; 2023 common year; fixed approved scores; PBS fiscal years kept separate','input_sha256':original_hashes,'tables':schema,'rules':['No score recalculation','No synthetic trade rows','No missing-to-zero replacement','No UK quantity metrics','No 2024/2025 observations in dashboard ranking','All six focus markets retained','Qualitative research groups copied from Phase 6, not computed']}
(ROOT/'dashboard/model_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print('Dashboard presentation tables:',{name:len(frame) for name,frame in frames.items()})
print('Approved input hashes unchanged. No native Power BI execution has been performed.')
