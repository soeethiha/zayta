import xmlrpc.client
from typing import Annotated, cast, Dict, List, Any, Tuple

from .odoo_model import Model, Attrib

from commons.config.config import config as cfg

XMLServer = Annotated[xmlrpc.client.ServerProxy, "XMLServer Object"]
OdooUserID = Annotated[int, "Odoo User ID"]


class OdooMixin:
    def __init__(self) -> None:
        self.db = cfg.odoo_db
        self.model = self._get_object()

    @staticmethod
    def _get_common() -> XMLServer:
        return xmlrpc.client.ServerProxy(cfg.odoo_xml_common.format(cfg.odoo_xml_url))

    @staticmethod
    def _get_object() -> XMLServer:
        return xmlrpc.client.ServerProxy(cfg.odoo_xml_object.format(cfg.odoo_xml_url))

    def verify(self) -> Dict[str, str]:
        return cast(Dict[str, str], self._get_common().version())
