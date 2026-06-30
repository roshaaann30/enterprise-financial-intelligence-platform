from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class MacroeconomicIndicator(Base):
    __tablename__ = "macroeconomic_indicators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    indicator: Mapped[str] = mapped_column(String(100), index=True)

    date: Mapped[str] = mapped_column(String(20))

    value: Mapped[float] = mapped_column(Float)

    source: Mapped[str] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )