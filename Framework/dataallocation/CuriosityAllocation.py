import json
import requests 
import time
import dataallocation.AllocationResultLookup

class CuriosityAllocation(object):
	def __init__(self):
		self.url = "http://localhost:8080";
		self.apiKey = "PtYawE1NRkqBmf4dy3tY6kJW5";
		self.serverName = "DESKTOP-3FUJ8B9";
		
	def runAllocation(self, poolName, allocationTypes):
		headers = {};
		headers["Content-Type"]= "application/json";

		createAllocBody = json.dumps(allocationTypes, default=lambda x: x.__dict__);
	
		createAllocRsp = requests.post(self.url + "/api/apikey/" + self.apiKey + "/allocation-pool/" + poolName + "/resolve/server/" + self.serverName + "/execute", headers=headers, data=createAllocBody, params={})

		curAllocationJob = createAllocRsp.json();
		
		jobTrackingURL = self.url + "/api/apikey/" + self.apiKey + "/job/" + str(curAllocationJob["id"]);
		print("Tracking URL: " + jobTrackingURL);

		while curAllocationJob["jobState"] != "Complete" and curAllocationJob["jobState"] != "Error":  
		
			createJobProgressRsps = requests.get(jobTrackingURL, headers=headers, params={})

			curAllocationJob = createJobProgressRsps.json();
			
			print("Allocation state: " + curAllocationJob["jobState"])
			
			time.sleep(2)

	def retrieveAllocationResult(self, curPool, curSuite, curTest):
		headers = {};
		headers["Content-Type"]= "application/json";

		mergeMethod = "NoMerge"
	
		dataLookup =  dataallocation.AllocationResultLookup.AllocationResultLookup(curPool, curSuite, curTest);
		
		allocLookupURL = self.url + "/api/apikey/" + self.apiKey + "/allocation-pool/suite/allocated-test/result/value?mergeMethod=" + mergeMethod;

		allocResultRsp = requests.post(allocLookupURL, headers=headers, data= json.dumps(dataLookup, default=lambda x: x.__dict__), params={})
	
		return allocResultRsp.json(); 