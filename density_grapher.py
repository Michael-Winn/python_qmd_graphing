import numpy as np
#import pylab as pl
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
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
static_dir_nb = 6
momentum_dir_nb = 7
number_of_files_to_import =1
number_of_sal = 11
static = []
momentum = []
values_t_0 = []
values_t_30 = []
############# STATIC [0]  OR MOMENTUM [1] OF BOTH [2]
wtp =1
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
  for k in range(50,71):
     j = float(k)/10.
#STATIC IMPORT
     if(wtp ==0 or wtp ==2) :
         if(k==50) : print('STATIC import files they number : {0}'.format(number_of_files_to_import))
         static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(j)+'/prop_out_'+str(i)+'.dat'
         time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
     	 static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
#MOMENTUM IMPORT
#for i in range(number_of_files_to_import) :
#  for k in range(53,70):
#    j = float(k)/10.
#    if(wtp ==1 or wtp ==2) :
#        if(k==50) : print('MOMENTUM import files they number : {0}'.format(number_of_files_to_import))
##	momentum_dir = current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(j)+'/prop_out_'+str(i)+'.dat'
##    	time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)
##    	momentum.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
#	r,rho_t,rho_p = import_rho_r(current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(j)+'/time_02.dat')
#	values_t_0.append([r,rho_t,rho_p])
#	r,rho_t,rho_p = import_rho_r(current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(j)+'/time_30.dat')
#	values_t_30.append([r,rho_t,rho_p])
#######################################################################
####################################################################### CALL THE PLOTTING ROUTINES
#upgraded_plotting_function(static,plot_info_static,momentum,plot_info_momentum,wtp)
#upgraded_plotting_function_density(static,plot_info_density_static,momentum,plot_info_density_momentum,wtp)
#plotting_function_rms(static,plot_info_rms_static,momentum,plot_info_rms_momentum)

#plotting_momentum_contribution(static,plot_info_static,momentum,plot_info_old,plot_info_new)


#plotting_density_function(static,momentum)

r,count_t,count_p,rho_t,rho_p = import_rho_r(current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(0)+'/xxx'+str(momentum_dir_nb)+'-'+str(0)+'-5.0/time_00.dat')
values_t_0.append([r,count_t,count_p,rho_t,rho_p])
print(values_t_0[0][1])
#plotting_density_r(values_t_0)


r,count_t,count_p,rho_t,rho_p = import_rho_r(current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(0)+'/xxx'+str(momentum_dir_nb)+'-'+str(0)+'-5.0/time_30.dat')
values_t_30.append([r,count_t,count_p,rho_t,rho_p])
print(values_t_30[0][1])
#plotting_density_r(values_t_30)
plotting_density_r(values_t_0,values_t_30)





