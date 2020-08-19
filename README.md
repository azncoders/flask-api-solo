# flask-api-solo
basic sample project flask-api solo


make sure master line within the github matches with local computer otherwise error will occur and local computer will be out of sync with master line in the cloud

pipenv manages virtual environment and dependencies

pypi

installs pipenv on your computer

`pip install pipenv`


initiate project as a pipenv project

pipenv only manages virtual environment and dependencies

`pipenv install`

`pip install pipenv==2018.11.26`

pipfile is a shopping list of what you are looking for such as packages

pip.lock is show exact location and address of where to get those packages

both file should never be changed except for the url within pipfile can change leading to a different location information within pip.lock


the app_test.py will require a code to be written so it can test the current applications code for mismatches and bugs


`# test_hello.py
from hello import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'`


tavis.yml if using tavis CI - a way for CI to install requirements for testing code when pushed into cloud

language: python
python:
  - "3.8"
install:
  - pip install pipenv
  - pipenv install --system
script: pytest