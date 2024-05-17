from typing import Annotated, Dict
from datetime import datetime, timedelta

from jose import jwt

from commons.config.config import config as cfg
from models.token_data import TokenData

JWTEncoded = Annotated[
    str, "The string representation of the header, claims, and signature."
]

JWTData = Annotated[Dict, "Decoded JWT Data seach Header, Payload..."]

def jwt_encode(data: TokenData) -> JWTEncoded:
    data.exp = datetime.utcnow() + timedelta(minutes=cfg.token_life_minutes)
    return jwt.encode(data.__dict__, cfg.key, algorithm=cfg.algorithm)


def jwt_decode(token: JWTEncoded) -> JWTData:
    return jwt.decode(token, cfg.key, algorithms=[cfg.algorithm])
