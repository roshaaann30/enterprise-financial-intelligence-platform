from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class ProcessedDataset(Base):

    __tablename__ = "processed_datasets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    dataset_name: Mapped[str] = mapped_column(
        String(100),
    )

    dataset_version: Mapped[str] = mapped_column(
        String(50),
    )

    source: Mapped[str] = mapped_column(
        String(100),
    )

    status: Mapped[str] = mapped_column(
        String(30),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )