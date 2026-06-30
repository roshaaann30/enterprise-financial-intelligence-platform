import re


class StrategicInitiativeDetector:

    """
    Enterprise Strategic Initiative Detector
    """

    INITIATIVE_PATTERNS = {

        "AI Adoption": [

            r"\bai\b",

            r"artificial intelligence",

            r"machine learning",

            r"generative ai",

        ],

        "Digital Transformation": [

            r"digital transformation",

            r"digital strategy",

            r"digital platform",

            r"digitization",

        ],

        "Cost Reduction": [

            r"cost reduction",

            r"cost optimization",

            r"efficiency initiative",

            r"expense reduction",

        ],

        "Global Expansion": [

            r"international expansion",

            r"global expansion",

            r"new geography",

            r"new markets",

        ],

        "Mergers & Acquisitions": [

            r"acquisition",

            r"acquired",

            r"merger",

            r"m&a",

        ],

        "ESG Strategy": [

            r"esg",

            r"sustainability",

            r"net zero",

            r"carbon reduction",

        ],

        "Cloud Migration": [

            r"cloud migration",

            r"cloud transformation",

            r"cloud infrastructure",

        ],

        "Automation": [

            r"automation",

            r"robotics",

            r"automated process",

        ],

        "R&D Investment": [

            r"research and development",

            r"r&d",

            r"innovation investment",

        ],

    }

    ###########################################################
    # Detect
    ###########################################################

    @classmethod
    def detect(

        cls,

        text,

    ):

        text = text.lower()

        initiatives = []

        for initiative, patterns in (

            cls.INITIATIVE_PATTERNS.items()

        ):

            matches = []

            for pattern in patterns:

                found = re.findall(

                    pattern,

                    text,

                )

                matches.extend(

                    found

                )

            if matches:

                initiatives.append(

                    {

                        "initiative":

                            initiative,

                        "mentions":

                            len(matches),

                        "priority":

                            cls.priority(

                                len(matches)

                            ),

                    }

                )

        return initiatives

    ###########################################################
    # Priority
    ###########################################################

    @staticmethod
    def priority(

        count,

    ):

        if count >= 5:

            return "High"

        elif count >= 2:

            return "Medium"

        return "Low"