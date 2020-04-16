BASEDIR=$(dirname "$0")
cd "$BASEDIR"

> updatelog.txt

echo "Starting Update $(date) \n" >> updatelog.txt
updir=${PWD%/*}

bash ./flaskserver.service
echo "Flask Service SET $(date) \n" >> updatelog.txt

sh ./dailycron.sh

echo "Daily Job $(date) \n" >> updatelog.txt

bash ./avahi.sh

sh ./db.sh
echo "Database Updated $(date) \n" >> updatelog.txt

apt-get  install  python3-pip -y
apt-get install python3-gpiozero -y
apt-get install mplayer -y
apt-get install bluealsa -y
apt-get install espeak -y
apt-get install hostapd -y
apt-get install dnsmasq -y
apt-get install dos2unix  -y 
service bluealsa start

echo "apt packages done $(date) \n" >> updatelog.txt


yes | pip3 install --timeout 1000 -r ../requirements.txt 
echo "requirements.txt process $(date) \n" >> updatelog.txt

#pip3 uninstall zeroconf --yes
#yes | pip3 install --timeout 1000 zeroconf==0.24.4
#sh ./apache.sh

grep -q resetbtn.py /etc/rc.local  || sudo sed -i  -e "\$i \sudo python3 ${updir}/www/commands/resetbtn.py &\n"  /etc/rc.local



#sed -i 's/BT WLAN/ADHAN/g'  /etc/nymea/nymea-networkmanager.conf
#systemctl restart nymea-networkmanager
#echo "restarted network manager $(date) \n" >> updatelog.txt

update-ca-certificates -f

#kill $(ps aux | grep [w]ww/index.py | awk '{print $2}')
#python3 ${PWD%/*}/www/index.py

cd hotspot
bash ./install
cd ..

echo "Update Finished $(date) \n" >> updatelog.txt

reboot





