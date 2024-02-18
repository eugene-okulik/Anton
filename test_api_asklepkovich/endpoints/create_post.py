import requests
import allure
from test_api_asklepkovich.endpoints.base_endpoint import BaseEndpoint


class CreatePost(BaseEndpoint):
    @allure.step('Create new post')
    def new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        print(f'self.post_id={self.post_id}')
        return self.response
