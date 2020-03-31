import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))

from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
from lib.chromecast import chromecast
from lib.shellcmds import shellcmd



speaker_blueprint = Blueprint('speaker', __name__, template_folder='../templates')

@speaker_blueprint.route("/speaker/api/speakerlist",methods=['GET'])
def speakerlist():
    chromecasts = chromecast().chromecastQuery()

    return jsonify(chromecasts)

@speaker_blueprint.route("/speaker/api/playMedia",methods=['GET'])
def playMedia():
    device = request.args.get('deviceName') # either a chrome or bluetooth
    media = request.args.get('mediaUrl')
    isBluetooth = len(device.split(':'))

    if isBluetooth > 5:
        _play = shellcmd().playBlueToothMedia(device, media)
        return _play
    else:
        mediaStatus = chromecast().play(device, media)     
        return mediaStatus

    return "error"