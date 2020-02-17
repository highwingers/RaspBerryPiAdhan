from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import pathlib


def reset():
    print("Reseting")
    codeDirectory = str(os.getcwd()) + '/RaspBerryPiAdhan'

    os.system("sudo rm -r " + codeDirectory)
    os.system("git clone https://github.com/highwingers/RaspBerryPiAdhan.git")

    print("Reseting Network")

    netWorkReset = str((pathlib.Path(__file__).parent)) + '/nmcli.sh'

def shutdown():
    reset()
    #os.system('sudo bash '+netWorkReset)
    #with open("/home/pi/RaspBerryPiAdhan/www/commands/test.txt", "a") as myfile:
        #myfile.write("Device Reset.")


shutdown_btn = Button(3, hold_time=5)
shutdown_btn.when_held = shutdown

pause()
