from fastapi import FastAPI
from core.routers.router_menu import router as router_menu
from core.routers.router_submenu import router as router_submenu
from core.routers.router_dishes import router as router_dishes


app = FastAPI(title="Restaurant")

app.include_router(router_menu)
app.include_router(router_submenu)
app.include_router(router_dishes)