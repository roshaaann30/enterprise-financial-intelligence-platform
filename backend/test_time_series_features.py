from app.ingestion.stock_ingestion import StockIngestion
from app.features.stock.pipeline import StockPipeline

ingestion = StockIngestion()

df = ingestion.fetch_stock_prices(
    "AAPL"
)

features = StockPipeline.process(
    df
)

columns = [
    "Date",
    "Year",
    "Quarter",
    "Month",
    "Week",
    "Day",
    "DayOfWeek",
    "DayOfYear",
    "TradingDay",
    "Month_Sin",
    "Month_Cos",
]

print(features[columns].head())