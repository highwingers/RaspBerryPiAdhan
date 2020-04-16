import subprocess
from subprocess import Popen
import os
import time
from threading import Thread
from .shellcmds import shellcmd



class wifiUtility:
        
    def scan_wifi_networks(self):
        iwlist_raw = subprocess.Popen(['iwlist', 'scan'], stdout=subprocess.PIPE)
        ap_list, err = iwlist_raw.communicate()
        ap_array = []

        for line in ap_list.decode('utf-8').rsplit('\n'):
            if 'ESSID' in line:
                ap_ssid = line[27:-1]
                if ap_ssid != '':
                    ap_array.append(ap_ssid)

        return ap_array

    def create_wpa_supplicant(self, ssid, wifi_key, country):
        temp_conf_file = open('wpa_supplicant.conf.tmp', 'w')

        temp_conf_file.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n')
        temp_conf_file.write('update_config=1\n')
        temp_conf_file.write('country='+ country +'\n')
        temp_conf_file.write('\n')
        temp_conf_file.write('network={\n')
        temp_conf_file.write('	ssid="' + ssid + '"\n')

        if wifi_key == '':
            temp_conf_file.write('	key_mgmt=NONE\n')
        else:
            temp_conf_file.write('	psk="' + wifi_key + '"\n')

        temp_conf_file.write('	}')

        temp_conf_file.close

        os.system('mv wpa_supplicant.conf.tmp /etc/wpa_supplicant/wpa_supplicant.conf')

    def ChkWifiUp(self):
        cmd = shellcmd().command("wpa_cli -i wlan0 status | grep 'ip_address' 2 >/dev/null")
        print('wifi response ' + cmd + '.')
        if cmd=='':
            return 'DOWN'
        else:
            return 'UP'