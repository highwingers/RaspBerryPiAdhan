import socket
import fcntl
import struct
import configparser
import os


class utility:
    def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15]))[20:24])

    def ConfigSectionMap(section):
        config = configparser.ConfigParser()
        path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')) + "/config.ini"
        config.read(path)
        return config[section]


