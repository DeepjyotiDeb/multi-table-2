from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID
import datetime

class Blogger(BaseModel): 
    title: str
    summary: str
    user_id: Optional[int]
    topic_id: int
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    mail: str
    class Config():
        orm_mode = True

class Topic(BaseModel):
    topic_name: str
    class Config():
        orm_mode = True
