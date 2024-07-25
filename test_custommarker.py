from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

account= [
    ("zanz","asgdav"),
    ("asdbab","12345")
    ]

@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window
    driver.get('https://demoqa.com/login')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.mark.positivetest
def test_login_success(setup):
    setup.find_element(By.ID,'userName').send_keys('idejongkok')
    setup.find_element(By.ID,'password').send_keys('asDF12#$')
    setup.find_element(By.ID,'login').click()
    name=setup.find_element(By.ID,'userName-value').text
    assert name == 'idejongkok'
    
@pytest.mark.negativetest
@pytest.mark.parametrize('a,b',account)
def test_login_invalid(setup,a,b):
    setup.find_element(By.ID,'userName').send_keys(a)
    setup.find_element(By.ID,'password').send_keys(b)
    setup.find_element(By.ID,'login').click()
    invalidText=setup.find_element(By.ID,'name').text
    assert invalidText == 'Invalid username or password!'
