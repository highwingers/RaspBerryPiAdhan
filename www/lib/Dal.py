import sqlite3

class Dal:

    connectionString = "/home/pi/RaspBerryPiAdhan/www/data/adhan.db"

    def __init__(self):
        self.conn = sqlite3.connect(Dal.connectionString)

    def AddSetting(self, speaker, lat, lnt, address):
        self.conn.execute("INSERT INTO SETTINGS (ID, SPEAKER,LAT,LNT,ADDRESS)  VALUES (NULL, '" + speaker + "', '" + lat + "','" + lnt + "', '" + address + "' )");
        #print("Record Added")
        self.conn.commit()
        self.conn.close()

    def GetSettings(self):
        cursor = self.conn.execute("SELECT * from SETTINGS")
        # get data by index d[0], d[1] etc etc
        return cursor.fetchone()

    def UpdateSettings(self, ID, SPEAKER,LAT,LNT,ADDRESS):
        sql = "Update SETTINGS                 set SPEAKER = '"+SPEAKER+"',\
                LAT='"+ LAT +"',\
                LNT='"+ LNT +"',\
                ADDRESS='"+ ADDRESS +"' \
            Where ID = 1 "
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()


#Dal().AddSetting('speaker', 'lat', 'lng', '20 ave')
#Dal().UpdateSettings(1,'kitchen2', 'lat1', 'lng2', '20 2 ave')
d = Dal().GetSettings()
print(d)