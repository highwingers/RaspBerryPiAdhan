updir=${PWD%/*}

#chown -R pi:pi  ${PWD%/*}/.git

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

sed -i  -e "\$i \sudo python3 $updir/www/commands/resetbtn.py &\n"  /etc/rc.local


sed -i 's/BT WLAN/ADHAN/g'  /etc/nymea/nymea-networkmanager.conf
systemctl restart nymea-networkmanager


python3 ${PWD%/*}/www/index.py





