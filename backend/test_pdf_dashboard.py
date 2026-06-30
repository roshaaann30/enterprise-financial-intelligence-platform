from app.pdf.dashboard.pdf_dashboard import (
    PDFDashboard,
)

dashboard = PDFDashboard.generate(

    company="Tesla",

    metrics={

        "Revenue":
            "96.7B",

        "Net Income":
            "12.4B",

        "EPS":
            "4.15",

    },

    risks=[

        {

            "risk_type":
                "Supply Chain Risk",

            "severity":
                "Medium",

        }

    ],

    opportunities=[

        {

            "opportunity_type":
                "AI Investment",

            "strength":
                "High",

        }

    ],

    sentiment={

        "sentiment":
            "Positive",

        "confidence":
            95,

    },

    outlook={

        "outlook":
            "Very Positive",

        "confidence":
            90,

    },

    strategies=[

        {

            "initiative":
                "AI Adoption",

            "priority":
                "High",

        }

    ],

    entities=[

        {

            "text":
                "Tesla",

            "label":
                "ORG",

        }

    ],

    executive_summary=

        "Management remains optimistic about growth.",

)

print(dashboard)