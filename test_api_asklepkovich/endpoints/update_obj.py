import allure
import requests
from test_api_asklepkovich.endpoints.base_endpoint import BaseEndpoint


class UpdatePost(BaseEndpoint):
    @allure.step('Request put endpoint /objects/id')
    def update_obj(self, post_id, payload, method='put', headers=None):
        headers = headers if headers else self.headers
        match method:
            case 'put':
                self.response = requests.put(
                    f'{self.url}/{post_id}',
                    json=payload,
                    headers=headers
                )
            case 'patch':
                self.response = requests.patch(
                    f'{self.url}/{post_id}',
                    json=payload,
                    headers=headers
                )
        self.json = self.response.json()
        return self.response
