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


def test_add_new_movie(browser):
    browser.get('http://127.0.0.1:5000/')

    try:

        # Pressing on "Add a New Movie"
        list_of_links = browser.find_elements(By.TAG_NAME, 'a')
        new_movie_link = next(
            link for link in list_of_links if 'New' in link.text)
        new_movie_link.click()

        values_to_insert = {
            'Title:': 'King Mory',
            'Director:': 'Hot Director',
            'Description': 'This is my description',
            'Year of Release:': 2023,
            'Actor 1:': 'Silvester',
            'Actor 2:': 'Sharon Stone',
            'Actor 3:': 'Pamela Anderson',
            'Actor 4:': 'Mr Bean'
        }

        # Find all input elements with type 'text'
        text_boxes = browser.find_elements(By.XPATH, "//input[@type='text']")

        for text_box in text_boxes:
            k = text_box.accessible_name
            text_box.send_keys(values_to_insert[k])

        # Find all <button> elements
        buttons = browser.find_elements(By.TAG_NAME, "button")
        if len(buttons) == 1:
            buttons[0].click()

    except Exception as e:
        pytest.fail(f"Failed to add new movie: {e}")
