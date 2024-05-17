from fastapi import FastAPI
from contextlib import asynccontextmanager

from commons.config.config import config as cfg
from api.v1.router import api_router

DOC_URL = f"{cfg.api_ver}/openapi.json"


class Server:
    @asynccontextmanager
    async def initialize(self, app: FastAPI):
        # do something here before starting up
        yield
        # do someting here before shutting down

    def start(self) -> FastAPI:
        app = FastAPI(
            title=cfg.title,
            openapi_url=DOC_URL,
            lifespan=self.initialize,
            description=cfg.description,
            version=cfg.version,
        )
        app.include_router(router=api_router, prefix=cfg.api_ver)
        return app
