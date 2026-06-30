from dataclasses import dataclass


@dataclass
class PortfolioHolding:

    symbol: str

    company: str

    sector: str

    weight: float


@dataclass
class PortfolioAnalysis:

    diversification_score: float

    concentration_score: float

    risk_score: float

    recommendation: str