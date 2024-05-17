from .odoo_mixin import OdooMixin
from models.odoo_creds import OdooCreds
from core.odoo.odoo_model import Model, Method


class Product(OdooMixin):
    def get_product(self, creds: OdooCreds):
        fields = {"fields": ["name"], "limit": 3}
        domain = [[]]
        return self.model.execute_kw(
            self.db,
            creds.uid,
            creds.pwd,
            Model.product,
            Method.search_read,
            domain,
            fields,
        )
