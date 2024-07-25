from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver =webdriver.Chrome()
driver.implicitly_wait(5)
account= [
    ("zanz","asgdav"),
    ("asdbab","12345")
    ]

@pytest.mark.parametrize('a,b',account)
def test_login(a,b):
    driver.get('https://demoqa.com/login')
    driver.find_element(By.ID,'userName').send_keys(a)
    driver.find_element(By.ID,'password').send_keys(b)
    driver.find_element(By.ID,'login').click()
    invalidText=driver.find_element(By.ID,'name').text
    assert invalidText == 'Invalid username or password!'
