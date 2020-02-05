import sqlite3,os

class Dal:

    connectionString =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')) + "/data/adhan.db"
    #print(connectionString)
    def __init__(self):
        self.conn = sqlite3.connect(Dal.connectionString)

    def AddSetting(self, speaker, lat, lnt, address):
        self.conn.execute("INSERT INTO SETTINGS (ID, SPEAKER,LAT,LNT,ADDRESS)  VALUES (NULL, '" + speaker + "', '" + lat + "','" + lnt + "', '" + address + "' )");
        #print("Record Added")
        self.conn.commit()
        self.conn.close()

    def AddSchedule(self, TITLE, RUNAT, CATEGORY, SPEAKER):
        try:
            TITLE = TITLE.replace("'","''").strip()
            SPEAKER = SPEAKER.replace("'","''")
            self.conn.execute("INSERT INTO SCHEDULE (ID,TITLE, RUNAT, CATEGORY, SPEAKER)  VALUES (NULL, '" + TITLE + "', '" + RUNAT + "', '"+ str(CATEGORY) +"',  '"+ SPEAKER +"' )");
            #print("Record Added")
            self.conn.commit()
            self.conn.close()
        except Exception as e :
            print(str(e))

    def DeleteSchedule(self, TITLE):
        try:
            _sql="DELETE FROM SCHEDULE WHERE TITLE='"+ TITLE.replace("'","''") + "'"
            self.conn.execute(_sql);
            print(_sql)
            self.conn.commit()
            self.conn.close()
        except Exception as e :
            print(str(e))


    def GetSettings(self, id):
        try:
            cursor = self.conn.execute("SELECT * from SETTINGS Where ID = '"+ str(id) +"'")
            # get data by index d[0], d[1] etc etc
            return cursor.fetchone()
        except :
            return None

    def GetAdhanSettings(self, id):
        try:
            cursor = self.conn.execute("SELECT * from ADHANSETTINGS Where ConfigID = '"+ str(id) +"'")
            # get data by index d[0], d[1] etc etc
            return cursor.fetchall()
        except :
            return None

    def updateAdhanSettings(self,lst):
        for adhan in lst:
            AdhanMedia = adhan["AdhanMedia"]
            AdhanID= adhan["AdhanID"]
            AdhanStatus= adhan["AdhanStatus"]
            sql = "UPDATE ADHANSETTINGS Set AdhanStatus='"+ str(AdhanStatus) +"', AdhanMedia='"+ AdhanMedia +"' where AdhanID='"+ str(AdhanID) +"'"
            self.conn.execute(sql)
            self.conn.commit()
            
        self.conn.close()
        return True





    def UpdateSettings(self, ID, SPEAKER,LAT,LNT,ADDRESS, METHOD, ASR, OFFSET, TIMEZONE):
        try:
            sql = "Update SETTINGS SET speaker='"+ SPEAKER.replace("'", "''") +"', LAT='"+ str(LAT)+ "', LNT='"+ str(LNT) +"', METHOD='"+ METHOD +"', OFFSET='"+ str(OFFSET) +"', ADDRESS='"+ ADDRESS.replace("'","''") +"', TIMEZONE='"+ TIMEZONE +"', ASR='" + ASR + "'  Where ID = 1 "
            self.conn.execute(sql)
            self.conn.commit()
            self.conn.close()
            return True
        except Exception as e:
            return str(e)



#Dal().AddSetting('speaker', 'lat', 'lng', '20 ave')
#Dal().UpdateSettings(1,'kitchen2', 'lat1', 'lng2', '20 2 ave')
#d = Dal().GetSettings()
#print(d)
