import socket 

def main():
    conn= socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
       raw_data, addr= conn.recvfrom(65500) 
       print(raw_data)
       print(addr)
    
if __name__=='__main__':
    main()