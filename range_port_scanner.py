import socket
 
class Scanner:
    def __init__(self, ip):
        self.ip =ip 
        self.open_ports=[]
        
    def __repr__(self):
        return 'Scanner:{}'. format(self.ip)
    
    def add_port(self,port):
        self.open_ports.append(port)
        
    def scan(self, lowerport ,upperport):
        for port in range(lowerport, upperport+1):
            if self.is_open(port):
                print(port)
                self.add_port(port) 
                
    def is_open(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))  
        print('Port {} :    {}'.format(port,result))
        s.close()
        return result==0 
    
    def write(self,filepath):
        openport = map(str,self.open_ports)
        with open(filepath,'w') as f:
            f.write('\n'.join(openport)) 

def main():
    ip= '192.168.0.102'
    scanner= Scanner(ip)
    scanner.scan(1,65535)
    print("\n\nPort ports are : ", scanner.open_ports)
    scanner.write('./open_ports')


if __name__=='__main__':
    main()