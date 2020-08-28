from abc import ABC, abstractmethod

from classes.utils.genID import GenID


class Tool(ABC):
    id: int
    name: str
    description: str
    _device = None

    def __init__(self, device=None, id_tool=None, name=None, description=None):
        self._device = device
        self.name = name
        self.description = description
        self.id = id_tool if id_tool is not None else GenID().gen()

    @abstractmethod
    def set_params(self, device):
        pass

    @abstractmethod
    def request(self):
        pass

    @property
    def id_tool(self):
        return self.id
