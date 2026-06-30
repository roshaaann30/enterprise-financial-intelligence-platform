from app.event_intelligence.event_extractor import (
    EventExtractor,
)

from app.event_intelligence.event_impact_analyzer import (
    EventImpactAnalyzer,
)

from app.event_intelligence.timeline_builder import (
    TimelineBuilder,
)


class EventIntelligenceEngine:

    @staticmethod
    def analyze(

        text,

    ):

        events = (

            EventExtractor.extract(

                text

            )

        )

        events = [

            EventImpactAnalyzer.analyze(

                event

            )

            for event in events

        ]

        timeline = (

            TimelineBuilder.build(

                events

            )

        )

        return timeline