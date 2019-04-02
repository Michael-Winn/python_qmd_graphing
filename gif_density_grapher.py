import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
import matplotlib.axes as axes
#Made modules import
from tools.function_with_time import *


############################################################KEY

#time = the timestep of the for of lenght the energy [0]
#tse = total system energy [1]
#tpe  = total potential energy [2]
#tke = total kinetic energy [3]
#tce = total coulomb energy [4]
#tme = total momentum energy [5]
#tae = total system asymetry energy [6]



############################################################ INPUT FILES
wptp = 3
data_density = []
data_rms = []
#STATIC IMPORT
if(wptp ==1 or wptp == 3 ) :
  radius,rho_p,rho_t,rho_f,timest = import_density('xxx1/fort.661')
  data_density.append([radius,rho_p,rho_t,rho_f,timest])
  timest,rms_p,rms_t,rms_f = import_rms('xxx1/fort.662')
  data_rms.append([timest,rms_p,rms_t,rms_f])
#MOMENTUM IMPORT
if(wptp ==1 or wptp == 3 ) :
  radius,rho_p,rho_t,rho_f,timest = import_density('xxx2/fort.661')
  data_density.append([radius,rho_p,rho_t,rho_f,timest])
  timest,rms_p,rms_t,rms_f = import_rms('xxx2/fort.662')
  data_rms.append([timest,rms_p,rms_t,rms_f])
############################################################ PLOTS 
############################## FIGURE 1 
for i in range(len(data_density[0][4][0])-1):
  plt.plot(data_density[0][0][i],data_density[0][1][i],label=r'$\rho_{projectile}(r)$ for time step ' + str(data_density[0][4][i][0])+ 'fm',color = 'purple',linestyle='-',marker='o',markevery = 10)
  print(i)
  plt.ylim(0,3)
  #plt.plot(data_density[0][0][i],data_density[0][2][i],label=r'$\rho_{target}(r)$ for time step ' + str(data_density[0][4][i][0])+' fm',linestyle='-',marker='v',markevery = 10)
  #plt.plot(data_density[0][0][i],data_density[0][3][i],label=r'$\rho_{fireball}(r)$ for time step ' + str(data_density[0][4][i][0])+' fm',linestyle='-',marker='+',markevery = 10)
  #plt.grid()
  #plt.legend()
  plt.xlabel('radius')
  plt.ylabel(r'density $\rho$')
  plt.title("Variation density in function of the radius for a specific time step ")
  plt.savefig('density_r_static/'+str(i)+'.png')
  plt.close()
