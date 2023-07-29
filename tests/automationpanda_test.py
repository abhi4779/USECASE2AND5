import pytest
from selenium import webdriver
from pages import AutomationPandaPage

@pytest.fixture(scope="module")
def driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/")
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver_init")
class TestAutomationPanda:
    def test_automation_panda_scenario_1(self,driver_init):
        page = AutomationPandaPage(driver_init)
        page.click_speaking()
        expected_title="Speaking | Automation Panda"
        actual_title=driver_init.title
        assert actual_title == expected_title, f"Page title is {actual_title}, but expected {expected_title}"

    def test_automation_panda_scenario_2(self,driver_init):
        page = AutomationPandaPage(driver_init)

        assert page.iskeynote_address_displayed(),"KeyNote address not displayed in the page"
        if(page.iskeynote_address_displayed()):
            expected_text="Keynote Addresses"
            actual_text=page.get_keynote_addresses_text()
            assert actual_text == expected_text , f"Actual message is {actual_text}, but expected {expected_text}"

        assert page.isconference_talks_displayed(),"Conference not displayed in the page"
        if(page.isconference_talks_displayed()):
            expected_text="Conference Talks"
            actual_text=page.get_conference_talks_text()
            assert actual_text == expected_text , f"Actual message is {actual_text}, but expected {expected_text}"
