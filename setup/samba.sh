apt-get install samba samba-common-bin
echo "
[share]
Comment = Pi shared folder
Path = /home/pi/RasoBerryPiAdhan
Browseable = yes
Writeable = Yes
only guest = no
create mask = 0777
directory mask = 0777
Public = yes
Guest ok = yes
" >> /etc/samba/smb.conf

smbpasswd -a pi

systemctl restart smbd

