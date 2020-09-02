import os
import yaml
import const
from classes.devices.device import Device


class DeviceRegistryService:
    def __init__(self):
        self.path_device_dir = const.DEVICE_DIR

    def _make_dir(self, path) -> bool:
        if not os.path.exists(path):
            os.mkdir(path)
            return True
        return False

    def get_all_device(self) -> list:
        devices: list = []
        for _dir, _dir_next, _file in os.walk(self.path_device_dir):
            if len(_file) > 0:
                for dev in _file:
                    try:
                        with open(os.path.join(_dir, dev)) as file:
                            _device = self.skeleton(yaml.safe_load(file.read()))
                            devices.append(_device)
                    except Exception as e:
                        print(f'===========> ОШИБКА: {e}')
        return devices

    def get_device(self, name) -> Device:
        for _dir, _dir_next, _file in os.walk(self.path_device_dir):
            if len(_file) > 0:
                for dev in _file:
                    with open(os.path.join(_dir, dev)) as file:
                        _device = yaml.safe_load(file.read())
                        if _device is not None and _device.get('name') == name:
                            return self.skeleton(_device)

    def add_device(self, device) -> bool:
        device_name = f'{device.name}.yml'
        path_dir = os.path.join(self.path_device_dir, device.vendor)
        path_device = os.path.join(path_dir, device_name)
        if not os.path.exists(path_dir):
            self._make_dir(path_dir)
        if not os.path.exists(path_device):
            with open(path_device, 'w') as f:
                f.write(yaml.dump(device.skeleton, sort_keys=True))
                return True
        return False

    def update_device(self, device) -> bool:
        path_dir = os.path.join(self.path_device_dir, device.vendor)
        path_device = os.path.join(path_dir, f'{device.name}.yml')
        if os.path.exists(path_device):
            with open(path_device, 'w') as f:
                f.write(yaml.dump(device.skeleton))
                return True
        return False

    def del_device(self, device) -> bool:
        if os.path.exists(device):
            os.mkdir(device)
            return True
        return False

    def skeleton(self, device: dict) -> Device:
        interfaces = list()
        for key, value in device['interfaces'].items():
            interface = type(value.get('type'), (), {})()
            for key_inter, value_inter in value.items():
                interface.__setattr__(key_inter, value_inter)
            interfaces.append(interface)
        _device: Device = Device(
            id_dev=device.get('id', '0000000000000000'),
            interfaces=interfaces,
            name=device.get('name', 'null'),
            vendor=device.get('vendor', 'null'),
            model=device.get('model', 'null'),
            description=device.get('description', 'null'),
            tool={key: value_key for key, value_key in device.get('tools').items()} if len(device.get('tools')) != 0 else None,
            user_name=device.get('user'),
            password=device.get('password')
        )
        return _device
