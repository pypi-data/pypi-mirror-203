# 1.  set the paths of masterbias, masterflat and science images. 
# 2. set the filter 
# output -folders of stacked images of each sets

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
from photutils.utils import calc_total_error
from astropy.stats import SigmaClip
from scipy import ndimage
from photutils.aperture import CircularAperture #from photutils import CircularAperture
from photutils.aperture import aperture_photometry #from photutils import aperture_photometry
from photutils.aperture import CircularAnnulus #from photutils import CircularAnnulus
from astropy.table import hstack
from astropy.table import Column
from single_obj_stack import *
from PIL import ImageTk, Image
from astropy.nddata import *
from photutils.segmentation import make_source_mask
#from trial_gui import *

def single_click(event):
    global X1,Y1
    if event.button == 3:
        X1, Y1 = event.xdata, event.ydata
        plt.close(1)

def Gauss2D(xy, x0, y0, s, A):                                 # 2D- gaussian fiting is better than ndimage_maximum_posiyion and Center_of_mass 
    x,y=xy
    c=1/(2*s**2)
    f = A*np.exp(-c*((x-x0)**2+(y-y0)**2))
    return(f)
k=15
def center(subimg):
    x = np.arange(0, subimg.shape[1],1)
    y = np.arange(0, subimg.shape[0], 1)
    xx, yy = np.meshgrid(x,y)
    x0 = k
    y0 = k
    s = max(*subimg.shape)*0.1
    A=np.max(subimg)
    initial_guess=[x0,y0,s,A]
    param, err = curve_fit(Gauss2D, (xx.ravel(), yy.ravel()), subimg.ravel(), p0=initial_guess)
    return(param)

def gauss1D(x, A, width, mu): 
    return A*np.exp(-(x-mu)**2/width)
#code_path= '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_code'
#path='/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data'
#band = ['R'] #'i'   # choose the filter
#bias_path = '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data/Bias'
#Flat_path = '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data/Flat'
# Stack = single_stack(path, 'HD19820', band, 48) # single_stack(path, bias_path,Flat_path, 'f33', band, 12 )

arr = np.arange(0, 30, 1) # 30 = 2*h)
arr1 = np.arange(0, 30, 0.01)
gain = 20
def photometry(code_path,path,star, band, cycl_len, Stack, gain):
    folder = path+'/'+star
    arr = np.arange(0, 30, 1) # 30 = 2*h)
    arr1 = np.arange(0, 30, 0.01)
    #savepath = '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Jan/EMPOL_Jan2021/EMPOL_Jan13/HD25443' 
    #save_path=folder+'/downloads'
    #if os.path.exists(save_path):
    #    shutil.rmtree(save_path)
    #com = 'mkdir '+save_path
    #os.system(com)
    os.chdir(folder)
    Bphot = []
    for B in range(0,len(band)):
        
        command = 'ls -d final_frac_med_'+band[B]+'_set_*'
        #print(command)
        os.system(command)
        #setlist = [line.rstrip("\n") for line in open('sets')]
        #p = len(setlist)
        #print(setlist)
        p = len(Stack[B])
        #print("this is p ", p)
        for q in range(1,p+1):
            #print('band = ', band[B], ' set: ',  q)
            #print(len(Stack[B][q-1]))
            imgpath = folder+'/final_frac_med_'+band[B]+'_set_'+str(q)
            #print("this is imgpath ", imgpath)
            img_list = os.listdir(imgpath)
            imgs = natsort.natsorted(img_list) # sorting numerically
            img1 = fits.getdata(os.path.join(imgpath,imgs[0]))
            img1 = Stack[B][q-1][0]
            #print(img1)
            mean, med, std = sigma_clipped_stats(img1)
            plt.imshow(img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
            plt.colorbar()
            plt.title('click on center of bright star \n'+ band[B]+'set: '+str(q)+', 0th image')
            cmd=plt.connect('button_release_event', single_click)
            plt.show()
            h=15
            k=15
            a=int(np.round(X1))
            b=int(np.round(Y1))
            #print(X1, Y1, a, b)
            sub_img=img1[b-h:b+h, a-h:a+h]
            sub_Cx,sub_Cy=center(sub_img)[0],center(sub_img)[1]
            actual_Cx,actual_Cy = a-h+sub_Cx,b-h+sub_Cy
            Cx = int(np.round(actual_Cx))
            Cy = int(np.round(actual_Cy))
            #print(actual_Cx, actual_Cy, Cx, Cy)
            datax = img1[Cy, Cx-15:Cx+15]
            datay = img1[Cy-15:Cy+15, Cx]
            data = (datax+datay)/2
            initial = [max(data), 2.5, 15]
            popt, pcov = curve_fit(gauss1D, arr, data, p0=initial)
            #print(popt)
            FWHM = 2.345*np.sqrt(popt[1]/2)  # 2.355
            #print(FWHM) 
            ###plt.plot(arr, data,'bo', label=str(FWHM))
            ###plt.plot(arr1, gauss1D(arr1, *popt))
            ###plt.legend()
            #plt.show()
            R = 1.5*FWHM  
            #print("R = ", R, Cx, Cy)#
            #R = float(input("aperture Radius : "))#
            #print("this is R ", R)
            radii = np.arange(1,10,0.1)

            #aasthacomment
            #plt.imshow(img1, cmap='gray', vmin = med-5*std, vmax = med+5*std)
            #plt.title( band[B]+'set: '+str(q)+', 0th image')
            #plt.scatter(actual_Cx,actual_Cy)
            #plt.scatter((Cx-h, Cx+h, Cx-h, Cx+h), (Cy-h, Cy+h, Cy+h, Cy-h))
            
            
            apertures = CircularAperture((actual_Cx,actual_Cy), r=R)
            #multi = [CircularAperture((actual_Cx,actual_Cy), r=r) for r in radii]
            #for i in range(len(radii)):
            #    multi[i].plot(color='red')
            ###apertures.plot(color='blue')
            #plt.show()
            annulus_apertures = CircularAnnulus((actual_Cx,actual_Cy), r_in=30., r_out=40.)
            ###annulus_apertures.plot(color='blue')
            #plt.show()
            #ph = []
            #for i in range(len(radii)):
            #    Flux = aperture_photometry(img1, multi[i])
            #    ph.append(Flux['aperture_sum'])
            #print(ph.dtype)
            #plt.plot(radii, ph)
            #plt.plot((R,R), (min(ph), max(ph)))
            #plt.show()
            #final_R = float(input('aperture size : '))
            apertures = CircularAperture((actual_Cx,actual_Cy), r=R)
            photC= []
            photE = []
            bg = []
            for i in range(0, cycl_len):
                #print(imgs[i])
                Final = fits.getdata(os.path.join(imgpath,imgs[i]))
                Final = Stack[B][q-1][i]
                mask = make_source_mask(Final, nsigma=2, npixels=5, dilate_size=11)
                mean1, median1, std1 = sigma_clipped_stats(Final, sigma=5.0, mask=mask)
                #print("Mean1, meadian1, std1 ", mean1, median1, std1)
                #print('background image stats: ', mean1, std1)
                bkg_err = np.ones((256,256))*std1
                error = calc_total_error(Final, bkg_err, gain)  
                #bkg_err = Final*0.1
                rawflux_table = aperture_photometry(Final, apertures, bkg_err)
                ap_err = rawflux_table['aperture_sum_err']
                bkgflux_table = aperture_photometry(Final, annulus_apertures, bkg_err)
                an_err =  bkgflux_table['aperture_sum_err']
                #phot_table = hstack([rawflux_table, bkgflux_table], table_names=['raw', 'bkg'])
                bkg_mean = bkgflux_table['aperture_sum']/annulus_apertures.area
                #print(bkgflux_table['aperture_sum'],annulus_apertures.area)
                # print(bkg_mean)
                bkg_sum = bkg_mean * apertures.area
                
                
                
                ###plt.scatter(i, bkg_sum)
                
                
                
                ap_bkg_err =  bkgflux_table['aperture_sum_err']*apertures.area/annulus_apertures.area
                final_sum = np.asarray(rawflux_table['aperture_sum'] - bkg_sum)
                #print(final_sum)
                final_err = np.asarray(np.sqrt(ap_bkg_err**2+ap_err**2))
                #print(final_err)
                rawflux_table.add_column(final_sum, name='phot_final')
                rawflux_table.add_column(final_err, name='phot_err')
                #print(rawflux_table)
                #phot_table['residual_aperture_sum'] = final_sum
                bg.append(bkg_sum)
                photC.append(final_sum)
                photE.append(final_err)
            plt.show()
            phot= np.c_[photC, photE]
            np.savetxt('bkg_'+star+'_'+band[B]+'_set_'+str(q)+'.txt', bg, header='background counts')
            np.savetxt('Final_phot_'+star+'_'+band[B]+'_set_'+str(q)+'.txt', phot, header='residual_aperture_sum      aperture_sum_err')
            Bphot.append('Final_phot_'+star+'_'+band[B]+'_set_'+str(q)+'.txt')
    os.chdir(code_path)
    return(Bphot)


#code_path= '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_code'
#path='/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data'
#band = ['R'] #'i'   # choose the filter


# code_path = '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Feb'

#P = photo(code_path, path, star,  band, cycl_len, Stack, gain)
# print(P[1])
  
















