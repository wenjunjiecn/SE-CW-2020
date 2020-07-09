# 图书信息表
from sqlalchemy import Column, String, INT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import ForeignKey, Sequence, MetaData, Table
from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy import create_engine
from db_mg import DatabaseManagement

db = DatabaseManagement()
engine = db.engine
Base = declarative_base()  # 创建对象的基类
md = MetaData(bind=engine)  # 引用MetaData


class Book(Base):  # 定义一个类，继承Base
    __table__ = Table("Book", md, autoload=True)  # 自动把数据库的表，映射到对象
    __tablename__='Book'

    def __init__(self, bookName, author, publisher, ISDN, category, num):  # 初始化对象
        self.bookName = bookName
        self.author = author
        self.publisher = publisher
        self.ISDN = ISDN
        self.category = category
        self.num = num

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result
