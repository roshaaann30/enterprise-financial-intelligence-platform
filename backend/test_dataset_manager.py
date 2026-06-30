from app.ingestion.stock_ingestion import StockIngestion
from app.warehouse.warehouse import DataWarehouse

ingestion = StockIngestion()

warehouse = DataWarehouse()

df = ingestion.fetch_stock_prices("AAPL")

summary = warehouse.summarize_dataset(df)

print(summary)