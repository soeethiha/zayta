from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .router_name import RouterName as Route
from models.token import Token
from models.token_data import TokenData
from models.user import Login
from commons.auth.auth_mixin import Auth

from commons.utils.exceptions import UnauthorizedException
from commons.config.config import set_odoo_uid

CLIENT_ID = "odoo"


PwdRequestFormDep = Annotated[OAuth2PasswordRequestForm, Depends()]

router = APIRouter()


@router.post(Route.login, response_model=Token)
async def login_for_access_token(form_data: PwdRequestFormDep):
    user_id = Auth.authenticate_user(
        login=Login(username=form_data.username, password=form_data.password)
    )
    if not user_id:
        raise UnauthorizedException

    return Token(
        access_token=Auth.create_access_token(data=TokenData(sub=str(user_id.uid)))
    )
