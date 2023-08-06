############### to solve negative angle problem ####################
# theta = 0.5* tan^(-1)(U/Q)
#U/Q = tan(2*theta) or 2*theta = A = than^(-1)(U/Q) in radian
# now theta can be negative for either U is negative or Q is negative.
# sin(2*theta) = U/sqrt(U^2+Q^2)  and   cos(2*theta) = Q/sqrt(U^2+Q^2)
# if u is negative then sin(2*theta) will be negative but cos will be positive - which is possible in forth quad.
# so the final angle wil be ... angle = (2*pi-A)/2
# if Q is negative then cos is negative and sin will be positive, implies it lies in 2nd quad
# so the angle become ... angle = (pi-A)/2


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
from astropy.wcs import WCS
from scipy import ndimage
from photutils.aperture import CircularAperture #from photutils import CircularAperture
from photutils.aperture import aperture_photometry #from photutils import aperture_photometry
from single_obj_stack import single_stack
from single_phot import photometry


def Intensity(angle, I0, Q, U):
    theta = np.pi*angle/180.
    I=(I0+(Q*np.cos(4*theta))+ (U*np.sin(4*theta)))/2.
    return(I)
def imgscl(img, factor1=1, factor2=1):         #Image scaling function (for display only)
    med = np.median(img)
    std = np.std(img)
    img_a = img.copy()
    ind = np.where(img < med-std*factor1)
    img_a[ind] = med-std*factor1
    ind = np.where(img > med+std*factor2)
    img_a[ind] = med+std*factor2
    return img_a

#code_path = '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Feb'
#band = ['I'] #'i'   # choose the filter
#path = '/home/namita/Documents/Open_clusters/Mt_ABU/EMPOL_Feb2022/Feb01'
#bias_path = '/home/namita/Documents/Open_clusters/Mt_ABU/EMPOL_Feb2022/Feb01/Bias'
#Flat_path = '/home/namita/Documents/Open_clusters/Mt_ABU/EMPOL_Feb2022/Feb01/Flat/flat_comb' 
code_path= '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_code'
path='/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data'
band = ['R'] #'i'   # choose the filter
bias_path = '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data/Bias'
Flat_path = '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data/Flat'
#Stack = single_stack(path,'HD19820', band, 48 )
#Photo = photo(code_path, path, 'HD19820',  band, 48, Stack)

def single_pol(code_path, path, star, band, cycl_len):
    Folder = path +'/'+star
    os.chdir(Folder)
    photlist = os.listdir(Folder)
    photlist = natsort.natsorted(photlist) # sorting numerically
    one_rot = 7.5 # one rotation corresponds to 15 deg if exp time is 0.7sec and 7.5 (= 360/48) if it is 0.5 sec
    theta = (np.arange(0,cycl_len,1)*one_rot)
    th1 = np.arange(0, cycl_len, 0.05)*one_rot # for plot only
    obj =[]
    for b in range(len(band)):
        sets = []
        for files in photlist:
            #print(files)
            if fnmatch.fnmatch(files, 'Final_phot_*'+band[b]+'_*'):
                sets.append(files)
        n = len(sets)
        #print(n)
        bkg_sets = []
        for files in photlist:
            if fnmatch.fnmatch(files, 'bkg_*'+band[b]+'_*'):
                bkg_sets.append(files)
        #print(bkg_sets)
        #print(sets)
        #n = len(photo[b])
        for i in range(n):
            print(sets[i])
            phot = np.loadtxt((sets[i]), comments='#')
            bkg = np.loadtxt(bkg_sets[i], comments = '#')
            #phot =np.asarray(photo[b][i])
            #print(phot[:,0])
            bg_popt, bg_pcov = curve_fit(Intensity, theta, bkg)
            popt, pcov = curve_fit(Intensity, theta, phot[:,0], sigma = phot[:,1]) # curve_fit(function, x-axis, y-axis)
            e_bI0 = bg_pcov[0,0]**0.5
            e_bQ = bg_pcov[1,1]**0.5
            e_bU = bg_pcov[2,2]**0.5
            e_I0 = pcov[0,0]**0.5
            e_Q = pcov[1,1]**0.5
            e_U = pcov[2,2]**0.5

            #print(popt)
            bP = np.sqrt(bg_popt[1]**2+bg_popt[2]**2)/bg_popt[0] 
            P = np.sqrt(popt[1]**2+popt[2]**2)/popt[0] 
            # deg of polarization = sqrt(q^2+u^2)/I   
            #print(P)
            PA = (np.arctan2(popt[2],popt[1])/2)*(180/np.pi)     # angle of polarization =1/2*tan_inverse (u/q) # arctan2 will handle the quadrant issue.
            bPA = (np.arctan2(bg_popt[2],bg_popt[1])/2)*(180/np.pi) 
            e_P = (np.sqrt((popt[1]**2*e_Q**2+popt[2]**2*e_U**2)/(popt[1]**2+popt[2]**2) + (popt[1]**2+popt[2]**2)/(popt[0]**2)))/popt[0]
            e_PA = (np.sqrt( (popt[1]**2*e_U**2) + (popt[2]**2*e_Q**2) )/(2*(popt[1]**2+popt[2]**2)))*(180/np.pi)
            #print('no. = ', i, 'pol = ', round(P*100,2), 'e_pol = ', round(e_P*100, 2), 'PA = ', round(PA, 2), 'e_PA = ', round(e_PA, 2) )
            #plt.plot(theta, phot,'.', markersize = 12)#, label = bands[b]+', P = '+str(round(P*100,2))+'+/-'+str(round(e_P*100, 2)) + ', PA = '+str(round(PA, 2))+'+/-' + str(round(e_PA, 2)))
            fig, (ax1, ax2) = plt.subplots(figsize=(12,11), nrows=2, sharex=True)
            ax1.errorbar(theta, phot[:,0], yerr = phot[:,1], fmt='o', color ='black', ecolor='gray', ls='none', capsize=3)
            ax1.plot(th1, Intensity(th1, *popt), '-', label = 'P = '+str(round(P*100,2))+'+/-'+str(round(e_P*100, 2)) + ', PA = '+str(round(PA, 2))+'+/-' + str(round(e_PA, 2)))
            #ax1.title(star+', filter = '+band[b])
            #plt.title('')
            #plt.text(theta[1], phot[1], s=str(i+1))
            plt.title("Figure" + str(i+1))

            plt.xlabel('half wave-plate angle'+r'($\theta$)', fontsize = 12)
            
            ax1.legend(fontsize = 12)
            ax2.plot(theta, bkg, 'bo', label = 'P = '+str(round(bP*100,2))+' , PA = '+str(round(bPA, 2)))
            ax2.plot(th1, Intensity(th1, *bg_popt), 'r-')
            ax2.legend()
            obj.append([band[b], 'set '+str(i+1), round(P*100,2), round(e_P*100, 2), round(PA, 2), round(e_PA, 2)] )
            plt.savefig("Final_polarization_single_"+ star +"_withmeanflat" + str(i+1) + ".png")
            plt.close()
            ###plt.show()
            
            
    np.savetxt('Final_polarization_single_'+star+'_withmeanflat.txt', obj, header = 'filter     set     pol     e_pol     PA     e_PA', fmt="%s")
    os.chdir(code_path)
    return(obj)
#band = ['R']
code_path= '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_code'
#path='/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data'
#polarization = single_pol(code_path, path, 'HD19820', band,  12)

