class InterfaceController:
    def add_interface(self, interface) -> bool:
        if not hasattr(self, interface.name):
            setattr(self, interface.name, interface)
            return True
        return False

    def del_interface(self, interface):
        delattr(self, interface.name)
