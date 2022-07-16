import socket
from _thread import *
import threading

import time
 
print_lock_receive = threading.Lock()
 
def receive_threaded(c):
    while True:
 
        data = c.recv(1024)
        if not data:
            print('Bye!')
             
            print_lock_receive.release()
            break
        else:
            print(f"got {data}")

        # # reverse the given string from client
        # data = data[::-1]
 
        # # send back reversed string to client
        # c.send(data)
 
    c.close()

# def send_threaded(c):
#     while True:
#         c.send(data)
#         time.sleep(1)
#     c.close()
 
 
def Main():
    host = "127.0.0.1"
 
    port_receive = 64000
    socket_receive = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_receive.bind((host, port_receive))
    print("receive socket binded to port", port_receive)
    socket_receive.listen(5)
    print("receive socket is listening")


    # port_send = 64001
    # socket_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket_send.bind((host, port_send))
    # socket_send.send("test".encode())

 
    # a forever loop until client wants to exit
    while True:
        print("Waiting...")
        
        connection, addr = socket_receive.accept()
 
        print_lock_receive.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        start_new_thread(receive_threaded, (connection,))

        print("before sleep")
        time.sleep(.5)
    socket_receive.close()
 
 
if __name__ == '__main__':
    Main()