from dataclasses import dataclass
from datetime import datetime


@dataclass
class Pizza:
    restaurant: str
    name: str
    size: str
    price: int
    category: str
    source: str
    collected_at: str = datetime.now().strftime("%Y-%m-%d")

