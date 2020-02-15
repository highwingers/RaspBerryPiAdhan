from gpiozero import Button
from subprocess import check_call
from signal import pause
import os

def shutdown():
    print("Down")
    os.system('bash ./nmcli.sh')
    with open("/home/pi/RaspBerryPiAdhan/www/commands/test.txt", "a") as myfile:
        myfile.write("Device Reset.")


shutdown_btn = Button(3, hold_time=2)
shutdown_btn.when_held = shutdown

pause()
