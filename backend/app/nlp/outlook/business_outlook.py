import re


class BusinessOutlook:

    """
    Enterprise Business Outlook Engine
    """

    POSITIVE_PATTERNS = [

        r"strong growth",

        r"continued growth",

        r"positive outlook",

        r"record revenue",

        r"expanding market",

        r"strong demand",

        r"improved margins",

        r"optimistic",

    ]

    NEGATIVE_PATTERNS = [

        r"economic slowdown",

        r"weak demand",

        r"declining revenue",

        r"uncertainty",

        r"headwinds",

        r"recession",

        r"cost pressure",

        r"challenging environment",

    ]

    ###########################################################
    # Analyze
    ###########################################################

    @classmethod
    def analyze(

        cls,

        text,

    ):

        text = text.lower()

        positive = 0
        negative = 0

        for pattern in cls.POSITIVE_PATTERNS:

            positive += len(

                re.findall(

                    pattern,

                    text,

                )

            )

        for pattern in cls.NEGATIVE_PATTERNS:

            negative += len(

                re.findall(

                    pattern,

                    text,

                )

            )

        score = positive - negative

        if score >= 5:

            outlook = "Very Positive"

        elif score >= 2:

            outlook = "Positive"

        elif score <= -5:

            outlook = "Very Negative"

        elif score <= -2:

            outlook = "Negative"

        else:

            outlook = "Neutral"

        confidence = min(

            100,

            50 + abs(score) * 10,

        )

        return {

            "outlook":

                outlook,

            "confidence":

                confidence,

            "positive_signals":

                positive,

            "negative_signals":

                negative,

            "outlook_score":

                score,

        }