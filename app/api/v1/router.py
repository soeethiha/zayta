from fastapi import APIRouter

from api.v1.endpoints import login, product, check, user, customers, sales
from .router_prefix import prefix, tag

api_router = APIRouter()


api_router.include_router(router=login.router, prefix=prefix.login, tags=[tag.login])

api_router.include_router(router=check.router, prefix=prefix.check, tags=[tag.check])

api_router.include_router(
    router=product.router, prefix=prefix.product, tags=[tag.product]
)

api_router.include_router(router=user.router, prefix=prefix.user, tags=[tag.user])

api_router.include_router(
    router=customers.router, prefix=prefix.customers, tags=[tag.customers]
)

api_router.include_router(router=sales.router, prefix=prefix.sales, tags=[tag.sales])
