import pytest
import requests
import jsonschema
import copy
import deepmerge
import random
import allure
from homework.anton_sklepkovich.exp_result import json_schema
from homework.anton_sklepkovich.exp_result.name_error import status_is_not_200, status_is_not_404

BASE_URL = 'https://api.restful-api.dev/objects'
BASE_HEADERS = {"content-type": "application/json"}
BASE_BODY = {
    "name": "Apple MacBook Pro 17",
    "data": {
        "year": 2018,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}


def delete_one(id_delete):
    response = requests.delete(
        BASE_URL + '/' + id_delete
    )
    return response


def generate_body():
    body = {
        "name": f"Apple MacBook Pro {random.randint(1, 20)}",
        "data": {
            "year": random.randint(2000, 2023),
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    return body


def get_obj(id_obj):
    url = BASE_URL + '/' + id_obj
    return requests.get(url)


@pytest.fixture(scope='session')
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def before_after():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def post_create_one(url=BASE_URL, body=BASE_BODY, headers=BASE_HEADERS):
    response = requests.post(
        url,
        json=body,
        headers=headers
    )
    yield response
    resp = requests.delete(
        BASE_URL + '/' + response.json()['id']
    )
    print(f'\nId has been deleted {resp.json()}')


@pytest.fixture()
def post_only_create(url=BASE_URL, body=BASE_BODY, headers=BASE_HEADERS):
    response = requests.post(
        url,
        json=body,
        headers=headers
    )
    return response


@allure.feature('Test api')
@allure.story('Test create object')
@allure.title('Test post create with different body')
# @allure.step('Request post')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.critical
@pytest.mark.parametrize('request_body', [generate_body() for _ in range(3)])
def test_post_create(request_body, start_end, before_after):
    with allure.step('Request post endpoint /objects'):
        response = requests.post(
            BASE_URL,
            json=request_body,
            headers=BASE_HEADERS
        )
    with allure.step('Check response status code = 200'):
        print(f'\nStatus code response = {response.status_code}')
        assert response.status_code == 200, status_is_not_200
    print(f'\nResponse body = {response.json()}')
    with allure.step('Check json schema response'):
        jsonschema.validate(response.json(), json_schema.json_schema_create)
    with allure.step(f'Check response body = {request_body["name"]}'):
        assert request_body['name'] == response.json()['name'], (f"The Name doesn't mismatch\n"
                                                                 f'act name = {response.json()["name"]}\n'
                                                                 f'exp name = {request_body["name"]}\n')
    with allure.step('Delete object'):
        delete_one(response.json()['id'])


@allure.feature('Test api')
@allure.story('Test update object')
@allure.title('Test put update object')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.medium
def test_update_obj(post_create_one, before_after):
    body = generate_body()
    body['data']['color'] = 'silver'
    id_resp = post_create_one.json()['id']
    with allure.step('Request put endpoint /objects/id'):
        response = requests.put(
            BASE_URL + '/' + id_resp,
            json=body,
            headers=BASE_HEADERS
        )
    with allure.step('Check response status code = 200'):
        print(f'Status code response = {response.status_code}')
        assert response.status_code == 200, status_is_not_200
    response = response.json()
    print(f'Response body = {response}')
    with allure.step('Check id response'):
        assert id_resp == response['id'], (f"The ID doesn't mismatch\n "
                                           f"act id = {response['id']}\n "
                                           f"exp id = {id_resp}\n")
    with allure.step(f'Check response body = {body["data"]}'):
        assert response['data'] == body['data'], (f"The Data doesn't mismatch\n "
                                                  f"act data = {response['data']}\n "
                                                  f"exp data = {body['data']}\n")
    with allure.step('Check json schema response'):
        jsonschema.validate(response, json_schema.json_schema_update)


@allure.feature('Test api')
@allure.story('Test update object')
@allure.title('Test patch update object')
@allure.severity(allure.severity_level.NORMAL)
def test_update_patch(post_create_one, before_after):
    body = generate_body()
    body_for_merge = copy.deepcopy(BASE_BODY)
    new_body = deepmerge.always_merger.merge(body_for_merge, body)
    id_resp = post_create_one.json()['id']
    with allure.step('Request patch endpoint /objects/id'):
        response = requests.patch(
            BASE_URL + '/' + id_resp,
            json=new_body,
            headers=BASE_HEADERS
        )
    with allure.step('Check response status code = 200'):
        print(f'Status code response = {response.status_code}')
        assert response.status_code == 200, status_is_not_200
    response = response.json()
    with allure.step('Check json schema response'):
        jsonschema.validate(response, json_schema.json_schema_update_patch)
        print(f'response body = {response}')
    with allure.step(f'Check response body-data = {new_body["data"]}'):
        assert response['data'] == new_body['data'], (f"The Data doesn't mismatch\n "
                                                      f"act data = {response['data']}\n"
                                                      f"exp data = {new_body['data']}\n")
    with allure.step(f'Check response body-name = {new_body["name"]}'):
        assert response['name'] == new_body['name'], (f"The Name doesn't mismatch\n "
                                                      f"act name = {response['name']}\n "
                                                      f"exp name = {new_body['name']}\n")


@allure.feature('Test api')
@allure.story('Test delete object')
@allure.title('Test delete object')
@allure.severity(allure.severity_level.NORMAL)
def test_delete_obj(post_only_create, before_after):
    with allure.step('Create object'):
        id_resp = post_only_create.json()['id']
    with allure.step('Delete object'):
        delete_one(id_resp)
    with allure.step("Request deleted object's id"):
        get_obj_response = get_obj(id_resp)
    with allure.step("Check response 404"):
        assert get_obj_response.status_code == 404, status_is_not_404
