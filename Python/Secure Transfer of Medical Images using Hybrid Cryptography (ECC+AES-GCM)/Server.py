import socket
import struct
import pickle
import os


import cryptoModules as CM
import NormalImage as NI
import dicomFile as DCM

import TransmissionFile as Trans

#seerialization Modules
import joblib
import dill


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"


if __name__ == "__main__":
    
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(50)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    print("Waiting for the client to connect... ")

    
    client_socket, address = s.accept()
    print(f"[+] {address} is connected.")
            
    #filereceived=client_socket.recv(BUFFER_SIZE, socket.MSG_WAITALL)
    #print(len(client_socket.recv(4096)))
    filereceived=Trans.recv_msg(client_socket)
    print('All the Image has been received....')
            
    #-convert from byte to str  
    msg_rec=dill.loads(filereceived)
    privkey = joblib.load('cleprivee.plk')
            
    #print('private key :', privkey)
    decryptedMsg = CM.decrypt_ECC(msg_rec, privkey)


    filename= input("Enter the Name and extension for your image: ")
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        NI.ImageTransformation(decryptedMsg,filename)
    else:
        dec=DCM.dicomDecoding(decryptedMsg)
        DCM.writeDicomImage(filename,dec)
 
            
            

                



