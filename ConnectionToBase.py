#creating python class for mysql workbench
import mysql.connector as mysql
from mysql.connector import MySQLConnection,Error

class ConnectionToBase:
    def get_connection(self):
        return mysql.connect(user='root',host='127.0.0.1',passwd='',database='test2')
    def close_connection(self,conn):
        if conn:
            conn.close()    
    def __init__(self):
        self.__db = self.get_connection()
        self.__cursor = self.__db.cursor()
    def input_schemas(self):
        print('show schemas')
        shema = str(input())
        query = "USE "+ shema
        print(query)
        self.__cursor.execute(query)
    def show_schema(self):
        self.__cursor.execute("SHOW SCHEMAS")
        data = self.__cursor.fetchall()
        for d in data:
            print(d)  
    def create_schema(self):
        print("create schema")
        shema = str(input())
        query = "CREATE SCHEMA "+ shema
        self.__cursor.execute(query)
        print(self.__cursor.fetchall())
        self.__db.commit()  
    def create_table(self):
        print("Choose schema")
        shema = str(input())
        query = "USE "+ shema
        print(query)
        print("create table")
        table = str(input())
        query_table = "CREATE TABLE "+ table+'(id int(11) not null primary key auto_increment)'
        self.__cursor.execute(query_table)
        print(self.__cursor.fetchall())
        self.__db.commit()         
    def show_tables(self):
        self.__cursor.execute("SHOW TABLES")
        tables = self.__cursor.fetchall()
        for table in tables:
            print(table)    
    def add_column(self):
        print("chose table")
        table = str(input())
        print("Add column")
        self.__cursor.execute("ALTER TABLE "+table+' ADD COLUMN '+ str(input()) +' ;')
        print(self.__cursor.fetchall())
        self.__db.commit()  
    def table_content(self,table):
        self.__cursor.execute("SELECT * FROM "+table)
        data = self.__cursor.fetchall()
        for d in data:
            print(d)    
    def delete_column(self,table,column):
        self.__cursor.execute("ALTER TABLE "+table+' DROP COLUMN '+ column)   
        data = self.__cursor.fetchall()
        for d in data:
            print(d)  
    def delete_by_id(self,table,id):
        try:
            self.__cursor.execute("DELETE FROM "+table+' WHERE id = '+str(id))
            data = self.__cursor.fetchall()
            for d in data:
                print(d)
            self.__db.commit()
        except (Exception,mysql.Error) as error:
            print('error while getting data',error)
            self.__db.rollback() 
    def truncate_table(self,table):
        try:
            self.__cursor.execute("TRUNCATE "+ table)
            data = self.__cursor.fetchall()
            for d in data:
                print(d)
            self.__db.commit()
        except (Exception,mysql.Error) as error:
            print('error while getting data',error)
            self.__db.rollback()  
    def insert_data(self,fname,lname):
        try:
            query = "INSERT INTO korisnik (fname,lname) VALUES (%s, %s)"
            data = [fname,lname]
            self.__cursor.execute(query,data)
            self.__db.commit()
            records = self.__cursor.fetchall()
            for r in records:
                print(r)
        except (Exception,mysql.Error) as error:
            print("error while getting data",error)
            self.__db.rollback()   
    def show_index(self,table):
        try:
            self.__cursor.execute("SHOW INDEX FROM "+ table)
            data = self.__cursor.fetchall()
            for d in data:
                print(d)
        except (Exception,mysql.Error) as error:
            print("error while getting data",error)
            self.__db.rollback()  
    def update_table(self,table,col1,val1,id):
        try:
            query_update = "UPDATE "+table +" SET "+str(col1)+" = "+str(val1)+" WHERE id = "+str(id)+";"
            self.__cursor.execute(query_update)
            self.__db.commit()
            records = self.__cursor.fetchall()
            for r in records:
                print(r)
        except (Exception,mysql.Error) as error:
            print("error while getting data",error)
            self.__db.rollback()                                                         
b = ConnectionToBase()










