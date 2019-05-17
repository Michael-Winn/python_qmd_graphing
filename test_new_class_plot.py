import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from tools.class_plotting import *
from tools.nuclei import *
from tools.import_methods import *

########################################################### COMMON VARIABLES
current_working_dir = '../altered_version_v11'
static_dir_nb =  888 #8 #333 # 333
momentum_dir_nb = 999 #9 # 334 # 334
sal_val = 5.25
sal_val_str = "%0.2f" % sal_val
nb_files = 1

########################################################### PLOTTING LEGEND ARGUMENTS
runs_static = run()
runs_momentum = run()
for k in [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00] : 
  sal_val  = k
  sal_val_str = "%0.2f" % sal_val
  print("SAL VALUE : {0}".format(k))
  for i in range(nb_files) :
      static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'.dat'
  #    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/temp_prop_out_'+str(i)+'.dat'
      time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
  
      static = nuclei('static')
      static.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p)
  #    static.set_global_attributes('variable',10,0.6)
      static.set_global_attributes(0.2,2,0.6)
      runs_static.runs.append(static)


sal_val = 5.00
sal_val_str = "%0.2f" % sal_val

for k in [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00] : 
  sal_val  = k
  sal_val_str = "%0.2f" % sal_val
  print("SAL VALUE : {0}".format(k))
  for i in range(nb_files) :
      momentum_dir = current_working_dir+'/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'.dat'
  #    momentum_dir = current_working_dir+'/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/12_prop_out_'+str(i)+'.dat'
      time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)
      momentum = nuclei('momentum')
      momentum.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p)
      momentum.set_global_attributes(0.2,2,0.6)
  #    momentum.set_global_attributes('variable',10,0.6)
      runs_momentum.runs.append(momentum)

values = [runs_static,runs_momentum]
#energy_plot(values)
#values = [runs_static]
#values = [runs_momentum]
sal_plot_rms(values)
sal_plot_rms_alt(values)
sal_plot_density(values)
#for k in range(2):
#    if(k==0) : m_or_s = 'static'
#    if(k==1) : m_or_s = 'momentum'
#    
#    if(m_or_s =='static') : 
#      fdir = '335'
#      sal = '5.25'
#      N = '50'
#    if(m_or_s =='momentum') : 
#      fdir = '336'
#      sal = '5.00'
#      N = '20'
#    print('len values {0}'.format(len(values)))
##    r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/first.dat')
#    r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/first_less.dat')
#    plot_density(r,rho,0,m_or_s,N)
#    
#    r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/second.dat')
#    plot_density(r,rho,2,m_or_s,N)
#    
#    r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/thirty.dat')
#    plot_density(r,rho,30,m_or_s,N)
#density_plot(values)





