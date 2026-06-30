from app.assistant.rag_financial_assistant import (
    RAGFinancialAssistant,
)

chunks = [

    "Revenue declined due to weaker consumer demand.",

    "Debt increased because of strategic acquisitions.",

    "Management expects recovery next year.",

    "AI investments remain a strategic priority.",

]

result = (

    RAGFinancialAssistant.ask(

        question="Why did revenue decline?",

        chunks=chunks,

        metric="Revenue",

        current=85,

        previous=100,

    )

)

print(result)