import pytest
from selenium import webdriver
import datetime;
import uuid
import time;
import reporting.CuriosityReporter
import reporting.TestPathRun
import reporting.TestPathRunStep

id = str(uuid.uuid4());

@pytest.fixture(scope="class")
def driver(request):
    print("initiating chrome driver")
	
    driver = webdriver.Chrome() 
	
    yield driver
    
    driver.close()
	
@pytest.fixture(scope="class")
def pathrun(request):
	pathrun = reporting.TestPathRun.TestPathRun()
	pathrun.runTimeStamp = int(time.mktime(datetime.datetime.utcnow().timetuple()) * 1000);
	pathrun.runColId = id;
	pathrun.vipRunId = id;

	yield pathrun

	reporter = reporting.CuriosityReporter.CuriosityReporter()
	reporter.postRunResults(pathrun);