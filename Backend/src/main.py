from fastapi import FastAPI
from src.lib.Users.infraestructure.routes.UserRoutes import user_routes
from src.lib.Users.infraestructure.database.DatabaseCofig import init_models


app = FastAPI()

app.include_router(user_routes)

@app.on_event("startup")
async def on_startup():
    await init_models()

app.get('/')
async def root():
    return {"message":"Api funcionando"}
