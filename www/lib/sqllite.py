#!/usr/bin/python3

import sqlite3, os
import os
from os import path
from pathlib import Path
import sys

class SqlLiteSchema:
    def __init__(self, dbDirectory, dbFound):     

        if dbFound:
            _old = dbDirectory + '/adhan.db'
            _new = dbDirectory + '/copy.db'

            _create = self.createDatabase(_new)
            if _create:
                self.dataImport(_new,_old)
            
        else:
            self.createDatabase(dbDirectory + '/adhan.db')
        
    def createDatabase(self,dbFile):
        if path.exists(dbFile):
            print("File "+ dbFile +" Already Exists!.")
            return False

        conn = sqlite3.connect(dbFile)
        conn.execute('''CREATE TABLE SETTINGS
                 (ID INTEGER PRIMARY KEY ,
                 SPEAKER           TEXT    NOT NULL,
                 LAT            FLOAT     NOT NULL,
                 LNT        FLOAT,
                 METHOD TEXT,
                 ASR TEXT,
                 OFFSET INTEGER,
                 TIMEZONE TEXT,
                 ADDRESS TEXT,
                 SPEAKER_NAME TEXT
                 );''')

        conn.execute('''CREATE TABLE ADHANSETTINGS
                 (ID INTEGER PRIMARY KEY ,
                 ConfigID INTEGER NOT NULL,
                 AdhanID           INTEGER    NOT NULL,
                 AdhanName            TEXT     NOT NULL,
                 AdhanMedia TEXT     NOT NULL,
                 AdhanStatus        INTEGER
                 );''')

        conn.execute('''CREATE TABLE SCHEDULE
                 (ID INTEGER PRIMARY KEY ,
                 TITLE TEXT NOT NULL,
                 RUNAT           TEXT    NOT NULL,
                 STAMP  DATETIME DEFAULT (datetime('now','localtime')),
                 CATEGORY INTEGER,
                 SPEAKER TEXT,
                 STATUS TEXT     TEXT
                 );''')

        conn.execute('''CREATE TABLE LOGS
                 (ID INTEGER PRIMARY KEY ,
                 Speaker TEXT NOT NULL,
                 Media   TEXT NOT NULL,
                 Message TEXT,
                 STAMP  DATETIME DEFAULT (datetime('now','localtime'))         
                 );''')






        conn.execute("INSERT INTO SETTINGS (ID, SPEAKER,LAT,LNT,ADDRESS, METHOD,ASR, OFFSET,TIMEZONE)  VALUES (NULL, '','','','','','', 0,'' )");


        conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,1,'FAJR','/static/media/fajr1.mp3',1)");
        conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,2,'DUHUR','/static/media/azan2.mp3',1)");
        conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,3,'ASR','/static/media/azan3.mp3',1)");
        conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,4,'MAGRIB','/static/media/azan4.mp3',1)");
        conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,5,'ISHA','/static/media/azan5.mp3',1)");



        conn.commit()
        print ("New Database "+ dbFile +" created successfully")
        conn.close

        return True

    def dataImport(self,NewDataBaseFile, OldDataBaseFile):
        

        connOld = sqlite3.connect(OldDataBaseFile)
        
        try:
            connOld.execute('ALTER TABLE SETTINGS ADD COLUMN SPEAKER_NAME;')
            connOld.executescript("""ATTACH DATABASE '"""+ NewDataBaseFile +"""' AS NewDataBaseFile;
                                    Update SETTINGS Set SPEAKER_NAME = (Select SPEAKER_NAME From NewDataBaseFile Limit 1)
            """)
        except:
            pass # handle the error
        connOld.close()

        connNew = sqlite3.connect(NewDataBaseFile)
        
        connNew.executescript("""ATTACH DATABASE '"""+ OldDataBaseFile +"""' AS OldDataBaseFile;
                        
                        DELETE From  SETTINGS;
                        INSERT INTO SETTINGS (SPEAKER,LAT,LNT,ADDRESS, METHOD,ASR, OFFSET,TIMEZONE,SPEAKER_NAME)
                        SELECT SPEAKER,LAT,LNT,ADDRESS, METHOD,ASR, OFFSET,TIMEZONE,SPEAKER_NAME From OldDataBaseFile.SETTINGS;    

                        DELETE From SCHEDULE;
                        INSERT into SCHEDULE(TITLE,RUNAT,STAMP,CATEGORY,SPEAKER,STATUS) Select TITLE,RUNAT,STAMP,CATEGORY,SPEAKER,STATUS From OldDataBaseFile.SCHEDULE;
                        
                        DELETE From ADHANSETTINGS;
                        INSERT INTO ADHANSETTINGS (ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus) Select ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus from OldDataBaseFile.ADHANSETTINGS;

                        """)
        os.remove(OldDataBaseFile)
        os.rename(NewDataBaseFile,OldDataBaseFile)
        print("Import Successfull")
        connNew.close()

        #conn.execute("INSERT INTO SETTINGS (ID, SPEAKER,LAT,LNT,ADDRESS, METHOD,ASR, OFFSET,TIMEZONE)  VALUES (NULL, '','','','','','', 0,'' )");
        #conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,1,'FAJR','/static/media/fajr1.mp3',1)");
        #conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,2,'DUHUR','/static/media/azan2.mp3',1)");
        #conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,3,'ASR','/static/media/azan3.mp3',1)");
        #conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,4,'MAGRIB','/static/media/azan4.mp3',1)");
        #conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,5,'ISHA','/static/media/azan5.mp3',1)");




##cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
##for row in cursor:
##   print ("NAME = ", row[1], "\n")
##
##
##
##	
#conn.execute('drop table if exists company;')





#conn.close()p



def readParam():
    _dbFlag=False
    _path = str(Path(__file__).parent.parent) + '/data'
    if sys.argv[1]=='True':
        _dbFlag = True
    else:
        _dbFlag = False
    SqlLiteSchema(_path, _dbFlag)


readParam()
