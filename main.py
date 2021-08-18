from selenium import webdriver
import time
import pytest

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(10)
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()

    def test_show_my_pets():
        pytest.driver.find_element_by_id('email').send_keys('vaya@mail.com')
        driver.implicitly_wait(5)
        pytest.driver.find_element_by_id('pass').send_keys('1245')
        driver.implicitly_wait(5)
        pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
        driver.implicitly_wait(5)
        assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0