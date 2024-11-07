from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.db import Base, engine
from api.routers import api_routers


def get_application() -> FastAPI:
    application = FastAPI()

    async def startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    origins = []
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", startup)

    for api_router in api_routers:
        application.include_router(api_router, prefix='/api/v1')

    return application


app = get_application()