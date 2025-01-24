def test_homepage_title(browser):
    browser.get("http://127.0.0.1:5000")
    assert "Welcome" in browser.title
