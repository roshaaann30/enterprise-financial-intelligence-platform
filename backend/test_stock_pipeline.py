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

print(features.columns)

print(features.head())