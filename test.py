from classes.controllers.deviceController import DeviceController
from classes.devices.device import Device
from classes.devices.hp import HP
from classes.devices.interfaces.ethernet import Ethernet
from classes.devices.mikrotik import Mikrotik
from classes.devices.ubiquiti import Ubiquiti
from classes.tools.ping import Ping
from classes.tools.snmp import Snmp
from classes.tools.ssh import Ssh

deviceController = DeviceController()
deviceController.add_device(
    Ubiquiti(name='ubnt_len_6_66', ip='172.21.32.66/20', tool=Snmp)
)
device_ubnt_len_6_66 = deviceController.get_device(name="ubnt_len_6_66")
'''device_trololo.tools.add_tool(Snmp)'''
'''device_ubnt_len_6_66.tools.add_tool(Snmp)
device_ubnt_len_6_66.tools.add_tool(Ping)'''
deviceController.update_device(device_ubnt_len_6_66)
print(device_ubnt_len_6_66.tools.snmp.request())

'''for i in range(1, 255):
    deviceController.add_device(
        Device(name=f'172.16.32.{i}', ip=f'172.21.32.{i}/24', vendor='other', tool=Snmp))

for device in deviceController.get_devices():
    print(device.tools.snmp.request())'''
