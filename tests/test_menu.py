import pytest
import requests


def post_menu():
    return requests.post('http://localhost:8000/api/v1/menus', json={"title": "My menu 1", "description": "My menu description 1"})


def get_all_menu():
    return requests.get('http://localhost:8000/api/v1/menus')


def get_menu(menu_id):
    return requests.get(f'http://localhost:8000/api/v1/menus/{menu_id}')


def patch_menu(menu_id):
    return requests.patch(f"http://localhost:8000/api/v1/menus/{menu_id}", json={"title": "My update menu 1", "description": "My update menu description 1"})


def delete_menu(menu_id):
    return requests.delete(f"http://localhost:8000/api/v1/menus/{menu_id}")


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