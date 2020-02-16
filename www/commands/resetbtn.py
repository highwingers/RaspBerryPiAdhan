from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import pathlib


currentPhysicalDirectory = str((pathlib.Path(__file__).parent)) + '/nmcli.sh'

def shutdown():
    print("Down")
    os.system('sudo bash '+currentPhysicalDirectory)
    #with open("/home/pi/RaspBerryPiAdhan/www/commands/test.txt", "a") as myfile:
        #myfile.write("Device Reset.")


shutdown_btn = Button(3, hold_time=2)
shutdown_btn.when_held = shutdown

pause()
