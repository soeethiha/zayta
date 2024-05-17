from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class TokenData(BaseModel):
    sub: str = ""
    exp: datetime = Field(default_factory=datetime.now)
