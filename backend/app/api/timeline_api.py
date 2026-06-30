from fastapi import APIRouter

router = APIRouter()


@router.get("/timeline")
def timeline():

    return [

        {
            "date": "2021",
            "event": "IPO",
            "impact": "+15%"
        },

        {
            "date": "2022",
            "event": "Revenue Growth",
            "impact": "+20%"
        },

        {
            "date": "2023",
            "event": "Major Acquisition",
            "impact": "+12%"
        },

        {
            "date": "2024",
            "event": "AI Product Launch",
            "impact": "+18%"
        },

        {
            "date": "2025",
            "event": "International Expansion",
            "impact": "+10%"
        }

    ]