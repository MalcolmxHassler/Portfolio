import socket
import joblib
import dill
import cryptoModules as CM
import NormalImage as NI
import dicomFile as DCM
import TransmissionFile as Trans


if __name__ == "__main__":
    

    #privKey = secrets.randbelow(curve.field.n)
    #pubKey = privKey * curve.g


    #joblib.dump(pubKey, 'clepublique.plk')
    #joblib.dump(privKey, 'cleprivee.plk')

    pubKey = joblib.load('clepublique.plk')

    #print('Public key : ',type(pubdata))

    #server connection
    s = socket.socket()
    host = "192.168.43.251" #Ip address of the server or hostname
    port = 5001 #Server Port
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected to ", host)

    '''for the name of the file to transfer '''
    filename = input("File to Transfer : ")

    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        '''case when image is normal'''
        converted_string= NI.ImageConversion(filename)
    else:
        '''case when its a DICOM Image'''
        converted_string= DCM.dicomEncoding(filename)

    
    '''encrypting the converted string before sending through the network'''
    encryptedMsg = CM.encrypt_ECC(converted_string, pubKey)
    
    print('Encryption Done...')

    '''conversion of the tuple to byte using dill module(serialization done)'''
    msg_en=dill.dumps(encryptedMsg)
    
    #sending the tuple on the network
    #s.sendall(msg_en)
    Trans.send_msg(s,msg_en)
    print('Image Sent Completely....')
    #s.close()
