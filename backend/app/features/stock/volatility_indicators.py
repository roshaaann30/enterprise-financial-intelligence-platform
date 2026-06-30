import pandas as pd

from ta.volatility import (
    AverageTrueRange,
    BollingerBands,
    DonchianChannel,
    KeltnerChannel,
    UlcerIndex,
)


class VolatilityIndicatorGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        high = df["High"]
        low = df["Low"]
        close = df["Close"]

        # ==================================
        # ATR
        # ==================================

        atr = AverageTrueRange(
            high,
            low,
            close,
        )

        df["ATR"] = atr.average_true_range()

        # ==================================
        # Bollinger Bands
        # ==================================

        bb = BollingerBands(close)

        df["BB_High"] = bb.bollinger_hband()
        df["BB_Low"] = bb.bollinger_lband()
        df["BB_Middle"] = bb.bollinger_mavg()
        df["BB_Width"] = bb.bollinger_wband()
        df["BB_Percent"] = bb.bollinger_pband()

        # ==================================
        # Donchian Channel
        # ==================================

        don = DonchianChannel(
            high,
            low,
            close,
        )

        df["Donchian_High"] = don.donchian_channel_hband()
        df["Donchian_Low"] = don.donchian_channel_lband()
        df["Donchian_Middle"] = don.donchian_channel_mband()
        df["Donchian_Width"] = don.donchian_channel_wband()

        # ==================================
        # Keltner Channel
        # ==================================

        kc = KeltnerChannel(
            high,
            low,
            close,
        )

        df["KC_High"] = kc.keltner_channel_hband()
        df["KC_Low"] = kc.keltner_channel_lband()
        df["KC_Middle"] = kc.keltner_channel_mband()
        df["KC_Width"] = kc.keltner_channel_wband()

        # ==================================
        # Ulcer Index
        # ==================================

        ui = UlcerIndex(close)

        df["Ulcer_Index"] = ui.ulcer_index()

        # ==================================
        # Historical Volatility
        # ==================================

        returns = close.pct_change()

        df["Historical_Volatility"] = (
            returns.rolling(20).std()
            * (252 ** 0.5)
        )

        df.bfill(inplace=True)

        return df