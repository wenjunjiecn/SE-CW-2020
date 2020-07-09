# 操作借阅信息表
from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from BookMes import BookMes
from sqlalchemy import and_

class OperBookMes():
    def __init__(self):
       pass

    def addBookMes(self,reg_obj):   #预约图书
        try:
            self.db_obj = DatabaseManagement()
            ann_obj = self.db_obj.add_obj(reg_obj)
            self.db_obj.close()
            return 1
        except:
            return 0

    def getMyList(self,userid):
        self.db_obj = DatabaseManagement()
        query_filter = and_(BookMes.readID == userid,BookMes.matter=='借阅')
        message_obj = self.db_obj.query_all(BookMes, query_filter)
        self.db_obj.close()
        return message_obj

    def getAllList(self):
        self.db_obj = DatabaseManagement()
        query_filter = and_(BookMes.userid != None)
        message_obj = self.db_obj.query_all(BookMes, query_filter)
        self.db_obj.close()
        return message_obj

    def deleteMessage(self, regid):
        self.db_obj = DatabaseManagement()
        query_filter = and_(BookMes.regid == regid)
        message_obj = self.db_obj.delete_by_filter(BookMes, query_filter)
        self.db_obj.close()

    def confirmReg(self, userid,bookisdn):
        try:
            self.db_obj = DatabaseManagement()
            query_filter = and_(BookMes.userid == userid,BookMes.bookisdn==bookisdn)
            message_obj = self.db_obj.delete_by_filter(BookMes, query_filter)
            self.db_obj.close()
            return 1
        except:
            return 0


def to_json(all_vendors):
    v = [ ven.dobule_to_dict() for ven in all_vendors ]
    return v

if __name__ == "__main__":
    myOperRegist = OperRegist()
    mm=myOperRegist.getMyList('201709000521')
    print(to_json(mm))
