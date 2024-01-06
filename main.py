from fastapi import FastAPI,  Form
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db, User
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.head('/new')
@app.get('/new')
async def main():
    return 'Hello World'


@app.get('/get_info_all_users')
async def get_info_all():
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
def add_new_user(name=Form(...), surname=Form(...), age=Form(...)):
    new_session = connect_to_db()
    # if age <= 0:
    #     raise HTTPException(status_code=422, detail='ERROR AGE')
    new_user = User(name=name, surname=surname, age=int(age), datetime=datetime.now())
    new_session.add(new_user)
    new_session.commit()
    stop_connect(new_session)


@app.post('/login')
def login(username=Form(...)):
    print(username)
    return username


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
