from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from Regist import Regist
from sqlalchemy import and_

class OperRegist():
    def __init__(self):
       pass

    def addRegist(self,reg_obj):   #预约图书
        try:
            self.db_obj = DatabaseManagement()
            ann_obj = self.db_obj.add_obj(reg_obj)
            self.db_obj.close()
            return 1
        except:
            return 0

    def getMyList(self,userid):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Regist.userid == userid)
        message_obj = self.db_obj.query_all(Regist, query_filter)
        self.db_obj.close()
        return message_obj

    def getAllList(self):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Regist.userid != None)
        message_obj = self.db_obj.query_all(Regist, query_filter)
        self.db_obj.close()
        return message_obj

    def deleteMessage(self, regid):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Regist.regid == regid)
        message_obj = self.db_obj.delete_by_filter(Regist, query_filter)
        self.db_obj.close()

    def confirmReg(self, userid,bookisdn):
        try:
            self.db_obj = DatabaseManagement()
            query_filter = and_(Regist.userid == userid,Regist.bookisdn==bookisdn)
            message_obj = self.db_obj.delete_by_filter(Regist, query_filter)
            self.db_obj.close()
            return 1
        except:
            return 0


def to_json(all_vendors):
    v = [ ven.dobule_to_dict() for ven in all_vendors ]
    return v

if __name__ == "__main__":
    myOperRegist = OperRegist()
    obj=Regist('112222', '1111111', 1,'shuming', 'author')
    mm=myOperRegist.addRegist(obj)

