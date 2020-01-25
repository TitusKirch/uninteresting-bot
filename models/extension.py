from sqlalchemy import Column, String, Boolean, Text
from models.base import Base
import sqlalchemy
from db import db_session

class Extension(Base):
    __tablename__ = 'extensions'
    
    name = Column(String, primary_key=True)
    isLoaded = Column(Boolean, server_default=u'false')
    description = Column(Text)
    author = Column(String, nullable=True)

    def __init__(self, name, isLoaded):
        self.name = name
        self.isLoaded = isLoaded

    @classmethod
    def get(cls, name):
        return db_session.query(Extension).filter(Extension.name==name).first()

    @classmethod
    def loaded(cls):
        return db_session.query(Extension).filter(Extension.isLoaded==1).all()

    @classmethod
    def unloaded(cls):
        return db_session.query(Extension).filter(Extension.isLoaded==0).all()