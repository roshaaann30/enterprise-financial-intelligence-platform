import re


class FinancialOpportunityExtractor:

    """
    Enterprise Opportunity Extraction Engine
    """

    OPPORTUNITY_PATTERNS = {

        "Revenue Growth": [

            r"revenue growth",

            r"growth opportunity",

            r"sales growth",

            r"strong demand",

        ],

        "Market Expansion": [

            r"market expansion",

            r"new market",

            r"international expansion",

            r"global growth",

        ],

        "AI Investment": [

            r"artificial intelligence",

            r"\bai\b",

            r"machine learning",

            r"generative ai",

        ],

        "Digital Transformation": [

            r"digital transformation",

            r"automation",

            r"digital platform",

            r"cloud migration",

        ],

        "Product Launch": [

            r"product launch",

            r"new product",

            r"new offering",

            r"innovation",

        ],

        "Acquisition": [

            r"acquisition",

            r"acquired",

            r"merger",

            r"m&a",

        ],

        "Partnership": [

            r"partnership",

            r"strategic alliance",

            r"joint venture",

            r"collaboration",

        ],

        "Cost Optimization": [

            r"cost reduction",

            r"efficiency improvement",

            r"operating leverage",

            r"productivity gains",

        ],

        "ESG Initiative": [

            r"esg",

            r"sustainability",

            r"carbon reduction",

            r"net zero",

        ],

    }

    ###########################################################
    # Extract Opportunities
    ###########################################################

    @classmethod
    def extract(

        cls,

        text,

    ):

        text = text.lower()

        opportunities = []

        for opportunity_type, patterns in (

            cls.OPPORTUNITY_PATTERNS.items()

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

                opportunities.append(

                    {

                        "opportunity_type":

                            opportunity_type,

                        "mentions":

                            len(matches),

                        "strength":

                            cls.strength(

                                len(matches)

                            ),

                    }

                )

        return opportunities

    ###########################################################
    # Strength
    ###########################################################

    @staticmethod
    def strength(

        count,

    ):

        if count >= 5:

            return "High"

        elif count >= 2:

            return "Medium"

        return "Low"