# maintainance-tracker api  [![Build Status](https://travis-ci.org/mwinel/maintainance-tracker.svg?branch=master)](https://travis-ci.org/mwinel/maintainance-tracker)  [![Coverage Status](https://coveralls.io/repos/github/mwinel/maintainance-tracker/badge.svg)](https://coveralls.io/github/mwinel/maintainance-tracker)

Track user requests...

## Stack
- Python
- Flask

## Installation and Set Up


Clone the repo from GitHub:

```
https://github.com/mwinel/maintainance-tracker.git
cd requests-tracker
```

## Create and activate virtualenv

```
python -m venv venv
venv\Scripts\activate => for windows
```

## Requirements

```
pip install -r requirements.txt
```

## Set enviroment variables

Update **config** and env variables:

```
set FLASK_APP="run.py"
```

## Run the Application

```
flask run
```

## Sample Requests

Index
```

http GET http://localhost:5000/api/v1/index

HTTP/1.0 200 OK
Content-Length: 45
Content-Type: application/json
Date: Sun, 27 May 2018 11:06:36 GMT
Server: Werkzeug/0.14.1 Python/3.6.5

{
    "message": "Hello World"
}

```

## Testing endpoints

```
python tests.py 
```

## API Endpoints

| Resource URL | Methods | Description | Requires Auth |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/index` | `GET`  | The index | `FALSE` |
| `/api/v1/users/requests` | `GET`  | Fetch all the requests of a logged in user | `TRUE` |
| `/api/v1/users/requests/<requestId>` | `GET`  | Fetch a request that belongs to a logged in user | `TRUE` |
| `/api/v1/users/requests` | `POST`  | Create a request | `TRUE` |
| `/api/v1/users/requests/<requestId>` | `PUT`  | Modify a request | `TRUE` | 

## Contribute
Would you like to make **book-a-meal** a better platform?
See [CONTRIBUTING.md](#) for the steps to contribute.
