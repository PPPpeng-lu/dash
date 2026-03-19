import yaml
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ElementLocator:
    def __init__(self, driver, config_path='elements.yaml'):
        self.driver = driver
        self.platform = driver.capabilities['platformName'].lower()
        with open(config_path, 'r', encoding='utf-8') as f:
            self.element_config = yaml.safe_load(f)

    def _map_locator(self, locator_type):
        """Map config locator types to AppiumBy"""
        mapping = {
            'android-uiautomator': AppiumBy.ANDROID_UIAUTOMATOR,
            'accessibility id': AppiumBy.ACCESSIBILITY_ID,
            'ios predicate string': AppiumBy.IOS_PREDICATE
        }
        return mapping.get(locator_type, locator_type)

    def tap_submit(self):
        config = self.element_config['submit_button'][self.platform]
        for locator_type, value in config:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.element_to_be_clickable((self._map_locator(locator_type), value))
                )
                element.click()
                return True
            except:
                continue
        return False
