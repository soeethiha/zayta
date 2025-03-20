from typing import List, Dict, cast

from models.odoo_creds import OdooCreds
from core.odoo.odoo_model import Model, Method

from .odoo_mixin import OdooMixin


class Customer(OdooMixin):
    def get_customers(self, creds: OdooCreds):
        fields = {"fields": ["customer_id"], "limit": 1000}
        domain = [[("customer_id", "!=", False)]]
        return self.model.execute_kw(
            self.db,
            creds.uid,
            creds.pwd,
            Model.partner,
            Method.search_read,
            domain,
            fields,
        )

    def check_customer(self, creds: OdooCreds, customer_id: str) -> List[Dict]:
        fields = {"fields": ["id"]}
        domain = [[("customer_id", "=", customer_id)]]
        return cast(
            List,
            self.model.execute_kw(
                self.db,
                creds.uid,
                creds.pwd,
                Model.partner,
                Method.search_read,
                domain,
                fields,
            ),
        )
