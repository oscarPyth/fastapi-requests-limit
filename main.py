from fastapi import FastAPI

from fastapi_requests_limit.configuration import Limiter
from route import router

app = FastAPI()
limiter = Limiter(storage_engine="memory")
app.include_router(router)
