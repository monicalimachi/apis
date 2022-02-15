# apis

- Install Fastapi to create the APIs


- Install Postman to verify APIs response. Examples
```bash
    http://127.0.0.1:8000/posts
```
-Run python venv
```bash
    source /../activate
```

- Run app: 
```bash
    uvicorn app.main:app --reload
```

FASTAPI docs:
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/docs

DATABASES with Docker
- Install postgres: port:15432:5432, add user, password, db, port
- Install pgAdmin: port:16543:80, email, anypass
```bash
    http://localhost:16543/
```
CONNECT postgres DB with fastApi: install psycopg2 in the venv

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