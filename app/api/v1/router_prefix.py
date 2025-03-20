class Prefix:
    login = "/login"
    check = "/check"
    security = "/security"
    product = "/product"
    user = "/user"
    customers = "/customers"
    customer_check = "/customer/check"
    sales="/sales"

class Tag(Prefix):
    def __init__(self) -> None:
        super().__init__()
        self.login = self.login[1:].upper()
        self.check = self.check[1:].upper()
        self.security = self.security[1:].upper()
        self.product = self.product[1:].upper()
        self.user = self.user[1:].upper()
        self.customers = self.customers[1:].upper()
        self.customer_check = self.customers[1:].upper()
        self.sales = self.sales[1:].upper()

prefix = Prefix()
tag = Tag()
