from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from Admins import Admins
from sqlalchemy import and_

class SearchAdmins():
    def __init__(self):
       pass

    def querry(self,adminID,passwords):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Admins.adminID==adminID )
        myuser = self.db_obj.query_all(Admins,query_filter)
        print(myuser)
        if len(myuser):
            if myuser[0].passwords == passwords:
                return True
            else:
                return False
        else:
            return False
        self.db_obj.close()







def to_json(all_vendors):
    v = [ ven.dobule_to_dict() for ven in all_vendors ]
    return v

if __name__ == "__main__":
    pass