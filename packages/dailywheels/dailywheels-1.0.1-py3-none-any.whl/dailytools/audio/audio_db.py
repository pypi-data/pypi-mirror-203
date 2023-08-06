# -*- coding: utf-8 -*
import sqlite3
from dailytools.__exceptions import *
from typing import *

class AudioData:
    def __init__(self):
        pass
        
    def connect(self, db_path: str):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.audiodb_name = "audio_content"
        self.create_table(self.audiodb_name)
        
    def create_table(self, table_name: str):
        try:
            self.cursor = self.conn.cursor()
            sql = '''create table IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                msg TEXT, 
                format CHARACTER(8) NOT NULL, 
                data BLOB NOT NULL,
                create_time timestamp not null default (datetime('now','localtime')),  
                is_delete BOOLEAN not null DEFAULT (False))'''.format(table_name)
            self.cursor.execute(sql)
        except AttributeError as e:
            raise AttributeError("Database Not Found: {}".format(e.__str__()))
        
    def insert_data(self, msg: str, audio, audio_format:str, **kwargs):
        table_name = kwargs.get("table_name", self.audiodb_name)
        
        try:
            sql_cmd = '''insert into {} (msg, format, data) 
            VALUES (?, ?, ?)'''.format(table_name)
            data_tuple = (msg, audio_format, audio)
            self.cursor.execute(sql_cmd, data_tuple)
            self.conn.commit()
        except AttributeError as e:
            raise e
        except Exception as e:
            raise DBInsertError(e.__str__())

    def find_audio(self, msg: str, **kwargs) -> List[str]:
        table_name = kwargs.get("table_name", self.audiodb_name)
        try:
            sql_cmd = '''select format, data from {} where msg="{}" and is_delete=0;'''.format(table_name, msg)
            self.cursor.execute(sql_cmd)
            rows = self.cursor.fetchall()
        except Exception as e:
            raise DBSearchError(e.__str__())
        result = []
        for r in rows:
            result.append({"fmt": r[0], "data": r[1]})
        return result
        
    def delete_audio(self, msg: str):
        try:
            sql_cmd = '''update ...'''
            self.cursor.execute(sql_cmd)
        except AttributeError as e:
            pass
    
    def close(self):
        self.conn.close()      