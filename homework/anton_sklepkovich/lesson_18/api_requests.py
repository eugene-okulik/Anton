import requests
import jsonschema
import json_schema
import copy
import deepmerge
from name_error import status_is_not_200, status_is_not_404


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


def post_create_one(url=BASE_URL, body=BASE_BODY, headers=BASE_HEADERS):
    response = requests.post(
        url,
        json=body,
        headers=headers
    )
    return response


def delete_one(id_delete):
    response = requests.delete(
        BASE_URL + '/' + id_delete
    )
    return response


def post_create():
    response = post_create_one()
    print(f'Status code response = {response.status_code}')
    assert response.status_code == 200, status_is_not_200
    print(f'Response body = {response.json()}')
    jsonschema.validate(response.json(), json_schema.json_schema_create)
    assert BASE_BODY['name'] == response.json()['name'], (f"The Name doesn't mismatch\n"
                                                          f'act name = {response.json()["name"]}\n'
                                                          f'exp name = {BASE_BODY["name"]}\n')


def get_obj(id_obj):
    url = BASE_URL + '/' + id_obj
    return requests.get(url)


def update_obj():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2020,
            "price": 2049.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "2 TB",
            "color": "silver"
        }
    }
    id_resp = post_create_one().json()['id']
    response = requests.put(
        BASE_URL + '/' + id_resp,
        json=body,
        headers=BASE_HEADERS
    )
    print(f'Status code response = {response.status_code}')
    assert response.status_code == 200, status_is_not_200
    response = response.json()
    print(f'Response body = {response}')
    assert id_resp == response['id'], (f"The ID doesn't mismatch\n "
                                       f"act id = {response['id']}\n "
                                       f"exp id = {id_resp}\n")
    assert response['data'] == body['data'], (f"The Data doesn't mismatch\n "
                                              f"act data = {response['data']}\n "
                                              f"exp data = {body['data']}\n")
    jsonschema.validate(response, json_schema.json_schema_update)
    delete_one(id_resp)


def update_patch():
    body = {
        "name": "Apple MacBook Pro 163",
        "data": {
            "CPU model": "Intel Core i00"
        }
    }
    body_for_merge = copy.deepcopy(BASE_BODY)
    new_body = deepmerge.always_merger.merge(body_for_merge, body)
    id_resp = post_create_one().json()['id']
    response = requests.patch(
        BASE_URL + '/' + id_resp,
        json=new_body,
        headers=BASE_HEADERS
    )
    print(f'Status code response = {response.status_code}')
    assert response.status_code == 200, status_is_not_200
    response = response.json()
    jsonschema.validate(response, json_schema.json_schema_update_patch)
    print(f'response body = {response}')
    assert response['data'] == new_body['data'], (f"The Data doesn't mismatch\n "
                                                  f"act data = {response['data']}\n "
                                                  f"exp data = {new_body['data']}\n")
    assert response['name'] == new_body['name'], (f"The Name doesn't mismatch\n "
                                                  f"act name = {response['name']}\n "
                                                  f"exp name = {new_body['name']}\n")
    delete_one(id_resp)


def delete_obj():
    id_resp = post_create_one().json()['id']
    response = delete_one(id_resp)
    get_obj_response = get_obj(id_resp)
    print(response.status_code)
    assert get_obj_response.status_code == 404, status_is_not_404


post_create()
update_obj()
update_patch()
delete_obj()
