from app.nlp.dashboard.executive_dashboard import (
    ExecutiveDashboard,
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

    },

    {

        "text":

            "Satya Nadella",

        "label":

            "PERSON",

    },

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

print()

print("=" * 60)

print("EXECUTIVE INTELLIGENCE DASHBOARD")

print("=" * 60)

print()

for key, value in dashboard.items():

    print(

        key,

        ":",

        value,

    )