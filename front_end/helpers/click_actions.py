from front_end.helpers.ExpectedConditionWait import ExpectedConditionWait


def click_element(css_selector):
    element = ExpectedConditionWait.wait_until_element_clickable(css_selector)
    element.click()

