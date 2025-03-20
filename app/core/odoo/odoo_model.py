from enum import Enum
from enum import IntEnum


class Attrib:
    MODEL = 0
    METHOD = 1


class Method:
    search = "search"
    read = "read"
    search_read = "search_read"


class Model:
    product = "product.template"
    user = "res.users"
    partner = "res.partner"
