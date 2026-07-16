from fastapi import APIRouter
from services.portfolio_risk import PortfolioRiskAnalyzer

router = APIRouter()

@router.get("/portfolio-risk")
def portfolio_risk():

    sample_returns = [
        0.02,
        -0.01,
        0.03,
        0.01,
        -0.02,
        0.04,
        0.01
    ]

    analyzer = PortfolioRiskAnalyzer()

    return analyzer.calculate_metrics(
        sample_returns
    )