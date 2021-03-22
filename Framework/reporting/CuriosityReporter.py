import json
import requests 

class CuriosityReporter(object):
	def __init__(self):
		self.url = "http://localhost:8080";
		self.apiKey = "PtYawE1NRkqBmf4dy3tY6kJW5";
		
	def postRunResults(self, run):
		headers = {};
		parameters = {};
		body = json.dumps(run, default=lambda x: x.__dict__);
		print(body)

		headers["Content-Type"]= "application/json";

		response = requests.post(self.url + "/api/apikey/" + self.apiKey + "/model/version/profile/testcollection/testsuite/testpath/run", headers=headers, data=body, params=parameters)
		response_body = response.json();
		print(response)
