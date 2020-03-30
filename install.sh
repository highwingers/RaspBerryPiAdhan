apt update
apt install git
sudo -u pi git clone --single-branch --branch bluetooth https://github.com/highwingers/RaspBerryPiAdhan.git
#chown pi:pi -R RaspBerryPiAdhan
sudo -u pi cp -R RaspBerryPiAdhan orignal_firmware

sudo rm orignal_firmware/www/data/adhan.db
cd orignal_firmware/setup
sudo sh  ./db.sh
cd ../..

#chown pi:pi -R orignal_firmware
cd RaspBerryPiAdhan/setup
sh ./setup.sh
