# Functional API Tests
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Mory" in response.data


def test_add_movie(client):
    # title, poster_path, director, description, release_year, actor1, actor2, actor3, actor4
    response = client.post('/post', data={'title': "Harry Potter and the Sorcerer's Stone",
                                          'poster_path': 'images\harry_potter.jpg',
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
