# Python_Test_Task
This is Python Test Task 

## Requirements

Basic models:
- User 
- Post (always made by a user)

Basic Features:
- user signup
- user login 
- post creation 
- post like 
- post unlike 
- analytics about how many likes was made. Example url
  /api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics
  aggregated by day. 
- user activity an endpoint which will show when user was login last time and when he
  mades a last request to the service.


## Installation
If [Docker](https://www.docker.com/) installed:

  ```docker-compose build```\
  for installing dependencies and generating images.
    
  ```docker-compose up``` \
  for creating and starting containers.

If [Docker](https://www.docker.com/) not installed:
1. Create database in [Postgres](https://www.postgresql.org/)
2. Input DB credentials in .env file or directly in setting.py
3. Run ```python manage.py runserver``` in command prompt