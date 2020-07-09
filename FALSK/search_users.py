from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from Users import Users
from sqlalchemy import and_

class SearchUsers():
    def __init__(self):
       pass

    def querry(self,readID,passwords):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Users.readID==readID )
        myuser = self.db_obj.query_all(Users,query_filter)
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