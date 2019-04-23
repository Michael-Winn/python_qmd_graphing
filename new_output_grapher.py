import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
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
static_dir_nb = 1
momentum_dir_nb = 2
number_of_files_to_import =7
static = []
momentum = []

###########################################################
plot_info_static = []
plot_info_momentum = []
plot_info_density_static = []
plot_info_density_momentum = []
plot_info_rms_static = []
plot_info_rms_momentum = []
plot_info_old = []
plot_info_new = []

plot_info_static = graph_settings_static(number_of_files_to_import*number_of_files_to_import)
plot_info_momentum = graph_settings_momentum(number_of_files_to_import*number_of_files_to_import)
plot_info_density_static = graph_settings_density_static()
plot_info_density_momentum = graph_settings_density_momentum()
plot_info_rms_static = graph_settings_rms_static()
plot_info_rms_momentum = graph_settings_rms_momentum()

plot_info_old = graph_settings_momentum_comparing_old(number_of_files_to_import)
plot_info_new = graph_settings_momentum_comparing_new(number_of_files_to_import)

for i in range(number_of_files_to_import) :
#  if(i==1 or i==5 or i ==6 or i==7):
#    if(i==1):
#      static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/prop_out_'+str(i)+'.dat'
#      time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
#      static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
#STATIC IMPORT
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/prop_out_'+str(i)+'.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
    static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
#MOMENTUM IMPORT
    momentum_dir = current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/prop_out_'+str(i)+'.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)
    momentum.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])

plotting_function(static,plot_info_static,momentum,plot_info_momentum)
#upgraded_plotting_function(static,plot_info_static,momentum,plot_info_momentum)
#plotting_function_stat(static,plot_info_static)
#plotting_function_density(static,plot_info_density_static,momentum,plot_info_density_momentum)
#plotting_function_rms(static,plot_info_rms_static,momentum,plot_info_rms_momentum)

#plotting_momentum_contribution(static,plot_info_static,momentum,plot_info_old,plot_info_new)
