from tools.data_tools import load_customers, load_products, load_orders, load_campaigns

from state import CampaignState

from agents.planner import PlannerAgent
from agents.customer_insights import CustomerInsightsAgent
from agents.product_selector import ProductSelectorAgent

customers = load_customers()
products = load_products()
orders = load_orders()
campaigns = load_campaigns()

print("Customers:", customers.shape)
print("Products:", products.shape)
print("Orders:", orders.shape)
print("Campaigns:", campaigns.shape)

print(customers.head())

state = CampaignState(user_request = "Create a spring email campaign for beginner gardeners interested in tomato seeds in Ohio.")

agents = [
    PlannerAgent(),
    CustomerInsightsAgent(),
    ProductSelectorAgent()
]

for agent in agents:
    state = agent.run(state)

print(state.recommended_products)