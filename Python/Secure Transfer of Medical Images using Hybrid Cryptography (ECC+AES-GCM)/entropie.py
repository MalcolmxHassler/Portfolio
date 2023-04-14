import sys, pydicom, cv2
import numpy as np
from scipy.stats import entropy as en

def H(image):
    p = np.array([(image==v).sum() for v in range(256)])
    p = p/p.sum()
    # Compute e = -sum(p(g)*log2(p(g)))
    e = -(p[p>0]*np.log2(p[p>0])).sum()
    return e

image = sys.argv[1]
ds = pydicom.dcmread(image)
print(ds.Modality)
if ds.file_meta.TransferSyntaxUID.is_compressed is True:
        ds.decompress()
pixels = ds.pixel_array
print("Entropie = " + str(H(pixels)))