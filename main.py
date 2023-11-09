from fastapi import FastAPI
from route import router
from fastapi_ratelimit.configuration import Limiter

app = FastAPI()
limiter = Limiter(host="localhost", storage_engine='redis')
app.include_router(router)
