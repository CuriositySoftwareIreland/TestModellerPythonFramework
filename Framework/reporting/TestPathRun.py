import reporting.TestPathRunStep

class TestPathRun(object):
	def __init__(self):
		self.testStatus = "Failed";
		self.message = "";
		self.vipRunId = None;
		self.lastRunGuid = None;
		self.jobId = None;
		self.testPathGuid = None;
		self.testPathRunSteps = [];
	
	def passTest(self, message):
		self.message = message;
		self.testStatus = "Passed";
	
	def addPassStep(self, message):
		runStep = reporting.TestPathRunStep.TestPathRunStep();
		runStep.stepName = message;
		self.getTestPathRunSteps().append(runStep);

	def addFailStep(self, message):
		runStep = reporting.TestPathRunStep.TestPathRunStep();
		runStep.stepName = message;
		runStep.testStatus = "Failed";		
		self.getTestPathRunSteps().append(runStep);
	
	def getTestStatus(self):
		return self.testStatus
		
	def setTestStatus(self, value):
		self.testStatus = value

	def getMessage(self):
		return self.message
		
	def setMessage(self, message):
		self.message = message
		
	def getVipRunId(self):
		return self.vipRunId
		
	def setVipRunId(self, vipRunId):
		self.vipRunId = vipRunId

	def getLastRunGuid(self):
		return self.lastRunGuid
		
	def setLastRunGuid(self, lastRunGuid):
		self.lastRunGuid = lastRunGuid

	def getRunTimeStamp(self):
		return self.runTimeStamp
		
	def setRunTimeStamp(self, runTimeStamp):
		self.runTimeStamp = runTimeStamp

	def getRunColId(self):
		return self.runColId
		
	def setRunColId(self, runColId):
		self.runColId = runColId

	def getJobId(self):
		return self.jobId
		
	def setJobId(self, jobId):
		self.jobId = jobId

	def getTestPathGuid(self):
		return self.testPathGuid
		
	def setTestPathGuid(self, testPathGuid):
		self.testPathGuid = testPathGuid

	def getRunTime(self):
		return self.runTime
		
	def setRunTime(self, runTime):
		self.runTime = runTime

	def getRunSource(self):
		return self.runSource
		
	def setRunSource(self, runSource):
		self.runSource = runSource

	def getTestPathRunSteps(self):
		return self.testPathRunSteps
		
	def setTestPathRunSteps(self, testPathRunSteps):
		self.testPathRunSteps = testPathRunSteps
