from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db, User
from datetime import datetime

app = FastAPI()


@app.get('/')
def test_print():
    return 'Hello world!'


@app.post('/add_new_user')
def add_new_user(name: str, surname: str, age: int):
    new_session = connect_to_db()
    new_user = User(name=name, surname=surname, age=age, datetime=datetime.now())
    new_session.add(new_user)
    new_session.commit()
    stop_connect(new_session)


def stop_connect(new_session):
    new_session.close()


def connect_to_db():
    engine = create_engine('sqlite:///TEST.db', echo=True)
    db.metadata.create_all(engine)
    Session = sessionmaker()
    new_session = Session(bind=engine)
    return new_session


def main():
    pass


if __name__ == '__main__':
    main()
