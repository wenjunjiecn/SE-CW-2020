from flask import Flask, render_template, jsonify
from db_mg import DatabaseManagement
from Book import Book
from sqlalchemy import and_
import paginate_sqlalchemy

class SearchBook():
    def __init__(self):
        pass

    def querry(self, type='bookName', words='',n=0):
        self.db_obj = DatabaseManagement()
        words = words.strip()
        words = words.split()
        if type == 'bookName':
            query_filter = and_(*[Book.bookName.like('%' + w + '%') for w in words])
        elif type == 'author':
            query_filter = and_(*[Book.author.like('%' + w + '%') for w in words])
        elif type == 'ISDN':
            query_filter = and_(*[Book.ISDN.like('%' + w + '%') for w in words])
        elif type == 'publisher':
            query_filter = and_(*[Book.publisher.like('%' + w + '%') for w in words])
        if n==0:
            book_list = self.db_obj.query_all(Book, query_filter)
        else:
            book_list = self.db_obj.query_limit(Book, query_filter, n)


        self.db_obj.close()
        return book_list


    def newbookquerry(self,pageIndex):
        self.db_obj = DatabaseManagement()
        sql='''
        select * from Book
        WHERE (DATEPART(yy, addtime) = DATEPART(yy, GETDATE())) AND (DATEPART(mm, addtime) = DATEPART(mm, GETDATE()))
        order by addtime DESC
        offset ((:pageIndex-1)*:pageSize) rows
        fetch next :pageSize rows only;
        '''
        book_list = self.db_obj.execute_sql_paginate(sql,{'pageIndex':pageIndex,'pageSize':5})

        self.db_obj.close()
        print(book_list)
        return book_list

    def addBook(self, book_obj):
        self.db_obj = DatabaseManagement()
        book_obj = self.db_obj.add_obj(book_obj)
        self.db_obj.close()

    def deleteBook(self, myISDN):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Book.ISDN == myISDN)
        book_obj = self.db_obj.delete_by_filter(Book, query_filter)
        self.db_obj.close()

    def editBook(self, book_obj, book_data):
        self.db_obj = DatabaseManagement()
        query_filter = and_(Book.ISDN == book_obj.ISDN)
        book_obj = self.db_obj.update_by_filter(book_obj, book_data, query_filter)
        self.db_obj.close()

    def decreseNum(self,isdn):
        self.db_obj = DatabaseManagement()
        print("update Book set num=num-1 where ISDN='{0}';".format(isdn))
        book_obj = self.db_obj.execute_sql("update Book set num=num-1 where ISDN='{0}';".format(isdn),fetch=False)
        print("查询的结果是",book_obj)
        self.db_obj.close()


def to_json(all_vendors):
    v = [ven.dobule_to_dict() for ven in all_vendors]
    return v


if __name__ == "__main__":
    mysearch = SearchBook()
    # mysearch = mysearch.querry()
    # data = to_json(mysearch)
    # print(data)
    mysearch.decreseNum('9787302501276')

