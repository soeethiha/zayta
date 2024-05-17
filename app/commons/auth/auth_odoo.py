from typing import Annotated, Dict, cast
from models.user import Login
from core.odoo.odoo_mixin import OdooMixin
from core.odoo.odoo_mixin import OdooUserID


class AuthOdoo(OdooMixin):
    def auth(self, login: Login) -> OdooUserID:
        return cast(
            OdooUserID,
            self._get_common().authenticate(
                self.db, login.username, login.password, {}
            ),
        )
