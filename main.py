from fastapi import FastAPI, HTTPException
# from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db, User
from datetime import datetime

app = FastAPI()


@app.get('/')
def test_print():
    return 'Hello world!'


@app.get('/get_info_all_users')
def get_info_all():
    new_session = connect_to_db()
    info = new_session.query(User).all()
    new_session.close()
    return info



@app.get('/get_info_with_surname')
def info_with_surname(surname_filter: str):
    new_session = connect_to_db()
    info = new_session.query(User).filter(User.surname == surname_filter).all()
    new_session.close()
    return info


@app.post('/add_new_user')
def add_new_user(name: str, surname: str, age: int):
    new_session = connect_to_db()
    if age <= 0:
        raise HTTPException(status_code=422, detail='ERROR AGE')
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


def check_adult(age: int):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
