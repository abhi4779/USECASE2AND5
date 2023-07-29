import pytest
from selenium import webdriver
from pages.flipkart_page import FlipkartPage

@pytest.fixture(scope="module")
def driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver_init")
class TestFlipkart:
    def test_flipkart_scenario_1(self,driver_init):
        page = FlipkartPage(driver_init)
        page.click_login_button()
        expected_title = "Online Shopping India | Buy Mobiles, Electronics, Appliances, Clothing and More Online at Flipkart.com"
        actual_title = driver_init.title
        assert actual_title == expected_title, f"Page title is {actual_title}, but expected {expected_title}"


    def test_flipkart_scenario_2(self,driver_init):
        page = FlipkartPage(driver_init)
        page.enter_phone_number("6303576265")
        phone_text = page.getphone_number()
        assert phone_text == "6303576265",f"Mobile Number is {phone_text}, but expected 6303576265"

    def test_flipkart_scenario_3(self,driver_init):
        page = FlipkartPage(driver_init)
        page.click_request_otp_button()
        expectedmessage="Please enter the OTP sent to"
        actualmessage=page.getmessage()
        assert actualmessage == expectedmessage,f"Mobile Number is {actualmessage}, but expected {expectedmessage}"


