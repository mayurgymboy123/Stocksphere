from decimal import Decimal
from portfolio.models import Portfolio

class DashboardService:
    @staticmethod
    def get_holdings(user):
        portfolios = Portfolio.objects.filter(
            user=user).select_related("company")
        holdings = []
        for portfolio in portfolios:

            investment = (portfolio.quantity * portfolio.average_buy_price)

            current_value = (portfolio.quantity * portfolio.company.current_price)

            total_return = (current_value - investment)

            if investment > 0:
                return_percent = (total_return/investment) * Decimal("100")
            else:
                return_percent = Decimal("0")

            holdings.append({"company": portfolio.company,
                             "portfolio": portfolio,
                             "shares":portfolio.quantity,
                             "average_buy_price": portfolio.average_buy_price,
                             "current_price": portfolio.company.current_price,
                             "investment": investment,
                             "current_value": current_value,
                             "total_return": total_return,
                             "return_percent": round(return_percent, 2)})
        return holdings