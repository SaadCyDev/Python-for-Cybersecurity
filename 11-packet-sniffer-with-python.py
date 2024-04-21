import socket 
from packet_capture_output import PCAPFile
from netypes import EthernetFrame, IPHeader, TCPSegment


def main():
    conn= socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
   #  pcap= PCAPFile('packets.pcap')
    while True:
       raw_data, addr= conn.recvfrom(65535) 
       ethframe= EthernetFrame(raw_data)
       print(ethframe)
       if ethframe.protocol==8:
          ipheader=IPHeader(ethframe.leftover_data)
          print(ipheader)
          if ipheader.protocol==6:
             tcp= TCPSegment(ipheader.leftover_data)
            #  print(tcp.__dict__)
             if tcp.src_port==80:
                print(tcp)
      #  break 
    #    print(raw_data)
    #    print(addr)
      #  pcap.write(raw_data)
   #  pcap.close()
    
if __name__=='__main__':
    main()