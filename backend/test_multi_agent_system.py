from app.agents.agent_orchestrator import (
    AgentOrchestrator,
)

from app.agents.research_agent import (
    ResearchAgent,
)

from app.agents.financial_analyst_agent import (
    FinancialAnalystAgent,
)

from app.agents.news_analyst_agent import (
    NewsAnalystAgent,
)

from app.agents.risk_analyst_agent import (
    RiskAnalystAgent,
)

from app.agents.forecasting_agent import (
    ForecastingAgent,
)

from app.agents.portfolio_analyst_agent import (
    PortfolioAnalystAgent,
)

from app.agents.executive_report_generator import (
    ExecutiveReportGenerator,
)

###########################################################

knowledge = {

    "company":

        "Tesla",

    "metrics": {

        "Revenue":

            "96.7B",

        "Net Income":

            "12.4B",

    },

    "risks": [

        {

            "risk_type":

                "Supply Chain Risk"

        }

    ],

    "opportunities": [

        {

            "opportunity_type":

                "AI Investment"

        },

        {

            "opportunity_type":

                "Market Expansion"

        }

    ],

    "sentiment": {

        "sentiment":

            "Positive"

    },

}

###########################################################

agents = [

    ResearchAgent(),

    FinancialAnalystAgent(),

    NewsAnalystAgent(),

    RiskAnalystAgent(),

    ForecastingAgent(),

    PortfolioAnalystAgent(),

]

###########################################################

orchestrator = (

    AgentOrchestrator(

        agents

    )

)

###########################################################

results = (

    orchestrator.run(

        {

            "knowledge":

                knowledge,

            "bankruptcy_score":

                40,

            "credit_score":

                30,

            "pdf_risk_score":

                35,

        }

    )

)

###########################################################

report = (

    ExecutiveReportGenerator.generate(

        results

    )

)

###########################################################

print()

print("=" * 60)

print("MULTI-AGENT FINANCIAL ANALYST")

print("=" * 60)

print()

print(report)