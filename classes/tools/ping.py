import os

from ipaddress import IPv4Address
from classes.tools.tool import Tool


class Ping(Tool):
    count: int
    size_packet: int
    timeout: int
    _ip_address: IPv4Address

    def __init__(self, device=None, count=1, size_packet=64, timeout=1000):
        super().__init__(device=device, name='ping', description='check the availability of a node')
        self.set_params(count, size_packet, timeout)

    def set_params(self, count=1, size_packet=64, timeout=1000, ip=None):
        self.count = count
        self.size_packet = size_packet
        self.timeout = timeout
        self._ip_address = self._device.interfaces.loopback.ip if ip is None else ip

    def request(self, ip=None) -> bool:
        ip = self._ip_address if ip is None else ip
        response = os.system(
            f"ping -n {self.count} -l {self.size_packet} -w {self.timeout} {ip} > nul ")
        return response == 0
