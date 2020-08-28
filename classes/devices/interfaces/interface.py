from abc import ABC
from ipaddress import IPv4Interface, IPv4Address


class Interface(ABC):
    name: str
    mac: str
    type: str
    ip: str
    mask: str

    def __init__(self, ip, name, mac, type_interface, mask=None):
        ip_interface = IPv4Interface(ip)
        self.ip = str(ip_interface.ip)
        self.type = type_interface
        self.name = name
        self.mac = mac
        self.mask = str(ip_interface.netmask) if mask is None else mask
