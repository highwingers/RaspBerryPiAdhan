import sys
sys.path.append('/home/pi/RaspBerryPiAdhan/www/lib')

from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
import datetime
from GeoPy import GeoData
from PrayerPy import PrayerData
from shellcmds import shellcmd
from schedule import schedule

address_blueprint = Blueprint('address', __name__, template_folder='../templates')


@address_blueprint.route("/address",methods=['GET', 'POST'])
def address():
    data = {
        'title': 'Enter your full address'
        }

    schedule.adhan(40.726116, -73.520770,"https://staticcrate.com/content/audio-pro/wwstrxylo-note-3.mp3", "https://staticcrate.com/content/audio-pro/wwstrxylo-note-3.mp3", "Office Ustairs speaker")

    if request.method == 'POST':

        timezone = request.form["timezone"]
        shellcmd().setTimeZone(timezone)

        _add = GeoData(request.form["address"], "adhan_player")
        coords = _add.getCoords()
        
        session['adhan'] = {"address": {"address": _add.address, "lat": _add.lat, "lng": _add.lng, "status":_add.status}}
        return redirect("address_confirm")

    return render_template('address.html', **data)

@address_blueprint.route("/address_confirm",methods=['GET', 'POST'])
def address_confirm():        

        sesData = session['adhan']['address']
        currentTime = shellcmd().command("date")
        if sesData["status"] == 1 :
            timezoneOffset =  shellcmd().getZoneOffset()
            pTimes = PrayerData(sesData["lat"],sesData["lng"], timezoneOffset).getTimes()
            session['pTimes'] = pTimes
        else:
            pTimes = None

        data = {
        'title': "Confirm Address",
        'address': sesData,
        "pTimes": pTimes,
        "deviceTime": currentTime
        }
        return render_template('address_confirm.html', **data)
