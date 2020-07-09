# 用于管理数据库的类
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManagement():
    def __init__(self):
        self.engine = create_engine('mssql+pyodbc://sa:123456wen@test', echo=True)  # 初始化数据库连接
        DBsession = sessionmaker(bind=self.engine)  # 创建DBsession类
        self.session = DBsession()  # 创建对象

    def add_obj(self, obj):  # 添加内容
        self.session.add(obj)
        self.session.commit()  # 提交
        return obj

    def query_all(self, target_class, query_filter):  # 查询内容
        result_list = self.session.query(target_class).filter(query_filter).all()
        return result_list

    def query_limit(self, target_class, query_filter,n):  # 查询内容

        result_list = self.session.query(target_class).filter(query_filter).limit(n)
        return result_list

    # def query_paginate(self, target_class, query_filter,order_prop=None,page=None, per_page=None,error_out=True, max_per_page=None):  # 查询内容
    #     result_list = self.session.query(target_class).filter(query_filter).order_by(order_prop).paginate(page=page, per_page=per_page,
    # error_out=error_out, max_per_page=max_per_page)
    #     return result_list

    def update_by_filter(self, obj, update_hash, query_filter):  # 更新内容
        self.session.query(obj.__class__).filter(query_filter).update(update_hash)
        self.session.commit()

    def delete_by_filter(self, obj, query_filter):  # 删除内容
        self.session.query(obj).filter(query_filter).delete()
        self.session.commit()

    def close(self):  # 关闭session
        self.session.close()

    def execute_sql(self, sql_str,fetch=True):  # 执行sql语句
        if fetch:
            obj=self.session.execute(sql_str).fetchall()
        else:
            obj= self.session.execute(sql_str)
        self.session.commit()

        return obj


    def execute_sql_paginate(self, sql_str,val):  # 执行sql语句
        return self.session.execute(sql_str,val).fetchall()