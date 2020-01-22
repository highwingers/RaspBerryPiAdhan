apt-get install apache2
apt-get install libapache2-mod-wsgi-py3


rm /home/pi/RaspBerryPiAdhan/www/adhan.wsgi

_wsgi="$(cat >  /home/pi/RaspBerryPiAdhan/www/adhan.wsgi << EOF
import sys
sys.path.insert(0, "/home/pi/RaspBerryPiAdhan/www")
from index import app as application
EOF
)"
echo "$_wsgi"

rm /etc/apache2/sites-available/adhan.conf




_conf="$(cat << EOF > /etc/apache2/sites-available/adhan.conf
 WSGIDaemonProcess adhan user=pi group=www-data threads=5
 WSGIScriptAlias / /home/pi/RaspBerryPiAdhan/www/adhan.wsgi
 <Directory "/home/pi/RaspBerryPiAdhan/www">
        WSGIProcessGroup adhan
        WSGIScriptReloading On
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
 </Directory>
 ErrorLog /home/pi/RaspBerryPiAdhan/www/logs/error.log
EOF
)"
echo "$_conf"


sudo /usr/sbin/a2dissite adhan.conf
sudo /usr/sbin/a2ensite adhan.conf

apachectl stop
/etc/init.d/apache2 start
/etc/init.d/apache2 reload

