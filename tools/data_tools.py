from pathlib import Path
import pandas as pd

data = Path(__file__).resolve().parent.parent / "data"

def load_customers():
    return pd.read_csv(data / "customers.csv")

def load_products():
    return pd.read_csv(data / "products.csv")

def load_orders():
    return pd.read_csv(data / "orders_full_schema.csv")

def load_campaigns():
    return pd.read_csv(data / "campaigns.csv")

def get_most_common_grow_zone(customers):
    grow_zone = customers["Grow_Zone"].mode()
    return grow_zone.iloc[0]
