import pytest
import allure
from test_api_asklepkovich.exp_result.json_schema import json_schema_update, json_schema_update_patch


TEST_DATA = [
    {
        "name": "Apple MacBook Pro",
        "data": {
            "year": 2018,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Apple MacBook Pro 100",
        "data": {
            "year": 2019,
            "price": 1850.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "2 TB"
        }
    }
]
TEST_DATA_UPDATE = [
    {
        "name": "Apple MacBook Pro",
        "data": {
            "year": 2024,
            "price": 1999.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    },
    {"name": "Apple MacBook"}
]


@allure.feature('Test api')
@allure.story('Test post object')
@allure.title('Test post object')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_create(create_post_endpoint, data, delete_post):
    response_id = create_post_endpoint.new_post(payload=data).json()['id']
    create_post_endpoint.check_status_is_200()
    create_post_endpoint.check_response_name_is_correct(data['name'])
    create_post_endpoint.check_jsonschema()
    delete_post.delete_post(response_id)


@allure.feature('Test api')
@allure.story('Test update object')
@allure.title('Test put update object')
@allure.severity(allure.severity_level.NORMAL)
def test_update_post(update_post_endpoint, post_create_and_delete):
    update_post_endpoint.update_obj(post_create_and_delete[0], TEST_DATA_UPDATE[0])
    update_post_endpoint.check_status_is_200()
    update_post_endpoint.check_response_name_is_correct(TEST_DATA_UPDATE[0]['name'])
    update_post_endpoint.check_data_response(TEST_DATA_UPDATE[0]['data'])
    update_post_endpoint.check_jsonschema(json_schema_update)


@allure.feature('Test api')
@allure.story('Test update object')
@allure.title('Test patch update object')
@allure.severity(allure.severity_level.NORMAL)
def test_update_patch(update_post_endpoint, post_create_and_delete):
    update_post_endpoint.update_obj(post_create_and_delete[0], TEST_DATA_UPDATE[1], method='patch')
    update_post_endpoint.check_status_is_200()
    update_post_endpoint.check_response_name_is_correct(TEST_DATA_UPDATE[1]['name'])
    update_post_endpoint.check_data_response(post_create_and_delete[1]['data'])
    update_post_endpoint.check_jsonschema(json_schema_update_patch)


@allure.feature('Test api')
@allure.story('Test delete object')
@allure.title('Test delete object')
@allure.severity(allure.severity_level.NORMAL)
def test_delete_obj(delete_post, only_post_create):
    delete_post.delete_post(only_post_create)
    delete_post.check_data_response(only_post_create)
    delete_post.check_status_is_200()
    delete_post.get_object(only_post_create)
    delete_post.check_status_is_404()
