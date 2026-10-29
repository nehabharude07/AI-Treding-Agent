class PortfolioManager:

    def __init__(self):
        self.positions = {}

    def update_position(self, market, size):
        self.positions[market] = self.positions.get(market, 0) + size
        return self.positions