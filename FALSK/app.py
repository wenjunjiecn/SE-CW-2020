# import base64
import hashlib
from flask import Flask, render_template, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
from search_book import SearchBook
# from db_mg import DatabaseManagement
from pub_announce import PubAnnounce
from Book import Book
from Announcement import Announcement
from search_users import SearchUsers
# from functools import cmp_to_key
from Message import Message
from pub_message import  PubMessage
from search_admins import SearchAdmins
from Regist import Regist
from oper_regist import OperRegist
from sqlalchemy import and_
from BookMes import BookMes
from oper_bookmes import OperBookMes
from oper_info import OperInfo
from db_mg import DatabaseManagement
from Info import Info
# import pyDes
# import os
import uuid
app = Flask(__name__)
CORS(app, supports_credentials=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:123456wen@test'  # (替换成自己的用户名，密码和dsn）
# db = SQLAlchemy(app)
# db = DatabaseManagement()

alltokens={}





def to_json(all_vendors):
    v = [ven.dobule_to_dict() for ven in all_vendors]
    return v




@cross_origin()
@app.route('/api')
def hello_world():
    return 'Hello World'


@app.route('/login', methods=['POST'])
def login():
    pass


@app.route('/api/addbook', methods=['POST'])
def addbook():
    data = request.get_json(silent=True)
    for k, v in data.items():
        if isinstance(data[k],str):
            data[k] = data[k].replace(' ', '').strip()
    print(data)
    if data['token'] in alltokens.keys() and alltokens[data['token']]['roles']=='admin':
        newbook = Book(data['bookName'], data['author'], data['publisher'], data['ISDN'], data['category'], data['num'])
        mysearch = SearchBook()
        mysearch = mysearch.addBook(newbook)
        return '添加成功'
    else:
        return '没有权限使用接口'

@app.route('/api/editbook', methods=['POST'])
def editbook():
    data = request.get_json(silent=True)
    print(data)
    for k,v in data.items():
        if  isinstance(data[k],str):
            data[k]=data[k].replace(' ','').strip()
    if data['token'] in alltokens.keys() and alltokens[data['token']]['roles'] == 'admin':
        cbook = Book(data['bookName'], data['author'], data['publisher'], data['ISDN'], data['category'], data['num'])
        mysearch = SearchBook()
        data.pop('token')
        mysearch = mysearch.editBook(cbook, book_data=data)
        return '修改成功'
    else:
        return '没有权限使用接口'


@app.route('/api/deletebook', methods=['POST'])
def deletebook():
    data = request.get_json(silent=True)
    print(data)
    mysearch = SearchBook()
    mysearch = mysearch.deleteBook(data['ISDN'])
    return '删除成功'



@cross_origin()
@app.route("/api/books/search", methods=['POST'])
def books():
    data = request.get_json(silent=True)
    print(data)
    mysearch = SearchBook()
    mysearch = mysearch.querry(type=data['type'],words=data['words'])
    data = to_json(mysearch)
    return (jsonify(data))


@cross_origin()
@app.route("/api/books")
def initbooks():
    mysearch = SearchBook()
    mysearch = mysearch.querry(n=100)
    data = to_json(mysearch)
    print(data)
    return (jsonify(data))


# 以下是公告部分
@app.route('/api/announcement/publish', methods=['POST'])
def addannouce():
    data = request.get_json(silent=True)
    print(data)
    newann = Announcement(data['content'], data['importance'], data['content_short'], data['author'],data['time'],data['title'],adminID=data['adminID'])
    myPubAnnounce = PubAnnounce()
    myPubAnnounce = myPubAnnounce.addAnnounce(newann)
    return '添加成功'

@cross_origin()
@app.route("/api/announcement")
def initann():
    token = request.args.get("token")
    if token in alltokens.keys() :
        myPubAnnounce = PubAnnounce()
        myPubAnnounce = myPubAnnounce.querry()
        data = to_json(myPubAnnounce)
        print(data)
        return (jsonify(data))
    else:
        return '没有访问接口的权限'



# 以下是留言部分
@app.route('/api/message/publish', methods=['POST'])
def addmessage():
    data = request.get_json(silent=True)
    print(data)
    newmes = Message(data['readID'], data['content'])
    myPubMessage = PubMessage()
    myPubMessage = myPubMessage.addMessage(newmes)
    return '添加成功'

@cross_origin()
@app.route("/api/message")
def initmes():
    token = request.args.get("token")
    if token in alltokens.keys() and alltokens[token]['roles']=='admin':
        myPubMessage = PubMessage()
        myPubMessage = myPubMessage.querry()
        data = to_json(myPubMessage)
        print(data)
        return (jsonify(data))
    else:
        return '没有访问接口权限'


@app.route('/api/deletemessage', methods=['POST'])
def deletemessage():
    data = request.get_json(silent=True)
    print(data)
    myPubMessage = PubMessage()
    myPubMessage = myPubMessage.deleteMessage(data['mesID'])
    return '删除成功'

@app.route('/api/deleteann', methods=['POST'])
def deleteann():
    data = request.get_json(silent=True)
    print(data)
    myPubAnnounce = PubAnnounce()
    myPubAnnounce = myPubAnnounce.deleteAnn(data['annID'])
    return '删除成功'

#登陆验证
@cross_origin()
@app.route("/api/login", methods=['POST'])
def login2():
    data = request.get_json(silent=True)
    print(data)
    token=uuid.uuid4().hex

    dataret={"code":20000,"data":{"token":token}}
    mpassword= hashlib.md5()
    mpassword.update(data['password'].encode(encoding='utf-8'))
    mpassword=mpassword.hexdigest()
    print("mppassword",mpassword)
    if data['usertype']=='user':
        searchusers = SearchUsers()
        if searchusers.querry(data['username'], mpassword):
            alltokens[token]={'roles':'user','id':data['username']}
            print("alltokens:", alltokens)
            return (jsonify(dataret))
        else:
            return (jsonify('用户ID或者密码错误'))

    elif data['usertype'] == 'admin' :
        searchadmins = SearchAdmins()
        if searchadmins.querry(data['username'], mpassword):
            alltokens[token] = {'roles': 'admin','id':data['username']}
            return (jsonify(dataret))
        else:
            return (jsonify('用户ID或者密码错误'))



#下面是新书部分
@cross_origin()
@app.route("/api/newbooks")
def initnewbooks():
    pageIndex = request.args.get("pageIndex")
    mysearch = SearchBook()
    mysearch = mysearch.newbookquerry(pageIndex)
    print(type(mysearch))
    data=[]
    for i in mysearch:
        tmp={'bookName':i[0],'author':i[1],'publisher':i[2],'ISDN':i[3],'category':i[4],'num':i[5],'addtime':i[6].strftime("%Y-%m-%d")}
        data.append(tmp)
    return (jsonify(data))


@cross_origin()
@app.route("/api/user/info", methods=['GET'])
def userinfo():
    token = request.args.get("token")
    if token in alltokens.keys():
        if alltokens[token]['roles']=='user':
            data={"code":20000,"data":{"roles":["user"],"introduction":"","avatar":"","name": alltokens[token]['id']}}
        if alltokens[token]['roles'] == 'admin':
            data = {"code": 20000, "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                                            "avatar": "",
                                            "name": alltokens[token]['id']}}
    print(alltokens)
    return (jsonify(data))

@cross_origin()
@app.route("/api/user/logout", methods=['POST'])
def logout():
    data = request.get_json(silent=True)
    alltokens.pop(data['token'])
    data={"code":20000}
    print(alltokens)
    return (jsonify(data))


# 以下是预约登记图书
@app.route('/api/regist', methods=['POST'])
def addRegist():
    data = request.get_json(silent=True)
    print("我刚刚预约的：",data)
    #判断是否借阅
    db_obj = DatabaseManagement()
    sql = '''
        SELECT COUNT(*)
        FROM [dbo].[BookMes]
        WHERE readID='{0}' AND ISDN='{1}'
        '''.format(data['userid'],data['isdn'])
    ann_obj = db_obj.execute_sql(sql, fetch=True)
    ann_obj=ann_obj[0][0]
    print("这里是预约登记", ann_obj,type(ann_obj))
    if ann_obj>0:
        print('已经借阅')
        return '已经借阅'
    db_obj.close()
    #判断是否已经预约
    db_obj = DatabaseManagement()
    sql = '''
            SELECT COUNT(*)
            FROM [dbo].[Regist]
            WHERE userid='{0}' AND bookisdn='{1}'
            '''.format(data['userid'], data['isdn'])
    ann_obj = db_obj.execute_sql(sql, fetch=True)
    ann_obj = ann_obj[0][0]
    print("这里是预约登记", ann_obj, type(ann_obj))
    if ann_obj>0:
        print('已经预约')
        return '已经预约'
    db_obj.close()
    #没有借阅也没有预约就进行登记
    newreg = Regist(data['userid'], data['isdn'], 1,data['bookname'],data['author'])
    myAddRegist = OperRegist()
    myPubAnnounce = myAddRegist.addRegist(newreg)
    if myPubAnnounce:
        mysearch=SearchBook()
        mysearch.decreseNum(isdn=data['isdn'])
    return '200'

#获取本人预约清单
@cross_origin()
@app.route('/api/myapplist', methods=['GET'])
def myAppoint():
    id = request.args.get('userid')
    print("我获取的数据",id)
    mysearch = OperRegist()
    mysearch = mysearch.getMyList(userid=id)
    data = to_json(mysearch)
    return (jsonify(data))

#获取全部预约清单
@cross_origin()
@app.route('/api/appointlist', methods=['GET'])
def AllAppoint():
    token = request.args.get('token')
    print('all收到的token',token)
    if token in alltokens.keys():
        print("我获取的数据",token)
        mysearch = OperRegist()
        mysearch = mysearch.getAllList()
        data = to_json(mysearch)
        return (jsonify(data))

# 以下是确认发放
@app.route('/api/confirmregist', methods=['POST'])
def confirmRegist():
    data = request.get_json(silent=True)
    print("我刚刚预约的：",data)
    myAddRegist = OperRegist()
    myConfirm = myAddRegist.confirmReg(data['userid'],data['bookisdn'])
    if myConfirm:
        myoper=OperBookMes()
        mybookmes=BookMes('借阅',data['bookisdn'],data['userid'])
        myoper=myoper.addBookMes(mybookmes)
    return '200'

def dobule_to_dict(title,obj):
    result = {}
    for i in range(len(obj)):
        result[title[i]] = str( obj[i])
    return result

def to_json2(title,all_vendors):
    v = [dobule_to_dict(title,ven) for ven in all_vendors]
    return v

#获取本人借阅清单
@cross_origin()
@app.route('/api/myborrow', methods=['GET'])
def myBorrow():
    id = request.args.get('userid')
    print("我获取的数据",id)
    db_obj = DatabaseManagement()
    sql="SELECT * FROM [BookMesInfo]WHERE readID='{0}' AND matter='借阅'".format(id)
    ann_obj = db_obj.execute_sql(sql,fetch=True)
    print("annobj",ann_obj)
    title=['matter','bookisdn','readID','opertime','bookname','author','publisher']
    ann_obj=to_json2(title,ann_obj)
    db_obj.close()
    return (jsonify(ann_obj))

#获取消息列表
@cross_origin()
@app.route('/api/getinfolist', methods=['GET'])
def getInfoList():
    token = request.args.get('token')
    id=alltokens[token]['id']
    print("验证得到的id是",id)
    print("我获取的数据", id)
    mysearch = OperInfo()
    mysearch = mysearch.querry(userid='201709000521')
    data = to_json(mysearch)
    print("获得的消息列表：",data)
    return (jsonify(data[::-1]))

# 发送消息
@app.route('/api/sendinfo', methods=['POST'])
def sendInfo():
    data = request.get_json(silent=True)
    print("我刚刚预约的：",data)
    newinfo = Info(data['sendid'],data['receiveid'],data['title'],data['content'],data['author'])
    myAdd = OperInfo()
    myNew = myAdd.addMessage(newinfo)
    return '200'

# 回复留言
@app.route('/api/remessage', methods=['POST'])
def reMessage():
    data = request.get_json(silent=True)
    token=data['token']
    print("我回复的：", data)
    print('alltokens', alltokens)
    id=alltokens[token]['id']

    newinfo = Info(id,data['readid'],'留言回复',data['content'],'管理员消息')
    myAdd = OperInfo()
    myNew = myAdd.addMessage(newinfo)
    return '200'

#删除消息
@app.route('/api/deleteinfo', methods=['POST'])
def deleteinfo():
    data = request.get_json(silent=True)
    token = data['token']
    if token in alltokens.keys():
        print(data)
        mydel = OperInfo()
        myPubMessage = mydel.deleteMessage(data['infoid'])
        return '删除成功'

#获取消息列表
@cross_origin()
@app.route('/api/getBorrowList', methods=['GET'])
def getBorrowList():
    # token = request.args.get('token')
    # id=alltokens[token]['id']
    db_obj = DatabaseManagement()
    sql = '''
    SELECT [ISDN]
      ,[readID]
      ,[time]
      ,[publisher]
      ,[author]
      ,[bookName]
      ,[userclass]
      ,[major]
      ,[username]
      ,[day],
	   DATEDIFF(day,GETDATE(),DATEADD(day,+day,time)) 
  FROM [dbo].[LeftDay]
    '''
    ann_obj = db_obj.execute_sql(sql, fetch=True)
    print("annobj", ann_obj)
    title = ['ISDN', 'readID', 'time', 'publisher', 'author', 'bookName', 'userclass','major','username','day','leftday']
    ann_obj = to_json2(title, ann_obj)
    db_obj.close()
    return (jsonify(ann_obj))

# 催促超期用户
@app.route('/api/urge', methods=['POST'])
def Urge():
    data = request.get_json(silent=True)
    token=data['token']
    print("我回复的：", data)
    print('alltokens', alltokens)
    adminid=alltokens[token]['id']
    db_obj = DatabaseManagement()
    sql='''
    SELECT [ISDN]
      ,[readID]
      ,[bookName]
      ,[day],
	   DATEDIFF(day,GETDATE(),DATEADD(day,+day,time)) as leftday
  FROM [dbo].[LeftDay]
  WHERE DATEDIFF(day,GETDATE(),DATEADD(day,+day,time))<=0
    '''
    ann_obj = db_obj.execute_sql(sql, fetch=True)
    print("annobj", ann_obj)
    title = ['ISDN', 'readID', 'bookName', 'day', 'leftday']
    ann_obj = to_json2(title, ann_obj)
    db_obj.close()
    print('tojson2',ann_obj,type(ann_obj))
    for item in ann_obj:
        message='您的借书《'+item['bookName']+'》已经超期,请您及时归还'
        userid=item['readID']
        newinfo = Info(adminid, userid, '催促还书', message, '系统消息')
        myAdd = OperInfo()
        myNew = myAdd.addMessage(newinfo)
    return '200'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1' ,port=5000)
    initbooks()