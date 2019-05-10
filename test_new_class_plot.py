import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from tools.class_plotting import *
from tools.nuclei import *
from tools.import_methods import *

########################################################### COMMON VARIABLES
current_working_dir = '../altered_version_v11'
static_dir_nb = 100
momentum_dir_nb = 200
sal_val = 5.25
sal_val_str = "%0.2f" % sal_val
nb_files = 2

########################################################### PLOTTING LEGEND ARGUMENTS
runs_static = run()
runs_momentum = run()
for i in range(nb_files) :
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)

    static = nuclei('static')
    static.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p)
#    static.set_global_attributes('variable',10,0.6)
    static.set_global_attributes(0.2,5,0.6)
    runs_static.runs.append(static)


sal_val = 5.25
sal_val_str = "%0.2f" % sal_val

for i in range(nb_files) :
    momentum_dir = current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)

    momentum = nuclei('momentum')
    momentum.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p)
    momentum.set_global_attributes(0.2,5,0.6)
#    momentum.set_global_attributes('variable',10,0.6)
    runs_momentum.runs.append(momentum)

values = [runs_static,runs_momentum]
energy_plot(values)
#density_plot(values)





