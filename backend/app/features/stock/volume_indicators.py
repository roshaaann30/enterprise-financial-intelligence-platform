import pandas as pd

from ta.volume import (
    OnBalanceVolumeIndicator,
    AccDistIndexIndicator,
    ChaikinMoneyFlowIndicator,
    EaseOfMovementIndicator,
    ForceIndexIndicator,
    MFIIndicator,
    NegativeVolumeIndexIndicator,
    VolumePriceTrendIndicator,
    VolumeWeightedAveragePrice,
)


class VolumeIndicatorGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        high = df["High"]
        low = df["Low"]
        close = df["Close"]
        volume = df["Volume"]

        # ==========================================
        # On Balance Volume
        # ==========================================

        df["OBV"] = (
            OnBalanceVolumeIndicator(
                close,
                volume,
            ).on_balance_volume()
        )

        # ==========================================
        # Accumulation Distribution
        # ==========================================

        df["ADI"] = (
            AccDistIndexIndicator(
                high,
                low,
                close,
                volume,
            ).acc_dist_index()
        )

        # ==========================================
        # Chaikin Money Flow
        # ==========================================

        df["CMF"] = (
            ChaikinMoneyFlowIndicator(
                high,
                low,
                close,
                volume,
            ).chaikin_money_flow()
        )

        # ==========================================
        # Ease of Movement
        # ==========================================

        eom = EaseOfMovementIndicator(
            high,
            low,
            volume,
        )

        df["EOM"] = eom.ease_of_movement()
        df["EOM_SMA"] = eom.sma_ease_of_movement()

        # ==========================================
        # Force Index
        # ==========================================

        force = ForceIndexIndicator(
            close,
            volume,
        )

        df["Force_Index"] = force.force_index()

        # ==========================================
        # Money Flow Index
        # ==========================================

        df["MFI"] = (
            MFIIndicator(
                high,
                low,
                close,
                volume,
            ).money_flow_index()
        )

        # ==========================================
        # Negative Volume Index
        # ==========================================

        df["NVI"] = (
            NegativeVolumeIndexIndicator(
                close,
                volume,
            ).negative_volume_index()
        )

        # ==========================================
        # Volume Price Trend
        # ==========================================

        df["VPT"] = (
            VolumePriceTrendIndicator(
                close,
                volume,
            ).volume_price_trend()
        )

        # ==========================================
        # VWAP
        # ==========================================

        df["VWAP"] = (
            VolumeWeightedAveragePrice(
                high,
                low,
                close,
                volume,
            ).volume_weighted_average_price()
        )

        df.bfill(inplace=True)

        return df