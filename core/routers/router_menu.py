from fastapi import APIRouter, status
from core.models.db_menu import MenuRepository as menu_db
from fastapi.responses import JSONResponse
from core.schemas.validator import Menu

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Menu"]
)


@router.get("")
def get_menus():
    return menu_db.get()


@router.get("/{target_menu_id}")
def get_menu(target_menu_id: str):
    return menu_db.get(menu_id=target_menu_id)


@router.post("", status_code=201)
def post_menus(query: Menu):
    return menu_db.insert(query)


@router.delete("/{target_menu_id}")
def del_menu(target_menu_id: str):
    return menu_db.delete(target_menu_id)


@router.patch("/{target_menu_id}")
def update_menu(query: Menu, target_menu_id: str):
    return menu_db.update(target_menu_id, query)
