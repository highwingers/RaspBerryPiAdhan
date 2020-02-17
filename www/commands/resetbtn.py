from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import pathlib


def reset():
    print("Reseting")

    os.system("sudo rm -r RaspBerryPiAdhan")
    os.system("sudo cp -R orignal_firmware RaspBerryPiAdhan")
    os.system("sudo chown pi:pi -R RaspBerryPiAdhan")

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
