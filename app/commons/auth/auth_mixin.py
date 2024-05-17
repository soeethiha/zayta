from typing import Annotated, cast

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from .token_jwt import jwt_decode, jwt_encode
from .auth_odoo import AuthOdoo
from commons.config.config import config as cfg
from models.user import Login, UserID
from models.token_data import TokenData
from commons.utils.exceptions import CredentialsException
from commons.auth.token_jwt import JWTEncoded

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=cfg.token_url)

TokenDep = Annotated[str, Depends(oauth2_scheme)]


class Auth:
    @staticmethod
    def authenticate_user(login: Login) -> UserID:
        """Auth to Odoo and return odoo user id.

        Args:
            login (Login): Odoo user name and password.

        Returns:
            BaseModel: UserID
        """
        return UserID(uid=AuthOdoo().auth(login=login))

    @staticmethod
    def create_access_token(data: TokenData) -> JWTEncoded:
        return jwt_encode(data=data)

    @staticmethod
    async def get_current_user(token: TokenDep) -> UserID:
        # like validate token
        try:
            payload = jwt_decode(token=token)
            uid = cast(int, payload.get("sub"))

            if uid is None:
                raise CredentialsException

            return UserID(uid=uid)
        except JWTError as err:
            raise CredentialsException


OdooUid = Annotated[UserID, Depends(Auth.get_current_user)]
