from dataclasses import dataclass

@dataclass
class CustomerSegment:
    state: str
    customer_count: int
    average_order_value: float
    club_member_count: int
    top_grow_zone: str
    target_description: str