from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    ticker: Mapped[str] = mapped_column(String(20), unique=True)

    company_name: Mapped[str] = mapped_column(String(255))

    sector: Mapped[str] = mapped_column(String(100))