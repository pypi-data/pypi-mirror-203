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
def center(subimg, r):
    x = np.arange(0, subimg.shape[1],1)
    y = np.arange(0, subimg.shape[0], 1)
    xx, yy = np.meshgrid(x,y)
    x0 = r
    y0 = r
    s = max(*subimg.shape)*0.1
    A=np.max(subimg)
    initial_guess=[x0,y0,s,A]
    param, err = curve_fit(Gauss2D, (xx.ravel(), yy.ravel()), subimg.ravel(), p0=initial_guess, maxfev=10000)
    return(param)

#outfile='Teutsch1'

def stacking(path, bias_path, Flat_path, cluster, filter, cycl_len, outfile ) : # outfile = 'Kron1' # all the arguments must be in string format.
    imgpath = path+ '/'+cluster
    #print(imgpath)
    setpath = imgpath+'/frac_med_setcombine12_'+ filter
    if os.path.exists(setpath):
        shutil.rmtree(setpath)
    com = 'mkdir '+setpath
    os.system(com)
    #bias_path = path+'/Bias'
    #Flat_path = path+'/Flat/flat_comb'Czernik3_B_30s_s1_36
    img_list = os.listdir(imgpath)
    img_list = natsort.natsorted(img_list)
    #print(img_list)
    #print(imgpath)
    sets=[]
    for files in img_list:
        if fnmatch.fnmatch(files, '*_'+filter+'_*s_s*_1.fits'): #'Kron1_'+filter+'_*s_s*_1.fits'
            sets.append(files)
    #sets = ['s4', 's5', 's6']
    p = len(sets) # number of sets
    #print(sets)
    #print(p)
    #p=1
    
    #p = len(sets)
    imgs =[]
    for k in range(0,p):   # there is no set as s0, set number starts from 1 (like - s1), so k starts from 1 and loop itterate p times (when second term is p+1)
        #print("This is K: ", k)
        setlist = []
        for files in img_list:
            if fnmatch.fnmatch(files, '*_'+filter+'_*s_s'+str(k+1)+'*.fits'):
                setlist.append(files)
        imgs.append(setlist)
    #print(imgs)
    flat_list = os.listdir(Flat_path)
    flat_list = natsort.natsorted(flat_list)
    #flats=[]
    #for filess in flat_list:
    #    if fnmatch.fnmatch(filess, '*_'+filter+'_*'):
    #        flats.append(filess)
    #print(imgs[0][0], flats[0])
    flat = fits.getdata(os.path.join(Flat_path, filter+'mean.fits'))
    img0 = fits.getdata(os.path.join(imgpath,imgs[0][0]))
    img0 = img0.astype('>f8')
    IMGS = (img0[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/flat#/fits.getdata(os.path.join(Flat_path, flats[0]))
    mean1, med1, std1 = sigma_clipped_stats(IMGS)
    plt.imshow(IMGS,cmap='gray', vmin = med1-5*std1, vmax = med1+5*std1)
    plt.colorbar()
    plt.title('press x on the center of bright star'+imgs[0][0]+'set shift')
    cmd=plt.connect('key_press_event', press)
    plt.show()
    ap=int(np.round(X2))
    bp=int(np.round(Y2))
    sub_img1p=IMGS[bp-30:bp+31, ap-30:ap+31]
    plt.imshow(sub_img1p,cmap='gray', vmin = med1-5*std1, vmax = med1+5*std1)
    #plt.show()
    #sub1_Cxp,sub1_Cyp=center(sub_img1p, 30)[0],center(sub_img1p, 30)[1]
    #apx, bpy = ap-30+sub1_Cxp,bp-30+sub1_Cyp
    #apx, bpy = COM_iter(IMGS,X2,Y2,30,31)
    apx, bpy = cent(IMGS,X2,Y2,20,20)
    #print(apx, bpy)
    k = 15
    stacked_imgs = []
    for q in range(1,p+1):
        #print(imgs[q-1][0])
        data = fits.getdata(os.path.join(imgpath,imgs[q-1][0]))
        data = data.astype('>f8')
        img1 = (data[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/flat#/fits.getdata(os.path.join(Flat_path, flats[0]))
        mean, med, std = sigma_clipped_stats(img1)
        #plt.imshow(img1[0,:,:], cmap='gray',vmin = med-4*std, vmax = med+4*std)
        #cbar = plt.colorbar()
        #plt.xticks(fontsize = 12)
        #plt.yticks(fontsize = 12)
        #cbar.ax.tick_params(labelsize=12)
        #plt.show()
        plt.imshow(img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
        plt.colorbar()
        plt.title('click on center of bright star '+str(imgs[q-1][0]))
        cmd=plt.connect('button_release_event', single_click)
        plt.show()
        #k=20
        a=int(np.round(X1))
        b=int(np.round(Y1))
        #print(X1, Y1, a, b)
        #sub_img1=img1[b-30:b+31, a-30:a+31]
        #sub1_Cx,sub1_Cy=center(sub_img1, 30)[0],center(sub_img1, 30)[1]
        #actual1_Cx,actual1_Cy = a-30+sub1_Cx,b-30+sub1_Cy
        #ax = int(np.round(actual1_Cx))
        #by = int(np.round(actual1_Cy))
        #ax, by = COM_iter(img1,X1,Y1,30,31)
        ax, by = cent(img1,X1,Y1,20,20)
        #print(filter)
        final_path= imgpath+'/Final_frac_med12_'+filter+'_set_'+str(q)    # directory for media combine files
        if os.path.exists(final_path):
            shutil.rmtree(final_path)
        com = 'mkdir '+final_path
        os.system(com)
        n=int(len(imgs[q-1])/cycl_len) # 48 
        # define a, b here
        stacked = []
        for i in range(0,cycl_len):
            m=0
            Cx=ax  # initial centeral x-coordinate
            Cy=by   # initial Y-coordinate
            img = np.zeros((256, 256, n))
            for j in range(n):
                # print(imgs[q-1][i+m])#, flats[i])
                image = fits.getdata(os.path.join(imgpath, imgs[q-1][i+m]))
                image = image.astype('>f8')
                image = (image[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))#/flat#/fits.getdata(os.path.join(Flat_path, flats[i]))
                meann, medd, stdd = sigma_clipped_stats(image)
                #plt.imshow(image, cmap='gray', vmin = medd-5*stdd, vmax = medd+5*stdd)
                #sub_img=image[Cy-20:Cy+21, Cx-20:Cx+21]
                #sub_Cx,sub_Cy=center(sub_img,20)[0],center(sub_img,20)[1]
                #actual_Cx,actual_Cy = Cx-20+sub_Cx,Cy-20+sub_Cy
                actual_Cx, actual_Cy = cent(image, Cx, Cy, 10, 10)
                if(np.isnan(actual_Cx)==True):
                    print('COM === TRUE ')
                    actual_Cx, actual_Cy = COM_iter(image, Cx, Cy,10,11)
                    if(np.isnan(actual_Cx)==True):
                        print('previous value')
                        actual_Cx = Cx
                        actual_Cy = Cy
                #actual_Cx, actual_Cy = COM_iter(image,Cx,Cy,20,21)
                #plt.scatter(actual_Cx, actual_Cy, c='red') 
                #plt.show()  
                Cx = int(np.round(actual_Cx))
                Cy = int(np.round(actual_Cy))
                #Cx = actual_Cx
                #Cy = actual_Cy
                shiftX, shiftY = apx-actual_Cx, bpy-actual_Cy 
                #print(shiftX, shiftY)
                #print(shiftX, shiftY)
                img[:,:,j]=ndimage.shift(image, [shiftY, shiftX], order=3, mode='constant', cval=0.0, prefilter=False) # mode = 'nearest'
                m=m+cycl_len
            #plt.show()
            header= getheader(os.path.join(imgpath, imgs[q-1][i]))
            Final = np.median(img, axis=2)  
            #plt.imshow(Final, cmap='gray')
            #plt.show()                             # median combine
            stacked.append(Final)
            F = os.path.join(final_path, outfile+'_'+filter+str(i)+'.fits')#'Kron1_'+filter+str(i)+'.fits')
            fits.writeto(F, Final, header)
        stacked_imgs.append(stacked)
    N = len(stacked_imgs)
    stacked_name= []
    for s in range(cycl_len):
        imgarr = np.zeros((256,256,N))
        for t in range(N):
            imgarr[:,:,t]= stacked_imgs[t][s]
        cmb=np.median(imgarr,axis=2)
        F1 = os.path.join(setpath, outfile+'_set_combined_'+filter+'_'+str(s)+'.fits')
        stacked_name.append(outfile+'_set_combined_'+filter+'_'+str(s)+'.fits')
        fits.writeto(F1, cmb, header)	
    print("Center finding done")  
    return(stacked_name)

#path = '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Data/23_oct'
#bias_path = path+'/Bias'
#Flat_path = path+'/Flat'
#A = stacking(path,bias_path, Flat_path, 'Teutsch1', 'R', 12, outfile)
#print(len(A))
       

    

'''
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################

imgpath = '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Jan/EMPOL_Jan2021/EMPOL_Jan14/Kronberger1'
bias_path = '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Jan/EMPOL_Jan2021/EMPOL_Jan14/Bias'
Flat_path = '/home/namita/Documents/Open_clusters/Mt_ABU/2021_Jan/EMPOL_Jan2021/EMPOL_Jan14/Flat/flat_comb'
img_list = os.listdir(imgpath)
img_list = natsort.natsorted(img_list) # sorting numerically
#print(img_list)

filter = 'i'   # choose the filter 

sets=[]
for files in img_list:
    if fnmatch.fnmatch(files, 'Kron1_'+filter+'_*s_s*_1.fits'):
        sets.append(files)
p = len(sets) # number of sets
print(sets)
print(p)
#### seggregate images according to sets ######
imgs =[]
for k in range(1,p+1):   # there is no set as s0, set number starts from 1 (like - s1), so k starts from 1 and loop itterate p times (when second term is p+1)
    setlist = []
    for files in img_list:
        if fnmatch.fnmatch(files, 'Kron1_'+filter+'_*s_s'+str(k)+'*.fits'):
            setlist.append(files)
    imgs.append(setlist)
#print(imgs)
################### masterflats of choosen filter  ######################################
flat_list = os.listdir(Flat_path)
flat_list = natsort.natsorted(flat_list)
flats=[]
for files in flat_list:
    if fnmatch.fnmatch(files, '*_'+filter+'_*'):
        flats.append(files)
#print(flats)

# 1
'''
'''
# old
for files in img_list:
    if fnmatch.fnmatch(files, '*r_10s_s1*'):
        img_R_s1.append(files)
    elif fnmatch.fnmatch(files, '*r_10s_s2*'):
        img_R_s2.append(files)

flat_list = os.listdir(Flat_path)
flat_list = natsort.natsorted(flat_list)
flatR=[]
flatI=[]
flatG=[]
flatZ=[]

for files in flat_list:
    if fnmatch.fnmatch(files, '*r*'):
        flatR.append(files)
    elif fnmatch.fnmatch(files, '*i*'):
        flatI.append(files)
    elif fnmatch.fnmatch(files, '*g*'):
        flatG.append(files)
    elif fnmatch.fnmatch(files, '*z*'):
        flatZ.append(files)
# old
'''
'''
img0 = fits.getdata(os.path.join(imgpath,imgs[0][0]))
IMGS = (img0[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/fits.getdata(os.path.join(Flat_path, flats[0]))
mean1, med1, std1 = sigma_clipped_stats(IMGS)
plt.imshow(IMGS,cmap='gray', vmin = med1-5*std1, vmax = med1+5*std1)
plt.colorbar()
plt.title('press x on the center of bright star'+imgs[0][0]+'set shift')
cmd=plt.connect('key_press_event', press)
plt.show()
ap=int(np.round(X2))
bp=int(np.round(Y2))
sub_img1p=IMGS[bp-30:bp+31, ap-30:ap+31]
plt.imshow(sub_img1p,cmap='gray', vmin = med1-5*std1, vmax = med1+5*std1)
plt.show()
sub1_Cxp,sub1_Cyp=center(sub_img1p, 30)[0],center(sub_img1p, 30)[1]
apx, bpy = ap-30+sub1_Cxp,bp-30+sub1_Cyp
print(apx, bpy)
#a_1 = int(np.round(apx))
#b_1 = int(np.round(bpy))
k = 15
##################################################### for all the sets #####################################################################################
for q in range(1,p+1):
    print(imgs[q-1][0], flats[0])
    data = fits.getdata(os.path.join(imgpath,imgs[q-1][0]))
    img1 = (data[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/fits.getdata(os.path.join(Flat_path, flats[0]))
    mean, med, std = sigma_clipped_stats(img1)
    #plt.imshow(img1[0,:,:], cmap='gray',vmin = med-4*std, vmax = med+4*std)
    #cbar = plt.colorbar()
    #plt.xticks(fontsize = 12)
    #plt.yticks(fontsize = 12)
    #cbar.ax.tick_params(labelsize=12)
    #plt.show()
    plt.imshow(img1,cmap='gray', vmin = med-5*std, vmax = med+5*std)
    plt.colorbar()
    plt.title('click on center of bright star '+str(imgs[q-1][0]))
    cmd=plt.connect('button_release_event', single_click)
    plt.show()
    #k=20
    a=int(np.round(X1))
    b=int(np.round(Y1))
    print(X1, Y1, a, b)
    sub_img1=img1[b-30:b+31, a-30:a+31]
    sub1_Cx,sub1_Cy=center(sub_img1, 30)[0],center(sub_img1, 30)[1]
    actual1_Cx,actual1_Cy = a-30+sub1_Cx,b-30+sub1_Cy
    ax = int(np.round(actual1_Cx))
    by = int(np.round(actual1_Cy))
    print(filter)
    final_path=imgpath+'/Final_frac_med_'+filter+'_set_'+str(q)
    com = 'mkdir '+final_path
    os.system(com)
    n=int(len(imgs[q-1])/48) # 48 
# define a, b here
    for i in range(0,48):
        m=0
        Cx=ax  # initial centeral x-coordinate
        Cy=by   # initial Y-coordinate
        img = np.zeros((256, 256, n))
        for j in range(n):
            print(imgs[q-1][i+m], flats[i])
            image = fits.getdata(os.path.join(imgpath, imgs[q-1][i+m]))
            img[:,:,j] = (image[0,:,:]-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/fits.getdata(os.path.join(Flat_path, flats[i]))
            #plt.imshow(imgscl(img[:,:,j],1,1), cmap='gray')
            sub_img=img[Cy-k:Cy+k, Cx-k:Cx+k, j]
            sub_Cx,sub_Cy=center(sub_img,k)[0],center(sub_img,k)[1]
            actual_Cx,actual_Cy = Cx-k+sub_Cx,Cy-k+sub_Cy
            #plt.scatter(actual_Cx, actual_Cy, c='red') 
            #plt.show()  
            Cx = int(np.round(actual_Cx))
            Cy = int(np.round(actual_Cy))
            #print(a, b, Cx, Cy)
            shiftX, shiftY = apx-actual_Cx, bpy-actual_Cy 
            #shiftX, shiftY = apx-actual_Cx, bpy-actual_Cy   # changes done for combining all the sets.
            print(shiftX, shiftY)
            img[:,:,j]=ndimage.shift(img[:,:,j], [shiftY, shiftX], order=3, mode='constant', cval=0.0, prefilter=False) # mode = 'nearest'
            #x_all.append(Cx)
            #y_all.append(Cy)
            m=m+48
        header= getheader(os.path.join(imgpath, imgs[q-1][i]))
        Final = np.median(img, axis=2)
        F = os.path.join(final_path, 'Kron1_'+filter+str(i)+'.fits')
        fits.writeto(F, Final, header)
        #plt.imshow(imgscl(Final,1,1), cmap='gray')
        #plt.show()
'''
#################################################################################################################

'''
# old

img1 = (fits.getdata(os.path.join(imgpath,img_R_s1[0]))-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/fits.getdata(os.path.join(Flat_path, flatR[0]))

plt.imshow(imgscl(img1[0,:,:],1,1),cmap='gray')
plt.colorbar()
plt.title('click on center of bright star in Cz_img_0.fits')
cmd=plt.connect('button_release_event', single_click)
plt.show()
#h=15
k=15
a=int(np.round(X1))
b=int(np.round(Y1))
print(X1, Y1, a, b)
#sub_img1 = img[]
'''
#1
#######################################################################################################
# commented
'''
x = np.arange(0, sub_img.shape[1],1)
y = np.arange(0, sub_img.shape[0], 1)
xx, yy = np.meshgrid(x,y)
x0 = h
y0 = k
s = max(*sub_img.shape)*0.1
A=np.max(sub_img)
initial_guess=[x0,y0,s,A]
param, err = curve_fit(Gauss2D, (xx.ravel(), yy.ravel()), sub_img.ravel(), p0=initial_guess)
'''
# end
################################ To compare center with 2d gaussian fitting, maximum position or center of mass #######################################
'''
#commented
K = ndimage.maximum_position(sub_img)
S= ndimage.center_of_mass(sub_img)
plt.show()
act_coord_gaus = X1-h+param[0], Y1-k+param[1]
#print('coordinates from gauss 2D : ', act_coord_gaus)
act_coord_max = X1-h+K[1], Y1-k+K[0]
#print('coordinates from ndimage_max : ', act_coord_max)
act_coord_COM = X1-h+S[1], Y1-k+S[0]
#print('coordinates from ndimage_COM : ', act_coord_COM)
#plt.imshow(imgscl(img1[0,:,:],0.6,0.6), cmap='gray')
#plt.scatter(act_coord_gaus[0], act_coord_gaus[1], c='red')
#plt.scatter(act_coord_max[0], act_coord_max[1], c='green', marker='x')
#plt.scatter(act_coord_COM[0], act_coord_COM[1], c='blue', marker='*')
#plt.show()
'''
#end
################### To check whether the center shifts or not ###############################################################
# commented
'''
def irtter(img, a1,b1):
    c=1
    k=15
    while(c==1):   
        sub_img = img[0, int(np.round(b1))-k:int(np.round(b1))+k, int(np.round(a1))-k:int(np.round(a1))+k]
        C = center(sub_img)
        A_C = a1-k+C[0], b1-k+C[1]
        if(np.sqrt((a1-A_C[0])**2+(b1-A_C[1])**2) < 0.6):                      # always greater than 0.5
            c=0
        else:
            a1=A_C[0]
            b1=A_C[1]
    return(a1, b1)
'''
#end
# 2
'''
final_path=imgpath+'/stacked_s2'
com = 'mkdir '+final_path
os.system(com)
######################################################      single set   ####################################################
k=15 # half length of square box around (a,b)
n=int(len(img_R_s1)/48)
# define a, b here
for i in range(0,48):
    m=0
    Cx=a  # initial centeral x-coordinate
    Cy=b   # initial Y-coordinate
    img = np.zeros((256, 256, n))
    x_all = []
    y_all = []
    for j in range(n):
        img[:,:,j] = (fits.getdata(os.path.join(imgpath, img_R_s1[i+m]))-fits.getdata(os.path.join(bias_path, 'masterBias.fits')))/fits.getdata(os.path.join(Flat_path, flatR[i]))
        #plt.imshow(imgscl(img[:,:,j],1,1), cmap='gray')
        sub_img=img[Cy-k:Cy+k, Cx-k:Cx+k, j]
        sub_Cx,sub_Cy=center(sub_img)[0],center(sub_img)[1]
        actual_Cx,actual_Cy = Cx-k+sub_Cx,Cy-k+sub_Cy
        #plt.scatter(actual_Cx, actual_Cy, c='red') 
        #plt.show()  
        Cx = int(np.round(actual_Cx))
        Cy = int(np.round(actual_Cy))
        #print(a, b, Cx, Cy)
        shiftX, shiftY = a-Cx, b-Cy
        #print(shiftX, shiftY)
        img[:,:,j]=ndimage.shift(img[:,:,j], [shiftY, shiftX], order=3, mode='constant', cval=0.0, prefilter=False) # mode = 'nearest'
        #x_all.append(Cx)
        #y_all.append(Cy)
        m=m+48
    header= getheader(os.path.join(imgpath, img_R_s1[i]))
    Final = np.median(img, axis=2)
    F = os.path.join(final_path, 'CZ_r'+str(i)+'.fits')
    fits.writeto(F, Final, header)
    #plt.imshow(imgscl(Final,1,1), cmap='gray')
    #plt.show()
'''
#2






################################# accesssing all the function ########################################




