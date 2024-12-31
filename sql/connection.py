from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

user = 'root'
password = ''
host = 'localhost'
database = 'jobcareers_flask'

engine = create_engine(
            f"mysql+pymysql://{user}@{host}/{database}", 
            echo=True
        )

class Base(DeclarativeBase):
    pass
