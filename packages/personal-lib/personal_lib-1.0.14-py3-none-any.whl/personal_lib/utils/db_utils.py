import pandas as pd
import pymysql
from pymysql.cursors import DictCursor
from dbutils.pooled_db import PooledDB

conn_pool = {}


def add_connect(host, port, user, passwd, db, name, pool_conn=0):
    '''

    :param host:
    :param port:
    :param user:
    :param passwd:
    :param db:
    :param name:
    :param pool_conn:  0则使用DBconn，非0则使用ThreadSafeDBConn
    :return:
    '''
    global conn_pool
    if pool_conn == 0:
        db = DBConn(host, port, user, passwd, db, name)
    else:
        db = ThreadSafeDBConn(host, port, user, passwd, db, name, pool_conn)
    conn_pool[db.name] = db


def get_conn(name):
    global conn_pool
    current_conn = conn_pool[name]
    return current_conn


class DBConn():
    def __init__(self, host, port, user, passwd, db, name):
        self.name = name
        self.conn = pymysql.connect(user=user, passwd=passwd, host=host, port=port, db=db)
        self.cur = self.conn.cursor(DictCursor)

    def check_conn(self):
        if not self.conn.open:
            self.conn.ping(True)

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def query_data(self, sql, args=None):
        self.cur.execute(sql, args)
        results = self.cur.fetchall()
        df = pd.DataFrame(results)
        return df

    def exec_sql(self, sql, args=None):
        self.cur.execute(sql, args)
        self.conn.commit()

    def exec_many(self, sql, args=None):
        self.cur.executemany(sql, args)
        self.conn.commit()


class ThreadSafeDBConn():
    def __init__(self, host, port, user, passwd, db, name, mincached=20):
        self.name = name
        self.pool = PooledDB(pymysql, mincached=mincached, host=host, port=port, user=user, passwd=passwd,
                             db=db)  # 5为连接池里的最少连接数

    def close(self):
        if self.pool is not None:
            self.pool.close()

    def query_data(self, sql, args=None):
        conn = self.pool.connection()
        cur = conn.cursor(DictCursor)
        cur.execute(sql, args)
        results = cur.fetchall()
        df = pd.DataFrame(results)
        conn.close()
        return df

    def exec_sql(self, sql, args=None):
        conn = self.pool.connection()
        cur = conn.cursor(DictCursor)
        cur.execute(sql, args)
        conn.commit()
        conn.close()

    def exec_many(self, sql, args=None):
        conn = self.pool.connection()
        cur = conn.cursor(DictCursor)
        cur.executemany(sql, args)
        conn.commit()
        conn.close()
