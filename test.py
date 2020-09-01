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
'''deviceController.add_device(
    Mikrotik(name='trololo', ip='172.21.32.1/24'),
    HP(name='trololoshki', ip='10.10.10.2/24'),
    Ubiquiti(name='ubnt_len_6_66', ip='172.21.32.66/20')
)
device_ubnt_len_6_66 = deviceController.get_device(name="ubnt_len_6_66")
device_trololo = deviceController.get_device(name="trololo")
device_trololoshki = deviceController.get_device(name="trololoshki")
device_trololo.interfaces.add_interface(Ethernet('172.16.32.1/24', 'ether1', 'c1:a3:43:da:dc:21'))
device_trololo.tools.add_tool(Ping)
device_trololo.tools.add_tool(Snmp)
device_trololo.tools.add_tool(Ssh)
device_trololo.tools.del_tool(Ping)
device_trololo.tools.ssh.set_params()
device_ubnt_len_6_66.tools.add_tool(Snmp)
device_ubnt_len_6_66.tools.add_tool(Ping)
deviceController.update_device(device_trololo, device_ubnt_len_6_66)
print(device_ubnt_len_6_66.tools.snmp.request())'''

for i in range(1, 255):
    deviceController.add_device(
        Device(name=f'172.16.32.{i}', ip=f'172.21.32.{i}/24', vendor='other', tool=Snmp))
