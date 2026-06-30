from datetime import datetime

from sqlalchemy import DateTime, Integer, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class EarningsTranscript(Base):
    __tablename__ = "earnings_transcripts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    ticker: Mapped[str] = mapped_column(String(20), index=True)

    fiscal_year: Mapped[int] = mapped_column(Integer)

    quarter: Mapped[str] = mapped_column(String(5))

    transcript: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )