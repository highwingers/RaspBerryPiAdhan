from __future__ import print_function
from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
import http
import os, sys
import time
import datetime
import subprocess
import json
from datetime import datetime
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

def getConfigSettings(id):
        _settings = Dal().GetSettings(id)
        if _settings is None:
            return '0'
        else:
            return _settings


@app.route("/",methods=['GET', 'POST'])
def index():
    data= {
        'title': 'Smart Adhan Player'
        }
    return render_template('index.html', **data)
@app.route('/config')
def config():
    return render_template('tabs/config.html')
@app.route('/settings')
def settings():
    _settings = getConfigSettings(1) 
    data= {
    'settings': _settings
    }
    return render_template('tabs/settings.html', **data)

@app.route('/api/getData')
def getSettings():
        id = request.args.get("id")
        return jsonify(getConfigSettings(1)  )

@app.route('/api/getAdhanSettings')
def getAdhanSettings():
        id = request.args.get("id")
        _data = Dal().GetAdhanSettings(id)
        return jsonify( _data )

@app.route('/api/updateAdhanSettings',methods=['POST'])
def updateAdhanSettings():
    try:
        _settings = json.loads(request.form["AdhanSettings"])
        _update = Dal().updateAdhanSettings(_settings)
        schedule().scheduleAdhans(1,os.path.abspath('commands/player.py'))
        return jsonify(1)
    except Exception as e :
        return 'Error: ' + print(str(e))

@app.route('/api/addCustomSchedule',methods=['POST'])
def addCustomSchedule():
    try:
        _settings = json.loads(request.form["AdhanSettings"])
        print(_settings)
        schedule().AddSchedule(1, datetime.strptime(_settings["datetime"],"%m/%d/%Y %I:%M %p") ,_settings["title"],os.path.abspath('commands/player.py'),_settings["surah"], _settings["frequency"])
        return jsonify(1)
    except Exception as e :
            return 'Error: ' + str(e)


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
        scheduleAdhan = schedule().scheduleAdhans(1,os.path.abspath('commands/player.py'))
        
        if not scheduleAdhan:
            return "Could not schedule Adhans " + scheduleAdhan

        return "Success"
    except Exception as e:
        return "Something Went Wrong " + str(e)





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


   
   

