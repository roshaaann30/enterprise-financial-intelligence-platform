from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class FinancialNews(Base):
    __tablename__ = "financial_news"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    ticker: Mapped[str] = mapped_column(String(20), index=True)

    title: Mapped[str] = mapped_column(String(500))

    publisher: Mapped[str] = mapped_column(String(200))

    published_at: Mapped[datetime] = mapped_column(DateTime)

    article_url: Mapped[str] = mapped_column(String(1000))

    summary: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )