import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
#Made modules import
from tools.import_methods import *
from tools.output_methods import *
############################################################KEY

#time = the timestep of the for of lenght the energy [0]
#tse = total system energy [1]
#tpe  = total potential energy [2]
#tke = total kinetic energy [3]
#tce = total coulomb energy [4]
#tme = total momentum energy [5]
#tae = total system asymetry energy [6]

########################################################### COMMON VARIABLES
current_working_dir = '../../altered_version_v11'
static_dir_nb = 100
position_static = []
rms_stuff = []
static = []
sal_val = 5.25
sal_val_str = "%0.2f" % sal_val

########################################################### PLOTTING LEGEND ARGUMENTS
for i in range(1) :
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-0-'+str(sal_val_str)+'/prop_out_'+str(i)+'.dat'
#    static_dir = current_working_dir + '/prop_out_0.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
    static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-0-'+str(sal_val_str)+'/position.dat'
#    static_dir = current_working_dir + '/position.dat'
    time,x,y,z,iso = import_position(static_dir)
#    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/rms.dat'
#    rmsp,rmst,xmt,ymt,zmt,xmp,ymp,zmp = import_rms(static_dir)
#    rms_stuff.append([rmsp,rmst,xmt,ymt,zmt,xmp,ymp,zmp])

#print(len(time))
#print(len(time[0]))
#print(len(x))
#print(len(y))
#print(len(z))
#print(len(iso))
#print(rms_stuff[0][2])


plotting_position(time,x,y,z,iso,static)
