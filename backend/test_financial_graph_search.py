from app.knowledge_graph.financial_graph_search import (
    FinancialGraphSearch,
)

results = (

    FinancialGraphSearch.find_relationships(

        graph,

        "Apple",

    )

)

print(results)