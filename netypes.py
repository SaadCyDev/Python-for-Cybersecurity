import socket 
from struct import unpack

def mac_addr(bytestring):
    return ':'.join('{:02x}'.format(piece) for piece in bytestring).upper()
class EthernetFrame:
    length =14 
    def __init__(self, data):
        unpacked_data= unpack('!6s6sH', data[0:self.length])
        self.protocol = socket.ntohs(unpacked_data[2])
        self.destination= mac_addr(data[0:6])
        self.source= mac_addr(data[6:12])
        self.leftover_data= data[self.length:]
        
    def __str__(self) :
        return """
           Source :        {source} 
           Destination :   {destination}
           Protocol :      {protocol} 
    """.format(**self.__dict__)