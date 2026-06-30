class EventImpactAnalyzer:

    POSITIVE_EVENTS = {

        "Product Launch",

        "Analyst Upgrade",

        "Dividend",

    }

    NEGATIVE_EVENTS = {

        "Lawsuit",

    }

    @staticmethod
    def analyze(

        event,

    ):

        if event.event_type in (

            EventImpactAnalyzer

            .POSITIVE_EVENTS

        ):

            event.impact_score = 80

            event.impact_type = (

                "Positive"

            )

        elif event.event_type in (

            EventImpactAnalyzer

            .NEGATIVE_EVENTS

        ):

            event.impact_score = 25

            event.impact_type = (

                "Negative"

            )

        else:

            event.impact_score = 50

            event.impact_type = (

                "Neutral"

            )

        return event