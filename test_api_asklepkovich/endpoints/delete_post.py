import allure
import requests
from test_api_asklepkovich.endpoints.get_object import GetObject
from test_api_asklepkovich.endpoints.base_endpoint import text_error


class DeletePost(GetObject):
    @allure.step('Delete post')
    def delete_post(self, post_id=None):
        post_id = post_id if post_id else self.post_id
        self.response = requests.delete(
            f'{self.url}/{post_id}'
        )
        self.json = self.response.json()
        print(self.json)
        return self.response

    @allure.step('Check response body after delete')
    def check_data_response(self, post_id):
        exp_data = {'message': f'Object with id = {post_id} has been deleted.'}
        assert self.json == exp_data, text_error(self.json, exp_data, 'Error response body after delete')
