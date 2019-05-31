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
current_working_dir = '../../../altered_version_v11'
#static_dir_nb = 2023 ### Soft static
#static_dir_nb1 = 2024 ### Hard static
#static_dir_nb2 = 2025 ### Soft momentum

#static_dir_nb = 2020 ### Soft static
#static_dir_nb1 = 2021 ### Hard static
#static_dir_nb2 = 2022 ### Soft momentum

static_dir_nb = 2030 ### Soft static
static_dir_nb1 = 2031 ### Hard static
static_dir_nb2 = 2032 ### Soft momentum

position_static = []
rms_stuff = []
static = []
sal_val = 5.25
#sal_val = 6.25
sal_val_str = "%0.2f" % sal_val

########################################################### PLOTTING LEGEND ARGUMENTS
for i in range(1) :
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-0-'+str(sal_val_str)+'/prop_out_'+str(i)+'_.25.dat'
#    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-0-'+str(sal_val_str)+'/temp_prop_out_'+str(i)+'.dat'
#    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-0-'+str(sal_val_str)+'/12_prop_out_'+str(i)+'.dat'
#    static_dir = current_working_dir + '/prop_out_0.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
    static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
    print("here")
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-0-'+str(sal_val_str)+'/position.dat'
    time,x,y,z,iso = import_position(static_dir)

    print("here 1 ")
    static_dir1 = current_working_dir + '/xxx'+str(static_dir_nb1)+'/xxx'+str(static_dir_nb1)+'-'+str(i)+'/xxx'+str(static_dir_nb1)+'-0-'+str(sal_val_str)+'/position.dat'
    time1,x1,y1,z1,iso1 = import_position(static_dir1)

    print("here 2")
#    sal_val=  5.00
    sal_val_str = "%0.2f" % sal_val
    static_dir2 = current_working_dir + '/xxx'+str(static_dir_nb2)+'/xxx'+str(static_dir_nb2)+'-'+str(i)+'/xxx'+str(static_dir_nb2)+'-0-'+str(sal_val_str)+'/position.dat'
    time2,x2,y2,z2,iso2 = import_position(static_dir2)
#plotting_position(time,x,y,z,iso,static)

animation_alt2(time,x,y,z,iso,static,time1,x1,y1,z1,iso1,time2,x2,y2,z2,iso2)
#testing()
