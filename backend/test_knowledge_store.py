from app.pdf.knowledge.knowledge_store import (
    KnowledgeStore,
)

sample = {

    "company":
        "Tesla",

    "metrics": {

        "Revenue":
            "96.7B"

    }

}

KnowledgeStore.save(

    sample,

    "knowledge.json",

)

loaded = (

    KnowledgeStore.load(

        "knowledge.json"

    )

)

print(loaded)