from classes.controllers.deviceController import DeviceController
from classes.devices.hp import HP
from classes.devices.interfaces.ethernet import Ethernet
from classes.devices.mikrotik import Mikrotik
from classes.tools.ping import Ping
from classes.tools.snmp import Snmp
from classes.tools.ssh import Ssh

deviceController = DeviceController()
deviceController.add_device(Mikrotik(name='trololo', ip='172.21.32.1/24'), HP(name='trololoshki', ip='10.10.10.2/24'))
device_trololo = deviceController.get_device(name="trololo")
device_trololoshki = deviceController.get_device(name="trololoshki")
device_trololo.interfaces.add_interface(Ethernet('172.16.32.1/24', 'ether1', 'c1:a3:43:da:dc:21'))
device_trololo.tools.add_tool(Ping)
'''device_trololo.tools.add_tool(Snmp)'''
device_trololo.tools.add_tool(Ssh)
device_trololo.tools.del_tool(Ping)
device_trololo.tools.ssh.set_params()
deviceController.update_device(device_trololo)
