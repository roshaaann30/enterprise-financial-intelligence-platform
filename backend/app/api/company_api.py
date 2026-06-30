from fastapi import APIRouter

router = APIRouter()

@router.get("/company")
def get_company():

    return {

        "company": "Tesla",

        "risk_score": 35,

        "investment_rating": "Buy",

    }