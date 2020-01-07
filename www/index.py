from __future__ import print_function
from flask import Flask, render_template,request,redirect
import time
import pychromecast
import datetime
import subprocess


app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   output = scan_wifi_networks() #subprocess.check_output(["iwlist","scan"])
   chromecasts = pychromecast.get_chromecasts()
   cc_array=[]


   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
	  'wifioutput': output,
	  'chromecasts':chromecasts
		}
   return render_template('index.html', **templateData)


@app.route("/address",methods=['GET', 'POST'])
def address():
    data= {
        'title': 'Enter your full address'
        }
    if request.method == 'POST':
        return redirect("speaker", code=302)

    return render_template('address.html', **data)

@app.route("/speaker",methods=['GET', 'POST'])
def speaker():
    data= {
        'title': 'Choose Speaker',
        'chromecasts': pychromecast.get_chromecasts()
        }
    if request.method == 'POST':
        a=1

    return render_template('speaker.html', **data)



def scan_wifi_networks():
	iwlist_raw = subprocess.Popen(['iwlist', 'scan'], stdout=subprocess.PIPE)
	ap_list, err = iwlist_raw.communicate()
	ap_array = []

	for line in ap_list.decode('utf-8').rsplit('\n'):
		if 'ESSID' in line:
			ap_ssid = line[27:-1]
			if ap_ssid != '':
				ap_array.append(ap_ssid)

	return ap_array

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
   

