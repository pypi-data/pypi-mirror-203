import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os
import fnmatch
from astropy.stats import sigma_clipped_stats
from astropy.modeling import models, fitting
from scipy.optimize import curve_fit
from scipy import interpolate
import natsort

def biascombine(path):
    bias_path = path +'/Bias' 
    img_list = os.listdir(bias_path) # list of all files in Bias folder
    img_list = natsort.natsorted(img_list) #natsort is natural sort
    imglist = []
    for files in img_list:
        if fnmatch.fnmatch(files, 'Bias*'):
            imglist.append(files)
    n = int(len(imglist))
    print('no. of bias frames = ', n)
    bias_arr = np.zeros((256,256,n))
    for i in range(len(imglist)):
        data, header = fits.getdata(os.path.join(bias_path,img_list[i]), header=True)
        bias_arr[:,:,i] = data[0,:,:]
    comb = np.median(bias_arr, axis=2) 
    fits.writeto(os.path.join(bias_path, 'masterBias.fits'), comb, header,overwrite=True)
#path='/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data'
#biascombine(path)