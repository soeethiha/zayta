from logging import getLogger

_logger = getLogger("uvicorn")

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # APP
    title: str = ""
    api_ver: str = ""
    description: str = ""
    version: str = ""

    # ASSET TOEKN
    token_url: str = ""
    key: str = ""
    algorithm: str = ""
    token_life_minutes: int = 1

    # LDAP
    ldap_server: str = ""
    ldap_server_port: int = 0
    ldap_binddn: str = ""
    ldap_filter: str = ""
    ldap_base: str = ""
    ldap_password: str = ""
    ldap_tls: bool = False
    ldap_chase_ref_disabled: bool = False

    # ODOO
    odoo_xml_common: str = ""
    odoo_xml_object: str = ""
    odoo_xml_url: str = ""
    odoo_db: str = ""
    odoo_user: str = ""
    odoo_pwd: str = ""
    odoo_uid: int = 0

    class Config:
        env_file = ".env"


_logger.info("Loading the config.")
config = Settings()


def set_odoo_uid(uid: int):
    config.odoo_uid = uid
