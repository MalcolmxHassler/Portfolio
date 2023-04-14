import base64
import os

def ImageConversion(filename):
    #convert image to string
    with open(filename, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    return converted_string


def ImageTransformation(decryptedMsg,filename):               
    with open('encode.bin', "wb") as file:
        file.write(decryptedMsg)
    #open the file for decoding
    file = open('encode.bin', 'rb')
    byte = file.read()
    file.close()
    #write the final file
    decodeit = open(filename, 'wb')
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()
    #pour supprimer le fichier Bin
    os.remove('encode.bin') 

