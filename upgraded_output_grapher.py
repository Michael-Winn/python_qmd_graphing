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
############# STATIC [0]  OR MOMENTUM [1] OF BOTH [2]
wtp = 2
########################################################### PLOTTING LEGEND ARGUMENTS
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
###########################################################  IMPORTS
if(wtp==0) : print('WTP = {0}, so only static values will be plotted'.format(wtp))
if(wtp==1) : print('WTP = {0}, so only momentum values will be plotted'.format(wtp))
if(wtp==2) : print('WTP = {0}, momentum and static values will be plotted'.format(wtp))
for i in range(number_of_files_to_import) :
#STATIC IMPORT
    if(wtp ==0 or wtp ==2) :
        if(i==0) : print('STATIC import files they number : {0}'.format(number_of_files_to_import))
	static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/prop_out_'+str(i)+'.dat'
    	time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
    	static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
#MOMENTUM IMPORT
for i in range(number_of_files_to_import) :
    if(wtp ==1 or wtp ==2) :
        if(i==0) : print('MOMENTUM import files they number : {0}'.format(number_of_files_to_import))
	momentum_dir = current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/prop_out_'+str(i)+'.dat'
    	time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)
    	momentum.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])

#######################################################################
####################################################################### CALL THE PLOTTING ROUTINES
upgraded_plotting_function(static,plot_info_static,momentum,plot_info_momentum,wtp)
upgraded_plotting_function_density(static,plot_info_density_static,momentum,plot_info_density_momentum,wtp)
#plotting_function_rms(static,plot_info_rms_static,momentum,plot_info_rms_momentum)

#plotting_momentum_contribution(static,plot_info_static,momentum,plot_info_old,plot_info_new)
