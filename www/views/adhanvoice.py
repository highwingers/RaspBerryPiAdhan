import sys
sys.path.append('../')

from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session


adhanvoice_blueprint = Blueprint('adhanvoice', __name__, template_folder='../templates')

@adhanvoice_blueprint.route("/adhanvoice",methods=['GET', 'POST'])
def address():
    sesData =  session['adhan']['speaker']
    data= {
        'title': 'Choose Adhan',
        'ses': sesData
        }
    return render_template('adhanvoice.html', **data)

