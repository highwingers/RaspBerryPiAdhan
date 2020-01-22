# bash ./flaskserver.service

sh ./avahi.sh

sh ./db.sh

apt-get  install  python3-pip 

pip3 install -r ../requirements.txt 


pip3 uninstall zeroconf
pip3 install zeroconf==0.24.3



