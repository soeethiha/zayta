from fastapi import APIRouter

from api.v1.endpoints import login, product, check
from .router_prefix import prefix, tag

api_router = APIRouter()


api_router.include_router(router=login.router, prefix=prefix.login, tags=[tag.login])

api_router.include_router(
    router=product.router, prefix=prefix.product, tags=[tag.product]
)
api_router.include_router(router=check.router, prefix=prefix.check, tags=[tag.check])
