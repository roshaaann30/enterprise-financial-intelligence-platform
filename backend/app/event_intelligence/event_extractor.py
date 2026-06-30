import re

from app.event_intelligence.event_schema import (
    FinancialEvent,
)


class EventExtractor:

    EVENT_PATTERNS = {

        "CEO Change":

            r"ceo|chief executive officer",

        "Earnings Release":

            r"earnings|quarterly results",

        "Product Launch":

            r"launch|released|introduced",

        "Acquisition":

            r"acquired|acquisition|merger",

        "Lawsuit":

            r"lawsuit|litigation|legal action",

        "Analyst Upgrade":

            r"upgrade|outperform|buy rating",

        "Dividend":

            r"dividend",

    }

    @classmethod
    def extract(

        cls,

        text,

    ):

        events = []

        lower_text = text.lower()

        for event_type, pattern in (

            cls.EVENT_PATTERNS.items()

        ):

            if re.search(

                pattern,

                lower_text,

            ):

                events.append(

                    FinancialEvent(

                        event_type=event_type,

                        title=event_type,

                        date="Unknown",

                        description=text[:250],

                    )

                )

        return events