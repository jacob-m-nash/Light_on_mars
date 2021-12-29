from _typeshed import Self
from typing_extensions import Concatenate


class LIFX_packet:
    def __init__(self,size,protocol,addressable,tagged,origin,source,target,res_required,ack_required,sequence,pkt_type,payload):
        self.size = size
        self.protocol = protocol
        self.addressable = addressable
        self.tagged = tagged
        self.origin = origin
        self.source = source
        self.target = target
        self.res_required -res_required
        self.ack_required = ack_required
        self.sequence = sequence
        self.pkt_type = pkt_type
        self.payload = payload

    def concatenate():
        return
    
    def toHex():
        packet = LIFX_packet.concatenate()
        packetvalue = int(packet)
        return hex(packetvalue)
