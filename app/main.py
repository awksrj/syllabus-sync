from fastapi import FastAPI
from app.routes import api_routes, ui_routes

app = FastAPI()

# API endpoints
app.include_router(api_routes.router, prefix="/api")

app.include_router(ui_routes.router)
