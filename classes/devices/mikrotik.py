from classes.devices.device import Device


class Mikrotik(Device):
    def __init__(self, id_dev=None, interfaces=None, ip=None, name='null', model='null', description='null', tool=None):
        super().__init__(id_dev=id_dev, interfaces=interfaces, ip=ip, name=name, vendor='Mikrotik', model=model,
                         description=description, tool=tool)
