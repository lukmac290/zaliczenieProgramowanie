from locust import HttpUser, task


class PerformanceTests(HttpUser):

    @task
    def prime_number(self):
        self.client.get(url='http://127.0.0.1:8000/project/primeverif/11')


