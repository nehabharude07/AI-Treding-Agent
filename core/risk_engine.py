class RiskEngine:

    def calculate_position_size(self, portfolio, trade_size):

        if trade_size > portfolio:
            trade_size = portfolio * 0.1

        return trade_size