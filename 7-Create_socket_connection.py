import socket 

def main():
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'www.google.com'
    port = 80
    try:
       result= s.connect_ex((host,port))
       if result==0:
           print("Successfully")
       else:
           print("connection refused")
       s.close()
    except Exception as e:
        print("error") 
        
if __name__=='__main__':
    main()
    