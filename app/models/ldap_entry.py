from pydantic import BaseModel


class LdapEntry(BaseModel):
    ldap_server: str
    ldap_server_port: str
    ldap_binddn: str
    ldap_filter: str
    ldap_base: str
