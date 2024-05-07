from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from .models import Base

DATABASE_URI = "sqlite:///./test.db"

engine = create_engine(DATABASE_URI)
BASE.metadata.create_all(engine)
