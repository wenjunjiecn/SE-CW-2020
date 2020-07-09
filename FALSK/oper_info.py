from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from Info import Info
from sqlalchemy import and_

class OperInfo():
    def __init__(self):
       pass

    def querry(self,userid):
        self.db_obj = DatabaseManagement()
        query_filter=and_(Info.receiveid==userid)
        list = self.db_obj.query_all(Info,query_filter)
        self.db_obj.close()
        return list

    def addMessage(self,ann_obj):
        self.db_obj = DatabaseManagement()
        ann_obj = self.db_obj.add_obj(ann_obj)
        self.db_obj.close()

    def deleteMessage(self, infoid):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Info.infoid == infoid)
        message_obj = self.db_obj.delete_by_filter(Info, query_filter)
        self.db_obj.close()


def to_json(all_vendors):
    v = [ ven.dobule_to_dict() for ven in all_vendors ]
    return v

if __name__ == "__main__":
    myPubAnnounce = OperInfo()

    print("结果是",myPubAnnounce.querry(userid='201709000521'))

