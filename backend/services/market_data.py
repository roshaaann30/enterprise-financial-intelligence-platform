import yfinance as yf


class MarketDataService:

    TICKERS = [
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN",
        "META",
        "NVDA",
        "TSLA"
    ]

    def get_market_data(self):

        results = []

        for ticker in self.TICKERS:

            stock = yf.Ticker(ticker)

            info = stock.info

            results.append({
                "ticker": ticker,
                "price": info.get("currentPrice"),
                "market_cap": info.get("marketCap"),
                "volume": info.get("volume")
            })

        return results