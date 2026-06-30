from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class FeatureStore(Base):

    __tablename__ = "feature_store"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    ticker: Mapped[str] = mapped_column(
        String(20),
        index=True,
    )

    feature_name: Mapped[str] = mapped_column(
        String(100),
    )

    feature_value: Mapped[float] = mapped_column(
        Float,
    )

    feature_version: Mapped[str] = mapped_column(
        String(20),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )