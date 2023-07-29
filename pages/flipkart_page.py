from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartPage:
    def __init__(self, driver):
        self.driver = driver

    login_button="//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[2]/div[2]/div/div"
    phone_text="(//input[contains(@type,'text')])[2]"
    requestotp="//button[contains(text(),'Request OTP')]"

    def click_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.login_button)))
        login_element = self.driver.find_element(By.XPATH,self.login_button)
        login_element.click()

    def enter_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.phone_text)))
        phone_element = self.driver.find_element(By.XPATH,self.phone_text)
        phone_element.send_keys(phone_number)

    def click_request_otp_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.requestotp)))
        otp_element = self.driver.find_element(By.XPATH, self.requestotp)
        otp_element.click()

    def getphone_number(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,self.phone_text)))
        phone_text = self.driver.find_element(By.XPATH,self.phone_text).get_attribute("value")
        return phone_text

    def getmessage(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]")))
        message = self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/div/div[1]").text
        return message
