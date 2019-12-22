import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver(request):
    print("initiating chrome driver")
	
    driver = webdriver.Chrome() 
	
    yield driver
    
    driver.close()