from app import my_app


# test_hello.py

def test_tc001_hello():
    response = my_app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello World'
