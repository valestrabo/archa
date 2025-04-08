# Transaction Management API

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/valestrabo/archa.git
$ cd archa
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ cd transaction_management
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/transactions/`.

## Endpoints

Django REST framework already has an interative HTTP request when run via a browser.

Run below API to retrieve all transactions or create a new transaction.
    http://127.0.0.1:8000/transactions/

Run below API to retrieve specific transactions by its ID.
    http://127.0.0.1:8000/transactions/<id>

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```
