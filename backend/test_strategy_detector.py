from app.nlp.strategy_detection.strategy_detector import (
    StrategicInitiativeDetector,
)

###########################################################

text = """

Management continues to invest heavily
in AI and machine learning.

Digital transformation remains a
core strategic priority.

The company plans international expansion.

Several automation initiatives are
expected to improve efficiency.

R&D investment increased significantly.

"""

###########################################################

results = (

    StrategicInitiativeDetector.detect(

        text

    )

)

###########################################################

print()

print("=" * 60)

print("STRATEGIC INITIATIVE DETECTION")

print("=" * 60)

print()

for item in results:

    print(

        item

    )