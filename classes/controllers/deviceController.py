from classes.devices.device import Device
from classes.services.deviceRegistryService import DeviceRegistryService


class DeviceController:
    _devices: list

    def __init__(self):
        self._devices = list()
        self._device_registry = DeviceRegistryService()

    def add_device(self, *args: Device):
        if len(args) != 0:
            for arg in args:
                self._device_registry.add_device(arg)
                # self._devices.append(arg)

    def del_device(self, id_dev=None, name=None, ip=None):
        for device in self._devices:
            if device.id == id_dev or device.name == name or device.interface.ip == ip:
                self._device_registry.del_device(device)
                # self._devices.remove(device)

    def get_device(self, id_dev=None, name=None) -> Device:
        return self._device_registry.get_device(name=name)

    def get_devices(self) -> list:
        return self._device_registry.get_all_device()

    def update_device(self, *args: Device):
        if len(args) != 0:
            for arg in args:
                self._device_registry.update_device(arg)
