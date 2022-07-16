import socket
from _thread import *
import threading

import time
 
print_lock = threading.Lock()
 
# thread function
def threaded(c):
    while True:
 
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye!')
             
            # lock released on exit
            print_lock.release()
            break
        else:
            print(f"got {data}")

        # # reverse the given string from client
        # data = data[::-1]
 
        # # send back reversed string to client
        # c.send(data)
 
    # connection closed
    c.close()
 
 
def Main():
    host = "127.0.0.1"
 
    port = 64000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
        print("Waiting...")
        
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))

        print("before sleep")
        time.sleep(.5)
    s.close()
 
 
if __name__ == '__main__':
    Main()