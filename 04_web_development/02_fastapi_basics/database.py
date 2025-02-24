from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#创建数据库引擎
engine = create_engine('sqlite:///./test.db')
Base = declarative_base

#定义数据库模型
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(True)

#创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#创建数据库表
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
