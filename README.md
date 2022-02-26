# APIs
All requirements with version included to install are located in requirements.txt
```bash
    pip install -r requirements.txt
```
## Some important info to review:
- Install Fastapi to create the APIs


- Install Postman to verify APIs response. Examples
```bash
    http://127.0.0.1:8000/posts
```
- Run python venv
```bash
    source /../activate
```

- Run app in your localhost: 
```bash
    uvicorn app.main:app --reload
```

FASTAPI docs:
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/docs

DATABASES with Docker
- Install postgres Example: port:15432:5432, add user, password, db, port
- Install pgAdmin Example: port:16543:80, email, anypass
```bash
    http://localhost:16543/
```
CONNECT postgres DB with fastApi: install psycopg2 in the venv
Where psycopg is the driver used

Use ```pip freeze``` tu verify all the apps installed in your env

Install and configure SQLAlchemy ORM to access postgresDB from FastAPI
```bash
    pip install SQLAlchemy
```
```bash 
    https://fastapi.tiangolo.com/tutorial/sql-databases/
```
Review or install email validator
```bash
    pip install email-validator
```
Install two libraries for password:
```bash
    pip install passlib[bcrypt]
```
Install OAUTH2 tool for login JWT tokens in Python
```bash
    pip install python-jose[cryptography]
```
Info and Examples: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

Install Alembic, migration tools, to update columns via sqlAlchemy to Database:
IT HELPS TO AUTOGENERATE CHANGES ON DATABASE
```bash
pip install alembic
```
URL: https://alembic.sqlalchemy.org/
some helpful commands:
```bash
    alembic --help
    alembic upgrade head
    alembic upgrade [Revision_ID]
    alembic downgrade [Revision_ID]
    alembic revision --autogenerate -m "add message"
```


CORS - Cross Origin Resource Sharing allows to make request from a web browser on one domain to a server on a different domain
Link  for more info: https://fastapi.tiangolo.com/tutorial/cors/?h=cors#more-info


## Deploy to Heroku
https://devcenter.heroku.com/articles/getting-started-with-python

Heroku tips
Create Procfile to start app
To restart app
```bash
heroku ps:restart
```
To create a DB on postgresql free-tier
```bash
heroku addons:create heroku-postgresql:hobby-dev
```
To update DB using alembic
```bash
    heroku run "alembic upgrade [somevalue]"
```
To review logs
```bash
heroku logs -t
```
## For testing purposes you can add Pytest to test the api
```bash
    pip install pytest
```
- Commands to use:
```bash
    pytest
    pytest folder/test_file
    pytest --disable-warnings -v
    pytest --disable-warnings -v -x
```
