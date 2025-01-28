import sqlite3
import pytest
from app import app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService



# For sharing fixtures among  multiple test files
@pytest.fixture
def init_db():
    conn = sqlite3.connect("test_movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS movie_tbl (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, poster_path TEXT, director TEXT, description TEXT, release_year INTEGER, actor1 TEXT, actor2 TEXT, actor3 TEXT, actor4 TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS review_tbl (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, content TEXT, date_posted TEXT, rating INTEGER, movie_id INTEGER)")
    conn.commit()
    yield
    conn.close()


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(params=["edge", "chrome", "firefox"], scope="class")
def driver(request):
    browser = request.param
    if browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    request.cls.driver = driver
    yield driver
    driver.quit()
