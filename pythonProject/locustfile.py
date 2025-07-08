from locust import TaskSet, HttpUser, task, run_single_user,between
class UserBehavior(TaskSet):
    def on_start(self):
        print('开始的时候执行')
    def on_stop(self):
        print("结束的时候执行")

    @task()
    def baidu(self):
        self.client.get("/")
class WebsiterUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1,2)
    host = "https://baidu.com"