from pydantic import BaseModel
from typing import List

class TradeRequest(BaseModel):
    features: List[float]
    portfolio_value: float
    trade_size: float
    market: str