from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class DataQualityReport(Base):

    __tablename__ = "data_quality_reports"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    dataset: Mapped[str] = mapped_column(
        String(100),
    )

    check_type: Mapped[str] = mapped_column(
        String(100),
    )

    status: Mapped[str] = mapped_column(
        String(20),
    )

    message: Mapped[str] = mapped_column(
        String(500),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )