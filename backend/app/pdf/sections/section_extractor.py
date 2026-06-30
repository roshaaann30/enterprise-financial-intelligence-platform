class SectionExtractor:

    """
    Extract text belonging to sections
    """

    @staticmethod
    def extract(

        text,

        sections,

    ):

        results = {}

        lower_text = text.lower()

        for section in sections:

            start = lower_text.find(

                section.lower()

            )

            if start != -1:

                results[section] = text[

                    start:start + 2000

                ]

        return results