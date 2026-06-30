from fastapi import APIRouter
from app.services.graph_builder import GraphBuilder

router = APIRouter()

graph_builder = GraphBuilder()


@router.get("/graph")
def get_graph():

    return graph_builder.build_company_graph(
        "Apple"
    )