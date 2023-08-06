import numpy as np
import numpy.ma as ma
import os
import astropy.units as u
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from astropy.stats import sigma_clipped_stats, sigma_clip
import subprocess
from astroquery.vizier import Vizier
from astropy.io import fits
import matplotlib.pyplot as plt
#%matplotlib inline
import os

def extcat(path, filter, cluster, cluster_name, ID, vizier_cat, column, lm_mag, name, ra_cl, dec_cl): # ra_cl = 'RA_ICRS'/'RAJ2000', dec_cl = 'DE_ICRS'/'DEJ2000'
    Folder= path+'/'+cluster+'/frac_med_setcombine12_'+filter
    print(Folder)
    f = fits.open(os.path.join(Folder, 'ed'+str(ID)+'_'+name+'_set_combined_'+filter+'_0w.fits'))
    print('ed'+str(ID)+'_'+name+'_set_combined_'+filter+'_0.fits')
    data = f[0].data  #This is the image array
    header = f[0].header
    Vizier.ROW_LIMIT = -1
    result = Vizier.query_region(SkyCoord.from_name(cluster_name),
                                 radius=5*u.arcmin,
                                 catalog=vizier_cat, column_filters={column:"< "+lm_mag}) 
    w = WCS(header)
    x, y = w.all_world2pix(result[0][ra_cl], result[0][dec_cl], 1)
    
    ra = np.array(result[0][ra_cl])
    dec = np.array(result[0][dec_cl])
    X=[]
    Y=[]
    RA = []
    DEC = []
    for i in range(len(x)):
        if(x[i] < 15): continue
        if(y[i] < 15): continue
        if(x[i] > 256-15): continue
        if(y[i] > 256-15): continue
        if(x[i]+y[i]< 20): continue
        if(x[i] + (256-y[i])) < 20: continue
        if((256-x[i])+y[i]) < 20: continue
        if((256-x[i]) + (256-y[i]) < 20): continue
        X.append(x[i])
        Y.append(y[i])
        RA.append(ra[i])
        DEC.append(dec[i])
    X = np.array(X)
    Y = np.array(Y)
    print(X,Y)
    source = np.loadtxt(os.path.join(Folder,'ed101_source_ext_'+name+'_'+filter+'_0.txt'), comments='#')
    source[:,0] = source[:,0]-1
    source[:,1] = source[:,1]-1

    mean, median, sigma = sigma_clipped_stats(data)
    plt.imshow(data, vmin=median-3*sigma, vmax=median+3*sigma, cmap='gray')
    plt.plot(X-1,Y-1, 'bx', markersize = 10)
    #plt.scatter(source[:,0], source[:,1], color= 'red', marker='o')
    plt.show()
    np.savetxt(os.path.join(Folder,'ed'+str(ID)+'_'+name+'_'+filter+'_Gaia.txt'), np.c_[X,Y, RA, DEC], header='x      y     ra     dec')
    return(X,Y)

#path= '/home/ubu123/Desktop/PRL/EMPOL/EMPOL_GUI/EMPOL_V2/V2_Data/23_oct'
#lm = input("enter limiting magnitude : ")
#command='no'
#while(command=='no'):
#    lm = input("enter limiting magnitude : ")
#    img_coo = extcat(path, 'R', 'Teutsch1','Teutsch1', '201', 'I/345/gaia2', "Gmag", lm , 'Teutsch1', 'RA_ICRS', 'DE_ICRS')
#    command = input('Are all the stars detected? ')



