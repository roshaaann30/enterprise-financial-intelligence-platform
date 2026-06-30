from app.database.session import SessionLocal
from app.ingestion.stock_ingestion import StockIngestion
from app.warehouse.orchestrator import FeaturePipelineOrchestrator

db = SessionLocal()

pipeline = FeaturePipelineOrchestrator(db)

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices("AAPL")

result = pipeline.run(
    "AAPL",
    df,
)

print(result["summary"])

db.close()