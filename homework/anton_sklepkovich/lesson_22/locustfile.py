from locust import task, HttpUser
import random


class BaseUser(HttpUser):
    token = None
    post_id = None

    @task(1)
    def get_all_object(self):
        self.client.get(
            '/objects'
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/objects/{random.randint(1, 5)}'
        )

    @task
    def post_new_object(self):
        data = {
            "name": "Apple MacBook Pro 17",
            "data": {
                "year": 2018,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = self.client.post(
            '/objects',
            json=data,
            headers={"content-type": "application/json"}
        )
        self.post_id = response.json()['id']
