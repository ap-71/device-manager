from classes.controllers.interfaceController import InterfaceController
from classes.controllers.toolController import ToolController
from classes.devices.interfaces.loopback import Loopback
from classes.utils.genID import GenID


class Device:
    id: int
    name: str
    vendor: str
    description: str
    model: str
    user: str
    password: str

    def __init__(self, id_dev=None, interfaces: list = None, ip=None, name='null', vendor='null', model='null',
                 description='null',
                 tool=None, user_name=None, password=None):
        self.name = name
        self.user = user_name if user_name is not None else 'admin'
        self.password = password if password is not None else 'admin'
        self.vendor = vendor
        self.model = model
        self.description = description
        self.interfaces = InterfaceController()
        self.tools = ToolController(self)
        self.id = id_dev if id_dev is not None else GenID.gen()
        if interfaces is not None and len(interfaces) != 0:
            for interface in interfaces:
                self.interfaces.add_interface(interface)
        else:
            self.interfaces.add_interface(Loopback(ip if ip is not None else '127.0.0.1'))
        if tool is not None:
            self.tools.add_tool(tool)

    @property
    def skeleton(self) -> dict:
        tools = {}
        skeleton = {}
        interfaces = {}
        device = self.__dict__
        for key, interface in self.interfaces.__dict__.items():
            if key[0] != '_':
                interfaces.update({key: {attr: val for attr, val in interface.__dict__.items()}})
                #interfaces[key].update({attr: val for attr, val in interface.__dict__.items()})
        for key, tool in self.tools.__dict__.items():
            if key[0] != '_':
                tools.update({key: {}})
                tools[key].update({attr: val for attr, val in tool.__dict__.items() if attr[0] != '_'})
        skeleton.update(device)
        skeleton['interfaces'] = interfaces
        skeleton['tools'] = tools
        skeleton_sorted = sorted(skeleton.items(), key=lambda x: x[0])
        skeleton = dict(skeleton_sorted)
        return skeleton
