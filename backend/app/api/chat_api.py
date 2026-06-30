from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
async def chat(data: dict):

    message = data.get("message", "")

    return {
        "response": f"""
Analysis for:

{message}

Risk Score: 35
Forecast Score: 81

Strengths:
• Revenue growth
• Strong market position
• Healthy cash flow

Risks:
• Competition
• Market volatility

Recommendation:
Moderate Buy
"""
    }