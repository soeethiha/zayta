from typing import Dict, Annotated
from fastapi import APIRouter

from commons.auth.auth_mixin import OdooUid
from commons.config.config import config as cfg

from core.odoo.product import Product
from models.odoo_creds import OdooCreds

from .router_name import RouterName as Route

ReturnDict = Annotated[Dict, "Dict of any Kay and Value"]

router = APIRouter()


@router.get(Route.product)
def product(user_id: OdooUid):
    creds = OdooCreds(uid=user_id.uid, pwd=cfg.odoo_pwd)
    return Product().get_product(creds=creds)
