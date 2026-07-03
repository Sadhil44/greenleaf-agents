from agents.base import BaseAgent

from state import CampaignState

from tools.data_tools import load_products, search_products

class ProductSelectorAgent(BaseAgent):
    name = "ProductSelectorAgent"

    def run(self, state: CampaignState) -> CampaignState:
        self.log("Selecting Campaign Products")
        products = load_products()
        keyword = "tomato"
        matching_products = search_products(products, keyword)
        top_products = matching_products.head(5)
        print(top_products)
        state.recommended_products = top_products.to_dict(orient="records")
        return state
