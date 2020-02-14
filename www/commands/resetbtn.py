from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    print("Down")
    with open("/home/pi/RaspBerryPiAdhan/www/commands/test.txt", "a") as myfile:
        myfile.write("appended text")

shutdown_btn = Button(3, hold_time=2)
shutdown_btn.when_held = shutdown

pause()
