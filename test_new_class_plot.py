import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from tools.class_plotting import *
from tools.nuclei import *
from tools.import_methods import *

########################################################### COMMON VARIABLES
current_working_dir = '../altered_version_v11'
static_dir_nb = 1
momentum_dir_nb = 2
sal_val = 5.25
sal_val_str = "%0.2f" % sal_val

########################################################### PLOTTING LEGEND ARGUMENTS
for i in range(1) :
    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-0-'+str(sal_val_str)+'/prop_out_'+str(i)+'.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)

static = nuclei('static')
static.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p)
static.set_global_attributes(0.2,5,0.6)


sal_val = 5.25
sal_val_str = "%0.2f" % sal_val

for i in range(1) :
    momentum_dir = current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-0-'+str(sal_val_str)+'/prop_out_'+str(i)+'.dat'
    time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)

momentum = nuclei('momentum')
momentum.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p)
momentum.set_global_attributes(0.2,5,0.6)

values = [static,momentum]
energy_plot(values)
density_plot(values)





