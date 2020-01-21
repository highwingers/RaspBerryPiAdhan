from __future__ import print_function
from flask import Flask, render_template,request,redirect,jsonify,Response,Blueprint,session
import time
import datetime
import subprocess
from views.index import index_blueprint
from views.address import address_blueprint
from views.speaker import speaker_blueprint
from views.adhanvoice import adhanvoice_blueprint



app = Flask(__name__)
app.secret_key = 'abc123$'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.register_blueprint(address_blueprint)
app.register_blueprint(speaker_blueprint)
app.register_blueprint(adhanvoice_blueprint)
app.register_blueprint(index_blueprint)

@app.route('/settings')
def send_js():
    return render_template('tabs/settings.html')



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

   
   

