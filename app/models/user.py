from pydantic import BaseModel


class User(BaseModel):
    """User Name"""

    username: str


class Login(User):
    """Inherit to User and added password, basically User Name and Password."""

    password: str


class UserID(BaseModel):
    """Dedicated model for Odoo User ID"""

    uid: int
