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

CONNECT postgres DB with fastApi: install psycopg2 in the venv