from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasePage:
    def wait_for_clickable_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            logger.info(f"元素可点击: {locator}")
            return element
        except TimeoutException:
            logger.error(f"元素不可点击: {locator}")
            raise

    def wait_for_visibility(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            logger.info(f"元素可见: {locator}")
            return element
        except TimeoutException:
            logger.error(f"元素不可见: {locator}")
            raise


class LoginPage(BasePage):
    LOCATORS = {
        'android': {
            'username_field': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example:id/username")'),
            'login_button': (AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiSelector().text("Login").className("android.widget.Button")')
        },
        'ios': {
            'username_field': (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField" AND name == "username"'),
            'login_button': (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND label == "Login"')
        }
    }

    def __init__(self, driver):
        super().__init__(driver)
        platform_name = driver.capabilities.get('platformName', '').lower()
        self.platform = 'android' if 'android' in platform_name else 'ios'
        self.locators = self.LOCATORS[self.platform]

    def enter_username(self, text):
        locator = self.locators.get('username_field')
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def click_login_button(self):
        locator = self.locators.get('login_button')
        element = self.wait_for_clickable_element(locator)
        element.click()
