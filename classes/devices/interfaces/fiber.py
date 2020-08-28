from classes.devices.interfaces.interface import Interface


class Fiber(Interface):

    def __init__(self, ip, name, mac):
        super().__init__(ip, name, mac, type_interface='fiber')

