from fastapi import FastAPI
from app.routers.twosum import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def root():
    return {"message": "DSA API - Available endpoints: /twosum"}
