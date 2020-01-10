import sys
sys.path.append('../')
from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
from lib.chromecast import chromecast

speaker_blueprint = Blueprint('speaker', __name__, template_folder='../templates')
@speaker_blueprint.route("/speaker",methods=['GET', 'POST'])
def speaker():
    data= {
        'title': 'Choose Speaker',
        }

    if request.method == 'POST':
        _spk = request.form["speaker"]
        session['adhan']['speaker'] = { "speaker": _spk}
        return redirect("adhanvoice")

    return render_template('speaker.html', **data)



@speaker_blueprint.route("/speakerlist",methods=['GET'])
def speakerlist():
    chromecasts = chromecast().chromecastQuery()
     
    data= {
        'chromecasts': chromecasts
        }
    return jsonify(chromecasts)