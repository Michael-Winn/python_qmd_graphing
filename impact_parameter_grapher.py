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
wptp = 1
data = []
data_density = []
number_of_files = 2
#STATIC IMPORT
for i in range(number_of_files):
  if(wptp ==1 or wptp == 3 ) :
    time,rho,rho_n,rho_p,rho_p_plus_n = import_density('xxx'+str(i) +'/density_out.dat')
    data_density.append([time,rho,rho_n,rho_p,rho_p_plus_n])

############################################################ PLOTS 
############################## FIGURE 1 


plt.figure(1)
plt.subplot(2,1,1)
for i in range(number_of_files):
  plt.plot(data_density[i][0],data_density[i][1],label=r" Total system density $\rho$",color='cyan',linestyle='-',markevery=10)
  plt.plot(data_density[i][0],data_density[i][4],label=r" Total system density of as a sum of n and p  $\rho_p + \rho_n$",linestyle='None',color='green',marker='o',markevery=10)
plt.grid()
plt.legend()
plt.xlabel('step (fm)')
plt.ylabel(r'density ($fm^{-3}$)')
plt.title("Variation of the density as a function of the step")


plt.subplot(2,2,1)
for i in range(number_of_files):
  plt.plot(data_density[i][0],data_density[i][2],label=r" Total system density of neutrons $\rho_n$",color='blue',marker='o',markevery=10)
  plt.plot(data_density[i][0],data_density[i][3],label=r" Total system density of protons $\rho_p$",color='green',marker='o',markevery=10)
plt.grid()
plt.legend()
plt.xlabel('step (fm)')
plt.ylabel(r'density ($fm^{-3}$)')
plt.title("Variation of the density as a function of the step")



############################################################ SHOW PLOTS 
plt.show()
