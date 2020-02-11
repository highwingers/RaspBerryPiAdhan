cd /etc/avahi/services

rm avahi.service

echo "<?xml version='1.0' standalone='no'?>" >> avahi.service
echo "<!DOCTYPE service-group SYSTEM 'avahi-service.dtd'>" >> avahi.service
echo "<service-group>" >> avahi.service
echo "<name replace-wildcards='yes'>Adhan Player %h</name>" >> avahi.service
echo "<service>" >> avahi.service
echo "<type>_http._tcp</type>" >> avahi.service
echo "<port>5500</port>" >> avahi.service
echo "</service>" >> avahi.service
echo "</service-group>" >> avahi.service 

service avahi-daemon restart
