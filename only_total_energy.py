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
number_of_files_to_import = 4
handles = []
data = []
plot_info = []
plot_info = graph_settings(number_of_files_to_import*10)
graph_count = 1
#STATIC IMPORT
time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx1/prop_out_2.dat')
data.append([time,tse,tpe,tke,tce,tme,tae])
#MOMENTUM IMPORT
time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx2/prop_out_2.dat')
data.append([time,tse,tpe,tke,tce,tme,tae])

time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx5/prop_out_2.dat')
data.append([time,tse,tpe,tke,tce,tme,tae])

time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx6/prop_out_2.dat')
data.append([time,tse,tpe,tke,tce,tme,tae])

handles.append(0)
handles.append(0)
handles.append(0)
handles.append(0)

############################################################ PLOTS 
############################## FIGURE 2 
plt.figure(1)
for i in range(number_of_files_to_import):
  plt.suptitle('CONSTANT DT=0.2 B=20 NUM=1 250 mev ',fontsize=18,y=0.05)
  if(i==2) : plot_info = graph_settings_2(number_of_files_to_import*10)
  plt.subplot(2,3,1)
  handles[i] = plt.plot(data[i][0],data[i][1],label=plot_info[i][0][0],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
  plt.grid()
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
  
plt.legend([handles[0],handles[1],handles[2],handles[3]],["STATIC NEW coulomb","MOMENTUM NEW coulomb","STATIC OLD coulomb","MOMENTUM OLD coulomb"],loc='upper center', bbox_to_anchor=(-1.8, 2.45),ncol=3, fancybox=True, shadow=True)
plt.show()
