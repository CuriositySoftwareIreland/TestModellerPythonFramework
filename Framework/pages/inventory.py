from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# http://modeller.dev.testinsights.io/app/#!/module-collection/guid/31dc8bae-3a2e-4ca9-8688-a8dc8ed2c764
class Home_BBC_News(object):
    
    Bailey_named_as_new_Bank_of_England_governorElem = (By.XPATH, "/html/body/div[7]/div/div[4]/div[2]/div[4]/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/a")

    MPs_debate_Johnsons_Brexit_bill_ahead_of_voteElem = (By.XPATH, "/html/body/div[7]/div/div[4]/div[2]/div[4]/div/div/div/div[1]/div/div[2]/div/div[2]/div/a")

    Video_4_minutes_12_secondsI_want_my_chemo_to_help_others_touched_by_cancerElem = (By.XPATH, "/html/body/div[7]/div/div[4]/div[2]/div[4]/div/div/div/div[2]/div/div[1]/div/div[2]/div/a")
    
    def __init__(self, driver):
        self.driver = driver
    
    def GoToUrl(self):
        self.driver.get('https://www.bbc.co.uk/news')

    def AssertURL(self):
        assert self.driver.current_url == 'https://www.bbc.co.uk/news'

    def Click_Bailey_named_as_new_Bank_of_England_governor(self):
        self.driver.find_element(self.Bailey_named_as_new_Bank_of_England_governorElem[0], self.Bailey_named_as_new_Bank_of_England_governorElem[1]).click()

    def Click_MPs_debate_Johnsons_Brexit_bill_ahead_of_vote(self):
        self.driver.find_element(self.MPs_debate_Johnsons_Brexit_bill_ahead_of_voteElem[0], self.MPs_debate_Johnsons_Brexit_bill_ahead_of_voteElem[1]).click()

    def Click_Video_4_minutes_12_secondsI_want_my_chemo_to_help_others_touched_by_cancer(self):
        self.driver.find_element(self.Video_4_minutes_12_secondsI_want_my_chemo_to_help_others_touched_by_cancerElem[0], self.Video_4_minutes_12_secondsI_want_my_chemo_to_help_others_touched_by_cancerElem[1]).click()