import allure
import requests
from test_api_asklepkovich.endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):
    @allure.step('Object get')
    def get_object(self, post_id):
        self.response = requests.get(
            f'{self.url}/{post_id}'
        )
        self.json = self.response.json()
        return self.response
