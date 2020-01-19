from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
from Dal import Dal

adhanvoice_blueprint = Blueprint('adhanvoice', __name__, template_folder='../templates')

@adhanvoice_blueprint.route("/adhanvoice",methods=['GET', 'POST'])
def address():
    speaker =  session['speaker']
    pTimes = session['pTimes']
    _add = session['adhan']['address']

    Dal().UpdateSettings(1,speaker, str(_add["lat"]), str(_add["lng"]), _add["address"].replace("'","''"))

    data= {
        'title': 'Choose Adhan',
        'speaker': speaker,
        'pTimes': pTimes
        }
    return render_template('adhanvoice.html', **data)

