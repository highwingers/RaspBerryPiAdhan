import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))

from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
from lib.chromecast import chromecast



speaker_blueprint = Blueprint('speaker', __name__, template_folder='../templates')

@speaker_blueprint.route("/speaker/api/speakerlist",methods=['GET'])
def speakerlist():
    chromecasts = chromecast().chromecastQuery()

    return jsonify(chromecasts)

@speaker_blueprint.route("/speaker/api/playMedia",methods=['GET'])
def playMedia():
    device = request.args.get('deviceName')
    media = request.args.get('mediaUrl')
    mediaStatus = chromecast().play(device, media)     
    return mediaStatus