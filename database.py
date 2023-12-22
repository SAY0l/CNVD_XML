import pymysql
from base import Task

Host = "127.0.0.1"
Port = 3306
Username = "root"
Password = "root"
Database = "cnnvd"
Tablename = "cnvd_data"

'''
create table `cnvd_data`(
    cnvd_id varchar(255) primary KEY,
    vulName varchar(255) not null,
    cve_id varchar(255) default null,
    vulType varchar(255) default null,
    hazardLevel varchar(255) default '中',
    vulDesc text default null,
    referUrl text default null,
    patch text default null,
    publishTime datetime
    
)DEFAULT CHARSET=utf8;
'''

def connect_database():
    conn = pymysql.connect(host=Host, port=Port,user=Username, password=Password, database=Database)
    cursor = conn.cursor()
    return conn,cursor

def insert_data(conn,cursor,values):
    sql = "INSERT INTO {} (cnvd_id, vulName,cve_id,vulType,hazardLevel,vulDesc,referUrl,patch,publishTime)\
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(Tablename)
    cursor.executemany(sql,values)

    conn.commit()

def close_database(conn,cursor):
    cursor.close()
    conn.close()

def insert_data_skip(conn,cursor,values):
    sql = "INSERT INTO {} (cnvd_id, vulName,cve_id,vulType,hazardLevel,vulDesc,referUrl,patch,publishTime)\
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(Tablename)
    for v in values:
        try:
            cursor.execute(sql, v)
            conn.commit()
        except Exception as e:
            print("Error occurred:", str(e))
            conn.rollback()


def mysql_insert_data(source_data):
    conn = None
    try:
        conn,cursor = connect_database()
        insert_data(conn,cursor,source_data)
        print(">>> save to database successfully!")
    except pymysql.IntegrityError as ie:
        Task.failure_flag = True
        print(">>> same primary key, exit...",ie)
    except pymysql.Error as e:
        print(">>> database wrong! skip!",e)  
    finally:
        if conn:
            close_database(conn,cursor) # stop版本，可能带来数据丢失

def mysql_insert_data_skip(source_data):
    conn = None
    try:
        conn,cursor = connect_database()
        insert_data_skip(conn,cursor,source_data)
        print(">>> save to database successfully!")
    except pymysql.Error as e:
        print(">>> database wrong! skip!",e)  
    finally:
        if conn:
            close_database(conn,cursor) # skip版本
