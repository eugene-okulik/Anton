import pytest
import random
from test_api_asklepkovich.endpoints.create_post import CreatePost
from test_api_asklepkovich.endpoints.update_obj import UpdatePost
from test_api_asklepkovich.endpoints.delete_post import DeletePost
from test_api_asklepkovich.endpoints.get_object import GetObject


@pytest.fixture(scope='session')
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def delete_post():
    return DeletePost()


@pytest.fixture()
def get_object():
    return GetObject()


@pytest.fixture()
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


@pytest.fixture()
def post_create_and_delete(create_post_endpoint, delete_post, generate_body):
    response = create_post_endpoint.new_post(generate_body)
    post_id = response.json()['id']
    response_data = {'data': response.json()['data']}
    yield post_id, response_data
    resp = delete_post.delete_post(post_id)
    print(f'\nId has been deleted {resp.json()}')


@pytest.fixture()
def only_post_create(create_post_endpoint, generate_body):
    response = create_post_endpoint.new_post(generate_body)
    return response.json()['id']
