from sqlalchemy import Column, MetaData, Integer
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()


class UserTBL(Base):
    __tablename__ = 'user_tbl'
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column('first_name', NullType)
    last_name = Column('last_name', NullType)
    dob = Column('dob', NullType)
    
class Person(Base):
# comment
   __tablename__ = 'table_person'
   person_id = Column(Integer, primary_key=True, index=True)
   person_username = Column('username', NullType)
   person_password = Column('password', NullType)
   person_email = Column('email', NullType)
   blog_id = Column('blog_id', NullType)
