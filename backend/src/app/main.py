from fastapi import FastAPI

app = FastAPI(title="Executioner 1v1")

@app.get("/health")
async def health():
    return {"status": "ok"}
