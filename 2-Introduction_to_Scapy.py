from scapy.all import *

paquet=IP(dst="alphorm.com")/ICMP()/"Hello there"
paquet.show()

#send(IP(dst="alphorm.com")/ICMP()/"Hello there", iface="wlp0s20f3", loop=1)

response,no_response= sr(IP(dst="google.com")/ICMP()/"Yes")
print(response) 
response.show()
print(no_response)
no_response.show()

conf.route.add(host="192.168.0.56",gw="192.168.0.1")
print(conf.route)

conf.route.resync()
print(conf.route)