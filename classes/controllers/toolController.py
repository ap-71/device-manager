class ToolController:
    _device = None

    def __init__(self, device):
        self._device = device

    def add_tool(self, tool):
        _tool = None
        if type(tool) is dict:
            for key, value in tool.items():
                _tool = type(key, (), {'device': self._device, 'description': value.get('description'), 'name': value.get('name')})
        else:
            _tool = tool(device=self._device)
        setattr(self, _tool.name, _tool)

    def del_tool(self, tool):
        _tool = tool(device=self._device)
        delattr(self, _tool.name)

    def get_tool(self, tool):
        _tool = tool(device=self._device)
        getattr(self, _tool.name, __default=None)
