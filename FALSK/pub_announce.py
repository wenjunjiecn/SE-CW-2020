from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from Announcement import Announcement
from sqlalchemy import and_

class PubAnnounce():
    def __init__(self):
       pass

    def querry(self):
        self.db_obj = DatabaseManagement()
        query_filter=and_(Announcement.title!=None)
        book_list = self.db_obj.query_all(Announcement,query_filter)
        self.db_obj.close()
        return book_list



    def addAnnounce(self,ann_obj):
        self.db_obj = DatabaseManagement()
        ann_obj = self.db_obj.add_obj(ann_obj)
        self.db_obj.close()

    def deleteAnn(self, mesID):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Announcement.mesID == mesID)
        message_obj = self.db_obj.delete_by_filter(Announcement, query_filter)
        self.db_obj.close()



def to_json(all_vendors):
    v = [ ven.dobule_to_dict() for ven in all_vendors ]
    return v

if __name__ == "__main__":
    myPubAnnounce = PubAnnounce()
    myann=Announcement('123','1','111','JACK','2017-09-11 12:12:12','TITLE')
    myPubAnnounce=myPubAnnounce.addAnnounce(myann)

