import sys
sys.path.append('../')

from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
import datetime
from lib.GeoPy import GeoData
from lib.PrayerPy import PrayerData
from lib.shellcmds import shellcmd

address_blueprint = Blueprint('address', __name__, template_folder='../templates')


@address_blueprint.route("/address",methods=['GET', 'POST'])
def address():
    data = {
        'title': 'Enter your full address'
        }



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
