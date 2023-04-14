import matplotlib.pyplot as plt
import pydicom
import pydicom.data
import numpy as np
import png
import matplotlib.image as image
from math import log10, sqrt
import cv2
import scipy

def dicom2png(dcm_file, png_name):
    """ dcm_file is the dicom file path
    "   png_name is the png destination file path
    """
    try:
        ds = pydicom.dcmread(dcm_file)
        shape = ds.pixel_array.shape
        # Convert to float to avoid overflow or underflow losses.
        image_2d = ds.pixel_array.astype(float)
        # Rescaling grey scale between 0-255
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
        
        # Convert to uint
        image_2d_scaled = np.uint8(image_2d_scaled)
        # Write the PNG file
        with open(png_name, 'wb') as png_file:
            w = png.Writer(shape[1], shape[0], greyscale=True)
            w.write(png_file, image_2d_scaled)
    except:
        return False


def PSNR(original, compressed):
    original = cv2.imread(original)
    compressed = cv2.imread(compressed, 1)
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr,mse

def MSE(original, compressed):
    original = cv2.imread(original)
    compressed = cv2.imread(compressed, 1)
    mse = np.mean((original - compressed) ** 2)
    return mse


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)


if __name__ == '__main__':
    
    #conversion en png
    dicom2png('tomographie.dcm','tomo.png')
    dicom2png('tomo.dcm','tomo_dec.png')
    
    #Calcul du psnr
    psnr=PSNR('tomo.png','tomo_dec.png')

    #calcul du mse
    mse=MSE('tomo.png','tomo_dec.png')

    print(" PSNR : {} db".format(psnr))
    print(" MSE : {} ".format(mse))

    
    

    
