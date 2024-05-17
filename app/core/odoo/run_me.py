from typing import List, Dict, Any, cast
from enum import Enum

from .odoo_model import Model

async def execute(
    method: Model, domain: List[Any] = [], fields: Dict[Any, Any] = {}
) -> List[Dict[Any, Any]]:
    return cast(
        List[Dict[Any, Any]],
        odoo_obj.model.execute_kw(
            odoo_obj.db,
            odoo_obj.uid,
            odoo_obj.pwd,
            method.value[Attrib.MODEL],
            method.value[Attrib.METHOLD],
            [[domain]],
            fields,
        ),
    )
