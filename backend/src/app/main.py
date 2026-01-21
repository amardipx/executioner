from fastapi import FastAPI
from app.api.v1 import auth

app = FastAPI(title="Executioner 1v1")

app.include_router(auth.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
