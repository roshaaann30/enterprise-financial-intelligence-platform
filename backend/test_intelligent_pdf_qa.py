from app.pdf.qa.intelligent_pdf_qa import (
    IntelligentPDFQA,
)

chunks = [

    "Revenue increased by 22%.",

    "AI investments remain a strategic priority.",

    "Management expects continued growth.",

]

result = (

    IntelligentPDFQA.ask(

        "What did management say about AI?",

        chunks,

    )

)

print(result)