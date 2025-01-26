<!-- TOC -->
* [Movie of project:](#movie-of-project)
* [Tests:](#tests)
  * [Test Cases:](#test-cases)
  * [Fixtures:](#fixtures)
  * [Test Reports:](#test-reports)
<!-- TOC -->
# Movie of project:

As part of the QA Experts course, I worked on a project to create a movie database with a Flask server.

The app has two main features:

1) Adding a movie
2) Rating a movie

I focused a lot on making the website easy and fun to use.
I'll explain more about how it works below.

Here is my website landing page:

<p align="center">
  <img src="images\homepage.jpg" width="700">
</p>

This is a second page, which shows all current movies in the database:


<p align="center">
  <img src="images\movie_posters.jpg" width="700">
</p>

This is third page, add a new movie:

<p align="center">
  <img src="images\post_new_movie.jpg" width="700">
</p>

Here is an illustration of the architecture of my app, we have 3 parts:
* The **SQlite DB** which stores the whole data in a table manner, both movies and reviews.
* The **Flask Server** listens to the user requests and connects to the DB and retrieves the relevant data.
* The end-user uses the **Browser** and requests or posts reviews.  

<p align="center">
  <img src="images\architecture.jpg" width="700">
</p>

# Tests:

## Test Cases:

1. Homepage Tests

test_homepage_title: Verifies the homepage title contains "Welcome".

test_click_homepage: Checks if the Homepage link navigates correctly.

test_home_page: Ensures the homepage loads successfully and contains expected content.

2. Movie Management Tests

test_click_new_movie: Ensures the "New Movie" link opens the correct page.

test_add_new_movie: Validates adding a new movie via form submission.

test_add_movie: Validates adding a movie through API.

3. Error Handling Tests

test_error_handling: Ensures appropriate error response for non-existent movie pages.

## Fixtures:

Fixtures are defined in tests/conftest.py and include:

init_db: Sets up a temporary SQLite database for testing.

browser: Initializes the Selenium WebDriver.

client: Provides a test client for functional API testing.

base_url: Provides the base URL of the Flask application.

