from app.pdf.summarization.pdf_summarizer import (
    PDFSummarizer,
)

sample_text = """

Revenue increased by 22%.

Management expects continued growth.

AI investments remain a strategic priority.

The company plans expansion into Asia.

Supply chain risks remain under monitoring.

"""

###########################################################

summary = PDFSummarizer.summarize(

    sample_text

)

###########################################################

print()

print("=" * 60)

print("PDF SUMMARY")

print("=" * 60)

print()

print(summary)