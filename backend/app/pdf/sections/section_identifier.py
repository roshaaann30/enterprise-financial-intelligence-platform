import re


class SectionIdentifier:

    """
    Enterprise Section Intelligence Engine
    """

    SECTION_PATTERNS = {

        "Business Overview": [

            r"business overview",

            r"company overview",

            r"our business",

        ],

        "Risk Factors": [

            r"risk factors",

            r"principal risks",

        ],

        "MD&A": [

            r"management discussion",

            r"management's discussion",

            r"md&a",

        ],

        "Financial Statements": [

            r"financial statements",

            r"consolidated statements",

            r"balance sheets",

            r"income statements",

        ],

        "ESG": [

            r"environmental",

            r"sustainability",

            r"esg",

        ],

        "Outlook": [

            r"outlook",

            r"future expectations",

            r"guidance",

        ],

        "Corporate Governance": [

            r"corporate governance",

            r"board of directors",

        ],

    }

    ###########################################################
    # Detect Sections
    ###########################################################

    @classmethod
    def identify(

        cls,

        text,

    ):

        text = text.lower()

        sections = []

        for section, patterns in (

            cls.SECTION_PATTERNS.items()

        ):

            for pattern in patterns:

                if re.search(

                    pattern,

                    text,

                ):

                    sections.append(

                        section

                    )

                    break

        return sections