from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from Message import Message
from sqlalchemy import and_

class PubMessage():
    def __init__(self):
       pass

    def querry(self):
        self.db_obj = DatabaseManagement()
        query_filter=and_(Message.content!=None)
        book_list = self.db_obj.query_all(Message,query_filter)
        self.db_obj.close()
        return book_list[::-1]



    def addMessage(self,ann_obj):
        self.db_obj = DatabaseManagement()
        ann_obj = self.db_obj.add_obj(ann_obj)
        self.db_obj.close()

    def deleteMessage(self, mesID):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Message.mesID == mesID)
        message_obj = self.db_obj.delete_by_filter(Message, query_filter)
        self.db_obj.close()


def to_json(all_vendors):
    v = [ ven.dobule_to_dict() for ven in all_vendors ]
    return v

if __name__ == "__main__":
    myPubAnnounce = PubMessage()
    myann=Message('201709000520','123')
    myPubAnnounce=myPubAnnounce.addMessage(myann)

