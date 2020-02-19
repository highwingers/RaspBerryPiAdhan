from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import pathlib


def reset():
    print("Reseting")
    currentWork = os.getcwd()

    os.system("sudo rm -r " + currentWork + "/RaspBerryPiAdhan")
    os.system("sudo -u pi cp -R " + currentWork + "/orignal_firmware " + currentWork + "/RaspBerryPiAdhan")
    #os.system("sudo chown pi:pi -R " + currentWork + "/RaspBerryPiAdhan")
    #os.system("sudo python3  "+ currentWork +"/RaspBerryPiAdhan/www/index.py")
    os.system("rm -f " + currentWork + "/RaspBerryPiAdhan/www/data/adhan.db")
    os.system("sh " + currentWork + "/RaspBerryPiAdhan/setup/db.sh")
    
    print("Reseting Network")

    netWorkReset = str((pathlib.Path(__file__).parent)) + '/nmcli.sh'
    os.system('sudo bash '+netWorkReset)
    os.system("sudo reboot")

def shutdown():
    reset()
    
    #with open("/home/pi/RaspBerryPiAdhan/www/commands/test.txt", "a") as myfile:
        #myfile.write("Device Reset.")


shutdown_btn = Button(3, hold_time=5)
shutdown_btn.when_held = shutdown

pause()
