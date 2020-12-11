from front_end.helpers.ExpectedConditionWait import ExpectedConditionWait


def send_text(css_selector, content):
    element = ExpectedConditionWait.wait_until_element_visible(css_selector)
    element.send_keys(content)
