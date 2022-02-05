from sqlalchemy.sql.schema import ForeignKey
from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class BlogDetails(Base):
    __tablename__ = 'blog-details'
    id = Column(Integer, primary_key= True, index = True)
    title = Column(String(20))
    summary = Column(String)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    creator = relationship("User", back_populates= "blogs")
    topic = Column(Integer, ForeignKey('topic.topic_id'))
    topic_creator = relationship("Topic")

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key= True, index = True)
    name = Column(String(20))
    mail = Column(String(20))
    blogs = relationship('BlogDetails', back_populates= "creator")

class Topic(Base):
    __tablename__ = 'topic'
    topic_id = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String(20))

