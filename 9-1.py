from range_port_scanner import Scanner 
from banner_reading_from_openPorts import Grabber 

def main():
    ip ='192.168.0.102'
    scanner =  Scanner(ip)
    scanner.scan(1,65000)
    print('\n\n-------------------------Reading from open ports---------------------------\n')
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip,port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print("Error ",e)
        
if __name__=='__main__':
    main()

