import pytest
import requests
from test_submenu import post_submenu


def post_dishes():
    submenu = post_submenu()
    menu_id = submenu["menu_id"]
    submenu_id = submenu["res"].json()["id"]
    return {"menu_id": menu_id, "submenu_id": submenu_id, "res": requests.post(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', json={"title": "My dish 1", "description": "My dish description 1", "price": "12.50"})}


def get_dishes(menu_id, submenu_id, dishes_id):
    return requests.get(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dishes_id}')


def get_dishes_submenu(menu_id, submenu_id):
    return requests.get(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes')


def patch_dishes(menu_id, submenu_id, dishes_id):
    return requests.patch(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dishes_id}', json={"title": "My updated dish 1", "description": "My updated dish description 1", "price": "14.50"})


def delete_dishes(menu_id, submenu_id, dishes_id):
    return requests.delete(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dishes_id}')


class TestClassDishes:
    def test_create(self):
        res_post = post_dishes()
        res_post_body = res_post["res"].json()
        assert res_post["res"].status_code == 201
        assert res_post_body["title"] == "My dish 1"
        assert res_post_body["description"] == "My dish description 1"

    def test_read(self):
        res_post = post_dishes()
        menu_id = res_post["menu_id"]
        submenu_id = res_post["submenu_id"]
        dish_id = res_post["res"].json()["id"]
        res_get = get_dishes(menu_id, submenu_id, dish_id)
        res_get_body = res_get.json()
        assert res_get.status_code == 200
        assert res_get_body["title"] == "My dish 1"
        assert res_get_body["description"] == "My dish description 1"
        assert res_get_body["price"] == "12.5"
        res_get_2 = get_dishes(menu_id, submenu_id, dish_id)
        assert res_get_2.status_code == 200
        assert res_get_2.json() != []

    def test_update(self):
        res_post = post_dishes()
        menu_id = res_post["menu_id"]
        submenu_id = res_post["submenu_id"]
        dish_id = res_post["res"].json()["id"]
        res_update = patch_dishes(menu_id, submenu_id, dish_id)
        res_update_body = res_update.json()
        assert res_update.status_code == 200
        assert res_update_body["title"] == "My updated dish 1"
        assert res_update_body["description"] == "My updated dish description 1"
        assert res_update_body["price"] == "14.5"

    def test_delete(self):
        res_post = post_dishes()
        menu_id = res_post["menu_id"]
        submenu_id = res_post["submenu_id"]
        dish_id = res_post["res"].json()["id"]
        res_get = get_dishes(menu_id, submenu_id, dish_id)
        assert res_get.status_code == 200
        res_delete = delete_dishes(menu_id, submenu_id, dish_id)
        assert res_delete.status_code == 200
        assert get_dishes(menu_id, submenu_id, dish_id).status_code == 404