class AllocationType(object):
	def __init__(self, poolName, suiteName, allocationTestName):
		self.poolName = poolName;
		self.suiteName = suiteName;
		self.allocationTestName = allocationTestName;
 
	def setPoolName(self, poolName):
		self.poolName = poolName
	
	def getPoolName(self):
		return self.poolName
		
	def setSuiteName(self, suiteName):
		self.suiteName = suiteName
	
	def getSuiteName(self):
		return self.suiteName
		
	def setAllocationTestName(self, allocationTestName):
		self.allocationTestName = allocationTestName
	
	def getAllocationTestName(self):
		return self.allocationTestName
		
	