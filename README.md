
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