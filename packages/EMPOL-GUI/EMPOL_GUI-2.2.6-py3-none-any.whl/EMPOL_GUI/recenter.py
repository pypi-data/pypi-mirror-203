# recenter 
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
from astropy.stats import sigma_clipped_stats
from scipy import ndimage
import shutil
from photutils.centroids import centroid_com, centroid_quadratic
from photutils.centroids import centroid_1dg, centroid_2dg

def cent_2g(Image,x,y,h,k ):
    x=int(round(x))
    y=int(round(y))
    sub = Image[y-k:y+k, x-h:x+h]
    xs, ys = centroid_2dg(sub)
    xp, yp = x-h+xs, y-k+ys
    return(xp,yp)

def cent(Image,x,y,h,k ):
    x = int(round(x))
    y = int(round(y))
    sub = Image[y-k:y+k, x-h:x+h]
    xs, ys = centroid_quadratic(sub)
    xp, yp = x-h+xs, y-k+ys
    return(xp,yp)
    
def COM(image,x,y,r,s):						## Function to find the centre of mass of an image
  x = int(round(x))
  y = int(round(y))
  #image = image - np.median(image)
  subimage = image[y-r:y+s,x-r:x+s]				## Prod Subimge containing only the star of interest by providing appx centres
  i=x-r 							## (0,0) location of subimage , later to be added to COM coord
  j=y-r
  p,q = ndimage.maximum_position(subimage)		## Getting values of actual centres of the subimage  measurements.center_of_mass
  #print "COM of subimage (x,y):", p,q
  a= q+i							## Getting information about the actual coordinates of that particular centre
  b= p+j							##added opposite since COM fn gives coordinates as (y,x)
  #print "Actual centres (x,y) :", a,b
  return (a,b)

def COM_iter(image,a,b,p,q):

  while True:

     a1,b1 = COM(image,a,b,p,q)
     if(math.sqrt((a1-a)**2+(b1-b)**2)<0.1):
        break
     else:
        a = a1
        b = b1
  return a1,b1
    
#path= '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Data/23_oct'
#cluster = 'Teutsch1'
#filter= 'R'
#ast_id= '201'
#name= 'Teutsch1'
#gain= 40
#imgpath = path+ "/" + cluster + '/frac_med_setcombine12_'+filter  
#points = np.loadtxt(os.path.join(imgpath, 'ed'+ast_id+'_'+name+'_'+filter+'_Gaia.txt'), comments='#')
#xo = points[:,0]-1    #  the sourceextractor assume the origin as (1,1) while python use (0,0)4
#yo = points[:,1]-1
#print(xo, yo)
#xc = []
#yc = []
def recenter_fun(path, cluster, name, filter, ast_id):
    imgpath = path+ "/" + cluster + '/frac_med_setcombine12_'+filter  
    points = np.loadtxt(os.path.join(imgpath, 'ed'+ast_id+'_'+name+'_'+filter+'_Gaia.txt'), comments='#')
    xo = points[:,0]-1    #  the sourceextractor assume the origin as (1,1) while python use (0,0)4
    yo = points[:,1]-1
    #print(xo, yo)
    xc = []
    yc = []
    img = fits.getdata(os.path.join(imgpath, name+'_set_combined_'+filter+'_0.fits'))
    mean, med, std = sigma_clipped_stats(img)
    for i in range(len(xo)):
        print(i, xo[i], yo[i])
        x, y = cent(img, xo[i], yo[i], 3, 3)
        print(x,y)
        if((np.isnan(y)==True) | (abs(yo[i]-y) > 3)):  # put ylimit only if the astrometric error is less than 1 arcsec
            print(' quad centroid failed' )
            x, y = cent_2g(img, xo[i], yo[i], 3, 3)
            print(x,y)
            if((np.isnan(y)==True) | (abs(yo[i]-y) > 3)):
                print(' cent 2g failed')
                x, y = COM(img, xo[i], yo[i],3,3)
                print(x,y)
                if((np.isnan(x)==True) | (abs(yo[i]-y) > 3)):
                    print(' cent COM failed')
                    x, y = xo[i], yo[i]
                    print(x,y)
        #plt.imshow(img,cmap='gray', vmin = med-5*std, vmax = med+5*std)
        #plt.plot(xo[i], yo[i], 'r.', label='original')
        #plt.plot(x, y, 'bx', label= 'shifted') 
        #plt.title('x='+str(abs(xo[i]-x))+' y='+str(abs(yo[i]-y))) 
        #plt.show()          
        xc.append(x)
        yc.append(y)
    shiftx = abs(xo-xc)
    shifty = abs(yo-yc)
    print(shiftx, shifty)
    plt.imshow(img,cmap='gray', vmin = med-5*std, vmax = med+5*std)
    plt.plot(xo, yo, 'r.', label='original')
    plt.plot(xc, yc, 'bx', label= 'shifted')
    plt.legend()
    plt.show()
    xpix = np.asarray(xc)+1
    ypix = np.asarray(yc)+1
    df = np.c_[xpix, ypix, points[:,2], points[:,3]]
    np.savetxt(os.path.join(imgpath, 'ed'+ast_id+'_'+name+'_'+filter+'_recenter.txt'), df, header='xpix    ypix    RAJ2000    DECJ2000')
    return(xpix,ypix)
