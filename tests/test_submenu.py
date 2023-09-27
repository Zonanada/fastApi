import pytest
import requests
from test_menu import post_menu


def post_submenu():
    menu_id = post_menu().json()["id"]
    return {"menu_id": menu_id, "res": requests.post(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus', json={"title": "My submenu 1", "description": "My submenu description 1"})}


def get_submenu(menu_id, submenu_id):
    return requests.get(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}')


def get_submenu_menu(menu_id):
    return requests.get(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus')


def patch_submenu(menu_id, submenu_id):
    return requests.patch(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}', json={"title": "My updated submenu 1", "description": "My updated submenu description 1"})


def delete_submenu(menu_id, submenu_id):
    return requests.delete(f'http://localhost:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}')


class TestClassSubmenu:
    def test_create(self):
        res_post = post_submenu()
        res_post_body = res_post["res"].json()
        assert res_post["res"].status_code == 201
        assert res_post_body["title"] == "My submenu 1"
        assert res_post_body["description"] == "My submenu description 1"

    def test_read(self):
        res_post = post_submenu()
        menu_id = res_post["menu_id"]
        submenu_id = res_post["res"].json()["id"]
        res_get = get_submenu(menu_id, submenu_id)
        res_get_body = res_get.json()
        assert res_get.status_code == 200
        assert res_get_body["title"] == "My submenu 1"
        assert res_get_body["description"] == "My submenu description 1"
        res_get_2 = get_submenu_menu(menu_id)
        assert res_get_2.status_code == 200
        assert res_get_2.json() != []

    def test_update(self):
        res_post = post_submenu()
        menu_id = res_post["menu_id"]
        submenu_id = res_post["res"].json()["id"]
        res_update = patch_submenu(menu_id, submenu_id)
        res_update_body = res_update.json()
        assert res_update.status_code == 200
        assert res_update_body["title"] == "My updated submenu 1"
        assert res_update_body["description"] == "My updated submenu description 1"

    def test_delete(self):
        res_post = post_submenu()
        menu_id = res_post["menu_id"]
        submenu_id = res_post["res"].json()["id"]
        res_get = get_submenu(menu_id, submenu_id)
        assert res_get.status_code == 200
        res_delete = delete_submenu(menu_id, submenu_id)
        assert res_delete.status_code == 200
        assert get_submenu(menu_id, submenu_id).status_code == 404