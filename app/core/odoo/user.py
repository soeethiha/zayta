from .odoo_mixin import OdooMixin
from models.odoo_creds import OdooCreds
from core.odoo.odoo_model import Model, Method

class User(OdooMixin):
    def get_user(self, creds: OdooCreds):
        fields = {"fields": ["login"]}
        domain = [[("id", "=", creds.uid)]]
        return self.model.execute_kw(
            self.db,
            creds.uid,
            creds.pwd,
            Model.user,
            Method.search_read,
            domain,
            fields,
        )
