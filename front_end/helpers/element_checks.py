from front_end.helpers.ExpectedConditionWait import ExpectedConditionWait


def check_content(css_selector, expected_content):
    element = ExpectedConditionWait.wait_until_element_visible(css_selector)
    assert element.text == expected_content
