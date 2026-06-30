from datetime import date

from sqlalchemy import Date, Float, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class StockPrice(Base):
    __tablename__ = "stock_prices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    ticker: Mapped[str] = mapped_column(String(20), nullable=False)

    date: Mapped[date] = mapped_column(Date, nullable=False)

    open_price: Mapped[float] = mapped_column(Float)

    high_price: Mapped[float] = mapped_column(Float)

    low_price: Mapped[float] = mapped_column(Float)

    close_price: Mapped[float] = mapped_column(Float)

    volume: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        Index(
            "idx_ticker_date",
            "ticker",
            "date",
            unique=True,
        ),
    )