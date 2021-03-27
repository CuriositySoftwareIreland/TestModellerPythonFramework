class AllocationResultLookup(object):
	def __init__(self, poolName, suiteName, testName):
		self.pool = poolName;
		self.suite = suiteName;
		self.testName = testName;
 
	def setPool(self, pool):
		self.pool = pool
	
	def getPool(self):
		return self.pool
		
	def setSuite(self, suite):
		self.suite = suite
	
	def getSuite(self):
		return self.suite
		
	def setTestName(self, testName):
		self.testName = testName
	
	def getTestName(self):
		return self.testName
		
	