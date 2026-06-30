from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dashboard_api import router as dashboard_router
from app.api.company_api import router as company_router
from app.api.forecast_api import router as forecast_router
from app.api.portfolio_api import router as portfolio_router
from app.api.graph_api import router as graph_router
from app.api.chat_api import router as chat_router
from app.api.monitoring_api import router as monitoring_router
from app.api.timeline_api import router as timeline_router
from app.api.explainability_api import router as explainability_router
from app.api.scenario_api import router as scenario_router
from app.api.system_api import router as system_router

app = FastAPI(
    title="Enterprise Financial Intelligence Platform",
    version="18.19"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_router)
app.include_router(company_router)
app.include_router(forecast_router)
app.include_router(portfolio_router)
app.include_router(graph_router)
app.include_router(chat_router)
app.include_router(monitoring_router)
app.include_router(timeline_router)
app.include_router(explainability_router)
app.include_router(scenario_router)
app.include_router(system_router)


@app.get("/")
def root():

    return {

        "platform":
            "Enterprise Financial Intelligence Platform",

        "version":
            "18.19",

        "status":
            "Online"

    }