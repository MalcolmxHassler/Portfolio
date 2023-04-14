import pydicom
import pickle

def dicomEncoding(dicomfile):
    #reading the dicom file
    ds = pydicom.dcmread(dicomfile)
    #converting the dicom file to bytes with pickle
    enc=pickle.dumps(ds)
    return enc

def dicomDecoding(byte_value):
    dec=pickle.loads(byte_value)
    return dec

def writeDicomImage(filename,dataset):
    pydicom.filewriter.dcmwrite(filename,dataset)
    
