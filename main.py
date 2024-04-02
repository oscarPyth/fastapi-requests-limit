from fastapi import FastAPI

from fastapi_requests_limit.configuration import Limiter
from route import router

app = FastAPI()
limiter = Limiter(host="localhost", port="6379", storage_engine="redis")
app.include_router(router)
