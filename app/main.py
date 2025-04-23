from fastapi import FastAPI
from app.api.routes_persona import router as persona_router

app = FastAPI()
app.include_router(persona_router)
