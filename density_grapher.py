import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
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
  radius,rho_p,rho_t,rho_f,timest,rho_pa,rho_ta,rho_fa = import_density('../xxx1/fort.661')
  data_density.append([radius,rho_p,rho_t,rho_f,timest,rho_pa,rho_ta,rho_fa])
  timest,rms_p,rms_t,rms_f = import_rms('../xxx1/fort.662')
  data_rms.append([timest,rms_p,rms_t,rms_f])
#MOMENTUM IMPORT
if(wptp ==1 or wptp == 3 ) :
  radius,rho_p,rho_t,rho_f,timest,rho_pa,rho_ta,rho_fa = import_density('../xxx2/fort.661')
  data_density.append([radius,rho_p,rho_t,rho_f,timest,rho_pa,rho_ta,rho_fa])
  timest,rms_p,rms_t,rms_f = import_rms('../xxx2/fort.662')
  data_rms.append([timest,rms_p,rms_t,rms_f])
############################################################ PLOTS 
############################## FIGURE 1 
plt.figure(1)
plt.suptitle('For the static dependence')
plt.subplot(2,1,1)
print(len(data_rms[0][0]))
print(len(data_density[0][5]))
plt.plot(data_rms[0][0],data_density[0][5],label=r'$\bar{\rho}_{projectile}(t)$',linestyle='-',marker='o',markevery = 10)
plt.plot(data_rms[0][0],data_density[0][6],label=r'$\bar{\rho}_{target}(t)$',linestyle='-',marker='o',markevery = 10)
plt.plot(data_rms[0][0],data_density[0][7],label=r'$\bar{\rho}_{fireball}(t)$',linestyle='-',marker='o',markevery = 10)
#plt.plot(data_density[0][0][0],data_density[0][1][0],label=r'$\bar{\rho}_{projectile}(t)$ for time step ' + str(data_density[0][4][0][0])+ 'fm',linestyle='-',marker='o',markevery = 10)
#plt.plot(data_density[0][0][50],data_density[0][2][0],label=r'$\bar{\rho}_{target}(t)$ for time step ' + str(data_density[0][4][0][0])+' fm',linestyle='-',marker='v',markevery = 10)
#plt.plot(data_density[0][0][80],data_density[0][3][0],label=r'$\bar{\rho}_{fireball}(t)$ for time step ' + str(data_density[0][4][0][0])+' fm',linestyle='-',marker='+',markevery = 10)
plt.grid()
plt.legend()
plt.xlabel(r'time step $(fm/c)$')
plt.ylabel(r' average density $\bar{\rho}$')
plt.title("Variation density in function of the radius for a specific time step ")
plt.subplot(2,1,2)
plt.plot(data_rms[0][0],data_rms[0][1],label=r'$rms_{projectile}$',linestyle = '-',marker = 'o',markevery=10)
plt.plot(data_rms[0][0],data_rms[0][2],label=r'$rms_{target}$',linestyle = '-',marker = 'v',markevery=10)
plt.plot(data_rms[0][0],data_rms[0][3],label=r'$rms_{fireball}$',linestyle = '-',marker = '+',markevery=10)
plt.grid()
plt.legend()
plt.xlabel(r'time step $(fm/c)$')
plt.ylabel(r'rms')
plt.title("Variation of the rms in  function of the timestep")


############################## FIGURE 2 
plt.figure(2)
plt.suptitle('For the momentum dependence')
plt.subplot(2,1,1)
plt.plot(data_rms[1][0],data_density[1][5],label=r'$\bar{\rho}_{projectile}(t)$',linestyle='-',marker='o',markevery = 10)
plt.plot(data_rms[1][0],data_density[1][6],label=r'$\bar{\rho}_{target}(t)$',linestyle='-',marker='o',markevery = 10)
plt.plot(data_rms[1][0],data_density[1][7],label=r'$\bar{\rho}_{fireball}(t)$',linestyle='-',marker='o',markevery = 10)
#plt.plot(data_density[1][0][0],data_density[1][1][0],label=r'$\bar{\rho}_{projectile}(t)$ for time step ' + str(data_density[1][4][0][0])+ 'fm',linestyle='-',marker='o',markevery = 10)
#plt.plot(data_density[1][0][50],data_density[1][2][0],label=r'$\bar{\rho}_{target}(t)$ for time step ' + str(data_density[1][4][0][0])+' fm',linestyle='-',marker='v',markevery = 10)
#plt.plot(data_density[1][0][80],data_density[1][3][0],label=r'$\bar{\rho}_{fireball}(t)$ for time step ' + str(data_density[1][4][0][0])+' fm',linestyle='-',marker='+',markevery = 10)
plt.grid()
plt.legend()
plt.xlabel(r'time step $(fm/c)$')
plt.ylabel(r'density $\rho$')
plt.title("Variation density in function of the radius for a specific time step ")
plt.subplot(2,1,2)
plt.plot(data_rms[1][0],data_rms[1][1],label=r'$rms_{projectile}$',linestyle = '-',marker = 'o',markevery=10)
plt.plot(data_rms[1][0],data_rms[1][2],label=r'$rms_{target}$',linestyle = '-',marker = 'v',markevery=10)
plt.plot(data_rms[1][0],data_rms[1][3],label=r'$rms_{fireball}$',linestyle = '-',marker = '+',markevery=10)
plt.grid()
plt.legend()
plt.xlabel(r'time step $(fm/c)$')
plt.ylabel(r'rms')
plt.title("Variation of the rms in  function of the timestep")



plt.show()
