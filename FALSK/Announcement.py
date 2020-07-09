# 公告表
from sqlalchemy import Column, String, INT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import ForeignKey, Sequence, MetaData, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from db_mg import DatabaseManagement

db = DatabaseManagement()
engine = db.engine
Base = declarative_base()  # 创建对象的基类
md = MetaData(bind=engine)  # 引用MetaData


class Announcement(Base):  # 定义一个类，继承Base
    __table__ = Table("Announcement", md, autoload=True)  # 自动把数据库的表，映射到对象
    __tablename__='Announcement'
    __table__.mesID = Column(String(30), primary_key=True, autoincrement=True)
    def __init__(self,content, important, content_short, author,time,title,adminID='1'):  # 初始化对象
        self.adminID = adminID
        self.content = content
        self.important = important
        self.content_short = content_short
        self.author = author
        self.time = time
        self.title = title

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result
