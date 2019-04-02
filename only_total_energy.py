import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
#Made modules import
from tools.function_with_time import *
from tools.graph_names import *
############################################################KEY

#time = the timestep of the for of lenght the energy [0]
#tse = total system energy [1]
#tpe  = total potential energy [2]
#tke = total kinetic energy [3]
#tce = total coulomb energy [4]
#tme = total momentum energy [5]
#tae = total system asymetry energy [6]

############################################################ 
current_working_dir = '../altered_version_v11'
number_of_files_to_import = 6
data = []
plot_info = []
plot_info = graph_settings(number_of_files_to_import*10)
graph_count = 1
#STATIC IMPORT
time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx3/prop_out_0.dat')
data.append([time,tse,tpe,tke,tce,tme,tae])
#MOMENTUM IMPORT
time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx4/prop_out_0.dat')
data.append([time,tse,tpe,tke,tce,tme,tae])

############################################################ PLOTS 
############################## FIGURE 2 
plt.figure(1)
for i in range(2):
  plt.subplot(2,3,1)
  plt.plot(data[i][0],data[i][1],label=plot_info[i][0][0],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
  plt.grid()
  plt.legend(loc='upper center', bbox_to_anchor=(1, 1.25),ncol=3, fancybox=True, shadow=True)
  plt.title("Variation of the TOTAL energy ")
  plt.xlabel('time step (fm)')
  plt.ylabel('energy (MeV)')
  
  plt.subplot(2,3,2)
  plt.plot(data[i][0],data[i][2],label=plot_info[i][0][1],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('energy (MeV)')
  plt.title("Variation of the POTENTIAL energy ")
  
  plt.subplot(2,3,3)
  plt.plot(data[i][0],data[i][3],label=plot_info[i][0][2],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('energy (MeV)')
  plt.title("Variation of the KINETIC energy ")
  
  plt.subplot(2,3,4)
  plt.plot(data[i][0],data[i][4],label=plot_info[i][0][3],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('energy (MeV)')
  plt.title("Variation of the COULOMB energy ")
  
  plt.subplot(2,3,5)
  plt.plot(data[i][0],data[i][5],label=plot_info[i][0][4],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('energy (MeV)')
  plt.title("Variation of the MOMENTUM energy ")
  
  plt.subplot(2,3,6)
  plt.plot(data[i][0],data[i][6],label=plot_info[i][0][5],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('energy (MeV)')
  plt.title("Variation of the ASYMMETRY energy ")


plt.show()
