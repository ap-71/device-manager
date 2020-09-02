from pysnmp.hlapi import *

from classes.tools.tool import Tool


class Snmp(Tool):
    community = None
    OIDs: dict = None
    _user = None
    _password = None
    _ip_address = None
    _port = None

    def __init__(self, device=None, community='public', user=None, password=None):
        Tool.__init__(self, device=device, name='snmp', description='Simple Network Management Protocol')
        self.set_params(community=community, user=user, password=password)

    def request(self) -> dict:
        response = dict()
        for oid_name, oid_value in self.OIDs.items():
            response.update({
                oid_name: exec_snmp(self._ip_address, self._port, self.community, oid_value, each=False)
            })
        return response

    def set_params(self, community='public', user=None, password=None, ip=None,
                   port=161, oids=None):
        if oids is None:
            oids = {'name': '1.0.8802.1.1.2.1.3.3.0'}
        self.community = community
        self._user = user
        self._password = password
        self.OIDs = oids
        self._port = port
        self._ip_address = self._device.interfaces.loopback.ip if ip is None else ip

    def add_oid(self, name, oid):
        self.OIDs.update({name: oid})


def snmp_bulk_cmd(community, ip, port, oid):
    return (bulkCmd(SnmpEngine(),
                    CommunityData(community, mpModel=0),
                    UdpTransportTarget((ip, port)),
                    ContextData(),
                    0, 20,
                    ObjectType(ObjectIdentity(oid))))


def snmp_getcmd(community, ip, port, oid):
    return (getCmd(SnmpEngine(),
                   CommunityData(community, mpModel=0),
                   UdpTransportTarget((ip, port)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid))))


def snmp_get_next(community, ip, port, oid, each=False):
    if not each:
        error_indication, error_status, error_index, var_binds = next(snmp_getcmd(community, ip, port, oid))
    else:
        error_indication, error_status, error_index, var_binds = next(snmp_bulk_cmd(community, ip, port, oid))
    for name, val in var_binds:
        return val.prettyPrint()


def exec_snmp(ip_address, port, community, oid, each=False) -> str:
    response = snmp_get_next(community, ip_address, port, oid, each)
    if response == "No Such Object currently exists at this OID" or response == "":
        response = "Object does not exist"
    return str(response)
