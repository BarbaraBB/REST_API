## REST_API

An example Django REST framework project.

### API Endpoints

#### Users

* **/users/** (List of registered users)
* **/users/me/** (Currently logged in user)

#### Login

* **/login/** (Login new user and return the REST Token)

#### Register

* **/register/** (Register new user and return the REST Token)


### Install 

    pip install -r requirements.txt

### Usage

    python manage.py runserver
