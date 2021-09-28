from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://google.co.id')
    yield driver
    driver.quit()

def test_googling(driver):
    driver.find_element_by_name('q').send_keys('Fina Afifana Rahman' + Keys.ENTER)
    assert 'Fina Afifana Rahman' in driver.find_element_by_css_selector('h3').text
    assert 'Fina Afifana Rahman' in driver.title 
    
def test_googling_fany(driver):
    driver.find_element_by_name('q').send_keys('Fany Pristiyanti Rahman' + Keys.ENTER)
    assert 'Fany Pristiyanti Rahman' in driver.find_element_by_css_selector('h3').text
    assert 'Fany Pristiyanti Rahman' in driver.title 