import re


class FinancialRiskExtractor:

    """
    Enterprise Financial Risk Extractor
    """

    RISK_PATTERNS = {

        "Operational Risk": [

            r"operational risk",

            r"production disruption",

            r"equipment failure",

            r"business interruption",

        ],

        "Market Risk": [

            r"market volatility",

            r"economic slowdown",

            r"interest rates",

            r"inflation",

        ],

        "Regulatory Risk": [

            r"regulatory",

            r"compliance",

            r"government policy",

            r"legal proceedings",

        ],

        "Supply Chain Risk": [

            r"supply chain",

            r"vendor",

            r"shortage",

            r"logistics",

        ],

        "Cybersecurity Risk": [

            r"cyber",

            r"data breach",

            r"ransomware",

            r"security incident",

        ],

        "Liquidity Risk": [

            r"liquidity",

            r"cash flow pressure",

            r"debt obligations",

            r"funding risk",

        ],

        "Competition Risk": [

            r"competition",

            r"competitive pressure",

            r"market share loss",

            r"new entrants",

        ],

    }

    ###########################################################
    # Extract Risks
    ###########################################################

    @classmethod
    def extract(

        cls,

        text,

    ):

        text = text.lower()

        risks = []

        for risk_type, patterns in (

            cls.RISK_PATTERNS.items()

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

                risks.append(

                    {

                        "risk_type":

                            risk_type,

                        "mentions":

                            len(matches),

                        "severity":

                            cls.severity(

                                len(matches)

                            ),

                    }

                )

        return risks

    ###########################################################
    # Severity
    ###########################################################

    @staticmethod
    def severity(

        count,

    ):

        if count >= 5:

            return "High"

        elif count >= 2:

            return "Medium"

        return "Low"