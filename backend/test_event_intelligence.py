from app.event_intelligence.event_intelligence_engine import (
    EventIntelligenceEngine,
)

text = """

The company announced a new dividend.

A major product launch was completed.

The company faces a lawsuit.

"""

timeline = (

    EventIntelligenceEngine.analyze(

        text

    )

)

for event in timeline:

    print(

        vars(event)

    )