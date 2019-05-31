import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from tools.class_plotting import *
from tools.nuclei import *
from tools.import_methods import *

########################################################### COMMON VARIABLES
current_working_dir = '../../altered_version_v11'
for k in range(3):
    r_table = []
    rho_table = []
    rho_0 = []
    rho_40 = []
    rho_80 = []
    sal_table = []
    time = []

    for sal_val in [5.25,6.25]:
	print(sal_val)
#        print("SAL VALUE IN MAIN {0}".format(sal_val))
        if(k==0) : m_or_s = 'static soft'
        if(k==1) : m_or_s = 'static hard'
        if(k==2) : m_or_s = 'momentum'
	print(m_or_s) 
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
          N = '5'
	for l in range(20):
	  rho = import_density_alone(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-'+str(l)+'/xxx'+fdir+'-'+str(l)+'-'+sal+'/time_0.dat')
          rho_0.append(rho)
          
	  rho = import_density_alone(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-'+str(l)+'/xxx'+fdir+'-'+str(l)+'-'+sal+'/time_40.dat')
          rho_40.append(rho)
          
	  rho = import_density_alone(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-'+str(l)+'/xxx'+fdir+'-'+str(l)+'-'+sal+'/time_80.dat')
          rho_80.append(rho)
#	print("Size of a rho_0 : {0} sal value : {1}".format(len(rho_0),sal)) 
#	print(current_working_dir + '/xxx'+fdir+'/xxx'+fdir+'-'+str(l)+'/xxx'+fdir+'-'+str(l)+'-'+sal+'/time_0.dat')
#	print("SAL : {0}, fdir : {1} , m_or_s : {2}".format(sal_val,fdir,m_or_s))
    plot_density_histo(rho_0,rho_40,rho_80,m_or_s)
#    plot_density_histo(rho_table,m_or_s)




