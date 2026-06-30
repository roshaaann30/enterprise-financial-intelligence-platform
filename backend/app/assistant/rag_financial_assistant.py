from app.assistant.financial_qa_engine import (
    FinancialQAEngine,
)

from app.assistant.company_comparison import (
    CompanyComparison,
)

from app.assistant.earnings_call_summarizer import (
    EarningsCallSummarizer,
)

from app.assistant.financial_explainer import (
    FinancialExplainer,
)


class RAGFinancialAssistant:

    """
    Enterprise Financial Assistant
    """

    ###########################################################
    # Question Type
    ###########################################################

    @staticmethod
    def detect_question_type(

        question,

    ):

        question = question.lower()

        if "compare" in question:

            return "comparison"

        if "earnings call" in question:

            return "earnings_call"

        if "why" in question:

            return "explanation"

        return "qa"

    ###########################################################
    # Build Executive Response
    ###########################################################

    @staticmethod
    def executive_response(

        answer,

        citations,

        confidence,

    ):

        return {

            "answer":

                answer,

            "confidence":

                confidence,

            "citations":

                citations,

        }

    ###########################################################
    # Main Assistant
    ###########################################################

    @staticmethod
    def ask(

        question,

        chunks=None,

        company_a=None,

        company_b=None,

        transcript=None,

        metric=None,

        current=None,

        previous=None,

    ):

        question_type = (

            RAGFinancialAssistant

            .detect_question_type(

                question

            )

        )

        #######################################################
        # Company Comparison
        #######################################################

        if question_type == "comparison":

            result = (

                CompanyComparison.compare(

                    company_a,

                    company_b,

                )

            )

            return {

                "question":

                    question,

                "type":

                    "comparison",

                "result":

                    result,

            }

        #######################################################
        # Earnings Call
        #######################################################

        if question_type == "earnings_call":

            result = (

                EarningsCallSummarizer

                .summarize(

                    transcript

                )

            )

            return {

                "question":

                    question,

                "type":

                    "earnings_call",

                "result":

                    result,

            }

        #######################################################
        # Financial Explanation
        #######################################################

        if question_type == "explanation":

            if (

                metric is not None

                and current is not None

                and previous is not None

            ):

                result = (

                    FinancialExplainer

                    .explain(

                        metric,

                        current,

                        previous,

                    )

                )

                return {

                    "question":

                        question,

                    "type":

                        "explanation",

                    "result":

                        result,

                }

        #######################################################
        # Default RAG QA
        #######################################################

        result = (

            FinancialQAEngine.ask(

                question,

                chunks,

            )

        )

        return {

            "question":

                question,

            "type":

                "financial_qa",

            "result":

                self.executive_response(

                    result["answer"],

                    result["citations"],

                    result["confidence"],

                )

        }