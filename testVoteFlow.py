from locust import HttpLocust, TaskSet, task
from locust.exception import StopLocust
import random

class MyTaskSet(TaskSet):
	
	table_numbers = [1,2,3,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21]
	
	@task
	def my_task(self):
		print("executing my_task")
		self.homepage()
		token = self.login()
		self.getQuestion(token)
		self.getImage()
		self.submitVote(token)
		
	def homepage(self):
		print("visting homepage")
		response=self.client.get("/")
		print(response.status_code)
	
	def login(self):
		print("executing login")
		table_num = MyTaskSet.table_numbers[random.randint(0, len(MyTaskSet.table_numbers)-1)]
		print("table_num " + str(table_num))
		self.client.headers['Content-Type'] = "application/json; charset=utf-8"
		response = self.client.post("service/validate_code_by_limit", json={
			u'event_id': 1,
			u'table_number': table_num
		})
		json_response_dict = response.json()
		print(json_response_dict)
		if json_response_dict['success']==False:
			raise StopLocust()
		token = json_response_dict['token']
		print(token)
		
		return token

	def getQuestion(self, token):
		print("executing getQuestion")
		self.client.headers['Content-Type'] = "application/json; charset=utf-8"
		response = self.client.get("service/get_questions_options?event_id=1&token="+token)
		json_response_dict = response.json()
		
	def getImage(self):
		print("executing getImage")
		self.client.headers['Content-Type'] = "application/json; charset=utf-8"
		response = self.client.get("images/team-photo/HKO.jpg")
		
	def submitVote(self, token):
		print("executing submitVote")
		self.client.headers['Content-Type'] = "application/json; charset=utf-8"
		rtn=random.sample(range(1,8),5)
		response = self.client.post("service/submit_vote", json={
			u'token': token,
			u'votes': [{"question_id":i, "option_id": rtn[i-1]} for i in range (1,6)]
		})
		
		json_response_dict = response.json()
		message = json_response_dict['message']
		print(message)


class WebsiteUser(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000