from pysnmp.hlapi import *


class Snmp:
    _log = None

    def snmp_bulkcmd(self, community, ip, port, oid):
        return (bulkCmd(SnmpEngine(),
                        CommunityData(community, mpModel=0),
                        UdpTransportTarget((ip, port)),
                        ContextData(),
                        0, 20,
                        ObjectType(ObjectIdentity(oid))))

    def snmp_getcmd(self, community, ip, port, oid):
        return (getCmd(SnmpEngine(),
                       CommunityData(community, mpModel=0),
                       UdpTransportTarget((ip, port)),
                       ContextData(),
                       ObjectType(ObjectIdentity(oid))))

    def snmp_get_next(self, community, ip, port, oid, each=False):
        if not each:
            error_indication, error_status, error_index, var_binds = next(self.snmp_getcmd(community, ip, port, oid))
        else:
            error_indication, error_status, error_index, var_binds = next(self.snmp_bulkcmd(community, ip, port, oid))
        for name, val in var_binds:
            return val.prettyPrint()

    def exec_snmp(self, ip_address, port, community, oid, each=False) -> str:
        response = self.snmp_get_next(community, ip_address, port, oid, each)
        if response == "No Such Object currently exists at this OID" or response == "":
            response = "Object does not exist"
        return str(response)