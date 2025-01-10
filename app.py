from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for Flask-WTF forms


class ReviewForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=100)])
    content = TextAreaField('Review', validators=[DataRequired(), Length(min=1)])
    rating = FloatField('Rating (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Submit Review')


def get_movies():
    with sqlite3.connect("movies.db") as my_db:
        my_db.row_factory = sqlite3.Row
        cur = my_db.cursor()
        movies = cur.execute('SELECT * FROM movie_tbl').fetchall()
        return [dict(row) for row in movies]


@app.route('/')
def index():
    return render_template("welcome.html")


@app.route("/homepage/", methods=['GET'])
def home_page():
    movies_list = []
    with sqlite3.connect("movies.db") as my_db:
        my_db.row_factory = sqlite3.Row
        cur = my_db.cursor()
        movies_posters_paths = cur.execute('SELECT poster_path FROM movie_tbl').fetchall()

        for movie in movies_posters_paths:
            movies_list += list(dict(movie).values())

        movies_list = [movie.replace('\\', '/') for movie in movies_list]

        if not movies_posters_paths:
            return "Movies were not found.", 404

    return render_template('homepage.html', elements=movies_list), 200


@app.route("/post/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        title = request.form.get('title')
        poster_path = request.form.get('poster_path')
        director = request.form.get('director')
        description = request.form.get('description')
        release_year = request.form.get('release_year')
        actor1 = request.form.get('actor1')
        actor2 = request.form.get('actor2')
        actor3 = request.form.get('actor3')
        actor4 = request.form.get('actor4')

        with sqlite3.connect("movies.db") as my_db:
            cur = my_db.cursor()
            poster_path = 'blabla'
            cur.execute(
                "INSERT INTO movie_tbl (title, poster_path, director, description, release_year, actor1, actor2, actor3, actor4) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (title, poster_path, director, description, release_year, actor1, actor2, actor3, actor4)
            )
            my_db.commit()
        return redirect(url_for('home_page'))
    return render_template("post_movie.html")


@app.route("/movie/<int:movie_id>", methods=['GET', 'POST'])
def movie_detail(movie_id):
    with sqlite3.connect("movies.db") as my_db:
        my_db.row_factory = sqlite3.Row
        cur = my_db.cursor()
        movie = cur.execute('SELECT * FROM movie_tbl WHERE id = ?', (movie_id,)).fetchone()
        if not movie:
            return "Movie not found.", 404

        form = ReviewForm()
        if form.validate_on_submit():
            year = datetime.now().year
            month = datetime.now().month
            day = datetime.now().day
            username = form.username.data
            content = form.content.data
            rating = form.rating.data

            # Ensure the rating is an integer and within the valid range (1-10)
            if rating < 0 or rating > 10:
                form.rating.errors.append("Please provide a valid rating between 1 and 10.")
                return render_template("movie_detail.html", movie=dict(movie), form=form, reviews=[])

            cur.execute(
                "INSERT INTO review_tbl (username, content, date_posted, rating, movie_id) VALUES (?, ?, ?, ?, ?)",
                (username, content, f"{day}-{month}-{year}", rating, movie_id)
            )
            my_db.commit()
            return redirect(url_for('movie_detail', movie_id=movie_id))

        reviews = cur.execute('SELECT * FROM review_tbl WHERE movie_id = ? ORDER BY date_posted DESC',
                              (movie_id,)).fetchall()
        reviews = [dict(row) for row in reviews]
        dict_fixed = dict(movie)
        dict_fixed['poster_path'] = dict_fixed['poster_path'].replace('\\', '/')
        return render_template("movie_detail.html",
                               movie=dict_fixed,
                               form=form,
                               reviews=reviews)


if __name__ == '__main__':
    app.run(debug=True)
