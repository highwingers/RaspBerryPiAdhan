#!/usr/bin/python3

import sqlite3, os

dir = os.path.abspath(os.path.join('', '..'))
print(dir)
conn = sqlite3.connect(dir + '/www/data/adhan.db')
#print "Opened database successfully";


conn.execute('''CREATE TABLE SETTINGS
         (ID INTEGER PRIMARY KEY ,
         SPEAKER           TEXT    NOT NULL,
         LAT            FLOAT     NOT NULL,
         LNT        FLOAT,
         METHOD TEXT,
         OFFSET INTEGER,
         TIMEZONE TEXT,
         ADDRESS TEXT);''')

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
         STATUS TEXT     TEXT
         );''')



conn.execute("INSERT INTO SETTINGS (ID, SPEAKER,LAT,LNT,ADDRESS, METHOD, OFFSET,TIMEZONE)  VALUES (NULL, '','','','','', 0,'' )");


conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,1,'FAJR','/static/media/fajr1.mp3',1)");
conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,2,'DUHUR','/static/media/azan2.mp3',1)");
conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,3,'ASR','/static/media/azan3.mp3',1)");
conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,4,'MAGRIB','/static/media/azan4.mp3',1)");
conn.execute("INSERT INTO ADHANSETTINGS (ID, ConfigID,AdhanID,AdhanName,AdhanMedia, AdhanStatus)  VALUES (NULL,1,5,'ISHA','/static/media/azan5.mp3',1)");



conn.commit()
print ("Records created successfully")




##cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
##for row in cursor:
##   print ("NAME = ", row[1], "\n")
##
##
##
##	
#conn.execute('drop table if exists company;')





conn.close()
