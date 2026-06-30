import pandas as pd

from ta.momentum import (
    RSIIndicator,
    StochasticOscillator,
    WilliamsRIndicator,
    ROCIndicator,
    TSIIndicator,
    PercentagePriceOscillator,
    UltimateOscillator,
    KAMAIndicator,
)


class MomentumIndicatorGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        close = df["Close"]
        high = df["High"]
        low = df["Low"]

        # RSI
        df["RSI"] = RSIIndicator(close).rsi()

        # Stochastic
        stoch = StochasticOscillator(
            high,
            low,
            close,
        )

        df["Stochastic_K"] = stoch.stoch()
        df["Stochastic_D"] = stoch.stoch_signal()

        # Williams %R
        df["Williams_R"] = WilliamsRIndicator(
            high,
            low,
            close,
        ).williams_r()

        # ROC
        df["ROC"] = ROCIndicator(close).roc()

        # TSI
        df["TSI"] = TSIIndicator(close).tsi()

        # PPO
        ppo = PercentagePriceOscillator(close)

        df["PPO"] = ppo.ppo()
        df["PPO_Signal"] = ppo.ppo_signal()
        df["PPO_Histogram"] = ppo.ppo_hist()

        # Ultimate Oscillator
        df["Ultimate_Oscillator"] = (
            UltimateOscillator(
                high,
                low,
                close,
            ).ultimate_oscillator()
        )

        # KAMA
        df["KAMA"] = (
            KAMAIndicator(close).kama()
        )

        df.bfill(inplace=True)

        return df