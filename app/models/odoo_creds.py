from pydantic import BaseModel


class OdooCreds(BaseModel):
    uid: int
    pwd: str
