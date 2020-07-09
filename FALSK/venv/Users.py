from sqlalchemy import Column, String, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 创建对象的基类

class Users(Base):  # 定义一个类，继承Base
    __table__ = Table("Users", md, autoload=True)

    def __init__(self, username, major,userclass,readID,usertype,passwords):
        self.username = username
        self.major = major
        self.userclass = userclass
        self.readID = readID
        self.usertype = usertype
        self.passwords = passwords

