import requests
from jsonschema import validate

from tests.helpers import get_schema

URL = 'https://reqres.in/api'


def test_login_user():
    url = URL + "/login"
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url=url, data=body)

    assert response.status_code == 200
    validate(response.json(), get_schema("success_login_user.json"))


def test_cant_login_user():
    url = URL + "/login"
    body = {
        "email": "test_email",
        "password": "test_password"
    }

    response = requests.post(url=url, data=body)

    assert response.status_code == 400
    validate(response.json(), get_schema("failure_login_user.json"))
    assert response.json()["error"] == "user not found"


def test_delete_user():
    user_id = 3
    url = URL + f"/users/{user_id}"

    response = requests.delete(url=url)

    assert response.status_code == 204


def test_cant_get_user():
    user_id = 23
    url = URL + f"/users/{user_id}"

    response = requests.get(url=url)

    assert response.status_code == 404
    validate(response.json(), get_schema("failure_get_user.json"))
    assert response.json() == {}


def test_update_user():
    user_id = 3
    body = {
        "name": "test_name",
        "job": "test_job"
    }
    url = URL + f"/users/{user_id}"

    response = requests.put(url=url, data=body)

    assert response.status_code == 200
    validate(response.json(), get_schema("success_update_user.json"))
    assert response.json()["job"] == "test_job"


def test_create_user():
    body = {
        "name": "test_name",
        "job": "test_job"
    }
    url = URL + "/users"

    response = requests.post(url=url, data=body)

    assert response.status_code == 201
    validate(response.json(), get_schema("success_create_user.json"))
    assert response.json()["name"] == "test_name"


def test_register_user():
    url = URL + "/register"
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url=url, data=body)

    assert response.status_code == 200
    validate(response.json(), get_schema("success_register_user.json"))


def test_cant_register_user():
    url = URL + "/register"
    body = {
        "password": "test_password"
    }

    response = requests.post(url=url, data=body)

    assert response.status_code == 400
    validate(response.json(), get_schema("failure_register_user.json"))
    assert response.json()["error"] == "Missing email or username"


def test_get_user():
    user_id = 3
    url = URL + f"/users/{user_id}"

    response = requests.get(url)

    assert response.status_code == 200
    validate(response.json(), get_schema("success_get_user.json"))
    assert response.json()["data"]["id"] == user_id


def test_get_resource():
    resource_id = 23
    url = URL + f"/unknown/{resource_id}"

    response = requests.get(url=url)

    assert response.status_code == 404
    validate(response.json(), get_schema("failure_get_resource.json"))
    assert response.json() == {}
