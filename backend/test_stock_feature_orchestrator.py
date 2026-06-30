from app.ingestion.stock_ingestion import StockIngestion

from app.features.stock.pipeline import (
    StockPipeline,
)

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices("AAPL")

features = StockPipeline.process(df)

print()

print("=" * 60)

print("Total Features")

print(len(features.columns))

print("=" * 60)

print(features.columns.tolist())