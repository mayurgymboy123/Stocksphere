import yfinance as yf


class YahooFinanceService:

    @classmethod
    def get_price(cls, yahoo_symbol):
        try:
            ticker = yf.Ticker(yahoo_symbol)
            history = ticker.history(period="1d")

            if history.empty:
                return {
                    "success": False,
                    "error": "Price not found"
                }

            return {
                "success": True,
                "price": float(history["Close"].iloc[-1])
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }