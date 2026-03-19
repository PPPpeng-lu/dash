'''
a. 使用谓词定位
'''
element = driver.find_element(AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeCell' AND label CONTAINS 'Order'")


'''
b. a list of order by python
'''
def extract_first_order_number(driver):
    wait = WebDriverWait(driver, 10)
    order_title = wait.until(
        expected_conditions.presence_of_element_located((
            AppiumBy.XPATH,
            "//*[contains(@label, 'Order #') or contains(@value, 'Order #')]"
        ))
    )
    full_text = order_title.text or order_title.get_attribute('label')
    return full_text.group(1)


'''
c.
1、页面没有加载完。处理方法：添加等待时间
2、元素被遮挡，如被弹窗遮挡或不在首页等。处理方法：预埋关闭弹窗的动作和滚动下一页的操作
'''