from app.agents.base_agent import (
    BaseAgent,
)


class NewsAnalystAgent(

    BaseAgent

):

    """
    Enterprise News Analyst Agent
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

    ):

        super().__init__(

            "NewsAnalystAgent"

        )

    ###########################################################
    # Market Sentiment
    ###########################################################

    @staticmethod
    def market_sentiment(

        sentiment,

    ):

        sentiment = sentiment.lower()

        if sentiment == "positive":

            return "Bullish"

        elif sentiment == "negative":

            return "Bearish"

        return "Neutral"

    ###########################################################
    # News Score
    ###########################################################

    @staticmethod
    def calculate_news_score(

        sentiment,

        opportunities,

        risks,

    ):

        score = 50

        if sentiment.lower() == "positive":

            score += 20

        elif sentiment.lower() == "negative":

            score -= 20

        score += (

            len(opportunities) * 5

        )

        score -= (

            len(risks) * 5

        )

        return max(

            0,

            min(

                score,

                100,

            ),

        )

    ###########################################################
    # Competitor Activity
    ###########################################################

    @staticmethod
    def competitor_activity(

        opportunities,

    ):

        if len(opportunities) >= 3:

            return "Increasing"

        elif len(opportunities) >= 1:

            return "Stable"

        return "Unknown"

    ###########################################################
    # Market Impact
    ###########################################################

    @staticmethod
    def market_impact(

        score,

    ):

        if score >= 80:

            return "Very Positive"

        elif score >= 65:

            return "Positive"

        elif score >= 50:

            return "Neutral"

        elif score >= 35:

            return "Negative"

        return "Very Negative"

    ###########################################################
    # Run
    ###########################################################

    def run(

        self,

        context,

    ):

        research = context.get(

            "research_findings",

            {},

        )

        #######################################################
        # Inputs
        #######################################################

        opportunities = research.get(

            "opportunities",

            [],

        )

        risks = research.get(

            "risks",

            [],

        )

        sentiment_data = research.get(

            "sentiment",

            {},

        )

        sentiment = sentiment_data.get(

            "sentiment",

            "Neutral",

        )

        #######################################################
        # Analysis
        #######################################################

        market_sentiment = (

            self.market_sentiment(

                sentiment

            )

        )

        news_score = (

            self.calculate_news_score(

                sentiment,

                opportunities,

                risks,

            )

        )

        competitor_activity = (

            self.competitor_activity(

                opportunities

            )

        )

        impact = (

            self.market_impact(

                news_score

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "news_analysis": {

                "market_sentiment":

                    market_sentiment,

                "news_score":

                    news_score,

                "competitor_activity":

                    competitor_activity,

                "market_impact":

                    impact,

                "opportunity_mentions":

                    len(

                        opportunities

                    ),

                "risk_mentions":

                    len(

                        risks

                    ),

            }

        }