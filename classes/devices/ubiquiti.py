from classes.devices.device import Device


class Ubiquiti(Device):
    def __init__(self, id_dev=None, ip=None, name='null', model='null', description='null', tool=None):
        super().__init__(id_dev=id_dev, ip=ip, name=name, vendor='Ubiquiti', model=model,
                         description=description, tool=tool)
