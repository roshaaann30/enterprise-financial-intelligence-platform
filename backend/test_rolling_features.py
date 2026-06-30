from app.ingestion.stock_ingestion import StockIngestion

from app.features.stock.pipeline import (
    StockPipeline,
)

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices(
    "AAPL"
)

features = StockPipeline.process(
    df
)

columns = [

    "Close",

    "RollingMean_20",

    "RollingStd_20",

    "RollingMin_20",

    "RollingMax_20",

    "RollingMedian_20",

    "RollingVariance_20",

    "RollingSkew_20",

    "RollingKurtosis_20",

    "RollingZScore_20",

]

print(
    features[
        columns
    ].tail()
)