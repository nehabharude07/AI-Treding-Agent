class ReputationEngine:

    def __init__(self):
        self.score = 0

    def update(self, pnl, validation_score):
        self.score += pnl * 0.1 + validation_score
        return self.score