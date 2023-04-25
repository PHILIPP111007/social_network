import time
from locust import HttpUser, TaskSet, task, between


class PostSection(TaskSet):

    login_token = ''
    wait_time = between(2, 7)

    @task(2)
    def user(self):
        self.client.get("user/test0")
    
    @task(2)
    def friends(self):
        self.client.get("friends/test0")

    @task(2)
    def dialogs(self):
        self.client.get("dialogs/test0")

    @task(2)
    def news(self):
        self.client.get("news/test0")
    
    @task
    def stop(self):
        self.interrupt()


class ListPostUser(HttpUser):
    wait_time = between(5, 10)
    tasks = [PostSection]
    login_token = ''

    def on_start(self):
        response = self.client.get("login/")
        csrftoken = response.cookies.get_dict()["csrftoken"]

        headers = {
            "X-CSRFToken": csrftoken
        }

        response = self.client.post(
            "login/",
            headers=headers,
            json={"username":"test0", "password":"test12345"}
        )

        self.login_token = response.json()['token']
