from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
from pathlib import Path
import pathlib


def reset_network():
	print("Reseting Network")
	os.system("rm -r /etc/NetworkManager/system-connections/*")
	os.system("sudo reboot")
	#os.system("sudo ip link set wlan0 down && sudo ip link set wlan0 up")
	#os.system("sudo systemctl restart nymea-networkmanager.service")


def reset_software():

    currentWork =  str(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..','..'))) # "/home/pi"   

    _file=open(currentWork + "/resetlog.txt", "a+")
    _file.write("Path: " + currentWork + "/RaspBerryPiAdhan \n")

    print("Reseting Started")    

    
    _file.write(currentWork + "\n")


    os.system("sudo rm -rf " + currentWork + "/RaspBerryPiAdhan")
    os.system("sudo -u pi cp -Rf " + currentWork + "/orignal_firmware " + currentWork + "/RaspBerryPiAdhan")
    os.system("sudo -u pi crontab -r")
    _file.write("Done Restoring \n")

    #os.system("rm -f " + currentWork + "/RaspBerryPiAdhan/www/data/adhan.db")
    #os.system("sh " + currentWork + "/RaspBerryPiAdhan/setup/db.sh")

    #print("Reseting Network")

    os.system("sudo shutdown -r +1")
    _file.write("Shutdown Schedule \n")
    _file.close()

    #netWorkReset = str((pathlib.Path(__file__).parent)) + '/nmcli.sh'
    #os.system('sudo bash '+netWorkReset)
    #_file.write("Networks Reseted")


def shutdown():
    reset()

    #with open("/home/pi/RaspBerryPiAdhan/www/commands/test.txt", "a") as myfile:
        #myfile.write("Device Reset.")
held_for=0.0
def resetInstructions():

    global held_for
    print("released after", held_for, "seconds.")

    if (held_for > 10.0):
        print("Restoring Data Files From Orignal Firmware")
        reset_software()
        _file.write("** Factory Reset Completed ** \n\n")
        held_for = 0.0
    elif (held_for > 5.0):

        reset_network()

	
        #currentWork =  "/home/pi" #str(Path(__file__).parents[3])
        #_file=open(currentWork + "/resetlog.txt", "a+")
        #print("Restarting Bluetooth Service after 5 Seconds")
        #os.system("sudo systemctl restart nymea-networkmanager.service")
        _file.write(" ** Reset Network**  \n\n")

        _file.close()
        held_for = 0.0
    else:
        print("Nothing to do")
        held_for = 0.0

def hld():
        # callback for when button is held
        #  is called every hold_time seconds
        global held_for
        # need to use max() as held_time resets to zero on last callback
        held_for = max(held_for, reset_btn.held_time + reset_btn.hold_time)
        print("held for", held_for, "seconds.")


reset_btn = Button(3, hold_time=1.0, hold_repeat=True)
reset_btn.when_held = hld
reset_btn.when_released  = resetInstructions

pause()

