from app.pdf.summarization.section_summarizer import (
    SectionSummarizer,
)

sections = {

    "Risk Factors":

        """
        Supply chain disruptions
        remain a significant concern.
        The company continues to
        monitor inflation.
        """,

    "Outlook":

        """
        Management expects
        strong growth next year.
        AI investments remain
        a strategic priority.
        """,

}

###########################################################

results = (

    SectionSummarizer.summarize_sections(

        sections

    )

)

###########################################################

for section, summary in (

    results.items()

):

    print()

    print(section)

    print(summary)