from fastapi import FastAPI, Depends
import models, schemas
from sqlalchemy.orm import Session
from database import get_db, engine

app = FastAPI()
models.Base.metadata.create_all(engine)

@app.get("/")
def test(db:Session = Depends(get_db)):
    posts = db.query(models.BlogDetails).all()
    return posts

@app.get("/get-post{uid}")
def post(uid:int, db:Session=Depends(get_db)):
    post = db.query(models.BlogDetails).filter(models.BlogDetails.id == uid).first()
    return post

@app.post('/create-posts/', tags = ['blogs'])
def create_post(user: schemas.Blogger, db:Session = Depends(get_db)):
    post = models.BlogDetails(title = user.title, 
                              summary = str(user.summary),
                              user_id = user.user_id,
                              topic = user.topic_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.post('/create-user/', tags = ['user'])
def create_user(user:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name=user.name, mail=user.mail)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post('/create-topic/', tags = ['blogs'])
def create_topic(topic:schemas.Topic, db:Session = Depends(get_db)):
    new_topic = models.Topic(topic_name=topic.topic_name)
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic