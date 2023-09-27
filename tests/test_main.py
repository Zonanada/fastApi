from ...ylab_2.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def post_menu():
    return client.post('api/v1/menus', json={"title": "My menu 1", "description": "My menu description 1"})


def get_all_menu():
    return client.get('api/v1/menus')


def get_menu(menu_id):
    return client.get(f'api/v1/menus/{menu_id}')


def patch_menu(menu_id):
    return client.patch(f"api/v1/menus/{menu_id}", json={"title": "My update menu 1", "description": "My update menu description 1"})


def delete_menu(menu_id):
    return client.delete(f"api/v1/menus/{menu_id}")

def post_submenu():
    menu_id = post_menu().json()["id"]
    return {"menu_id": menu_id, "res": client.post(f'api/v1/menus/{menu_id}/submenus', json={"title": "My submenu 1", "description": "My submenu description 1"})}


def get_submenu(menu_id, submenu_id):
    return client.get(f'api/v1/menus/{menu_id}/submenus/{submenu_id}')


def get_submenu_menu(menu_id):
    return client.get(f'api/v1/menus/{menu_id}/submenus')


def patch_submenu(menu_id, submenu_id):
    return client.patch(f'api/v1/menus/{menu_id}/submenus/{submenu_id}', json={"title": "My updated submenu 1", "description": "My updated submenu description 1"})


def delete_submenu(menu_id, submenu_id):
    return client.delete(f'api/v1/menus/{menu_id}/submenus/{submenu_id}')

def post_dishes():
    submenu = post_submenu()
    menu_id = submenu["menu_id"]
    submenu_id = submenu["res"].json()["id"]
    return {"menu_id": menu_id, "submenu_id": submenu_id, "res": client.post(f'api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', json={"title": "My dish 1", "description": "My dish description 1", "price": "12.50"})}


def get_dishes(menu_id, submenu_id, dishes_id):
    return client.get(f'api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dishes_id}')


def get_dishes_submenu(menu_id, submenu_id):
    return client.get(f'api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes')


def patch_dishes(menu_id, submenu_id, dishes_id):
    return client.patch(f'api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dishes_id}', json={"title": "My updated dish 1", "description": "My updated dish description 1", "price": "14.50"})


def delete_dishes(menu_id, submenu_id, dishes_id):
    return client.delete(f'api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dishes_id}')


class TestClassMenu:
    def test_create(self):
        res_post = post_menu()
        res_post_body = res_post.json()
        assert res_post.status_code == 201
        assert res_post_body["title"] == "My menu 1"
        assert res_post_body["description"] == "My menu description 1"

    def test_read(self):
        res_post = post_menu()
        res_get = get_menu(res_post.json()["id"])
        res_get_body = res_get.json()
        assert res_get.status_code == 200
        assert res_get_body["title"] == "My menu 1"
        assert res_get_body["description"] == "My menu description 1"
        res_get_2 = get_all_menu()
        assert res_get_2.status_code == 200
        assert res_get_2.json() != []

    def test_update(self):
        res_post = post_menu()
        res_update = patch_menu(res_post.json()["id"])
        res_update_body = res_update.json()
        assert res_update.status_code == 200
        assert res_update_body["title"] == "My update menu 1"
        assert res_update_body["description"] == "My update menu description 1"

    def test_delete(self):
        res_post = post_menu()
        res_get = get_menu(res_post.json()["id"])
        assert res_get.status_code == 200
        res_delete = delete_menu(res_post.json()["id"])
        assert res_delete.status_code == 200
        assert get_menu(res_post.json()["id"]).status_code == 404


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
