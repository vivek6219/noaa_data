from fastapi import FastAPI
from routes.routes import router

app = FastAPI()
app.include_router(router=router)

# @app.get("/")
# def hello():
#     return {"Hello": "world"}