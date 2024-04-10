from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

def open_db():
    engine = create_engine('sqlite:///database.db')
    return sessionmaker(bind=engine)()

def save(obj):
    db = open_db()
    db.add(obj)
    db.commit()
    db.close()

# classes (tables for database)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(50), unique=True)
    password = Column(String(64))
    created_at = Column(DateTime, default=datetime.now)

class ImageUpload(Base):
    __tablename__ = 'image_uploads'
    id = Column(Integer, primary_key=True)
    path = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)

if __name__ == '__main__':
    Base.metadata.create_all(create_engine('sqlite:///database.db')) 
    print('Database created')