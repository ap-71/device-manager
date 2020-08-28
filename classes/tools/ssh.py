from classes.tools.tool import Tool


class Ssh(Tool):
    _user: str
    _password: str
    _ip: str

    def __init__(self, device=None):
        super().__init__(device=device, name='ssh', description='SSH connect')
        self.set_params(device)

    def set_params(self, user=None, password=None):
        self._user = user if user is not None else self._device.user
        self._password = password if password is not None else self._device.password
        self._ip = self._device.interfaces.loopback.ip

    def request(self):
        pass
