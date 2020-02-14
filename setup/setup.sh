chown -R pi:pi  ${PWD%/*}/.git

bash ./flaskserver.service

sh ./dailycron.sh

sh ./avahi.sh

sh ./db.sh

apt-get  install  python3-pip 
apt-get install python3-gpiozero

pip3 install --timeout 1000 -r ../requirements.txt 


pip3 uninstall zeroconf
pip3 install --timeout 1000 zeroconf==0.24.3

#sh ./apache.sh

sed -i -e '$i \python3 /home/pi/RaspBerryPiAdhan/www/commands/resetbtn.py &\n' /etc/rc.local


python3 ${PWD%/*}/www/index.py





