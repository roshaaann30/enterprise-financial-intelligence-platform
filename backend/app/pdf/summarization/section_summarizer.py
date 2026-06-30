class SectionSummarizer:

    """
    Summarize individual sections
    """

    @staticmethod
    def summarize_sections(

        section_data,

    ):

        summaries = {}

        for section, content in (

            section_data.items()

        ):

            summaries[section] = (

                content[:500]

                + "..."

            )

        return summaries