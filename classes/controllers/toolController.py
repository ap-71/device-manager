from classes.tools.tool import Tool
from classes.tools.snmp import Snmp
from classes.tools.ping import Ping
from classes.tools.ssh import Ssh


class ToolController:
    _device = None

    def __init__(self, device):
        self._device = device

    def add_tool(self, tool):
        _tool = None
        if type(tool) is dict:
            for key, value in tool.items():
                _tool = globals()[key.title()](device=self._device)
                setattr(self, _tool.name, _tool)
        elif type(tool) is list:
            for tmp_tool in tool:
                specific_tool = tmp_tool(device=self._device)
                setattr(self, specific_tool.name, specific_tool)
        else:
            _tool = tool(device=self._device)
            setattr(self, _tool.name, _tool)

    def del_tool(self, tool):
        _tool = tool(device=self._device)
        delattr(self, _tool.name)

    def get_tool(self, tool):
        _tool = tool(device=self._device)
        getattr(self, _tool.name, __default=None)
