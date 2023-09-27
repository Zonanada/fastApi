from fastapi import APIRouter, status
from core.models.db_submenu import SubmenuRepository as submenu_db
from fastapi.responses import JSONResponse
from core.schemas.validator import Menu

router = APIRouter(
    prefix="/api/v1/menus/{target_menu_id}/submenus",
    tags=["Submenu"]
)


@router.get("/{target_submenu_id}")
def get_submenu(target_submenu_id):
    return submenu_db.get(submenu_id=target_submenu_id)


@router.get("")
def get_submenu_menu(target_menu_id):
    return submenu_db.get(menu_id=target_menu_id)


@router.post("", status_code=201)
def post_menus(query: Menu, target_menu_id):
    return submenu_db.insert(target_menu_id, query)


@router.patch("/{target_submenu_id}")
def update_submenu(query: Menu, target_submenu_id: str):
    return submenu_db.update(target_submenu_id, query)


@router.delete("/{target_submenu_id}")
def del_submenu(target_submenu_id: str):
    return submenu_db.delete(target_submenu_id)
