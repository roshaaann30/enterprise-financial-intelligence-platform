import pandas as pd

from ta.trend import (
    SMAIndicator,
    EMAIndicator,
    MACD,
)

from ta.momentum import RSIIndicator

from ta.volatility import BollingerBands

from ta.volume import OnBalanceVolumeIndicator


class TechnicalIndicatorGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        # ===========================
        # Moving Averages
        # ===========================

        df["SMA_5"] = SMAIndicator(
            close,
            window=5,
        ).sma_indicator()

        df["SMA_10"] = SMAIndicator(
            close,
            window=10,
        ).sma_indicator()

        df["SMA_20"] = SMAIndicator(
            close,
            window=20,
        ).sma_indicator()

        df["SMA_50"] = SMAIndicator(
            close,
            window=50,
        ).sma_indicator()

        df["EMA_5"] = EMAIndicator(
            close,
            window=5,
        ).ema_indicator()

        df["EMA_10"] = EMAIndicator(
            close,
            window=10,
        ).ema_indicator()

        df["EMA_20"] = EMAIndicator(
            close,
            window=20,
        ).ema_indicator()

        df["EMA_50"] = EMAIndicator(
            close,
            window=50,
        ).ema_indicator()

        # ===========================
        # MACD
        # ===========================

        macd = MACD(close)

        df["MACD"] = macd.macd()

        df["MACD_Signal"] = macd.macd_signal()

        df["MACD_Histogram"] = macd.macd_diff()

        # ===========================
        # RSI
        # ===========================

        df["RSI"] = RSIIndicator(
            close
        ).rsi()

        # ===========================
        # Bollinger Bands
        # ===========================

        bb = BollingerBands(close)

        df["BB_High"] = bb.bollinger_hband()

        df["BB_Low"] = bb.bollinger_lband()

        df["BB_Middle"] = bb.bollinger_mavg()

        df["BB_Width"] = bb.bollinger_wband()

        # ===========================
        # OBV
        # ===========================

        df["OBV"] = (
            OnBalanceVolumeIndicator(
                close,
                volume,
            ).on_balance_volume()
        )

        df.bfill(inplace=True)

        return df