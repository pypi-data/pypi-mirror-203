# need proxy setting on terminal for executing wget 
# run thi sfor one file per filter - since all the stars in 48 angles (per filetr) are at same postion, their image and equitorial coordinates be same.
import numpy as np
#import pyfitsf
import os, sys
import time
import math
import time, datetime
import string
import urllib.request, urllib.parse, urllib.error
from astropy.io import fits
from astropy.wcs import WCS
from astropy.stats import sigma_clipped_stats
import glob
import subprocess
import warnings
import matplotlib.pyplot as plt
import photutils
import natsort
import pyregion
import wget
import fnmatch
import os.path

#filter = 'R'
#cluster = 'Teutsch1'
#match = 'W7'

proxies = {'http':'http://namita:physics@172.16.0.1:3128',
           'https':'https://namita:physics@172.16.0.1:3128'}
sexcommand = 'sex'
#path = '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Data/23_oct'
#F = '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Feb/EMPOL_Feb2021/Feb_6'
"""
Folder= path +'/'+cluster+'/frac_med_setcombine12_'+ filter
img_list = os.listdir(Folder)
img_list = natsort.natsorted(img_list)
imglist = []
for files in img_list:
    if fnmatch.fnmatch(files, 'W7*'):
        print(files)
        imglist.append(files)
print(imglist)
"""

# CD1_1, CD2_1, CD1_2, CD2_2 are conversion matrix (rotational and translational) from CRPX1, CRPX2 (image center) to CRVAL1, CRVAL2 (cental ra, dec) 
def edheader(Image, hdr, ra, dec, outpath, outfile): #add some quantities to the image headers
    hdr.set('RA', ra)  # central ra
    hdr.set('DEC', dec)  # central dec 
    hdr.set('CD1_1',0.00018) # fix for empol
    hdr.set('CD1_2',0.000008)  # fix for empol
    hdr.set('CD2_1',0.000008) # fix for empol
    hdr.set('CD2_2',-0.00018) # fix for empol
    hdr.set('CRPIX1',128) #central x-pixel (for empol 256/2 == header('NAXIS1')/2)
    hdr.set('CRPIX2',128) #central y- pixel (for empol 256/2 == header('NAXIS2')/2)
    hdr.set('CRVAL1',ra) 
    hdr.set('CRVAL2',dec)
    hdr.set('CTYPE1', 'RA---TAN') # fix
    hdr.set('CTYPE2', 'DEC--TAN') # fix
    hdr.set('EQUINOX',2000.0) #fix
    F = os.path.join(outpath, outfile)
    fits.writeto(F, Image, hdr, overwrite=True)
    return(F) 
def getcat(catalog, ra, dec, outpath, outfile):
    boxsize= 1000#740#370 # (in arcsec) fix for empol
    url = "http://tdc-www.harvard.edu/cgi-bin/scat?catalog=" + catalog +  "&ra=" + str(ra) + "&dec=" + str(dec) + "&system=J2000&rad=" + str(boxsize) + "&sort=mag&epoch=2000.00000&nstar=6400" # catalog in string like 'ua2'(mag range 12-22) - for cezernik (for more catalogs visit imwcs site)
    #out=os.path.join(outpath, outfile) #outfile and outpath must be a string
    filename = wget.download(url, os.path.join(outpath, outfile))
    #print(outfile)
    return(outfile)

def Sextractor(code_path, NewImgName, border, corner, outpath, outfile, mag, flg): # NewImage having additional hedaer info (after edheader), border - x,y pixel to exclude 
    #print(outpath)
    #print(NewImgName)
    os.chdir(code_path)
    os.system(sexcommand + ' -c default.sex'+ ' '+ NewImgName) # default.sex file and all the default files in the /usr/share/sextractor folder sho'uld be present in the same folder as the Image files. The extracted source file will be saved in the same folder with name present in default.sex (source.cat)
    xmin = ymin = border
    xmax = ymax = 256-border
    source = np.loadtxt(os.path.join(code_path,'source.cat'), comments='#')
    M = source[:,7]
    ind = np.where(M==99)
    M = np.delete(M, ind[0])
    #print(max(source[:,7]), min(source[:,7]))
    #source[:,0] = source[:,0]-1   # the sourceextractor assume the origin as (1,1) while python use (0,0) 
    #source[:,1] = source[:,1]-1   #  minus 1 is introduce to convert the Sextractor output to python
    goodsource=[]
    i=0
    while(i<len(source[:,0 ]-1)):
        star = source[i,:] # one row all the columns (0=id, 1=mag, 2=x, 3=y)
        i=i+1
        if(star[0] < xmin): continue # exclude all the points with xpix < 15 
        if(star[0] > xmax): continue # exclude all the points with xpix > 240 
        if(star[1] < ymin): continue # exclude all the points with ypix < 15 
        if(star[1] > ymax): continue # # exclude all the points with ypix > 240 
        if(star[0]+star[1]< corner): continue
        if(star[0] + (256-star[1])) < corner: continue
        if((256-star[0]) < corner): continue
        if((256-star[0]) + (256-star[1]) < corner): continue
        if(star[8] > mag): continue    # magnitude error constraint - change it if necessary
        if(star[9] > flg): continue
        if(star[7] >= max(M)-3.0):continue
        goodsource.append(star)
       

#print(goodsource, len(goodsource))
    np.savetxt(os.path.join(outpath, outfile), goodsource, header='1 X_IMAGE    Object position along x    [pixel] \n 2 Y_IMAGE    Object position along y    [pixel] \n 3 MAG_BEST    Best of MAG_AUTO and MAG_ISOCOR    [mag] \n 4 FLUX_APER    Flux vector within fixed circular aperture(s)    [count] \n 5 FLUXERR_APER    RMS error vector for aperture flux(es)    [count] \n 6 MAG_APER    Fixed aperture magnitude vector    [mag] \n 7 MAGERR_APER    RMS error vector for fixed aperture mag.    [mag] \n 8 FLAGS    Extraction flags') # header should be same as that of the 'source.cat' file (source extracter file), so edit header if u are editing default.params   
    return(goodsource) 


#Folder= path+'/'+cluster+'/frac_med_setcombine12_'+filter


###################################### for one file only ra = 15.78 & dec 62.787 (CZ3), ra = 111.533 & dec = -15.093(waterloo 7)#########################


def do_astrometry(code_path, path,cluster,filter, name, imglist, ra, dec):
    out=[]
    Folder= path+'/'+cluster+'/frac_med_setcombine12_'+filter
    #img_list = os.listdir(Folder)
    #img_list = natsort.natsorted(img_list)
    #print(img_list)
    #imglist = []
    #for files in img_list:
    #    if fnmatch.fnmatch(files, name+'*'):
    #        imglist.append(files)
    #print(imglist[0])
    img = fits.getdata(os.path.join(Folder, imglist[0]))
    hdul = fits.open(os.path.join(Folder,imglist[0])) 
    hdr = hdul[0].header
    #print(hdr)
    cat = ['ua2', 'ucac4','tmc']
    con1 = np.array([10, 0.25, 0.2, 0.15, 0.1]) # e_mag constrain
    con2 = np.array([0, 100]) # flag (only integer values are possible)
    err = []
    ID = []
    for a in range(0,3):
        cat_down = getcat(cat[a], ra, dec, Folder, 'cat_'+cat[a]+'.txt')
        for b in range(0, len(con1)):
            for c in range(0, len(con2)):
                edimg = edheader(img, hdr, ra, dec, Folder, 'ed'+str(a)+str(b)+str(c)+'_'+imglist[0])
                Source_ext = Sextractor(code_path, edimg, 10, 20, Folder, 'ed'+str(a)+str(b)+str(c)+'_source_ext_'+name+'_'+filter+'_0.txt', con1[b], con2[c]) 
                os.chdir(Folder)
                os.system('imwcs' + ' -d ' + os.path.join(Folder, 'ed'+str(a)+str(b)+str(c)+'_source_ext_'+name+'_'+filter+'_0.txt') + ' -c '+cat_down+' -q i9 -v -w ' + edimg+' > output.txt') 
                time.sleep(2)
                I = 'ed'+str(a)+str(b)+str(c)+'_'+imglist[0]
                initial = I[:-5]
                print(initial)
                file_exists = os.path.isfile(initial+'w.fits')
                if file_exists:
                   print('exist')
                else:
                    head = hdr
                    head.set('WCSSEP', 100)
                    fits.writeto(initial+'w.fits', img, head)
                final = fits.open(initial+'w.fits')
                sep = final[0].header['WCSSEP']
                print(a,b,c,' = ', sep)
                ID.append(str(a)+str(b)+str(c))
                err.append(sep)
                os.chdir(code_path)
    min_err = np.argmin(err)
    print(err[min_err], ID[min_err])
    out.append(err[min_err])
    out.append(ID[min_err])
    return(out)

#code_path = '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Code'
#path = '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Data/23_oct'
#cluster = 'Teutsch1'
#filter = 'R'
#imgpath = path+'/'+cluster+'/frac_med_setcombine12_'+filter
#imglist = os.listdir(imgpath)
#imglist = natsort.natsorted(imglist)
#name = 'Teutsch1'
#ra = 84.87208  ##15.77875 #15.77875 #113.661 #111.532
#dec= 33.34611
#ast_id = astrometry(code_path, path,cluster,filter, name, imglist, ra, dec)
#print("This is ast", ast_id)


#Folder= path+'/'+cluster+'/frac_med_setcombine12_'+filter
