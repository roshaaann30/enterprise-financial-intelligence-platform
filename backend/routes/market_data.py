from fastapi import APIRouter

from services.market_data import MarketDataService

router = APIRouter()


@router.get("/market-data")
def market_data():

    service = MarketDataService()

    return service.get_market_data()