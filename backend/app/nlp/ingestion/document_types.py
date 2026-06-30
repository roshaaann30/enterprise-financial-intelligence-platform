from enum import Enum


class DocumentType(Enum):

    EARNINGS_CALL = "earnings_call"

    ANNUAL_REPORT = "annual_report"

    QUARTERLY_REPORT = "quarterly_report"

    CEO_LETTER = "ceo_letter"

    INVESTOR_PRESENTATION = "investor_presentation"

    FINANCIAL_NEWS = "financial_news"

    UNKNOWN = "unknown"