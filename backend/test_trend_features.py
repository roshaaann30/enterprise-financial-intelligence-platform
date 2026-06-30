from app.ingestion.stock_ingestion import StockIngestion
from app.features.pipeline import FeatureEngineeringPipeline

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices("AAPL")

pipeline = FeatureEngineeringPipeline()

features = pipeline.process(df)

print(features.columns)