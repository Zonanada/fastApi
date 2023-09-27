from fastapi import APIRouter, status
from core.models.db_dishes import DishesRepository as dishes_db
from fastapi.responses import JSONResponse
from core.schemas.validator import Dishes

router = APIRouter(
    prefix="/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes",
    tags=["Dishes"]
)


@router.get("")
def get_dishes_submenu(target_submenu_id: str):
    return dishes_db.get(submenu_id=target_submenu_id)


@router.get("/{api_test_dish_id}")
def get_dishes(api_test_dish_id):
    return dishes_db.get(dish_id=api_test_dish_id)


@router.post("", status_code=201)
def post_menus(target_submenu_id, query: Dishes):
    return dishes_db.inser(target_submenu_id, query)


@router.patch("/{api_test_dish_id}")
def update_menu(api_test_dish_id, query: Dishes):
    return dishes_db.update(api_test_dish_id, query)


@router.delete("/{api_test_dish_id}")
def del_dishes(api_test_dish_id):
    return dishes_db.delete(api_test_dish_id)
