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

########################################################### COMMON VARIABLES
current_working_dir = '../altered_version_v11'
wptp = 1
number_of_files_to_import = 6
###########################################################
handles = []
data = []
plot_info = []
plot_info = graph_settings_2(number_of_files_to_import*10)
graph_count = 1
for i in range(number_of_files_to_import*10):
  handles.append(0)
if(wptp == 1 or wptp == 3) :
  for i in range(number_of_files_to_import):
      print(i)
    #STATIC IMPORT
  #  if(wptp ==1 or wptp == 3 ) :
#      time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx1/xxx1-'+str(i)+'/prop_out_'+str(i)+'.dat')
      time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx3/xxx3-'+str(i)+'/prop_out_'+str(i)+'.dat')
      data.append([time,tse,tpe,tke,tce,tme,tae])
    #MOMENTUM IMPORT
  #  if(wptp ==2 or wptp == 3 ) :
#      time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx2/xxx2-'+str(i)+'/prop_out_'+str(i)+'.dat')
#      time,tse,tpe,tke,tce,tme,tae = import_energies_alt(current_working_dir+'/xxx4/xxx4-'+str(i)+'/prop_out_'+str(i)+'.dat')
#      data.append([time,tse,tpe,tke,tce,tme,tae])
  
  ############################################################ PLOTS 
  ############################## FIGURE 1 
#  for i in range(number_of_files_to_import*2):
  for i in range(number_of_files_to_import):
#      print(i)
      fig = plt.figure(figsize=(19.2,10.8), dpi=100)
      plt.figure(graph_count)
      graph_count += 1
      title = plt.suptitle('CONSTANT DT=0.2  TIME STEP B=20 NUM=1 Beam energy = 250 Mev',fontsize=20,y=0.05)
      plt.subplot(2,3,1)
      plt.plot(data[i][0],data[i][1],label=plot_info[i][0][0],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=10)
      plt.grid()
  #    plt.legend(loc='upper center', bbox_to_anchor=(1, 1.25),ncol=3, fancybox=True, shadow=True)
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
      plt.plot(data[i][0],data[i][3],label=plot_info[i][0][2],color=plot_info[i][1],linestyle=plot_info[i][2],marker=plot_info[i][3],markevery=25)
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
 ################################################################SAVE OUT 
#      plt.legend([handles[0],handles[1]],["Energy per nucleon for the STATIC calculation","Energy per nucleon for the MOMENTUM calculation"],loc='upper center', bbox_to_anchor=(-1.2, 2.6),ncol=3, fancybox=True, shadow=True)
  #     fig.tight_layout()
#      plt.subplots_adjust(top=0.8)
#        plt.savefig('output_graphs_python/constant/' + str(i)+'.png',dpi=fig.dpi,bbox_extra_artists=(title,),bbox_inches='tight')
#      plt.savefig('output_graphs_python/constant/' + str(i)+'.png')
      
  
  ############################################################ SHOW PLOTS 
plt.show()
