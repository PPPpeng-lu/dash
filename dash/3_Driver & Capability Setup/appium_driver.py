import pytest
import yaml
from appium import webdriver
import os


@pytest.fixture(scope="session")
def appium_driver():
    driver = None
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'capabilities.yaml')
        with open(config_path, 'r') as f:
            caps = yaml.safe_load(f)
        driver = webdriver.Remote('http://localhost:4723', caps)
        driver.implicitly_wait(5)
        yield driver
    except Exception as e:
        pytest.fail(f"启动Appium driver失败: {e}")
        yield None
    finally:
        # 4. 测试结束后退出driver
        if driver:
            driver.quit()