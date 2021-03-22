class TestPathRunStep(object):
	def __init__(self):
		self.id = None;
		self.stepName = "";
		self.stepDescription = "";
		self.testStatus = "Passed";
		self.message = None;
		self.image = None;
		self.nodeGuid = None;

	def getId(self):
		return self.id
		
	def setId(self, id):
		self.id = id

	def getStepName(self):
		return self.stepName
		
	def setStepName(self, stepName):
		self.stepName = stepName

	def getStepDescription(self):
		return self.stepDescription
		
	def setStepDescription(self, stepDescription):
		self.stepDescription = stepDescription

	def getTestStatus(self):
		return self.testStatus
		
	def setTestStatus(self, testStatus):
		self.testStatus = testStatus
		
	def getMessage(self):
		return self.message
		
	def setMessage(self, message):
		self.message = message
		
	def getImage(self):
		return self.image
		
	def setImage(self, image):
		self.image = image
		
	def getNodeGuid(self):
		return self.nodeGuid
		
	def setNodeGuid(self, nodeGuid):
		self.nodeGuid = nodeGuid