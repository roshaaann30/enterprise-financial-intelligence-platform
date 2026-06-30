from app.pdf.sections.section_identifier import (
    SectionIdentifier,
)

from app.nlp.risk_extraction.risk_extractor import (
    FinancialRiskExtractor,
)


class PDFRiskPipeline:

    """
    Enterprise PDF Risk Pipeline
    """

    @staticmethod
    def analyze(

        text,

    ):

        #######################################################
        # Identify Sections
        #######################################################

        sections = (

            SectionIdentifier.identify(

                text

            )

        )

        #######################################################
        # Extract Risks
        #######################################################

        risks = (

            FinancialRiskExtractor.extract(

                text

            )

        )

        #######################################################
        # Score
        #######################################################

        risk_score = 0

        for risk in risks:

            severity = risk[

                "severity"

            ]

            if severity == "High":

                risk_score += 25

            elif severity == "Medium":

                risk_score += 15

            else:

                risk_score += 5

        risk_score = min(

            risk_score,

            100,

        )

        #######################################################
        # Output
        #######################################################

        return {

            "sections":

                sections,

            "risks":

                risks,

            "risk_score":

                risk_score,

        }