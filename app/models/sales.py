from typing import List
from pydantic import BaseModel


class Lines(BaseModel):
    # [{"product_id":2,"price":1000,"qty":10,"discount_perc":"5"}]
    product_id: int
    price: int
    qty: int
    discount_peric: float


class Sales(BaseModel):
    customer_id: str
    tx_date: str
    lines: List[Lines]
