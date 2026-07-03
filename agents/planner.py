from agents.base import BaseAgent

from state import CampaignState

class PlannerAgent(BaseAgent):
    name = "PlannerAgent"

    def run(self, state: CampaignState) -> CampaignState:
        self.log("Creating a campaign execution plan")

        state.plan = [
            "Analyze the user request",
            "Identify the best customer segment",
            "Select relevant products",
            "Generate campaign content",
            "Evaluate the campaign quality",
        ]

        return state
    