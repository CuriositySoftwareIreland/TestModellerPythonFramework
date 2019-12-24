from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

""" http://modeller.dev.testinsights.io/app/#!/module-collection/guid/3d7c6b10-c1b2-495f-b124-591862a95ae8 """
class Create_New_Customer_Account(object):
    
    First_NameElem = (By.XPATH, "//INPUT[@name='firstname']")

    Last_NameElem = (By.XPATH, "//INPUT[@name='lastname']")

    EmailElem = (By.ID, "email_address")

    PasswordElem = (By.ID, "password")

    Confirm_PasswordElem = (By.XPATH, "//INPUT[@name='password_confirmation']")

    Create_an_AccountElem = (By.XPATH, "/html/body/div[1]/main/div[3]/div/form/div/div[1]/button/span")
    
    def __init__(self, driver):
        self.driver = driver
	
    
    def GoToUrl(self):
        self.driver.get('https://magento.nublue.co.uk/customer/account/create/')
    
    def AssertUrl(self):
        assert self.driver.current_url == 'https://magento.nublue.co.uk/customer/account/create/'

    def Enter_First_Name(self, text):
        self.driver.find_element(self.First_NameElem[0], self.First_NameElem[1]).send_keys(text)

    def Enter_Last_Name(self, text):
        self.driver.find_element(self.Last_NameElem[0], self.Last_NameElem[1]).send_keys(text)

    def Enter_Email(self, text):
        self.driver.find_element(self.EmailElem[0], self.EmailElem[1]).send_keys(text)

    def Enter_Password(self, text):
        self.driver.find_element(self.PasswordElem[0], self.PasswordElem[1]).send_keys(text)

    def Enter_Confirm_Password(self, text):
        self.driver.find_element(self.Confirm_PasswordElem[0], self.Confirm_PasswordElem[1]).send_keys(text)

    def Click_Create_an_Account(self):
        self.driver.find_element(self.Create_an_AccountElem[0], self.Create_an_AccountElem[1]).click()
