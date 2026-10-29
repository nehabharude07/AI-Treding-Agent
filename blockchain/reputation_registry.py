class ReputationRegistry:

    def update_reputation(self, agent, score):
        return {
            "agent": agent,
            "new_score": score
        }