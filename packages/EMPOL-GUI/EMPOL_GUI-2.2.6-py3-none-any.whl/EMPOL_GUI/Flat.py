import numpy as np
import math
import matplotlib.pyplot as plt
from astropy.io import fits
import os
import fnmatch
from astropy.io.fits import getheader
from astropy.stats import sigma_clipped_stats
from astropy.modeling import models, fitting
from scipy.optimize import curve_fit
from scipy import interpolate
import natsort
from scipy import ndimage
from photutils.aperture import CircularAperture #from photutils import CircularAperture
from photutils.aperture import aperture_photometry
from photutils.aperture import CircularAnnulus
from astropy.table import hstack
from astropy.table import Column


def flatCombine(path, filter, cycl_len):   # arguments - flatpath = '/home/namita/Documents/Open_clusters/Mt_ABU/2020_nov/empol_nov2020/20201113/Flat', Filter= r
    flatpath = path +'/Flat'
    bias_path = path +'/Bias'
    flatlist = os.listdir(flatpath) # list of all files in Flat folder
    flatlist = natsort.natsorted(flatlist)
    filter_list=[]
    for files in flatlist:
        if fnmatch.fnmatch(files, '*'+str(filter)+'*'):
            filter_list.append(files)
    n=int(len(filter_list)/cycl_len)
    imgarr = np.zeros((256,256,cycl_len))
    for j in range(0,cycl_len):
        a=0
        flatarr = np.zeros((256, 256, n))
        for i in range(n):
            data=fits.getdata(os.path.join(flatpath, filter_list[j+a]))
            flatarr[:,:,i] = data[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits'))
            header = getheader(os.path.join(flatpath, filter_list[j+a]))
            #norm=np.median(Img)    # normalization constant
            #flatarr[:,:,i]=Img/norm    # first normalize with median then median combine
            a=a+cycl_len
        Img = np.mean(flatarr,axis=2)
        imgarr[:,:,j]= Img/np.median(Img)
    Final = np.median(imgarr, axis=2)
    fits.writeto(os.path.join(flatpath, filter +'mean.fits'), Final, header, overwrite=True) 
    return(Final)

#path='/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data'
#filter='R'
#cycl_len=12
#flatCombine(path, filter, cycl_len)
