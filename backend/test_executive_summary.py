from app.nlp.dashboard.executive_dashboard import (
    ExecutiveDashboard,
)

from app.nlp.dashboard.executive_summary import (
    ExecutiveSummary,
)

###########################################################

sentiment = {

    "sentiment":
        "Positive",

    "confidence":
        96.2,

}

###########################################################

risks = [

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

###########################################################

opportunities = [

    {

        "opportunity_type":
            "AI Investment",

        "strength":
            "High",

    },

    {

        "opportunity_type":
            "Market Expansion",

        "strength":
            "Medium",

    },

]

###########################################################

strategies = [

    {

        "initiative":
            "AI Adoption",

        "priority":
            "High",

    },

    {

        "initiative":
            "Digital Transformation",

        "priority":
            "Medium",

    },

]

###########################################################

outlook = {

    "outlook":
        "Very Positive",

    "confidence":
        90,

}

###########################################################

entities = [

    {

        "text":
            "Microsoft",

        "label":
            "ORG",

    }

]

###########################################################

dashboard = (

    ExecutiveDashboard.generate(

        sentiment,

        risks,

        opportunities,

        strategies,

        outlook,

        entities,

    )

)

###########################################################

summary = ExecutiveSummary.generate(

    dashboard

)

###########################################################

print()

print("=" * 60)

print("AI EXECUTIVE SUMMARY")

print("=" * 60)

print()

print(summary)