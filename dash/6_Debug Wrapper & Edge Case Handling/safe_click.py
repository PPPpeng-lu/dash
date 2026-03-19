def safe_click(element, driver):
    try:
        element.click()
        logger.info("点击成功")
        return True
    except Exception as e:
        logger.error(f"点击失败: {e}")
        logger.error(f"元素文本: {element.text}")
        logger.error(f"元素content-desc: {element.get_attribute('content-desc')}")
        logger.error(f"元素位置: {element.location}")
        logger.error(f"元素大小: {element.size}")