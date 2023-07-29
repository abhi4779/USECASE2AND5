from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutomationPandaPage:
    def __init__(self, driver):
        self.driver = driver

    speakinglink="/html/body/div[1]/header/div/nav/div/ul/li[4]"
    keynoteaddress="//*[@id='post-10589']/div/h2[1]"
    conferencetalks="//*[@id='conferences']"

    def click_speaking(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.speakinglink)))
        speaking = self.driver.find_element(By.XPATH, self.speakinglink)
        speaking.click()

    def iskeynote_address_displayed(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.keynoteaddress)))
        keynote_displayed = self.driver.find_element(By.XPATH, self.keynoteaddress).is_displayed()
        return keynote_displayed

    def get_keynote_addresses_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.keynoteaddress)))
        keynote_text = self.driver.find_element(By.XPATH, self.keynoteaddress).text
        return keynote_text

    def isconference_talks_displayed(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.keynoteaddress)))
        conference_displayed = self.driver.find_element(By.XPATH, self.keynoteaddress).is_displayed()
        return conference_displayed

    def get_conference_talks_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.conferencetalks)))
        conference_text = self.driver.find_element(By.XPATH, self.conferencetalks).text
        return conference_text

