import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from tools.class_plotting import *
from tools.nuclei import *
from tools.import_methods import *

########################################################### COMMON VARIABLES
current_working_dir = '../../altered_version_v11'
static_dir_nb =  1598#7777 #3333 #333 #8888 #888 #8 #333 # 333
momentum_dir_nb = 1599 #8888 #7777 #7777 #334 #9999 #999 #9 # 334 # 334
nb_files = 1
#impact_parameter = "13.75"
########################################################### PLOTTING LEGEND ARGUMENTS
#para_list = np.arange(0.25,14.00,0.25)
#para_list = [20.00]
#print(para_list)
#for para in range(len(para_list)):
#  sal_val = 5.25
#  #sal_val = 5.00
#  sal_val_str = "%0.2f" % sal_val
#  impact_parameter = para_list[para]
#  impact_parameter = "%0.2f" % impact_parameter
#  print("Current impact paramter {0}".format(impact_parameter))
##  if(para == 0) : impact_parameter = ".25"
##  if(para == 1) : impact_parameter = ".50"
##  if(para == 2) : impact_parameter = ".75"
#  runs_static = run()
#  runs_momentum = run()
#  #for k in [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00] : 
#  for k in [sal_val]: 
#    sal_val  = k
##    sal_val_str = "%0.2f" % sal_val
##    print("SAL VALUE : {0}".format(k))
#    for i in range(nb_files) :
#        static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_0_'+impact_parameter+'.dat'
#  #      static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'_11.00.dat'
#    #    static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/temp_prop_out_'+str(i)+'.dat'
#        time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
#    
#        static = nuclei('static')
#        static.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p)
#    #    static.set_global_attributes('variable',10,0.6)
#        static.set_global_attributes("varaible",impact_parameter,40,0.6)
#        runs_static.runs.append(static)
#  
#  
#  nb_files = 1
#  sal_val = 5.00
#  sal_val_str = "%0.2f" % sal_val
#  
#  #for k in [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00] : 
#  for k in [sal_val] :
#    sal_val  = k
##    sal_val_str = "%0.2f" % sal_val
##    print("SAL VALUE : {0}".format(k))
#    for i in range(nb_files) :
#        momentum_dir = current_working_dir+'/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_0_'+impact_parameter+'.dat'
#  #      momentum_dir = current_working_dir+'/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/prop_out_'+str(i)+'_11.00.dat'
#    #    momentum_dir = current_working_dir+'/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'-'+str(sal_val_str)+'/12_prop_out_'+str(i)+'.dat'
#        time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)
#        momentum = nuclei('momentum')
#        momentum.attribution(time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p)
#        momentum.set_global_attributes("variable",impact_parameter,10,0.6)
#    #    momentum.set_global_attributes('variable',10,0.6)
#        runs_momentum.runs.append(momentum)
#  
#  values = [runs_static,runs_momentum]
#  energy_plot(values)
#  
#
#


#values = [runs_static]
#values = [runs_momentum]
#sal_plot_rms(values)
#sal_plot_rms_alt(values)
#sal_plot_density(values)
for k in range(3):
    r_table = []
    rho_table = []
    sal_table = []
    time = []

    for sal_val in [5.25,6.25]:
        print("SAL VALUE IN MAIN {0}".format(sal_val))
        if(k==0) : m_or_s = 'static soft'
        if(k==1) : m_or_s = 'static hard'
        if(k==2) : m_or_s = 'momentum'
        
        if(m_or_s =='static soft') : 
	  if(sal_val == 5.25) :fdir = '2020'
          if(sal_val == 6.25) :fdir = '2023'
          sal = str(sal_val)
          N = '5'
    
        if(m_or_s =='static hard') : 
          if(sal_val == 5.25) :fdir = '2021'
          if(sal_val == 6.25) :fdir = '2024'
          sal = str(sal_val)
          N = '5'
    
        if(m_or_s =='momentum') : 
          if(sal_val == 5.25) :fdir = '2022'
          if(sal_val == 6.25) :fdir = '2025'
          sal = str(sal_val)
	  if(sal_val == 5.25):  sal = '5.00'
          N = '5'
    #    print('len values {0}'.format(len(values)))
    #    r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/first.dat')
        r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/time_0.dat')
        r_table.append(r)
        sal_table.append(sal)
        rho_table.append(rho)
        time.append(0)
    #    plot_density(r,rho,0,m_or_s,N)
        
        r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/time_40.dat')
        r_table.append(r)
        rho_table.append(rho)
        sal_table.append(sal)
        time.append(40)
    #    plot_density(r,rho,40,m_or_s,N)
        
        r, rho = import_density_first(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-0/xxx'+fdir+'-0-'+sal+'/time_80.dat')
        r_table.append(r)
        rho_table.append(rho)
        sal_table.append(sal)
        time.append(80)
    #    plot_density(r,rho,80,m_or_s,N)
    plot_density_sub(r_table,rho_table,time,m_or_s,N,sal_table)




