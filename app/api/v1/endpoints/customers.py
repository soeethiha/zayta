from typing import Annotated

from fastapi import APIRouter, Path, status, HTTPException


from commons.auth.auth_mixin import OdooUid
from commons.config.config import config as cfg

from core.odoo.customers import Customer
from models.odoo_creds import OdooCreds

from .router_name import RouterName as Route


router = APIRouter()


@router.get(Route.customers)
def customers(user_id: OdooUid):
    creds = OdooCreds(uid=user_id.uid, pwd=cfg.odoo_pwd)
    return Customer().get_customers(creds=creds)


@router.get(Route.customer_check)
async def check_customer(
    user_id: OdooUid,
    customer_id: Annotated[str, Path(title="Customer ID to check whether have or not")],
):
    creds = OdooCreds(uid=user_id.uid, pwd=cfg.odoo_pwd)
    result = Customer().check_customer(creds=creds, customer_id=customer_id)
    if result:
        return result
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer ID : {customer_id} not found",
        )
