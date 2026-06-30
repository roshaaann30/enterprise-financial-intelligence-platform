from app.pdf.sections.section_identifier import (
    SectionIdentifier,
)

sample_text = """

Business Overview

The company operates globally.

Risk Factors

Supply chain disruptions remain a concern.

Management Discussion and Analysis

Revenue increased by 18%.

Financial Statements

Consolidated statements of income.

Outlook

Management expects continued growth.

"""

###########################################################

sections = (

    SectionIdentifier.identify(

        sample_text

    )

)

###########################################################

print()

print("=" * 60)

print("SECTION INTELLIGENCE")

print("=" * 60)

print()

for section in sections:

    print(

        "-",

        section,

    )