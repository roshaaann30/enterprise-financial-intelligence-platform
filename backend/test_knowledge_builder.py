from app.pdf.knowledge.knowledge_builder import (
    FinancialKnowledgeBuilder,
)

knowledge = (

    FinancialKnowledgeBuilder.build(

        company="Tesla",

        metrics={

            "Revenue":
                "96.7B",

            "NetIncome":
                "12.4B",

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

        outlook={

            "outlook":
                "Positive",

        },

        sections=[

            "Risk Factors",

            "MD&A",

        ],

    )

)

print(knowledge)