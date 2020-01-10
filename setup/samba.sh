apt-get install samba samba-common-bin
echo '[share]' >> /etc/samba/smb.conf 
echo 'Comment = Pi shared folder' >> /etc/samba/smb.conf
echo 'Path = /home/pi/RaspBerryPiAdhan' >> /etc/samba/smb.conf
echo 'Browseable = yes' >> /etc/samba/smb.conf
echo 'Writeable = Yes' >> /etc/samba/smb.conf
echo 'only guest = no' >> /etc/samba/smb.conf
echo 'create mask = 0777' >> /etc/samba/smb.conf
echo 'directory mask = 0777' >> /etc/samba/smb.conf
echo 'Public = yes' >> /etc/samba/smb.conf
echo 'Guest ok = yes' >> /etc/samba/smb.conf


smbpasswd -a pi



systemctl restart smbd
