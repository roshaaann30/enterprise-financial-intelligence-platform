import pandas as pd

from ta.trend import (
    ADXIndicator,
    CCIIndicator,
    AroonIndicator,
    IchimokuIndicator,
    TRIXIndicator,
    DPOIndicator,
    PSARIndicator,
)


class TrendIndicatorGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        high = df["High"]
        low = df["Low"]
        close = df["Close"]

        # ============================
        # ADX
        # ============================

        adx = ADXIndicator(
            high,
            low,
            close,
        )

        df["ADX"] = adx.adx()
        df["DI_Positive"] = adx.adx_pos()
        df["DI_Negative"] = adx.adx_neg()

        # ============================
        # CCI
        # ============================

        cci = CCIIndicator(
            high,
            low,
            close,
        )

        df["CCI"] = cci.cci()

        # ============================
        # Aroon
        # ============================

        aroon = AroonIndicator(
            high,
            low,
        )

        df["Aroon_Up"] = aroon.aroon_up()
        df["Aroon_Down"] = aroon.aroon_down()
        df["Aroon_Indicator"] = (
            aroon.aroon_indicator()
        )

        # ============================
        # Ichimoku
        # ============================

        ichi = IchimokuIndicator(
            high,
            low,
        )

        df["Ichimoku_A"] = ichi.ichimoku_a()
        df["Ichimoku_B"] = ichi.ichimoku_b()
        df["Ichimoku_Base"] = (
            ichi.ichimoku_base_line()
        )
        df["Ichimoku_Conversion"] = (
            ichi.ichimoku_conversion_line()
        )

        # ============================
        # TRIX
        # ============================

        df["TRIX"] = (
            TRIXIndicator(close)
            .trix()
        )

        # ============================
        # DPO
        # ============================

        df["DPO"] = (
            DPOIndicator(close)
            .dpo()
        )

        # ============================
        # Parabolic SAR
        # ============================

        psar = PSARIndicator(
            high,
            low,
            close,
        )

        df["PSAR"] = psar.psar()
        df["PSAR_Up"] = psar.psar_up()
        df["PSAR_Down"] = psar.psar_down()

        df.bfill(inplace=True)

        return df