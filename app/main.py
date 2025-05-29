from fastapi import FastAPI
from app.routes.routes import router

app = FastAPI()
app.include_router(router=router)



@app.get("/ping")
def hello():
    return {"message": "pong"}