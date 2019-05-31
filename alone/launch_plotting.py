import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from tools.class_plotting import *
from tools.nuclei import *
from tools.import_methods import *

########################################################### COMMON VARIABLES
current_working_dir = '../../altered_version_v11'
static_dir_nb =  1598 
momentum_dir_nb = 1599 
static_dir_hard_nb = 1600
nb_files = 7
store_static = []
store_static_hard = []
store_momentum = []
########################################################### PLOTTING LEGEND ARGUMENTS
sal_val = 5.25
sal_val_str = "%0.2f" % sal_val
impact_parameter = 20.00 
impact_parameter = "%0.2f" % impact_parameter
print("Current impact paramter {0}".format(impact_parameter))
runs_static = run()
runs_static_hard = run()
runs_momentum = run()
#for k in [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00] : 

for k in [sal_val]: 
   sal_val  = k
   sal_val_str = "%0.2f" % sal_val
   print("SAL VALUE : {0}".format(k))
   for i in range(nb_files) :
      static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'_'+impact_parameter+'.dat'
      time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
  
      static = nuclei('static')
      static.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p)
      static.set_global_attributes(0.2,impact_parameter,10,0.6)
      runs_static.runs.append(static)
      store_static.append(static)


nb_files = 7
sal_val = 5.25
sal_val_str = "%0.2f" % sal_val

for k in [sal_val] :
   sal_val  = k
   sal_val_str = "%0.2f" % sal_val
   print("SAL VALUE : {0}".format(k))
   for i in range(nb_files) :
      momentum_dir = current_working_dir+'/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'_'+impact_parameter+'.dat'
      time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)
      momentum = nuclei('momentum')
      momentum.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p)
      momentum.set_global_attributes(0.2,impact_parameter,10,0.6)
      runs_momentum.runs.append(momentum)
      store_momentum.append(momentum)

for k in [sal_val]: 
   sal_val  = k
   sal_val_str = "%0.2f" % sal_val
   print("SAL VALUE : {0}".format(k))
   for i in range(nb_files) :
      static_dir_hard = current_working_dir + '/xxx'+str(static_dir_hard_nb)+'/xxx'+str(static_dir_hard_nb)+'-'+str(i)+'/xxx'+str(static_dir_hard_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'_'+impact_parameter+'.dat'
      time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir_hard)
  
      static_hard = nuclei('static hard')
      static_hard.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p)
      static_hard.set_global_attributes(0.2,impact_parameter,10,0.6)
      runs_static_hard.runs.append(static_hard)
      store_static_hard.append(static_hard)

#values = [runs_static,runs_momentum]
print('store static len {0}'.format(len(store_static)))
print('store momentum len {0}'.format(len(store_momentum)))
values = [store_static,store_momentum]
#values = [store_static,store_momentum,store_static_hard]
individual_energy_plot(values)
