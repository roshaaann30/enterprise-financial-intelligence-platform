from dataclasses import dataclass


@dataclass
class FinancialEvent:

    event_type: str

    title: str

    date: str

    description: str

    impact_score: float = 0.0

    impact_type: str = "Neutral"

    source: str = ""