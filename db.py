from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup database engine, create tables and setup session
db_engine = create_engine('sqlite:///uninteresting.db', encoding="utf8", echo=False)
Session = sessionmaker(bind=db_engine)
db_session = Session()