import sys
sys.path.append('../')

from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session


adhanvoice_blueprint = Blueprint('adhanvoice', __name__, template_folder='../templates')

@adhanvoice_blueprint.route("/adhanvoice",methods=['GET', 'POST'])
def address():
    speaker =  session['speaker']
    data= {
        'title': 'Choose Adhan'
        }
    return render_template('adhanvoice.html', **data)

