from datetime import datetime
import sys


a = sys.argv[1]

##for arg in sys.argv:
##    a = arg
    


myFile = open('/home/pi/RaspBerryPiAdhan/www/append.txt', 'a') 
myFile.write(a)
