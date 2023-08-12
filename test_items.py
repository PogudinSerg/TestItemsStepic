import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_appeared_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        result = True
    except NoSuchElementException:
        result = False
    assert result is True, "Add to basket button didn't appeared"
