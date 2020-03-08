apt update
apt install git
sudo -u pi git clone https://github.com/highwingers/RaspBerryPiAdhan.git
#chown pi:pi -R RaspBerryPiAdhan
sudo -u pi cp -R RaspBerryPiAdhan orignal_firmware

sudo sh  orignal_firmware/setup/db.sh


#chown pi:pi -R orignal_firmware
cd RaspBerryPiAdhan/setup
sh ./setup.sh
