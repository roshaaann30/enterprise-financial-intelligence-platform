import numpy as np
import pandas as pd


class TimeSeriesFeatureGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        df["Date"] = pd.to_datetime(df["Date"])

        # ==========================================
        # Calendar Features
        # ==========================================

        df["Year"] = df["Date"].dt.year
        df["Quarter"] = df["Date"].dt.quarter
        df["Month"] = df["Date"].dt.month
        df["Week"] = df["Date"].dt.isocalendar().week.astype(int)
        df["Day"] = df["Date"].dt.day
        df["DayOfWeek"] = df["Date"].dt.dayofweek
        df["DayOfYear"] = df["Date"].dt.dayofyear

        # ==========================================
        # Boolean Features
        # ==========================================

        df["IsMonthStart"] = (
            df["Date"].dt.is_month_start.astype(int)
        )

        df["IsMonthEnd"] = (
            df["Date"].dt.is_month_end.astype(int)
        )

        df["IsQuarterStart"] = (
            df["Date"].dt.is_quarter_start.astype(int)
        )

        df["IsQuarterEnd"] = (
            df["Date"].dt.is_quarter_end.astype(int)
        )

        df["IsYearStart"] = (
            df["Date"].dt.is_year_start.astype(int)
        )

        df["IsYearEnd"] = (
            df["Date"].dt.is_year_end.astype(int)
        )

        df["Weekend"] = (
            df["DayOfWeek"] >= 5
        ).astype(int)

        # ==========================================
        # Trading Day Index
        # ==========================================

        df["TradingDay"] = np.arange(
            len(df)
        )

        # ==========================================
        # Cyclical Encoding
        # ==========================================

        df["Month_Sin"] = np.sin(
            2 * np.pi * df["Month"] / 12
        )

        df["Month_Cos"] = np.cos(
            2 * np.pi * df["Month"] / 12
        )

        df["DayOfWeek_Sin"] = np.sin(
            2 * np.pi * df["DayOfWeek"] / 7
        )

        df["DayOfWeek_Cos"] = np.cos(
            2 * np.pi * df["DayOfWeek"] / 7
        )

        df["DayOfYear_Sin"] = np.sin(
            2 * np.pi * df["DayOfYear"] / 365
        )

        df["DayOfYear_Cos"] = np.cos(
            2 * np.pi * df["DayOfYear"] / 365
        )

        return df