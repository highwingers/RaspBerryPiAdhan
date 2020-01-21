from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session


index_blueprint = Blueprint('index', __name__, template_folder='../templates')

@index_blueprint.route("/",methods=['GET', 'POST'])
def address():
    data= {
        'title': 'Smart Adhan Player'

        }
    return render_template('index.html', **data)
