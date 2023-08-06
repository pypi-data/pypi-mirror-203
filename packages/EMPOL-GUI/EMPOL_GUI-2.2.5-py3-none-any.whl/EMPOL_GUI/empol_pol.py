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
from photutils.aperture import CircularAperture
from photutils.aperture import aperture_photometry
from astropy.stats import sigma_clipped_stats
#import empol_photometry
#import extcatalog


def Intensity(angle, I0, Q, U):
    theta = np.pi*angle/180
    I=(I0+(Q*np.cos(4*theta))+(U*np.sin(4*theta)))/2
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

def polarization(path,cluster, ID, filter, name, cycl_len):
    imgpath = path+'/Teutsch1/frac_med_setcombine12_R/phot'
    photl = os.listdir(imgpath)
    photl = natsort.natsorted(photl)
    photlist= []
    photlist = photl


    direc = path+'/'+cluster+'/frac_med_setcombine12_'+filter
    p = path+'/'+cluster+'/frac_med_setcombine12_'+filter+'/phot'
    #print(photlist)
    #back = np.loadtxt(os.path.join(direc, 'bkg.txt'), comments = '#')
    os.chdir(direc)
    #plist = os.listdir(p)
    Img, header=fits.getdata('ed'+str(ID)+'_'+name+'_set_combined_'+filter+'_0w.fits', header=True) # astrometric file
    mean, med, std = sigma_clipped_stats(Img)
    w = WCS(header)
    one_rot = 7.5 # one rotation corresponds to 15 deg if exp time is 0.7sec and 7.5 (= 360/48) if it is 0.5 sec
    phot1 = np.loadtxt(os.path.join(p, photlist[1]), comments='#')
    #print("photlist[1]", photlist[1])
    print("phot1", phot1)
    #print(phot1[:,3])
    
    """
    plt.imshow(Img,cmap='gray', vmin = med-3*std, vmax = med+3*std)
    plt.colorbar()
    plt.plot(phot1[:,1]-1, phot1[:,2]-1,'r.')
    #aperture.plot(color='blue')
    for i in range(len(phot1)):
        plt.text(phot1[i,1]-1, phot1[i,2]-1, s = str(i), color = 'red')
    plt.show()
    
    """
    
    indx = np.argwhere(~np.isnan(phot1).any(axis=1))
    #print(indx)
    n = len(phot1[:,0]) # number of stars =15
    
    #print('number of stars = ', n) 
    star =[]
    output2=[]
    theta = np.arange(0,cycl_len,1)*one_rot
    th1 = np.arange(0, cycl_len, 0.05)*one_rot # for plot only
    #b_popt, b_pcov = curve_fit(Intensity, theta, back)
    #bP = np.sqrt(b_popt[1]**2+b_popt[2]**2)/b_popt[0]   # deg of polarization = sqrt(q^2+u^2)/I   
    #bPA = (np.arctan2(b_popt[2],b_popt[1])/2)*(180/np.pi)     # angle of polarization =1/2*tan_inverse (u/q) 
    #e_bQ = b_pcov[1,1]**0.5
    #e_bU = b_pcov[2,2]**0.5
    #e_bP = (np.sqrt((b_popt[1]**2*e_bQ**2+b_popt[2]**2*e_bU**2)/(b_popt[1]**2+b_popt[2]**2) + (b_popt[1]**2+b_popt[2]**2)/(b_popt[0]**2)))/b_popt[0]
    #e_bPA = (np.sqrt( (b_popt[1]**2*e_bU**2) + (b_popt[2]**2*e_bQ**2) )/(2*(b_popt[1]**2+b_popt[2]**2)))*(180/np.pi)
    #print('background ', 'pol = ', round(bP*100,2), 'e_pol = ', round(e_bP*100, 2), 'PA = ', round(bPA, 2), 'e_PA = ', round(e_bPA, 2) )
    #plt.plot(theta, back, 'bo')
    #plt.plot(th1, Intensity(th1, *b_popt), 'r-')
    #plt.show()
    #Flag = []
    for i in range(n):
        #print(photl[0])
        star_count = np.loadtxt(os.path.join(p,photlist[0]), comments='#')
        #print("length of photlist= ", len(photlist)) #length of photlist= 12
        #print("Star count= ", star_count)
        #SC = star_count[i,12]
        #if(SC < 2*back[0]):
        #    Flag.append(i+1)
        number = []
        s = []
        #Ib = []
        for j in range(len(photlist)):
            #print(i, photlist[j])
            phot = np.loadtxt(os.path.join(p,photlist[j]), comments='#')
            counts = phot[:,5][i]  # 12 for multiple phot - modified, 5 for empol_photopmetry.py
            print(i,j)
            #counts_b = phot[:,6][i]#*corr[j] # 6th col = modified 2FWHM without bkg
            #sig = phot[:,6][i]
            #s.append(sig)
            #Ib.append(counts_b)
            number.append(counts)
        print(len(theta))
        print(len(number))
        df = np.c_[theta, number]

        print(df)
        df = df[~np.isnan(df).any(axis=1), :]
        if(len(df[:,0])!=0):
            popt, pcov = curve_fit(Intensity, df[:,0], df[:,1])#, sigma=s) # curve_fit(function, x-axis, y-axis)
            #poptb, pcovb = curve_fit(Intensity, theta, Ib)
            #print(i, popt)
            q = popt[1]/popt[0]
            u = popt[2]/popt[0]
            #print('Q/I = ', q, ' U/I = ', u)
            e_I0 = pcov[0,0]**0.5
            e_Q = pcov[1,1]**0.5
            e_U = pcov[2,2]**0.5
            #print('U = ', popt[2], ' & Q = ', popt[1] )
            P = np.sqrt(popt[1]**2+popt[2]**2)/popt[0]   # deg of polarization = sqrt(q^2+u^2)/I   
            PA = (np.arctan2(popt[2],popt[1])/2)*(180/np.pi)     # angle of pol df = np.c_[theta, number] polarization =1/2*tan_inverse (u/q) 
            e_P = (np.sqrt((popt[1]**2*e_Q**2+popt[2]**2*e_U**2)/(popt[1]**2+popt[2]**2) + ((popt[1]**2+popt[2]**2)/(popt[0]**2))*e_I0**2))/popt[0]
            e_PA = (np.sqrt( (popt[1]**2*e_U**2) + (popt[2]**2*e_Q**2) )/(2*(popt[1]**2+popt[2]**2)))*(180/np.pi)
        
            #qb = poptb[1]/poptb[0]
            #ub = poptb[2]/poptb[0]
            #print('Q/I = ', q, ' U/I = ', u)
            #e_I0b = pcovb[0,0]**0.5
            #e_Qb = pcovb[1,1]**0.5
            #e_Ub = pcovb[2,2]**0.5
            #print('U = ', popt[2], ' & Q = ', popt[1] )
            #Pb = np.sqrt(poptb[1]**2+poptb[2]**2)/poptb[0]   # deg of polarization = sqrt(q^2+u^2)/I   
            #PAb = (np.arctan2(poptb[2],poptb[1])/2)*(180/np.pi)     # angle of polarization =1/2*tan_inverse (u/q) 
            #e_Pb = (np.sqrt((poptb[1]**2*e_Qb**2+poptb[2]**2*e_Ub**2)/(poptb[1]**2+poptb[2]**2) + (poptb[1]**2+poptb[2]**2)*e_I0b**2/(poptb[0]**2)))/poptb[0]
            #e_PAb = (np.sqrt( (poptb[1]**2*e_Ub**2) + (poptb[2]**2*e_Qb**2) )/(2*(poptb[1]**2+poptb[2]**2)))*(180/np.pi)
            print( 'no. = ', i, 'pol = ', round(P*100,2), 'e_pol = ', round(e_P*100, 2), 'PA = ', round(PA, 2), 'e_PA = ', round(e_PA, 2) )
            #print('with bkg sub  ', 'no. = ', i, 'pol = ', round(Pb*100,2), 'e_pol = ', round(e_Pb*100, 2), 'PA = ', round(PAb, 2), 'e_PA = ', round(e_PAb, 2) )
            #fig, (ax1, ax2, ax3) = plt.subplots(figsize=(12,10), nrows=3, sharex=True)
            #plt.figure(figsize=(12,10))
            #plt.plot(df[:,0], df[:,1], 'ko')
            #ax1.errorbar(theta, number, yerr = s, fmt='o', color ='black', ecolor='gray', ls='none', capsize=3)
            #plt.plot(th1, Intensity(th1, *popt), 'r-', label = 'without bkg sub   P = '+str(round(P*100,2))+'+/-'+str( round(e_P*100, 2))+ '   PA = '+str(round(PA, 2))+'+/-'+str(round(e_PA, 2)))
            #plt.legend()
            #ax2.plot(theta, back, 'bo')
            #ax2.plot(th1, Intensity(th1, *b_popt), 'b-', label='bkg counts(sky) P = '+ str(round(bP*100,2))+ '+/-'+ str(round(e_bP*100, 2))+ '   PA = '+str(round(bPA, 2))+'+/-'+str(round(e_bPA, 2)))
            #ax2.legend()
            #ax3.plot(theta, Ib, 'go')
            #ax3.plot(th1, Intensity(th1, *poptb), 'g-', label='with bkg sub P = '+str(round(Pb*100,2))+'+/-'+str( round(e_Pb*100, 2))+ '   PA = '+str(round(PAb, 2))+'+/-'+str(round(e_PAb, 2)))
            #ax1.title('star '+ str(i))
            #ax3.legend()
            #plt.subplots_adjust(left=0.05, right=0.98, top=0.95, bottom=0.05)
            #plt.savefig(os.path.join(direc, 'fitting_star'+str(i)+'.png'), format='png')
            #plt.xlabel('theta')
            #plt.ylabel('counts')
            #plt.show()
            e_q = q*np.sqrt((e_Q**2/popt[1]**2) + (e_I0**2/popt[0]**2))
            e_u = u*np.sqrt((e_U**2/popt[2]**2) + (e_I0**2/popt[0]**2))
            #print(q*np.sqrt((e_Q/popt[1])**2+(e_I0/popt[0])**2), u*np.sqrt((e_U/popt[2])**2+(e_I0/popt[0])**2) )
            #plt.plot(q, u,  'r.', markersize=12)
            #plt.text(q,u, str(i), color='blue')
            #plt.errorbar(q,u, e_q, e_u, ecolor='gray')
            #plt.plot(popt[1],popt[2],  'r.', markersize=12)
            #plt.text(popt[1], popt[2], str(i), color='blue')
            #plt.errorbar(popt[1], popt[2], e_Q, e_U, ecolor='gray')
            star.append([i+1, round(P*100,2), round(e_P*100, 2), round(PA, 2), round(e_PA, 2), round(popt[1], 2), round(e_Q, 2), round(popt[2], 2), round(e_U, 2), round(popt[0],2), round(e_I0, 2),  q, e_q, u, e_u])

    #ss =  np.loadtxt('ed'+str(ID)+'_'+name+'_'+filter+'_Gaia.txt', comments='#')#, usecols=(0,1))
    #print(len(ss[:,3]))
    #source = np.loadtxt(os.path.join(Folder, 'isolated_sources.txt'), comments='#')
    #source[:,0] = source[:,0]-1
    #source[:,1] = source[:,1]-1
    ss =np.loadtxt('ed'+ID+'_'+name+'_R_recenter.txt', comments = '#')
    #ra2000, dec2000 = w.all_pix2world(source[:,0]+1, source[:,1]+1, 1) # source [:,0 & 1] corresponds to xcenter, ycenter (the coordinates should be same as source extractor)

    final_file = np.c_[star,ss[indx,2], ss[indx,3], ss[indx,0], ss[indx,1]] # stacking all the columns
    

    np.savetxt('Final_pol_'+name+'_ed'+str(ID)+'_'+filter+'_without_bkg_modified.txt', final_file, header='Corrdinates are based on (1,1) center as used by ds9 or IRAF \n No     Pol     e_pol     PA     e_PA     Q     e_Q     U     e_U     I     e_I     q     e_q     u     e_u     RA     DEC     Xcenter_pix     Ycenter_Pix')

    #aperture = CircularAperture(source, r=5)
    plt.imshow(Img,cmap='gray', vmin = med-3*std, vmax = med+3*std)
    plt.colorbar()
    plt.plot(ss[:,0]-1, ss[:,1]-1,'b.',  mew=3)
    #aperture.plot(color='blue')
    for i in range(len(ss)):
        plt.text(ss[i,0]-1, ss[i,1]-1, s = str(i), color = 'red')
    plt.show()
    #print(Flag)
    return(final_file)

#path= '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Data/23_oct'
#imgpath = path+'/Teutsch1/frac_med_setcombine12_R/phot'
#photl = os.listdir(imgpath)
#photl = natsort.natsorted(photl)
#print(photl)
#photlist= []
#filter = 'R'
#for filess in photl:
#        if fnmatch.fnmatch(filess, 'phot_*'+filter+'*_withoutbkg*'):
#            photlist.append(filess)
#photlist = photl
#print(photlist) #lists all the files names in folder "phot"
#P = polarization(path,'Teutsch1','201', 'R', 'Teutsch1', photlist,12)