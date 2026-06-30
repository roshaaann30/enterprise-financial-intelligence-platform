from app.ingestion.stock_ingestion import StockIngestion
from app.warehouse.warehouse import DataWarehouse

ingestion = StockIngestion()

warehouse = DataWarehouse()

df = ingestion.fetch_stock_prices("AAPL")

features = warehouse.process_dataset(df)

print(features.head())