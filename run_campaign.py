from tools.data_tools import load_customers, load_products, load_orders, load_campaigns

customers = load_customers()
products = load_products()
orders = load_orders()
campaigns = load_campaigns()

print("Customers:", customers.shape)
print("Products:", products.shape)
print("Orders:", orders.shape)
print("Campaigns:", campaigns.shape)

print(customers.head())