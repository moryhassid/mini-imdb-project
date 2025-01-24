# Selenium Tests
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_homepage_title(browser):
    browser.get("http://127.0.0.1:5000")
    assert "Welcome" in browser.title


def test_click_homepage(browser):
    browser.get('http://127.0.0.1:5000/')
    try:
        list_of_links = browser.find_elements(By.TAG_NAME, 'a')
        homepage_link = next(
            link for link in list_of_links if 'Homepage' in link.text)
        homepage_link.click()
        WebDriverWait(browser, 10).until(EC.title_contains('Homepage'))
    except Exception as e:
        pytest.fail(f"Failed to click Homepage link: {e}")


def test_click_new_movie(browser):
    browser.get('http://127.0.0.1:5000/')
    try:
        list_of_links = browser.find_elements(By.TAG_NAME, 'a')
        new_movie_link = next(
            link for link in list_of_links if 'New' in link.text)
        new_movie_link.click()
        WebDriverWait(browser, 10).until(EC.title_contains('New Movie'))
    except Exception as e:
        pytest.fail(f"Failed to click New Movie link: {e}")
