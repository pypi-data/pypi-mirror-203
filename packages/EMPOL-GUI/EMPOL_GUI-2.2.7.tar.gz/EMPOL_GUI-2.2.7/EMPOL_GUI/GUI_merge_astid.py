################################################################################################################################################################################################################
######################### GUI for a Single-lined optical design with revised (based on manufacturer's responses on materials' availability) materials #############################################################
################################################################################################################################################################################################################
##################################################################################### Prachi Prajapati, March 10, 2022 ########################################################################################
################################################################################################################################################################################################################
import numpy as np
import numpy as geek
import scipy as scp
from scipy.constants import c,h,k
from scipy.integrate import quad
import matplotlib
matplotlib.use('TkAgg')
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from numpy import genfromtxt
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import os
import natsort

import tkinter 
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
window = Tk()
from tkinter import filedialog

#v2
from empol_center_finding import stacking
from empol_astrometry import do_astrometry
from extcatalog import extcat
from recenter import recenter_fun
from empol_photometry import photo
from empol_pol import polarization

#v1
from Bias import biascombine
from Flat import flatCombine
from single_obj_stack import single_stack
from single_phot import photometry
from empol_pol_single_obj import single_pol



#TITLE OF THE GUI WINDOW
window.title("EMPOL Data Reduction GUI")
window.geometry("750x600+10+20")

#welcome
def welcome():
	wel = messagebox.showinfo("Hey!","Welcome to the EMPOL's Data Reduction GUI!")    		

wel = Button(window, text = "Welcome!", bg="blue", fg="white", command = welcome)
wel.pack()
wel.place(x=225, y=5)

# Create text widget and specify size.
T = tkinter.Text(window, height = 5, width = 52)

#LABEL WIDGET
label_widget = tkinter.Label(window, text="User inputs", fg='green', font=("Helvetica", 16))
label_widget.pack() 
label_widget.place(x=213.5,y=40)

#Fact = """A man can be arrested in Italy for wearing a skirt in public."""

#BUTTON STYLES FOR THE GUI WINDOW
styleb = ttk.Style()

styleb.configure('W.TButton', font =
               ('calibri', 14, 'bold'),	#, 'underline'),
                foreground = 'blue')



#VARIOUS WIDGETS' PACKS ARE USED TO SHOW THE OBJECT IN THE GUI WINDOW

var_star = tkinter.StringVar()
var_path = tkinter.StringVar()
#band = tkinter.StringVar()
var_cycl_len= tkinter.IntVar()
var_RA=tkinter.DoubleVar()
var_dec=tkinter.DoubleVar()
var_magnitude_cut=tkinter.DoubleVar()
var_aperture_value=tkinter.DoubleVar()
#path_var = tkinter.StringVar()


###########
# Select Band Type 
###########  

var = StringVar()
def sel():
   selection = messagebox.showinfo("Band Type","You selected the option " + str(var.get()))
  # label.config(text = selection)

 
R1 = Radiobutton(window, text="U", variable=var, value="U",
                  command=sel)
R1.pack()#( anchor = W )

R2 = Radiobutton(window, text="B", variable=var, value="B",
                  command=sel)
R2.pack()#( anchor = W )

R3 = Radiobutton(window, text="V", variable=var, value="V",
                  command=sel)
R3.pack()#( anchor = W )

R4 = Radiobutton(window, text="R", variable=var, value="R",
                  command=sel)
R4.pack()#( anchor = W )

R5 = Radiobutton(window, text="I", variable=var, value="I",
                  command=sel)
R5.pack()#( anchor = W )

R6 = Radiobutton(window, text="u", variable=var, value="u",
                  command=sel)
R6.pack()#( anchor = W )

R7 = Radiobutton(window, text="g", variable=var, value="g",
                  command=sel)
R7.pack()#( anchor = W )

R8 = Radiobutton(window, text="r", variable=var, value="r",
                  command=sel)
R8.pack()#( anchor = W )

R9 = Radiobutton(window, text="i", variable=var, value="i",
                  command=sel)
R9.pack()#( anchor = W )

R10 = Radiobutton(window, text="z", variable=var, value="z",
                  command=sel)
R10.pack()#( anchor = W )

#label = Label(window)
#label.pack()



def astrometry():
   selection = messagebox.showinfo("Astrometry","You selected " + str(yesno_astrometry.get()))

def browseFiles():
   filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select file for astrometry",
										filetypes = (("Fits files","*.fits*"),("all files","*.*")))
   new_filename = os.rename(filename,"ed"+000)
   disp2 = messagebox.showinfo("Alert!", "You selected " + str(filename))

yesno_astrometry=StringVar()
Yes_astrometry=Radiobutton(window, text="Upload File", variable=yesno_astrometry,value="Upload File", command=browseFiles)
No_astrometry=Radiobutton(window, text="Default", variable=yesno_astrometry,value="Default", command=astrometry)

def object_selected_star():
    close_cluster.place_forget()
    dwnld_btn_cluster.place_forget()
    RA_entry.place_forget()
    RA_label.place_forget()
    RA_entry.place_forget()
    dec_label.place_forget()
    dec_entry.place_forget()
    Yes_astrometry.place_forget()
    No_astrometry.place_forget()
    globalsel.place_forget()
    local.place_forget()
    astrometry_label.place_forget()
    global_local_label.place_forget()


    dwnld_btn_star.pack()
    dwnld_btn_star.place(x=250, y=325)

    close_star.pack()
    close_star.place(x=275, y=375)
    

def object_selected_cluster():
    dwnld_btn_star.place_forget()
    close_star.place_forget()
    RA_label.pack()
    RA_entry.pack()
    dec_label.pack()
    dec_entry.pack()
    Yes_astrometry.pack()
    No_astrometry.pack()
    globalsel.pack()
    local.pack()
    astrometry_label.pack()
    global_local_label.pack()


    RA_label.place(x=100, y=325)
    RA_entry.place(x=300, y =325)
    dec_label.place(x=100, y=350)
    dec_entry.place(x=300, y=350)
    astrometry_label.place(x=100, y=375)
    Yes_astrometry.place(x=285, y=375)
    No_astrometry.place(x=360, y=375)
    global_local_label.place(x=100, y=400)
    globalsel.place(x=285, y=400)
    local.place(x=360, y=400)

    dwnld_btn_cluster.pack()
    dwnld_btn_cluster.place(x=250, y=425)
    
    close_cluster.pack()
    close_cluster.place(x=275, y=475)

object_type=StringVar()
type_star=Button(window, text = "Single Star", command = object_selected_star)
type_star.pack()
type_cluster=Button(window,text = "Cluster", command = object_selected_cluster)



def global_local():
    selection = messagebox.showinfo("Global or Local","You selected " + str(global_local_var.get()))

global_local_var=StringVar()
globalsel=Radiobutton(window, text="Global", variable=global_local_var, value="Global", command= global_local)
local=Radiobutton(window, text="Local", variable=global_local_var, value="Local", command = global_local)



code_path= '/home/ubuntu/Desktop/Merged_Code'


star_label = ttk.Label(window, text = 'Object', font=('calibre',10, 'bold'))
star_entry = ttk.Entry(window,textvariable = var_star, font=('calibre',10,'normal'))

path_label = ttk.Label(window, text = 'Object Path', font=('calibre',10, 'bold'))
path_entry = ttk.Entry(window,textvariable = var_path, font=('calibre',10,'normal'), width=50)
#path_entry.insert(0,"/home/ubu123/Desktop/PRL/EMPOL/EMPOL_DATA")

cycl_len_label = ttk.Label(window, text = 'Cycle Length', font=('calibre',10, 'bold'))
cycl_len_entry = ttk.Entry(window,textvariable = var_cycl_len, font=('calibre',10,'normal'))

band_label = ttk.Label(window, text = 'Select Band', font=('calibre',10, 'bold')) #label for band
objecttype_label = ttk.Label(window, text = "Object Type",font=('calibre', 10, 'bold')) #label for object type
astrometry_label=ttk.Label(window, text='Astrometry', font=('calibre',10, 'bold')) #label for astrometry - yes/no
recenter_label=ttk.Label(window, text="Recenter", font=('calibre',10, 'bold')) #label for recenter - yes/no
global_local_label=ttk.Label(window, text="Select Global or Local", font=('calibre',10, 'bold')) #label for global or local


RA_label = ttk.Label(window, text = 'RA', font=('calibre',10, 'bold'))
RA_entry = ttk.Entry(window,textvariable = var_RA, font=('calibre',10,'normal'))

dec_label = ttk.Label(window, text = 'DEC', font=('calibre',10, 'bold'))
dec_entry = ttk.Entry(window,textvariable = var_dec, font=('calibre',10,'normal'))

magnitude_cut_label = ttk.Label(window, text = 'Magnitude Cut', font=('calibre',10, 'bold'))
magnitude_cut_entry = ttk.Entry(window,textvariable = var_magnitude_cut, font=('calibre',10,'normal'))

aperture_value_label = ttk.Label(window, text = 'Aperture Value', font=('calibre',10, 'bold'))
aperture_value_entry = ttk.Entry(window,textvariable = var_aperture_value, font=('calibre',10,'normal'))



def download_star():
  #bias_path = str(path.get()) + '/Bias'
  #Flat_path = StringVar.get(path) + '/Flat'
    gain = 20
    path = var_path.get()
    cycl_len=  var_cycl_len.get()
    star = var_star.get()
    filter=var.get()
    band = [filter]
    #bias and flat function
    biascombine(path)
    flatCombine(path, filter, cycl_len)
    dis1 = messagebox.showinfo("Alert", "Masterbias.fits and Rmean.fits files created successfully. ")
    disp = messagebox.showinfo("Alert", "The process may take some time, sit and relax!")

    Stack = single_stack(path, star, band, cycl_len)

    disp3 = messagebox.showinfo("Alert","Stacking Done!")

    photometry(code_path, path, star,  band, cycl_len, Stack, gain)

    disp4 = messagebox.showinfo("Alert","Photometry Done!")

    single_pol(code_path, path, star, band, cycl_len)
    disp5 = messagebox.showinfo("Alert","Polarization Done. Polarization curve saved.")
    res = messagebox.showinfo("Alert","The files have been saved to the downloads folder in " + path + "/downloads")
		
def download_cluster():
    path = var_path.get()
    cycl_len=  var_cycl_len.get()
    star = var_star.get()
    cluster=star
    outfile = star
    name = star
    cluster_name = star
    fband=var.get()
    ra = var_RA.get()
    dec = var_dec.get()
    filter=fband
    band = [fband]
    bias_path= path+'/Bias'
    Flat_path = path+'/Flat'
   #recenter = yesno_recentre.get()

   #dis_load = messagebox.showinfo("Loading", )

   
   #bias and flat function
    biascombine(path)
    flatCombine(path, filter, cycl_len)
    dis1 = messagebox.showinfo("Alert", "Masterbias.fits and Rmean.fits files created successfully. ")
   
    disp = messagebox.showinfo("Alert", "The process may take some time, sit and relax!")


   #center finding
    stacking(path, bias_path, Flat_path, cluster, filter, cycl_len, outfile)
    dis2 = messagebox.showinfo("Alert","Center Finding Done.")
    
   #astrometry
    result1=[]
    if yesno_astrometry.get()=="Default":
        imgpath = path+'/'+cluster+'/frac_med_setcombine12_'+filter
        imglist = os.listdir(imgpath)
        imglist = natsort.natsorted(imglist)
        result1 = do_astrometry(code_path, path,cluster,filter, name, imglist, ra, dec)
        dis3 = messagebox.showinfo("Alert", "Ast ID = " + str(result1[1]) + "\n" + "Error = " + str(result1[0]))
        ast_id = result1[1]
    elif yesno_astrometry.get()=="Upload File":
        ast_id = 000
        display3 = messagebox.showinfo("Alert", "Ast ID = " + str(result1[1]))
   
   #ext_cat - detecting stars
    option="no"
   #ast_id = '201'
    while(option.lower() == "no"):
        lm = askstring('Limiting Magnitude', 'Enter Limiting Magnitude: ')
        showinfo('Limiting Magnitude', 'Limiting Magnitude is {}'.format(lm))
        extcat(path, filter, cluster, cluster_name, ast_id, 'I/345/gaia2', 'Gmag', lm, name, 'RA_ICRS', 'DE_ICRS')
        option=askstring('Stars Detected', 'Are all stars detected?? ')
    dis4 = messagebox.showinfo("Alert", "Stars Detected")
   

   
   #Recenter
    recenter = askstring('Recenter', 'Do you want to Recenter? (Yes/No)')
    if recenter.lower()!="yes" and recenter.lower()!="no":
        recenter = askstring("Incorrect Input","Please Enter Yes/No. Do you want to Recenter?")
    if recenter.lower() =="yes":
        recenter_fun(path, cluster, name, filter, ast_id)
    if recenter.lower()=="no":
        os.rename(path +"/"+ cluster + "/frac_med_setcombine"+ str(cycl_len) + "_" + filter + "/ed" + ast_id + "_" + star + "_" + filter + "_Gaia.txt", path +"/"+ cluster + "/frac_med_setcombine"+ str(cycl_len) + "_" + filter + "/ed" + ast_id + "_" + star + "_" + filter + "_recenter.txt")
       
    dis5 = messagebox.showinfo("Alert","Recenter Done")

   #ast_id = '201'
    gain = 20
   #Photometry
    photo(code_path, path, cluster, filter, ast_id, name, cycl_len, gain)
    dis6= messagebox.showinfo("Alert", "Photometry Done")

   
   #Polarisation
    polarization(path,cluster, ast_id, filter, name, cycl_len)
    dis7= messagebox.showinfo("Alert", "Polarisation Done")
    #disp10 = messagebox.showinfo("Result", "No. of stars = ")
    res = messagebox.showinfo("Alert", "The files have been saved to the following path: "+ path)

dwnld_btn_star = Button(window,text = 'Download Files', fg="yellow", bg="green", command= download_star)
dwnld_btn_cluster = Button(window,text = 'Download Files', fg="yellow", bg="green", command= download_cluster)




#close
def close_window():
    exit()
        
close_star = Button(window, text = "Close", bg="blue", fg="white", command = close_window)
close_cluster = Button(window, text = "Close", bg="blue", fg="white", command = close_window)


star_label.pack()
star_label.place(x=100, y=75)

star_entry.pack()
star_entry.place(x=300, y=75)


path_label.pack()
path_label.place(x=100, y=100)

path_entry.pack()
path_entry.place(x=300, y=100)


cycl_len_label.pack()
cycl_len_label.place(x=100, y=125)

cycl_len_entry.pack()
cycl_len_entry.place(x=300, y=125)

band_label.pack()
band_label.place(x=100, y=150)
R1.place(x=285, y=150)
R2.place(x=285, y=175)
R3.place(x=285, y=200)
R4.place(x=285, y=225)
R5.place(x=285, y=250)
R6.place(x=350, y=150)
R7.place(x=350, y=175)
R8.place(x=350, y=200)
R9.place(x=350, y=225)
R10.place(x=350, y=250)
#var.get()

objecttype_label.pack()
objecttype_label.place(x=100, y=275)
type_star.place(x=285, y = 275)
type_cluster.place(x =400, y = 275)












#FOR A COMBO BOX WITH MULTIPLE OPTIONS - ONE/MULTIPLE TO BE SELECTED AMONG THESE OPTIONS
#var = StringVar()
#var.set("one")

'''
filter_label = ttk.Label(window, text = 'Filter', font=('calibre',10, 'bold'))
filter_var = ("Y", "J", "H", "Ks/K")
filters = Combobox(window, values=filter_var)
'''

#filter_entry = ttk.Entry(window,textvariable = filter_var, font=('calibre',10,'normal'))

'''
filter_label.place(x=55,y=300)
filters.place(x=100,y=300)	
'''	

window.mainloop()	


###
"""
aperture_value_label.pack()
aperture_value_label.place(x=100, y=400)
aperture_value_entry.pack()
aperture_value_entry.place(x=300, y=400)
"""

"""
magnitude_cut_label.pack()
magnitude_cut_label.place(x=100, y=325)

magnitude_cut_entry.pack()
magnitude_cut_entry.place(x=300, y=325)
"""

"""
recenter_label.pack()
recenter_label.place(x=100,y=350)
Yes_recentre.place(x=285, y=350)
No_recentre.place(x=350, y=350)
"""