from typing import Dict, Annotated, cast
from fastapi import APIRouter

from commons.auth.auth_mixin import OdooUid
from commons.config.config import config as cfg

from core.odoo.user import User
from models.odoo_creds import OdooCreds

from .router_name import RouterName as Route

ReturnDict = Annotated[Dict, "Dict of any Kay and Value"]

router = APIRouter()

key = "login"


@router.get(Route.user)
def user(user_id: OdooUid):
    creds = OdooCreds(uid=user_id.uid, pwd=cfg.odoo_pwd)
    user = cast(Dict, User().get_user(creds=creds))
    for val in user:
        val[key] = val[key].upper()

    return user
