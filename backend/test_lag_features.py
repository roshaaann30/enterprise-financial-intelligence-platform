from app.ingestion.stock_ingestion import StockIngestion

from app.features.stock.pipeline import (
    StockPipeline,
)

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices(
    "AAPL"
)

features = StockPipeline.process(df)

columns = [

    "Close",

    "Close_Lag_1",

    "Close_Lag_5",

    "Close_Lag_10",

    "Volume_Lag_5",

    "Return_Lag_5",

]

print(
    features[
        columns
    ].tail()
)