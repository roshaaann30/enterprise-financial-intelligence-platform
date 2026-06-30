from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class CompanyFinancials(Base):
    __tablename__ = "company_financials"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    ticker: Mapped[str] = mapped_column(String(20), index=True)

    statement_type: Mapped[str] = mapped_column(String(30), index=True)

    metric: Mapped[str] = mapped_column(String(150))

    period: Mapped[str] = mapped_column(String(20))

    value: Mapped[float] = mapped_column(Float)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )