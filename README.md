# GreenLeaf Gardens Synthetic Marketing Dataset

Generated for an agentic marketing intelligence project. Data is synthetic but modeled after a gardening/e-commerce order schema.

Files:
- customers.csv: 5000 customer profiles with grow zones, club status, and preference fields.
- products.csv: 300 gardening products across seeds, plants, tools, fertilizer, pest control, and indoor growing.
- orders_full_schema.csv: 20000 orders using a production-inspired OMS schema.
- order_items.csv: line-item detail for orders.
- campaigns.csv: historical campaign metadata and performance.
- carts.csv: abandoned/recovered cart data for Klaviyo-style workflows.
- brand_voice_guide.txt and past_campaign_insights.txt: documents intended for RAG.

Suggested agent tools:
1. Segment customers by grow zone, club membership, category preference, and recency.
2. Recommend products based on season, inventory, margin, and customer segment.
3. Retrieve brand/past campaign guidance before generating copy.
4. Evaluate campaign output for audience relevance, brand fit, product fit, and KPI clarity.
