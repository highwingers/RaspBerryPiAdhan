updir=${PWD%/*}

#chown -R pi:pi  ${PWD%/*}/.git

bash ./flaskserver.service

sh ./dailycron.sh

bash ./avahi.sh

sh ./db.sh

apt-get  install  python3-pip 
apt-get install python3-gpiozero
apt-get install mplayer
apt-get install bluealsa

service bluealsa start


pip3 install --timeout 1000 -r ../requirements.txt 


pip3 uninstall zeroconf
pip3 install --timeout 1000 zeroconf==0.24.3

#sh ./apache.sh

grep -q resetbtn.py /etc/rc.local  || sudo sed -i  -e "\$i \sudo python3 ${updir}/www/commands/resetbtn.py &\n"  /etc/rc.local



sed -i 's/BT WLAN/ADHAN/g'  /etc/nymea/nymea-networkmanager.conf
systemctl restart nymea-networkmanager

update-ca-certificates -f

python3 ${PWD%/*}/www/index.py





