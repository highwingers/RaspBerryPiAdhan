apt update
apt install git
-u pi git clone https://github.com/highwingers/RaspBerryPiAdhan.git
#chown pi:pi -R RaspBerryPiAdhan
-u pi cp -R RaspBerryPiAdhan orignal_firmware
#chown pi:pi -R orignal_firmware
cd RaspBerryPiAdhan/setup
sh ./setup.sh
