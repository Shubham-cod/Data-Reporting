# Project: Data reporter
# Author:  Shubham Agarwal
# Date:    01/06/2020

####################################   creating socket TCP server to recieve the data   #########################################

import socket
import pickle

HOST = '127.0.0.1'  # hostname or IP address
PORT = 65432        # Port to listen

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))        #assigning socket as a server socket
    s.listen(5)                 #listens to incoming client signal 
    conn, addr = s.accept()     #accepts the signal from client and connection is established
    from_client = b""           #variable to concatenate and store recieved data
    with conn:
        print('Connected by', addr)
        while True:
            
            data = conn.recv(3000024)
            
            if not data:
                break
            else:
                from_client += data             #concatenating recieving data
            data_rec = pickle.loads(data)       #unpickling/extracting recieved data
            print(data_rec)                     #printing recieved data
            s.close()


###############################################################  END   ###########################################################
