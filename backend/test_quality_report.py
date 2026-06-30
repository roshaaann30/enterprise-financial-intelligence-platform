from app.database.session import SessionLocal
from app.ingestion.stock_ingestion import StockIngestion
from app.quality.validator import DataValidator

db = SessionLocal()

validator = DataValidator(db)

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices("AAPL")

expected_columns = [
    "Ticker",
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
]

report = validator.generate_quality_report(
    "Stock Prices",
    df,
    expected_columns,
)

print(report)

db.close()