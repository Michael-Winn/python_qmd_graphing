import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
#Made modules import
from tools.function_with_time import *


############################################################KEY
#radius the radius step used in the output of the density
#rho_p the projectile density per radius step
#rho_t the target density per radius step
#rho_f the fireball density per radius step
#timest the time step
#rho_pa the average density in the projectile per time step
#rho_ta the average density in the target per time step
#ro_fa the average density in the fireball per time step
#rms_p the rms for the projectile per time step
#rms_t the rms for the target per time step
#rms_f the rms for the fireball per time step
############################################################ INPUT FILES
num_plots = 6 #Number of plots 
data_density = []
data_rms = []
sal_values = []
#IMPORT STATIC EVEN MOMENTUM ODD
for i in range(1,num_plots+1):
  print(i)
  radius,rho_p,rho_t,rho_f,timest,rho_pa,rho_ta,rho_fa = import_density('xxx'+str(i)+'/fort.661')
  data_density.append([radius,rho_p,rho_t,rho_f,timest,rho_pa,rho_ta,rho_fa])
  timest,rms_p,rms_t,rms_f = import_rms('xxx' + str(i) +'/fort.662')
  data_rms.append([timest,rms_p,rms_t,rms_f])

############################################################ PLOTS 
############################## FIGURE 1 
print('GOT TO THE PLOTTING PART')
plt.figure(1)
plt.suptitle('For the static dependence')

sal_values.append(5.2)
sal_values.append(5.2)
sal_values.append(5.5)
sal_values.append(5.5)
sal_values.append(6)
sal_values.append(6)
print('VALUES OF SAL : {0}'.format(sal_values))
for i in range(num_plots):
  print(i)
  if(i  == 0 ) : plt.subplot(2,3,1)
  if(i  == 2 ) : plt.subplot(2,3,2)
  if(i  == 4 ) : plt.subplot(2,3,3)
  if(i % 2 == 0 or i== 0):
      plt.plot(data_rms[i][0],data_density[i][5],label=r'$\rho_{projectile}(r)$ SAL: ' + str(sal_values[i]),linestyle='-',marker='o',markevery = 10)
      plt.plot(data_rms[i][0],data_density[i][6],label=r'$\rho_{target}(r)$ SAL: '+str(sal_values[i]),linestyle='-',marker='v',markevery = 10)
      plt.plot(data_rms[i][0],data_density[i][7],label=r'$\rho_{fireball}(r)$ SAL: '+str(sal_values[i]),linestyle='-',marker='+',markevery = 10)
#plt.plot(data_density[0][0][0],data_density[0][1][0],label=r'$\rho_{projectile}(r)$ for time step ' + str(data_density[0][4][0][0])+ 'fm',linestyle='-',marker='o',markevery = 10)
#plt.plot(data_density[0][0][50],data_density[0][2][0],label=r'$\rho_{target}(r)$ for time step ' + str(data_density[0][4][0][0])+' fm',linestyle='-',marker='v',markevery = 10)
#plt.plot(data_density[0][0][80],data_density[0][3][0],label=r'$\rho_{fireball}(r)$ for time step ' + str(data_density[0][4][0][0])+' fm',linestyle='-',marker='+',markevery = 10)
      plt.grid()
      plt.legend()
      plt.xlabel('radius')
      plt.ylabel(r' average density $\rho$')
      plt.title("Variation density in function of the radius for a specific time step ")
for i in range(num_plots):
  if(i  == 0 ) : plt.subplot(2,3,4)
  if(i  == 2 ) : plt.subplot(2,3,5)
  if(i  == 4 ) : plt.subplot(2,3,6)
  if(i % 2  == 0 or i==0 ) :
	print(i)
	plt.plot(data_rms[i][0],data_rms[i][1],label=r'$rms_{projectile}$ SAL: '+str(sal_values[i]),linestyle = '-',marker = 'o',markevery=10)
    	plt.plot(data_rms[i][0],data_rms[i][2],label=r'$rms_{target}$ SAL: '+str(sal_values[i]),linestyle = '-',marker = 'v',markevery=10)
    	plt.plot(data_rms[i][0],data_rms[i][3],label=r'$rms_{fireball}$ SAL: '+str(sal_values[i]),linestyle = '-',marker = '+',markevery=10)
	plt.grid()
	plt.legend(loc=4)
	plt.xlabel(r'time step $(fm/c^2)$')
	plt.ylabel(r'rms')
	plt.title("Variation of the rms in  function of the timestep")


############################## FIGURE 2 
plt.figure(2)
plt.suptitle('For the momentum dependence')
for i in range(num_plots):
  if(i  == 1 ) : plt.subplot(2,3,1)
  if(i  == 3 ) : plt.subplot(2,3,2)
  if(i  == 5 ) : plt.subplot(2,3,3)
  if(i % 2 != 0 ) :
      plt.plot(data_rms[i][0],data_density[i][5],label=r'$\rho_{projectile}(r)$ SAL: '+str(sal_values[i]),linestyle='-',marker='o',markevery = 10)
      plt.plot(data_rms[i][0],data_density[i][6],label=r'$\rho_{target}(r)$ SAL: '+str(sal_values[i]),linestyle='-',marker='v',markevery = 10)
      plt.plot(data_rms[i][0],data_density[i][7],label=r'$\rho_{fireball}(r)$ SAL: '+str(sal_values[i]),linestyle='-',marker='+',markevery = 10)

#plt.plot(data_density[1][0][0],data_density[1][1][0],label=r'$\rho_{projectile}(r)$ for time step ' + str(data_density[1][4][0][0])+ 'fm',linestyle='-',marker='o',markevery = 10)
#plt.plot(data_density[1][0][50],data_density[1][2][0],label=r'$\rho_{target}(r)$ for time step ' + str(data_density[1][4][0][0])+' fm',linestyle='-',marker='v',markevery = 10)
#plt.plot(data_density[1][0][80],data_density[1][3][0],label=r'$\rho_{fireball}(r)$ for time step ' + str(data_density[1][4][0][0])+' fm',linestyle='-',marker='+',markevery = 10)
      plt.grid()
      plt.legend()
      plt.xlabel('radius')
      plt.ylabel(r'density $\rho$')
      plt.title("Variation density in function of the radius for a specific time step ")
for i in range(num_plots):
  if(i  == 1 ) : plt.subplot(2,3,4)
  if(i  == 3 ) : plt.subplot(2,3,5)
  if(i  == 5 ) : plt.subplot(2,3,6)
  if(i % 2 != 0 ) :
      plt.plot(data_rms[i][0],data_rms[i][1],label=r'$rms_{projectile}$ SAL: '+str(sal_values[i]),linestyle = '-',marker = 'o',markevery=10)
      plt.plot(data_rms[i][0],data_rms[i][2],label=r'$rms_{target}$ SAL: '+str(sal_values[i]),linestyle = '-',marker = 'v',markevery=10)
      plt.plot(data_rms[i][0],data_rms[i][3],label=r'$rms_{fireball}$ SAL: '+str(sal_values[i]),linestyle = '-',marker = '+',markevery=10)
      plt.grid()
      plt.legend(loc=4)
      plt.xlabel(r'time step $(fm/c^2)$')
      plt.ylabel(r'rms')
      plt.title("Variation of the rms in  function of the timestep")



plt.show()
