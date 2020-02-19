from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
from pathlib import Path
import pathlib


def reset():
    print("Reseting")

    _file=open("/home/pi/resetlog.txt", "a+")



    currentWork = str(Path(__file__).parents[3])

    _file.write(currentWork)


    os.system("sudo rm -r " + currentWork + "/RaspBerryPiAdhan")
    os.system("sudo -u pi cp -R " + currentWork + "/orignal_firmware " + currentWork + "/RaspBerryPiAdhan")

    os.system("rm -f " + currentWork + "/RaspBerryPiAdhan/www/data/adhan.db")
    os.system("sh " + currentWork + "/RaspBerryPiAdhan/setup/db.sh")

    print("Reseting Network")

    os.system("sudo shutdown -r +1")

    netWorkReset = str((pathlib.Path(__file__).parent)) + '/nmcli.sh'
    os.system('sudo bash '+netWorkReset)


def shutdown():
    reset()

    #with open("/home/pi/RaspBerryPiAdhan/www/commands/test.txt", "a") as myfile:
        #myfile.write("Device Reset.")


shutdown_btn = Button(3, hold_time=3)
shutdown_btn.when_held = shutdown

pause()
