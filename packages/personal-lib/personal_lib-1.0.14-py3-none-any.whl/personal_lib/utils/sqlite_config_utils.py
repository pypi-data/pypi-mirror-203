import sqlite3
import json

db_file = '/grdata/sqlite/server_config'

def dictToObj(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    d = Dict()
    for k, v in dictObj.items():
        d[k] = dictToObj(v)
    return d

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

def get_configs() -> Dict:
    dict = {}
    # 1.创建数据库连接
    conn = sqlite3.connect(db_file)
    # 2.创建游标
    cursor = conn.cursor()
    results = cursor.execute("SELECT * FROM t_config")
    results = results.fetchall()  # 结果转成元组
    for rs in results:
        value = json.loads(rs[1])[rs[0]]
        dict[rs[0]] = value
    cursor.close()  # 关闭cursor对象
    conn.close()  # 关闭数据库连接
    cfg_cls = Dict(dict)
    cfg_cls = dictToObj(cfg_cls)
    return cfg_cls

def get_config(key):
    # 1.创建数据库连接
    conn = sqlite3.connect(db_file)
    # 2.创建游标
    cursor = conn.cursor()
    results = cursor.execute(f"SELECT * FROM t_config where key='{key}'")
    results = results.fetchall()  # 结果转成元组
    cursor.close()  # 关闭cursor对象
    conn.close()  # 关闭数据库连接
    if len(results)==1:
        return json.loads(results[0][1])[key]
    else:
        return None


def add_config(key_values: list):
    # 1.创建数据库连接
    conn = sqlite3.connect(db_file)
    # 2.创建游标
    cursor = conn.cursor()
    for k, v in key_values:
        v = json.dumps({k:v})
        sql = f"insert into t_config values('{k}','{v}')"
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def update_config(key_values: list or tuple):
    # 1.创建数据库连接
    conn = sqlite3.connect(db_file)
    # 2.创建游标
    cursor = conn.cursor()
    if isinstance(key_values,list):
        for k, v in key_values:
            v = json.dumps({k:v})
            sql = f"update t_config set value='{v}' where key='{k}'"
            cursor.execute(sql)
    elif isinstance(key_values,tuple):
        k = key_values[0]
        v = key_values[1]
        v = json.dumps({k:v})
        sql = f"update t_config set value='{v}' where key='{k}'"
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def remove_config(key: list or str):
    # 1.创建数据库连接
    conn = sqlite3.connect(db_file)
    # 2.创建游标
    cursor = conn.cursor()
    if isinstance(key, list):
        for k in key:
            cursor.execute(f"delete from t_config where key='{k}'")
            conn.commit()
    elif isinstance(key, str):
        cursor.execute(f"delete from t_config where key='{key}'")
        conn.commit()
    else:
        raise Exception('key字段格式不符合要求')
    cursor.close()
    conn.close()