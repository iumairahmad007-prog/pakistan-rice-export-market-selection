// Create a Text parameter named DataFolder pointing to dashboard/data.
// Paste this complete script into a blank query named DashboardData; disable its load.
// Then create seven reference queries: = DashboardData[Markets], etc.
let
    ReadCsv = (FileName as text, ColumnTypes as list) as table =>
        let
            Source = Csv.Document(File.Contents(DataFolder & "/" & FileName),
                [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]),
            Headers = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),
            MissingAsNull = Table.ReplaceValue(Headers, "", null, Replacer.ReplaceValue, Table.ColumnNames(Headers)),
            Typed = Table.TransformColumnTypes(MissingAsNull, ColumnTypes, "en-US")
        in
            Typed,
    Markets = ReadCsv("Markets.csv", {
        {"EconomyID", type text},
        {"ComtradeCode", Int64.Type},
        {"SourceMarketName", type text},
        {"SourceISO", type text},
        {"PanelCode", type text},
        {"StrictPanel", type logical},
        {"EstimatedAddition", type logical},
        {"EstimatedYears", Int64.Type},
        {"MeanImportValueUSD", type number},
        {"QuantityCAGR", type number},
        {"GrowthSD", type number},
        {"PooledUnitValueUSDt", type number},
        {"FullUnitValueWindow", type logical},
        {"PakistanShare2018", type number},
        {"PakistanShare2023", type number},
        {"PakistanShareChangePP", type number},
        {"WorldValue2023USD", type number},
        {"MetricSourceFiles", type text},
        {"Market", type text},
        {"IsFocus", type logical},
        {"FocusOrder", Int64.Type},
        {"QuantityComplete", type logical},
        {"Panel", type text},
        {"StrictBaseScore", type number},
        {"StrictBaseRank", type number},
        {"BestStrictRank", type number},
        {"WorstStrictRank", type number},
        {"Top10Scenarios", type number},
        {"ExtendedBaseScore", type number},
        {"ExtendedBaseRank", type number},
        {"ReviewNote", type text},
        {"Population2023", type number},
        {"GDPPerCapita2023USD", type number},
        {"ResearchGroup", type text},
        {"Status", type text}
    }),
    AnnualImports = ReadCsv("AnnualImports.csv", {
        {"EconomyID", type text},
        {"Year", Int64.Type},
        {"WorldImportValueUSD", type number},
        {"WorldQuantityTonnes", type number},
        {"QuantityQuality", type text},
        {"AnyQuantityEstimated", type logical},
        {"NetWeightEstimated", type logical},
        {"QuantityFieldReview", type logical},
        {"WorldSourceFile", type text},
        {"PakistanImportValueUSD", type number},
        {"PakistanSourceFile", type text},
        {"PakistanObservationPresent", type logical}
    }),
    Scenarios = ReadCsv("Scenarios.csv", {
        {"ScenarioID", type text},
        {"Scenario", type text},
        {"Family", type text},
        {"ScenarioOrder", Int64.Type},
        {"UniverseN", Int64.Type},
        {"SizeWeight", type number},
        {"GrowthWeight", type number},
        {"StabilityWeight", type number},
        {"UnitValueWeight", type number},
        {"Interpretation", type text}
    }),
    Screening = ReadCsv("Screening.csv", {
        {"EconomyID", type text},
        {"Score", type number},
        {"OriginalRank", Int64.Type},
        {"SizePercentile", type number},
        {"GrowthPercentile", type number},
        {"StabilityPercentile", type number},
        {"UnitValuePercentile", type number},
        {"ScenarioID", type text}
    }),
    SupplierShares = ReadCsv("SupplierShares.csv", {
        {"EconomyID", type text},
        {"Year", Int64.Type},
        {"SupplierID", type text},
        {"Supplier", type text},
        {"SupplierType", type text},
        {"ImportValueUSD", type number},
        {"ValueShare", type number},
        {"SourceFile", type text},
        {"SupplierDisplay", type text}
    }),
    MirrorComparison = ReadCsv("MirrorComparison.csv", {
        {"EconomyID", type text},
        {"Year", Int64.Type},
        {"ImporterValueUSD", type number},
        {"PakistanExporterValueUSD", type number},
        {"ImporterQuantityTonnes", type number},
        {"ExporterQuantityTonnes", type number},
        {"ImporterSourceFile", type text},
        {"ExporterSourceFile", type text}
    }),
    PBSBasmati = ReadCsv("PBSBasmati.csv", {
        {"EconomyID", type text},
        {"FiscalYear", type text},
        {"ExportValueUSDRounded", Int64.Type},
        {"ExportQuantityTonnes", Int64.Type},
        {"SourceFile", type text},
        {"SourceNote", type text}
    })
in
    [ Markets = Markets, AnnualImports = AnnualImports, Scenarios = Scenarios, Screening = Screening, SupplierShares = SupplierShares, MirrorComparison = MirrorComparison, PBSBasmati = PBSBasmati ]
