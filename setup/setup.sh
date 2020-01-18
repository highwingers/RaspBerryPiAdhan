bash ./flaskserver.service

sh ./db.sh

apt-get  install  python3-pip 

apt-get install pulseaudio pulseaudio-module-bluetooth

pip3 install -r ../requirements.txt 


pip3 uninstall zeroconf
pip3 install zeroconf==0.24.3



