#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('/home/pi/RaspBerryPiAdhan/www/data/adhan.db')
#print "Opened database successfully";


conn.execute('''CREATE TABLE SETTINGS
         (ID INT PRIMARY KEY     NOT NULL,
         SPEAKER           TEXT    NOT NULL,
         LAT            TEXT     NOT NULL,
         LNT        TEXT,
         ADDRESS TEXT);''')

##conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
##
##conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
##
##conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
##
##conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");



conn.commit()
print ("Records created successfully")




##cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
##for row in cursor:
##   print ("NAME = ", row[1], "\n")
##
##
##
##	
##conn.execute('drop table if exists company;')





conn.close()
