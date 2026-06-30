from app.pdf.risk_analysis.risk_dashboard import (
    RiskDashboard,
)

analysis = {

    "risk_score": 35,

    "risks": [

        {

            "risk_type":
                "Supply Chain Risk",

            "severity":
                "Medium",

        },

        {

            "risk_type":
                "Cybersecurity Risk",

            "severity":
                "Low",

        },

    ]

}

dashboard = (

    RiskDashboard.generate(

        analysis

    )

)

print(dashboard)