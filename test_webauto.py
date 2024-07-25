from selenium import webdriver
import pytest

driver =webdriver.Chrome()

Url= [
    ("https://secondhand.binaracademy.org/","SecondHand"),
    ("https://www.facebook.com","Facebook – log in or sign up")
    ]

@pytest.mark.parametrize('address,result',Url)
def test_openUrl(address,result):
    driver.get(address)
    Title = driver.title
    assert Title == result
