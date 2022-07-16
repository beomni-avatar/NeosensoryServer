# echo-server.py

import socket
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT_RECEIVE = 64000  # Port to listen on (non-privileged ports are > 1023)
PORT_SEND = 64001

recieveSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recieveSocket.settimeout(1)
recieveSocket.bind((HOST, PORT_RECEIVE))
recieveSocket.listen()

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendSocket.settimeout(1)
sendSocket.bind((HOST, PORT_SEND))

while True:
    print(f"Waiting...")

    try:
        # Will either connect or timeout and kick us out of the loop
        conn, addr = recieveSocket.accept()

        print(f"Connected by {addr}")


        while True:
            print(f"checking...")
        
            data = conn.recv(1024)

            if (data):
                    print(f"Data recieved {data}")
            if not data:
                break
        
            # sendSocket.send("test from python".encode())
            time.sleep(.1)

    except socket.timeout:
        pass
    except Exception as e:
        print(f"Error: {e}")
        pass
    
    time.sleep(.1)