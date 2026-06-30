class HealthClassifier:

    """
    Enterprise Financial Health Classifier

    Converts a financial health score into

    - Health Rating
    - Risk Level
    - Recommendation
    """

    ###########################################################
    # Classification
    ###########################################################

    @staticmethod
    def classify(score):

        score = float(score)

        #######################################################

        if score >= 90:

            return {

                "HealthRating": "Excellent",

                "RiskLevel": "Very Low",

                "Recommendation":
                "Maintain current financial strategy and continue investing for growth.",

                "Color": "green",

            }

        #######################################################

        elif score >= 75:

            return {

                "HealthRating": "Good",

                "RiskLevel": "Low",

                "Recommendation":
                "Strong financial position with minor opportunities for improvement.",

                "Color": "lightgreen",

            }

        #######################################################

        elif score >= 60:

            return {

                "HealthRating": "Average",

                "RiskLevel": "Moderate",

                "Recommendation":
                "Improve profitability and operational efficiency.",

                "Color": "yellow",

            }

        #######################################################

        elif score >= 40:

            return {

                "HealthRating": "Poor",

                "RiskLevel": "High",

                "Recommendation":
                "Reduce leverage, improve liquidity, and strengthen cash flow.",

                "Color": "orange",

            }

        #######################################################

        else:

            return {

                "HealthRating": "Critical",

                "RiskLevel": "Very High",

                "Recommendation":
                "Immediate financial restructuring is recommended.",

                "Color": "red",

            }

    ###########################################################
    # Batch Classification
    ###########################################################

    @staticmethod
    def classify_dataframe(df):

        dataframe = df.copy()

        if "FinancialHealthScore" not in dataframe.columns:

            raise ValueError(

                "FinancialHealthScore column not found."

            )

        dataframe["HealthRating"] = dataframe[
            "FinancialHealthScore"
        ].apply(

            lambda score:

            HealthClassifier.classify(score)[
                "HealthRating"
            ]

        )

        dataframe["RiskLevel"] = dataframe[
            "FinancialHealthScore"
        ].apply(

            lambda score:

            HealthClassifier.classify(score)[
                "RiskLevel"
            ]

        )

        dataframe["Recommendation"] = dataframe[
            "FinancialHealthScore"
        ].apply(

            lambda score:

            HealthClassifier.classify(score)[
                "Recommendation"
            ]

        )

        dataframe["Color"] = dataframe[
            "FinancialHealthScore"
        ].apply(

            lambda score:

            HealthClassifier.classify(score)[
                "Color"
            ]

        )

        return dataframe

    ###########################################################
    # Summary
    ###########################################################

    @staticmethod
    def summary(df):

        return {

            "Excellent": int(

                (df["HealthRating"] == "Excellent").sum()

            ),

            "Good": int(

                (df["HealthRating"] == "Good").sum()

            ),

            "Average": int(

                (df["HealthRating"] == "Average").sum()

            ),

            "Poor": int(

                (df["HealthRating"] == "Poor").sum()

            ),

            "Critical": int(

                (df["HealthRating"] == "Critical").sum()

            ),

        }