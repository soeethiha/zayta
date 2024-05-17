from typing import Dict, Annotated
from fastapi import APIRouter

from commons.auth.auth_mixin import OdooUid

from .router_name import RouterName as Route

ReturnDict = Annotated[Dict, "Dict of any Kay and Value"]

router = APIRouter()


@router.get(Route.me)
def check_me(user_id: OdooUid) -> ReturnDict:
    return user_id.__dict__
