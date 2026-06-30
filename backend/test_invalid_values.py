from app.database.session import SessionLocal
from app.ingestion.stock_ingestion import StockIngestion
from app.quality.validator import DataValidator

db = SessionLocal()

validator = DataValidator(db)

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices("AAPL")

report = validator.validate_invalid_values(
    "Stock Prices",
    df,
)

print(report)

db.close()