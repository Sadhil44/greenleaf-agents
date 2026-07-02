from dataclasses import dataclass, field

@dataclass
class CampaignState:
    user_request: str

    plan: list[str] = field(default_factory=list)
    customer_segment: dict = field(default_factory=dict)
    recommended_products: list[dict] = field(default_factory=list)
    campaign_text: str = ""
    evaluation: dict = field(default_factory=dict)
    
