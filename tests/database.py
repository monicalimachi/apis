from fastapi.testclient import TestClient
from app.main import app

import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db, Base

from alembic import command


#SQLALCHEMY_DATABASE_URL = 'postgresql://dulcinea:root@localhost:15432/fastapi_test'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Set cope accord type of test: scope="module" or scope="session", default:scope="function"
@pytest.fixture()
def session():
    #command.upgrade("head")
    #command.downgrade("base")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


#Use Fixture from Pytest to get a Client #yield run the code before test runs #and run some code after test runs
@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


#All import information was added to coftest.py, by default pytest use that path file to reuse in all testcases