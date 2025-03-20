from typing import Dict, Annotated, cast
from fastapi import APIRouter

from commons.auth.auth_mixin import OdooUid
from commons.config.config import config as cfg

from core.odoo.user import User
from models.odoo_creds import OdooCreds
from models.sales import Sales

from .router_name import RouterName as Route

ReturnDict = Annotated[Dict, "Dict of any Kay and Value"]

router = APIRouter()

key = "login"


@router.get(Route.sales)
def sales(para: Sales, user_id: OdooUid):
    creds = OdooCreds(uid=user_id.uid, pwd=cfg.odoo_pwd)
    print(f"Sale Transactions : {para}")
