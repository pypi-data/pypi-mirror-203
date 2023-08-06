# 1.  set the paths of masterbias, masterflat and science images. 
# 2. set the filter 
# output -folders of stacked images of each sets
# new_stacked_band_set is files having the centers of all the images in all the sets lying at the same points.
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
#from trial_gui import *
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
k=20
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

def single_stack(path, star, band, cycl_len ): 
    imgpath = path +'/'+star
    bias_path = path +'/Bias'
    Flat_path = path +'/Flat'
    img_list = os.listdir(imgpath)
    img_list = natsort.natsorted(img_list) 
    #print(img_list)
    #for j in range(n):
    #   print(imgs[i+m], flats[i])
    #  imgN = fits.getdata(os.path.join(imgpath, imgs[i+m]))# sorting numerically
    #print(img_list)
    Simgs = []
    Sname = []
    for B in range(0,len(band)):   # loop on bands
        flat_list = os.listdir(Flat_path)
        flat_list = natsort.natsorted(flat_list)
        #print(flat_list)
        #flats=[]
        #for files in flat_list:
        #    if fnmatch.fnmatch(files, '*_'+band[B]+'_*'):
        #        flats.append(files)
        #print(flats)
        flat = fits.getdata(os.path.join(Flat_path, band[B]+'mean.fits')) 
        sets=[]
        for files in img_list:
            if fnmatch.fnmatch(files, star+'_'+band[B]+'_*s_s*_1.fits'):
                sets.append(files)
        p = len(sets) # number of sets
        print('number of sets: ', p)
        #print(sets)
        imgs =[]
        if p==0:
            p = 1
        for k in range(1,p+1):   # there is no set as s0, set number starts from 1 (like - s1), so k starts from 1 and loop itterate p times (when second term is p+1)
            setlist = []
            for files in img_list:
                if p ==1 :
                    if fnmatch.fnmatch(files, '*_'+band[B]+'_*s_*'):
                        setlist.append(files)
                else:
                    if fnmatch.fnmatch(files,  '*_'+band[B]+'_*s_s'+str(k)+'_*'):
                        setlist.append(files)
            imgs.append(setlist)
        #print(imgs)
        set_imgs = []
        set_name=[]
        #print(imgs)
        for q in range(1,p+1):   # loop on sets
            print('set number: ', q)
            #print(imgs[q-1][0], flats[0])
            data = fits.getdata(os.path.join(imgpath,imgs[q-1][0]))
            data = data.astype('>f8')
            img1 = (data[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/flat#/fits.getdata(os.path.join(Flat_path, flats[0]))
            mean, med, std = sigma_clipped_stats(img1)
            plt.imshow(img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
            plt.colorbar()
            plt.title('click on center of bright star '+str(imgs[q-1][0]))
            cmd=plt.connect('button_release_event', single_click)
            plt.show()
            k=20
            a=int(np.round(X1))
            b=int(np.round(Y1))
            #print(X1, Y1, a, b)
            #sub_img1=img1[b-30:b+31, a-30:a+31]
            #sub1_Cx,sub1_Cy=center(sub_img1, 30)[0],center(sub_img1, 30)[1]
            #actual1_Cx,actual1_Cy = a-30+sub1_Cx,b-30+sub1_Cy
            #ax = int(np.round(actual1_Cx))
            #by = int(np.round(actual1_Cy))
            #print(band[B])
            actual1_Cx,actual1_Cy =  cent(img1,X1,Y1,30,30)
            ax = int(np.round(actual1_Cx))
            by = int(np.round(actual1_Cy))
            final_path=imgpath+'/final_frac_med_'+band[B]+'_set_'+str(q)
            if os.path.exists(final_path):
                shutil.rmtree(final_path)
            com = 'mkdir '+final_path
            os.system(com)
            n =int(len(imgs[q-1])/cycl_len)
            SSimgs = []
            SSname=[]
            for i in range(0,cycl_len):    # loop on individual images in a cycle
                m=0
                Cx=ax  # initial centeral x-coordinate
                Cy=by   # initial Y-coordinate
                img = np.zeros((256,256, n))
                for j in range(n):
                    #print(imgs[q-1][i+m])#, flats[i])
                    image = fits.getdata(os.path.join(imgpath, imgs[q-1][i+m]))
                    image = image.astype('>f8')
                    imge = (image[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/flat#/fits.getdata(os.path.join(Flat_path, flats[i]))
                    #sub_img=img[Cy-k:Cy+k+1, Cx-k:Cx+k+1, j]
                    #sub_Cx,sub_Cy=center(sub_img,20)[0],center(sub_img,20)[1]
                    #actual_Cx,actual_Cy = Cx-k+sub_Cx,Cy-k+sub_Cy
                    actual_Cx,actual_Cy = cent(imge, Cx, Cy, 20, 20)
                    if(np.isnan(actual_Cx)==True):
                        print('COM === TRUE ')
                        actual_Cx, actual_Cy = COM_iter(image, Cx, Cy,20,21)
                    #plt.scatter(actual_Cx, actual_Cy, c='red') 
                    #plt.show()  
                    Cx = actual_Cx
                    Cy = actual_Cy                    
                    #Cx = int(np.round(actual_Cx))
                    #Cy = int(np.round(actual_Cy))
                    #print(ax, by, Cx, Cy)
                    shiftX, shiftY = actual1_Cx-actual_Cx, actual1_Cy-actual_Cy
                    #print(shiftX, shiftY)
                    img[:,:,j]=ndimage.shift(imge, [shiftY, shiftX], output=None, order=3, mode='constant', cval=0.0, prefilter=False) # mode = 'nearest'
                    #x_all.append(Cx)
                    #y_all.append(Cy)
                    m=m+cycl_len
                header= getheader(os.path.join(imgpath, imgs[q-1][i]))
                Final = np.median(img, axis=2)
                SSimgs.append(Final)
                SSname.append(star+'_'+band[B]+'_'+str(i)+'.fits')
                F = os.path.join(final_path, star+'_'+band[B]+'_'+str(i)+'.fits')
                fits.writeto(F, Final, header)
            set_imgs.append(SSimgs)
            set_name.append(SSname)
        Simgs.append(set_imgs)
        Sname.append(set_name)
    #print(Sname)
    #print(len(Sname), len(Sname[0]), len(Sname[0][0]))
    return(Simgs)
               
#band = ['R'] #'i'   # choose the filter
#path = '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data'
#bias_path = '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data/Bias'
#Flat_path = '/home/ubu123/Desktop/PRL/EMPOL/empol_gui/EMPOL_V1/V1_Data/Flat' 
#Stack = single_stack(path, star, band, cycl_len )
#print(len(Stack), len(Stack[0]), len(Stack[0][0]))
#print(Stack.shape)
