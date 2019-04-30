import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#Made modules import
from tools.function_with_time import *
from tools.graph_names import *
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
current_working_dir = '../altered_version_v11'
static_dir_nb = 3
position_static = []
rms_stuff = []
static = []
########################################################### PLOTTING LEGEND ARGUMENTS
for i in range(1) :
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/prop_out_'+str(i)+'.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
    static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/position.dat'
    time,x,y,z,iso = import_position(static_dir)
#    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/rms.dat'
#    rmsp,rmst,xmt,ymt,zmt,xmp,ymp,zmp = import_rms(static_dir)
#    rms_stuff.append([rmsp,rmst,xmt,ymt,zmt,xmp,ymp,zmp])

print(len(time))
print(len(x))
print(len(y))
print(len(z))
print(len(iso))
#print(rms_stuff[0][2])


plotting_position(time,x,y,z,iso,static)
