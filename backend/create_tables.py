from app.database.base import Base
from app.database.session import engine


# Import all models so SQLAlchemy knows about them
from app.models.company import Company
from app.models.stock_price import StockPrice
from app.models.company_financials import CompanyFinancials
from app.models.earnings_transcript import EarningsTranscript
from app.models.financial_news import FinancialNews
from app.models.macroeconomic_indicator import MacroeconomicIndicator
from app.models.data_quality_report import DataQualityReport
from app.models.feature_store import FeatureStore
from app.models.processed_dataset import ProcessedDataset

Base.metadata.create_all(bind=engine)

print("✅ Database tables created successfully!")