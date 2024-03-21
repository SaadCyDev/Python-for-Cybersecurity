import socket 

def port_scan(target_host, target_ports):
    try:
        target_ip= socket.gethostbyname(target_host)
        
        for target_port in target_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result= sock.connect_ex((target_ip,target_port))
            if result==0:
                print(f"Port {target_port} is open")
            else:
                print(f"Port {target_port} is closed")
            sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved!!")
    except socket.error:
        print("Could not connect to server!")

if __name__=="__main__":
    target_host=input("Enter target IP address or URL")
    
    ports_input=input("Enter ports to scan (comma-separated):")
    target_ports=[int(port.strip()) for port in ports_input.split(',')]
    
    port_scan(target_host,target_ports)