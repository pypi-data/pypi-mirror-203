import numpy as np
#import pyfitsf
import os, sys
import math
import time, datetime
import string
import fnmatch
#import urllib.request, urllib.parse, urllib.error
from astropy.io import fits
from astropy.wcs import WCS
from astropy.stats import SigmaClip
from photutils.background import Background2D, MedianBackground
from photutils.utils import calc_total_error
from astropy.stats import sigma_clipped_stats
from astropy.modeling import models, fitting
from scipy.optimize import curve_fit
import natsort
import subprocess
import warnings
import matplotlib.pyplot as plt
from photutils.aperture import CircularAperture
from photutils.aperture import CircularAnnulus
from photutils.aperture import ApertureStats
from photutils.aperture import aperture_photometry
from photutils.segmentation import make_source_mask
from astropy.table import Column
#import extcatalog

def single_click(event):
    global X1,Y1
    if event.button == 3:
        X1, Y1 = event.xdata, event.ydata
        plt.close(1)

def press(event):
    global X2,Y2
    if event.key == 'x':
        X2, Y2 = event.xdata, event.ydata
        plt.close(1)

def Gauss2D(xy, x0, y0, s, A):                                 # 2D- gaussian fiting is better than ndimage_maximum_posiyion and Center_of_mass 
    x,y=xy
    c=1/(2*s**2)
    f = A*np.exp(-c*((x-x0)**2+(y-y0)**2))
    return(f)

def center(subimg,r):
    x = np.arange(0, subimg.shape[1],1)
    y = np.arange(0, subimg.shape[0], 1)
    xx, yy = np.meshgrid(x,y)
    x0 = r
    y0 = r
    s = max(*subimg.shape)*0.1
    A=np.max(subimg)
    initial_guess=[x0,y0,s,A]
    param, err = curve_fit(Gauss2D, (xx.ravel(), yy.ravel()), subimg.ravel(), p0=initial_guess)
    return(param)
def imgscl(img, factor1=1, factor2=1):         #Image scaling function (for display only)
    med = np.median(img)
    std = np.std(img)
    img_a = img.copy()
    ind = np.where(img < med-std*factor1)
    img_a[ind] = med-std*factor1
    ind = np.where(img > med+std*factor2)
    img_a[ind] = med+std*factor2
    return img_a
def gauss1D(x, A, width, mu, B): 
    return(B+(A*np.exp(-(x-mu)**2/width)))
'''
####################################################  result from extcatalog.py #######################################################################################################################
path= '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Feb/EMPOL_Feb2021/Feb_6'
command='no'
while(command=='no'):
    lm = input("enter limiting magnitude : ")
    source = extcatalog.extcat(path, 'g', 'waterloo7', '140', 'I/345/gaia2', "Gmag", lm , 'W7', 'RA_ICRS', 'DE_ICRS')
    command = input('Are all the stars detected? ')
source = (np.asarray(source)).transpose()

############################################## continue later ##########################################################################################################################################
'''

def photo(code_path, path, cluster, filter, ast_id, name, cycl_len, gain):
    imgpath = path+'/'+cluster+'/frac_med_setcombine12_'+filter
    imglist = os.listdir(imgpath)
    imglist = natsort.natsorted(imglist)
    points = np.loadtxt(os.path.join(imgpath, 'ed'+ast_id+'_'+name+'_'+filter+'_recenter.txt'), comments='#', usecols=(0,1))
    p = path+'/'+cluster+'/frac_med_setcombine12_'+filter
    #print(p)
    A =[]
    for files in imglist:
        if fnmatch.fnmatch(files, 'Teutsch1*'): #'Kron1_'+filter+'_*s_s*_1.fits'
            A.append(files)

    h = 10
    k = 15
    arr = np.arange(0, 30, 1) # 30 = 2*h)
    arr1 = np.arange(0, 30, 0.01)
    os.chdir(p)
    #img_list = os.listdir(p)
    #img_list = natsort.natsorted(img_list)
    #print(img_list)
    #obj=[]
    #for files in img_list:
    #    if fnmatch.fnmatch(files, name+'*'):
    #       obj.append(files)
    #print(obj)
    points[:,0] = points[:,0]-1    #  the sourceextractor assume the origin as (1,1) while python use (0,0)4
    points[:,1] = points[:,1]-1
    Img1= fits.getdata(A[0])
    mean, med, std = sigma_clipped_stats(Img1)
    plt.imshow(Img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
    plt.scatter(points[:,0], points[:,1], color= 'red', marker='.')
    #plt.scatter(Sx, Sy, color= 'blue', marker='x')
    #plt.scatter(source[:,2], source[:,3], color= 'red', marker='.')
    #plt.scatter(source[:,4], source[:,5], color= 'black', marker='.')
    #plt.scatter(source[:,6], source[:,7], color= 'blue', marker='.')
    plt.title('press x on the center of isolated bright star')
    cmd=plt.connect('key_press_event', press)
    plt.show()
    ap=int(np.round(X2))
    bp=int(np.round(Y2))
    sub_img1p=Img1[bp-15:bp+15, ap-15:ap+15]   # 20 pixel will wake the center hift a little bit
    mu, mid, sig = sigma_clipped_stats(sub_img1p)
    sub1_Cxp,sub1_Cyp=center(sub_img1p, 15)[0],center(sub_img1p, 15)[1]
    plt.imshow(sub_img1p,cmap='gray', vmin = mid-5*sig, vmax =mid+5*sig)
    plt.scatter(sub1_Cxp,sub1_Cyp)
    plt.show()
    actual1_Cxp,actual1_Cyp = ap-15+sub1_Cxp,bp-15+sub1_Cyp
    plt.imshow(Img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
    plt.scatter(actual1_Cxp,actual1_Cyp)
    plt.show()
    apx = int(np.round(actual1_Cxp))
    bpy = int(np.round(actual1_Cyp))
    datax = Img1[bpy, apx-k:apx+k]
    datay = Img1[bpy-k:bpy+k, apx]
    data = (datax+datay)/2
    initial = [max(data), 2.5, 15, min(data)]
    popt, pcov = curve_fit(gauss1D, arr, data, p0=initial)
    print(popt)
    FWHM = 2.355*np.sqrt(popt[1]/2)
    print(FWHM) 
    plt.plot(arr, data,'bo', label=str(FWHM))
    plt.plot(arr1, gauss1D(arr1, *popt))
    plt.legend()
    plt.show()
    R = 1.5*FWHM
    print(R, 2*R)
    #if(R > 5):
    #    R = 5.0
    #print(R)
    #R = 5
    aperture = CircularAperture(points, r=1.5*FWHM)# r =5 (corresponds to FWM = 3.3)
    aper1  = CircularAperture(points, r=0.5*FWHM)
    aper2 = CircularAperture(points, r=FWHM)
    radii = np.array([1.5*FWHM, 1*FWHM, 0.5*FWHM])
    apertureO =  [CircularAperture(points, r=r) for r in radii]
    plt.imshow(Img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
    #for i in range(len(radii)):
    #    apertureO[i].plot(color='red')
    aperture.plot(color='red')
    aper1.plot(color='red')
    aper2.plot(color='red')
    plt.colorbar()
    plt.title('click where you want to find background sky')
    cmd=plt.connect('button_release_event', single_click)
    plt.show()
    a=int(np.round(X1))
    b=int(np.round(Y1))
    print(X1, Y1, a, b)
    ap = CircularAperture((a,b), r=h)  # background aperture
    #annulus_aper = CircularAnnulus(points, r_in=R+5., r_out=R+7)
    plt.imshow(Img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
    ap.plot(color='blue')
    #annulus_aper.plot(color='blue')
    plt.show()
    final_path=p+'/phot'
    com = 'mkdir '+final_path
    os.system(com)
    phot_name = []
    back = []
    for i in range(0,cycl_len):
        print(imglist[i])
        Img = fits.getdata(imglist[i])
        mask = make_source_mask(Img, nsigma=2, npixels=5, dilate_size=11)
        mean1, median1, std1 = sigma_clipped_stats(Img, sigma=3.0, mask=mask)
        #print((mean1, median1, std1)) 
        bkg_err = np.ones((256, 256))*std1
        #error = bkg_err
        error = calc_total_error(Img, bkg_err, gain)  
        #plt.imshow(imgscl(Img,1,1),cmap='gray')
        #aperture.plot(color='red')
        #plt.show()
        phot_tableO = aperture_photometry(Img, apertureO) 
        phot_table = aperture_photometry(Img, aperture, error)   ######## changed 
        ap_err = phot_table['aperture_sum_err']
        #print(phot_table)
        #aperstats = ApertureStats(Img, annulus_aper)
        #bg_med = aperstats.median
        bg = Img[b-h:b+h, a-h:a+h] 
        bg_med = np.median(bg) # median combine (this value corresponds to one pixel)
        bg_sum = bg_med*aperture.area
        bg_err = np.sqrt(bg_sum) 
        plt.scatter(i, bg_sum)
        back.append(bg_sum)
        #print(bg_median)
        phot_final =phot_table['aperture_sum']-bg_sum
        final_err = np.asarray(np.sqrt(bg_err**2+ap_err**2))
        #plt.scatter(i, phot_table['aperture_sum'][5])
        phot_table.add_column(phot_final, name='phot_final') # adding bg sub photometry to previous phot_table
        phot_table.add_column(final_err, name='phot_final_err')
        print(phot_table['aperture_sum'], bg_sum, phot_table['aperture_sum']-bg_sum )
        np.savetxt(os.path.join(final_path,'phot_'+name+'_'+filter+'_'+str(i)+'_3FWHM.txt'), phot_table, header='id     Xcenter_pix     Ycenter_Pix     aperure_sum     aperture_sum_error      phot_final      phot_final_err')
        #for j in range(len(radii)):
        #    bkg_ap = bg_med*apertureO[j].area
        #    phot_ap = phot_tableO['aperture_sum_'+str(j)]-bkg_ap
        #    phot_tableO.add_column(phot_ap, name = 'phot_final_ap'+str(j))
        #np.savetxt(os.path.join(final_path,'multi_phot_'+name+'_'+filter+'_'+str(i)+'.txt'), phot_tableO, header='id     Xcenter_pix     Ycenter_Pix     aperure_sum3     aperture_sum2     aperture_sum1    phot_final_ap3   phot_final_ap2     phot_final_ap1')
        np.savetxt(os.path.join(p ,'bkg.txt'), back, header='background_counts')
        phot_name.append('phot_'+name+'_'+filter+'_'+str(i)+'.txt')
    plt.show()
    os.chdir(code_path)
    return(phot_name)

#code_path='/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Code'
#path= '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Data/23_oct'
#cluster = 'Teutsch1'
#filter= 'R'
#ast_id= "201"
#name= 'Teutsch1'
#gain= 20
#imgpath = path+'/'+cluster+'/frac_med_setcombine12_'+filter
#points = np.loadtxt(os.path.join(imgpath, 'ed'+ast_id+'_'+name+'_'+filter+'_recenter.txt'), comments='#', usecols=(0,1))
#print(points)
#imglist = os.listdir(imgpath)
#imglist = natsort.natsorted(imglist)
#A =[]
#for files in imglist:
#   if fnmatch.fnmatch(files, 'Teutsch1*'): #'Kron1_'+filter+'_*s_s*_1.fits'
#       A.append(files)
#Cz3_phot = photo(code_path, path, cluster, filter, ast_id, name, 12,gain, points, A)
#print(Cz3_phot)