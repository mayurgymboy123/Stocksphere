import requests

from django.conf import settings


class StockService:
    BASE_URL = "https://api.twelvedata.com"

    @classmethod
    def get_price(cls, symbol):
        url = f"{cls.BASE_URL}/price"

        params = {
            "symbol": symbol,
            "apikey": settings.TWELVE_DATA_API_KEY,
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get("status") == "error":
                return {
                    "success": False,
                    "error": data.get("message", "Unknown API error"),
                }

            return {
                "success": True,
                "symbol": symbol,
                "price": float(data["price"]),
            }

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timed out.",
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Unable to connect to Twelve Data.",
            }

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e),
            }
        
    
    @classmethod
    def search_companies(cls, query):
        url = f"{cls.BASE_URL}/symbol_search"

        params = {
            "symbol": query,
            "apikey": settings.TWELVE_DATA_API_KEY,
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get("status") == "error":
                return {
                    "success": False,
                    "error": data.get("message", "Unknown API error"),
                }

            return {
                "success": True,
                "results": data.get("data", []),
            }

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e),
            }