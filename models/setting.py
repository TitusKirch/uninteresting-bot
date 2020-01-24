from sqlalchemy import Column, String
from models.base import Base
import sqlalchemy
from db import db_session

class Setting(Base):
    __tablename__ = 'settings'
    
    name = Column(String, primary_key=True)
    value = Column(String)

    @classmethod
    def get(cls, name):
        return db_session.query(Setting).filter(Setting.name==name).first().value