from agents.base import BaseAgent

from state import CampaignState

from tools.data_tools import load_customers, load_orders, get_most_common_grow_zone

class CustomerInsightsAgent(BaseAgent):
    name = "CustomerInsightsAgent"

    def run(self, state: CampaignState) -> CampaignState:
        self.log("Analyzing Customer Data")
        customers = load_customers()
        orders = load_orders()

        ohio_customers = customers[customers["State"] == "OH"]
        ohio_orders = orders[orders["State"] == "OH"]

        customer_count = len(ohio_customers)
        avg_order_value = ohio_orders["Invoice_Total"].mean()

        club_members = ohio_customers[ohio_customers["Club_Member"] == True]
        club_member_count = len(club_members)

        top_grow_zone = get_most_common_grow_zone(customers)
        state.customer_segment = {
            "state": "OH",
            "customer_count": customer_count,
            "average_order_value": round(avg_order_value, 2),
            "club_member_count": club_member_count,
            "top_grow_zone": top_grow_zone,
            "target_description": "Ohio gardening customers likely to respond to a spring beginner tomato campaign",
        }

        return state