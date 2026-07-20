from companies.models import Company
from companies.services.stock_service import StockService
from companies.services.yahoo_service import YahooFinanceService


class CompanyImportService:

    @classmethod
    def import_company(cls, symbol):
        # Check if company already exists
        company = Company.objects.filter(symbol=symbol).first()

        if company:
            return company

        # Search company from Twelve Data
        result = StockService.search_companies(symbol)

        if not result["success"] or not result["results"]:
            return None

        data = result["results"][0]

        yahoo_symbol = data["symbol"]

        if data["exchange"] == "NSE":
            yahoo_symbol = f"{data['symbol']}.NS"
        elif data["exchange"] == "BSE":
            yahoo_symbol = f"{data['symbol']}.BO"

        # Get live price
        price_result = YahooFinanceService.get_price(yahoo_symbol)

        current_price = 0

        if price_result["success"]:
            current_price = price_result["price"]

        # Create company
        company = Company.objects.create(
            name=data.get("instrument_name", symbol),
            symbol=data.get("symbol", symbol),
            yahoo_symbol=yahoo_symbol,
            exchange=data.get("exchange", ""),
            country=data.get("country", ""),
            currency=data.get("currency", ""),
            current_price=current_price,
        )

        return company