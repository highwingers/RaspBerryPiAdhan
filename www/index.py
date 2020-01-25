from __future__ import print_function
from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
import time
import datetime
import subprocess
#from views.index import index_blueprint
#from views.address import address_blueprint
from views.speaker import speaker_blueprint
#from views.adhanvoice import adhanvoice_blueprint
from lib.Dal import Dal
from lib.shellcmds import shellcmd
from lib.PrayerPy import PrayerData
from lib.GeoPy import GeoData
from lib.schedule import schedule


app = Flask(__name__)

app.secret_key = 'abc123$'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#app.register_blueprint(address_blueprint)
app.register_blueprint(speaker_blueprint)
#app.register_blueprint(adhanvoice_blueprint)
#app.register_blueprint(index_blueprint)


@app.route("/",methods=['GET', 'POST'])
def index():
    data= {
        'title': 'Smart Adhan Player'
        }
    return render_template('index.html', **data)
@app.route('/settings')
def settings():
    return render_template('tabs/settings.html')

@app.route('/api/getData')
def getSettings():
    try:
        id = request.args.get("id")
        data = Dal().GetSettings(id)
        return jsonify(data)
    except :
        return jsonify(0)

    

@app.route('/api/configureDevice',methods=['POST'])
def configureDevice():

    try:
        address = request.form["address"]
        speaker = request.form["speaker"]
        method = request.form["method"]
        timezone = request.form["timezone"]
    
        shellcmd().setTimeZone(timezone)
        timezoneOffset =  shellcmd().getZoneOffset()

        _add = GeoData(address, "adhan_player")
        coords = _add.getCoords()

        if _add.status==0:
            return "Address was not Verified"

        #return _add.address

        result = Dal().UpdateSettings(1, speaker,_add.lat, _add.lng, _add.address, method, timezoneOffset, timezone)
        if result is not True:
             return result
        #Below Call with Schedule Adhans for Today
        scheduleAdhan = schedule().scheduleAdhans(1)
        if not scheduleAdhan:
            return "Could not schedule Adhans " + scheduleAdhan

        return "Success"
    except Exception as e:
        return "Something Went Wrong " + str(e)





if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)


   
   

