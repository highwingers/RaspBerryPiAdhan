from __future__ import print_function
from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
import http
import os, sys
import time
import datetime
import subprocess
import json
from datetime import datetime
from dateutil.parser import parse
import getpass
from pathlib import Path

from views.speaker import speaker_blueprint
from lib.Dal import Dal
from lib.shellcmds import shellcmd
from lib.PrayerPy import PrayerData
from lib.GeoPy import GeoData
from lib.schedule import schedule
from lib.utility import utility
from lib.poco.BlueToothDevice import BlueToothDevice

app = Flask(__name__)

app.secret_key = 'abc123$'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#app.register_blueprint(address_blueprint)
app.register_blueprint(speaker_blueprint)
#app.register_blueprint(adhanvoice_blueprint)
#app.register_blueprint(index_blueprint)
_rootPath = os.path.abspath(os.path.dirname( __file__ ))

def getConfigSettings(id):
        _settings = Dal().GetSettings(id)
        if _settings is None:
            return '0'
        else:
            return _settings


@app.route("/",methods=['GET', 'POST'])
def index():
    data= {
        'title': 'Smart Adhan Player',
        'username' : getpass.getuser()
        }    
    
    return render_template('tabs/config.html', **data)
@app.route('/config')
def config():
    data={'title': 'Configure Device'}
    shellcmd().command("pwd > ./index-path.txt",False)
    return render_template('tabs/config.html', **data)
@app.route('/settings')
def settings():
    _settings = getConfigSettings(1) 
    data= {
    'settings': _settings,
    'title': 'Settings'
    }
    return render_template('tabs/settings.html', **data)
@app.route('/support')
def support():
    data= {'username' : getpass.getuser(),
           'title': 'Support'
           }
    return render_template('tabs/support.html', **data)

@app.route('/history')
def history():
    try:
        _jobs = schedule().queryJobs()
        _time = shellcmd().command("date")
        _logs = Dal().GetLogs(50)
        data= {
        'Jobs': _jobs,
        'shellTime': _time,
        'pythonTime': datetime.now(),
        'title': 'History',
        'logs': _logs
        }
        return render_template('tabs/history.html', **data)
    except Exception as e : 
        return render_template('tabs/history.html')




@app.route('/api/getData')
def getSettings():
        id = request.args.get("id")
        return jsonify(getConfigSettings(1)  )

@app.route('/api/updateSoftware', methods=['POST'])
def updateSoftware():
        #c = shellcmd().command("sudo sh update.sh")
        c2 = shellcmd().command("sudo -u pi git reset --hard && sudo -u pi git pull")
        c3 = shellcmd().command("sudo sh  ../setup/setup.sh")


        return jsonify(True)

@app.route('/api/getAdhanSettings')
def getAdhanSettings():
        id = request.args.get("id")
        _data = Dal().GetAdhanSettings(id)
        return jsonify( _data )


@app.route('/api/deleteJob', methods=['POST'])
def deleteJob():
    _param = json.loads(request.data)
    _jobid = _param["jobid"].strip()
    r = schedule().deleteJob(_jobid)
    return jsonify( r )

@app.route('/api/updateAdhanSettings',methods=['POST'])
def updateAdhanSettings():
    try:
        _settings = json.loads(request.form["AdhanSettings"])
        _update = Dal().updateAdhanSettings(_settings)
        schedule().scheduleAdhans(1,_rootPath + '/commands/player.py')
        return jsonify(1)
    except Exception as e :
        return 'Error: ' + print(str(e))

@app.route('/api/addCustomSchedule',methods=['POST'])
def addCustomSchedule():
    try:
        _settings = json.loads(request.form["AdhanSettings"])
        _date = _settings["datetime"]
        if _date.find("/") == -1:
            _datetime = parse(str(datetime.now().date()) + " " + _date)
        else:
            _datetime = parse(_date)

        #print(_datetime)

        schedule().AddSchedule(1, _datetime ,_settings["title"],os.path.abspath('commands/player.py'),_settings["surah"], _settings["frequency"],_settings["speaker"])
        return jsonify(1)
    except Exception as e :
            return 'Error: ' + str(e)


@app.route('/api/configureDevice',methods=['POST'])
def configureDevice():

    try:
        address = request.form["address"]
        speaker = request.form["speaker"]
        speakername = request.form["speakername"]
        method = request.form["method"]
        timezone = request.form["timezone"]
        asr = request.form["asr"]
        isBluetooth = len(speaker.split(':'))
        shellcmd().setTimeZone(timezone)
        timezoneOffset =  shellcmd().getZoneOffset()

        if isBluetooth > 5:
            shellcmd().setBluetoothSpeaker(speaker)
        else:
            shellcmd().command("rm ~pi/.asoundrc")

        _add = GeoData(address, "adhan_player_piZero")
        coords = _add.getCoords()

        if _add.status==0:
            return "Address was not Verified"

        #return _add.address

        result = Dal().UpdateSettings(1, speaker,speakername,_add.lat, _add.lng, _add.address, method, asr , timezoneOffset, timezone)
        if result is not True:
             return result
        #Below Call with Schedule Adhans for Today
        scheduleAdhan = schedule().scheduleAdhans(1,_rootPath + '/commands/player.py')
        
        if not scheduleAdhan:
            return "Could not schedule Adhans " + scheduleAdhan
        Dal().LogEntry(speakername, '', "Deviced Configured")
        return "Success"
    except Exception as e:
        Dal().LogEntry(speakername, '', "Deviced Config Error")
        return "Something Went Wrong " + str(e)

@app.route("/api/exeCommand",methods=['POST'])
def exeCommand():
    content = request.get_json(silent=True)
    qry = content.get('query')
    if qry==1:
        _reboot = shellcmd().command("sudo shutdown -r +1")
        return "Device is rebooting now. Please Hit 'OK' button and wait for 'APP' to reload. (Approx. 3 minutes)"

    return "Nothing to Execute"

@app.route("/api/bluetooth/scan",methods=['GET'])
def scanbluetooth():
    _d = shellcmd().command("{   printf 'scan on\n\n';     sleep 10;     printf 'devices\n\n';     printf 'quit\n\n'; } | bluetoothctl | grep ^Device", False)
    list = []  
    for line in _d.splitlines():
        _arr = line.split(None, 2)
        _mac = _arr[1]
        _devicename = _arr[2]
        list.append( BlueToothDevice(_mac, _devicename).__dict__) 

    return json.dumps(list)
@app.route("/api/bluetooth/connect",methods=['POST'])
def connectbluetooth():
    # E4:F0:42:51:C7:72 
    #_mac = request.args.get("mac")
    content = request.get_json(silent=True)
    _mac = content.get('mac')
    _d = shellcmd().command("{   printf 'trust "+ _mac +"\n\n';     sleep 5;     printf 'pair "+ _mac +"\n\n';     sleep 5;     printf 'connect "+ _mac +"\n\n';     sleep 5; } | bluetoothctl", False)
    return _d
@app.route("/api/bluetooth/disconnect",methods=['GET'])
def disconnectbluetooth():
    _mac = request.args.get("mac")
    _d = shellcmd().command("{   printf 'disconnect "+ _mac +"\n\n';     sleep 5;      } | bluetoothctl", False)
    return _d
@app.route("/api/bluetooth/remove",methods=['GET'])
def removebluetooth():
    # un pair
    _mac = request.args.get("mac")
    _d = shellcmd().command("{   printf 'remove "+ _mac +"\n\n';     sleep 5;      } | bluetoothctl", False)
    return _d
@app.route("/api/bluetooth/info",methods=['GET'])
def infobluetooth():
    #if returns EMPTY, it was NEVER Paired in past
    #if returns Connected:no then just use the Connect method and all set
    #if returns Connected:yes just play media
    _mac = request.args.get("mac")
    print("{  printf 'info  "+ _mac +"\n\n';  sleep 2;printf 'quit\n\n';} | bluetoothctl | grep Connected")
    _d = shellcmd().command("{  printf 'info  "+ _mac +"\n\n';  sleep 2;printf 'quit\n\n';} | bluetoothctl | grep Connected", False)
    return _d







if __name__ == "__main__":
    
    _port =  int(utility.ConfigSectionMap("SetUp")["port"])

    #print("PORT IS " + _port )

    app.run(host='0.0.0.0', port=_port, debug=True)


   
   

