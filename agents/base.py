from abc import ABC, abstractmethod
from state import CampaignState

class BaseAgent(ABC):
    name: str = "BaseAgent"

    def log(self, message: str):
        print(f"[{self.name}] {message}")

    def run(self, state: CampaignState) ->  CampaignState:
        pass