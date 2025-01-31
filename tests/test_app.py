# Functional API Tests
import sqlite3


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Mory" in response.data


def test_add_movie(client):
    # title, poster_path, director, description, release_year, actor1, actor2, actor3, actor4
    response = client.post('/post', data={'title': "Harry Potter and the Sorcerer's Stone",
                                          'poster_path': r'images\harry_potter.jpg',
                                          'director': 'Chris Columbus',
                                          'description': 'fantasy film',
                                          'release_year': '2001',
                                          'actor1': 'Daniel Radcliffe',
                                          'actor2': 'Rupert Grint',
                                          'actor3': 'Emma Watson',
                                          'actor4': 'Richard Harris',
                                          }, follow_redirects=True)
    assert response.status_code == 200


def test_error_handling(client):
    # Attempt to access a non-existent movie
    response = client.get('/movie/9999')  # Adjust ID to something that does not exist
    assert response.status_code == 500 or response.status_code == 404  # Expecting a 404 error for non-existent resources


def test_get_reviews(client, init_db):
    with sqlite3.connect("test_movies.db") as my_db:
        cur = my_db.cursor()
        cur.execute(
            "INSERT INTO movie_tbl (title, poster_path, director, description, release_year, actor1, actor2, actor3, actor4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Harry Potter', 'test_path', 'Test Director', 'Test Description', 2024, 'Actor1', 'Actor2', 'Actor3',
             'Actor4'))

        cur.execute("INSERT INTO review_tbl (username, content, date_posted, rating, movie_id) VALUES (?, ?, ?, ?, ?)",
                    ('Tester', 'Great movie!', '28-07-2024', 8, 1))
        my_db.commit()
    response = client.get('/movie/1')

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    assert b"Harry Potter" in response.data, "Movie title not found in response"
    assert b"Great movie" in response.data, "Review content not found in response"
