from fastapi import FastAPI
from services.historial import router as historial_router
app = FastAPI()
app.include_router(historial_router)
@app.get("/")
def root():
    return None