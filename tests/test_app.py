# Functional API Tests
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Mini IMDB" in response.data


# def test_add_movie(client):
#     # title, poster_path, director, description, release_year, actor1, actor2, actor3, actor4
#     response = client.post('/post', data={'title': "Harry Potter and the Sorcerer's Stone",
#                                           'poster_path': '',
#                                           'director': '',
#                                           'description': '',
#                                           'release_year': '',
#                                           'actor1': '',
#                                           'actor2': '',
#                                           'actor3': '',
#                                           'actor4': '',
#                                           })
#     assert response.status_code == 200
#     assert b"Inception" in response.data
