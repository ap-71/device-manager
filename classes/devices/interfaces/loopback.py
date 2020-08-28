from classes.devices.interfaces.interface import Interface


class Loopback(Interface):

    def __init__(self, ip='127.0.0.1', mac='ff:ff:ff:ff:ff:ff'):
        super().__init__(ip=ip, name='loopback', mac=mac, type_interface='loopback')

