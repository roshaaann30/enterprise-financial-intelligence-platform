from app.pdf.dashboard.dashboard_report import (
    DashboardReport,
)

sample_dashboard = {

    "company":
        "Tesla",

    "executive_summary":
        "Management remains optimistic.",

    "financial_metrics": {

        "Revenue":
            "96.7B"

    },

    "business_outlook": {

        "outlook":
            "Positive"

    },

    "risk_analysis": {

        "risk_count":
            1

    },

    "opportunity_analysis": {

        "opportunity_count":
            2

    },

    "strategic_initiatives": [

        {

            "initiative":
                "AI Adoption"

        }

    ],

    "entities": [

        {

            "text":
                "Tesla"

        }

    ]

}

print(

    DashboardReport.generate(

        sample_dashboard

    )

)