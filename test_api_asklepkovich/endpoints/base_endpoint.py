import allure
import jsonschema
from test_api_asklepkovich.exp_result.json_schema import json_schema_create


def text_error(act, exp, message):
    return (f"{message}\n"
            f"act_result = {act}\n"
            f"exp_result = {exp}\n")


class BaseEndpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {"content-type": "application/json"}
    post_id = None

    @allure.step('Check that response status is 200')
    def check_status_is_200(self):
        exp = 200
        assert self.response.status_code == exp, text_error(
            self.response.status_code, exp, f"Error status code isn't {exp}"
        )

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name, text_error(
            self.json['name'], name, "--Error The Name doesn't mismatch"
        )

    @allure.step('Check json schema response')
    def check_jsonschema(self, schema=json_schema_create):
        jsonschema.validate(self.json, schema)

    @allure.step('Check response body>data')
    def check_data_response(self, data):
        assert self.json['data'] == data, text_error(self.json['data'], data, "The Data doesn't mismatch")

    @allure.step('Check response code after delete')
    def check_status_is_404(self):
        exp = 404
        assert self.response.status_code == exp, text_error(
            self.response.status_code, exp, f"Error status code isn't {exp}"
        )
