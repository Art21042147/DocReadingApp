from fastapi import FastAPI
from contextlib import asynccontextmanager

from backend.db.base import Base, engine



@asynccontextmanager
async def lifespan(_):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", reload=True)
