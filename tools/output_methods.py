import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
#Made modules import
from tools.function_with_time import *
from tools.graph_names import *

def plotting_function_rms(static,plot_static,momentum,plot_momentum):
#  for j in range(len(static)):
#    for i in range(len(static[0][0])):
#        static[j][9][i] = 394./(4./3.*np.pi*(5./3.*static[j][9][i])**3)
#        momentum[j][9][i] = 394./(4./3.*np.pi*(5./3.*momentum[j][9][i])**3)
  plt.figure(figsize=(19.2,10.8), dpi=100)
  plt.suptitle('CONSTANT DT=0.2 B=20 NUM=5 100 MeV RMS ',fontsize=18,y=0.05)
  plt.subplot(2,3,1)
  print(len(static[0]))
  plt.plot(static[0][0],static[0][9],label=plot_static[0][0][0],color=plot_static[0][1],linestyle=plot_static[0][2][0],marker=plot_static[0][3],markevery=10)
  plt.plot(static[0][0],static[0][10],label=plot_static[0][0][1],color=plot_static[0][1],linestyle=plot_static[0][2][1],marker=plot_static[0][3],markevery=10)
  plt.plot(momentum[0][0],momentum[0][9],label=plot_momentum[0][0][0],color=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10)
  plt.plot(momentum[0][0],momentum[0][10],label=plot_momentum[0][0][1],markeredgecolor=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10,mfc='none')
  plt.grid()
  plt.title("Variation of the rms for the TOTAL energy ")
  plt.xlabel('time step (fm)')
  plt.ylabel('rms (fm)')
  plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 1.2),ncol=1, fancybox=True, shadow=True)
  
  plt.subplot(2,3,2)
  plt.plot(static[1][0],static[1][9],label=plot_static[0][0][0],color=plot_static[0][1],linestyle=plot_static[0][2][0],marker=plot_static[0][3],markevery=10)
  plt.plot(static[1][0],static[1][10],label=plot_static[0][0][1],color=plot_static[0][1],linestyle=plot_static[0][2][1],marker=plot_static[0][3],markevery=10)
  plt.plot(momentum[1][0],momentum[1][9],label=plot_momentum[0][0][0],color=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10)
  plt.plot(momentum[1][0],momentum[1][10],label=plot_momentum[0][0][1],markeredgecolor=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10,mfc='none')
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('rms (fm)')
  plt.title("Variation of the rms for the POTENTIAL energy ")
  
  plt.subplot(2,3,3)
  plt.plot(static[2][0],static[2][9],label=plot_static[0][0][0],color=plot_static[0][1],linestyle=plot_static[0][2][0],marker=plot_static[0][3],markevery=10)
  plt.plot(static[2][0],static[2][10],label=plot_static[0][0][1],color=plot_static[0][1],linestyle=plot_static[0][2][1],marker=plot_static[0][3],markevery=10)
  plt.plot(momentum[2][0],momentum[2][9],label=plot_momentum[0][0][0],color=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10)
  plt.plot(momentum[2][0],momentum[2][10],label=plot_momentum[0][0][1],markeredgecolor=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10,mfc='none')
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('rms (fm)')
  plt.title("Variation of the rms for the KINETIC energy ")
  
  plt.subplot(2,3,4)
  plt.plot(static[3][0],static[3][9],label=plot_static[0][0][0],color=plot_static[0][1],linestyle=plot_static[0][2][0],marker=plot_static[0][3],markevery=10)
  plt.plot(static[3][0],static[3][10],label=plot_static[0][0][1],color=plot_static[0][1],linestyle=plot_static[0][2][1],marker=plot_static[0][3],markevery=10)
  plt.plot(momentum[3][0],momentum[3][9],label=plot_momentum[0][0][0],color=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10)
  plt.plot(momentum[3][0],momentum[3][10],label=plot_momentum[0][0][1],markeredgecolor=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10,mfc='none')
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('rms (fm)')
  plt.title("Variation of the rms for the COULOMB energy ")
  
  plt.subplot(2,3,5)
  plt.plot(static[4][0],static[4][9],label=plot_static[0][0][0],color=plot_static[0][1],linestyle=plot_static[0][2][0],marker=plot_static[0][3],markevery=10)
  plt.plot(static[4][0],static[4][10],label=plot_static[0][0][1],color=plot_static[0][1],linestyle=plot_static[0][2][1],marker=plot_static[0][3],markevery=10)
  plt.plot(momentum[4][0],momentum[4][9],label=plot_momentum[0][0][0],color=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10)
  plt.plot(momentum[4][0],momentum[4][10],label=plot_momentum[0][0][1],markeredgecolor=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10,mfc='none')
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('rms (fm)')
  plt.title("Variation of the rms for the MOMENTUM energy ")
  
  plt.subplot(2,3,6)
  plt.plot(static[5][0],static[5][9],label=plot_static[0][0][0],color=plot_static[0][1],linestyle=plot_static[0][2][0],marker=plot_static[0][3],markevery=10)
  plt.plot(static[5][0],static[5][10],label=plot_static[0][0][1],color=plot_static[0][1],linestyle=plot_static[0][2][1],marker=plot_static[0][3],markevery=10)
  plt.plot(momentum[5][0],momentum[5][9],label=plot_momentum[0][0][0],color=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10)
  plt.plot(momentum[5][0],momentum[5][10],label=plot_momentum[0][0][1],markeredgecolor=plot_momentum[0][1],linestyle=plot_momentum[0][2],marker=plot_momentum[0][3],markevery=10,mfc='none')
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel('rms (fm)')
  plt.title("Variation of the rms for the ASYMMETRY energy ")

#  plt.subplots_adjust(top=0.8)
  plt.savefig('output_graphs_python/rms/rms.pdf')
  plt.show()

def plotting_momentum_contribution(static,plot_static,momentum,plot_old,plot_new):
    plt.figure(1,figsize=(19.2,10.8), dpi=100)
    plt.suptitle('CONSTANT DT=0.2 B=20 NUM=1 250 mev ',fontsize=18,y=0.05)
    plt.subplot(2,2,1)
    plt.plot(momentum[1][0],momentum[1][1],label=plot_old[0][0][0],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    plt.plot(momentum[2][0],momentum[2][1],label=plot_new[0][0][0],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.title("Variation of the TOTAL energy ")
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    
    plt.subplot(2,2,2)
    plt.plot(momentum[0][0],momentum[0][2],label=plot_old[0][0][1],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    plt.plot(momentum[3][0],momentum[3][2],label=plot_new[0][0][1],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the POTENTIAL energy ")
    
    plt.subplot(2,2,3)
    plt.plot(momentum[1][0],momentum[1][5],label=plot_old[0][0][4],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    plt.plot(momentum[2][0],momentum[2][5],label=plot_new[0][0][4],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the MOMENTUM energy ")
    handles = [] 
    for i in range(len(momentum[1][5])):
      momentum[1][5][i] = momentum[1][5][i] + momentum[0][2][i]
      momentum[2][5][i] = momentum[2][5][i] + momentum[3][2][i]
    handles.append(0)
    handles.append(0)
    handles.append(0)
    plt.subplot(2,2,4)
    handles[0] = plt.plot(static[0][0],static[0][2],label=plot_static[0][0][2],color=plot_static[0][1],linestyle=plot_static[0][2],marker=plot_static[0][3],markevery=10)
    handles[1] = plt.plot(momentum[1][0],momentum[1][5],label=plot_old[0][0][4],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    handles[2] = plt.plot(momentum[2][0],momentum[2][5],label=plot_new[0][0][4],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the MOMENTUM+POTENTIAL STATIC energy ")
    
    plt.legend(["POTENTIAL STATIC","POTENTIAL MOMENTUM OLD","POTENTIAL MOMENTUM OPTICAL"],loc='upper center', bbox_to_anchor=(-1, 2.65),ncol=1, fancybox=True, shadow=True)
#    plt.legend(handles[0],handles[1],handles[2],["POTENTIAL MOMENTUM OLD","POTENTIAL MOMENTUM OPTICAL","POTENTIAL STATIC"],loc='upper center', bbox_to_anchor=(-0.2, 2.6),ncol=1, fancybox=True, shadow=True)
#    plt.legend(handles,loc='upper center', bbox_to_anchor=(0, 2.6),ncol=1, fancybox=True, shadow=True)
#
    plt.subplots_adjust(top=0.8)
    plt.show()


def upgraded_plotting_function(static,plot_static,momentum,plot_momentum,wtp):
  for i in range(len(static)):
    print(i)
    print(len(static))
    plt.figure(i,figsize=(19.2,10.8), dpi=100)
    plt.suptitle('CONSTANT DT=0.2 B=20 NUM=1 250 mev ',fontsize=18,y=0.05)
    if(wtp ==0 or wtp ==2):
      upgraded_plot_inner(i,static,plot_static)
      plt.savefig('output_graphs_python/constant/static/' + plot_static[0][4][i]+'.pdf')
    plt.clf()
    if(wtp==1 or wtp ==2):
      upgraded_plot_inner(i,momentum,plot_momentum)
      plt.savefig('output_graphs_python/constant/momentum/' + plot_static[0][4][i]+'.pdf')
    if(wtp==2) :  
      upgraded_plot_inner(i,static,plot_static)
      plt.savefig('output_graphs_python/constant/' + plot_static[0][4][i]+'.pdf')

  plt.show()

def upgraded_plot_inner(i,values,info):
    plt.figure(i)
    plt.subplot(2,3,1)
    plt.plot(values[i][0],values[i][1],label=info[0][0][0],color=info[0][1],linestyle=info[0][2],marker=info[0][3],markevery=10)
    plt.grid()
    plt.title("Variation of the TOTAL energy ")
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    
    plt.legend(loc='upper center', bbox_to_anchor=(1, 1.25),ncol=3, fancybox=True, shadow=True)
    plt.subplot(2,3,2)
    plt.plot(values[i][0],values[i][2],label=info[0][0][1],color=info[0][1],linestyle=info[0][2],marker=info[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the POTENTIAL energy ")
    
    plt.subplot(2,3,3)
    plt.plot(values[i][0],values[i][3],label=info[0][0][2],color=info[0][1],linestyle=info[0][2],marker=info[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the KINETIC energy ")
    
    plt.subplot(2,3,4)
    plt.plot(values[i][0],values[i][4],label=info[0][0][3],color=info[0][1],linestyle=info[0][2],marker=info[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the COULOMB energy ")
    
    plt.subplot(2,3,5)
    plt.plot(values[i][0],values[i][5],label=info[0][0][4],color=info[0][1],linestyle=info[0][2],marker=info[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the momentum energy ")
    
    plt.subplot(2,3,6)
    plt.plot(values[i][0],values[i][6],label=info[0][0][5],color=info[0][1],linestyle=info[0][2],marker=info[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the ASYMMETRY energy ")

def upgraded_plotting_function_density(static,plot_static,momentum,plot_momentum,wtp):
###########################################RHOM
  plt.figure(figsize=(19.2,10.8), dpi=100)
  plt.suptitle('CONSTANT DT=0.2 B=20 NUM=5 100 MeV RHOM METHOD ',fontsize=18,y=0.05)
  if(wtp==0 or wtp ==2) : upgraded_density_inner(static,plot_static)
  if(wtp==1 or wtp ==2) : upgraded_density_inner(momentum,plot_momentum)
  plt.savefig('output_graphs_python/density/density.pdf')
#  plt.show()

def upgraded_density_inner(values,info):
  plt.subplot(2,3,1)
  plt.plot(values[0][0],values[0][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
  plt.plot(values[0][0],values[0][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
  plt.grid()
  plt.title("Variation of the density for the TOTAL energy ")
  plt.xlabel('time step (fm)')
  plt.ylabel(r'$\rho (fm^{-3})$')
  
  plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 1.2),ncol=1, fancybox=True, shadow=True)
  plt.subplot(2,3,2)
  plt.plot(values[1][0],values[1][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
  plt.plot(values[1][0],values[1][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel(r'$\rho (fm^{-3})$')
  plt.title("Variation of the density for the POTENTIAL energy ")
  
  plt.subplot(2,3,3)
  plt.plot(values[2][0],values[2][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
  plt.plot(values[2][0],values[2][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel(r'$\rho (fm^{-3})$')
  plt.title("Variation of the density for the KINETIC energy ")
  
  plt.subplot(2,3,4)
  plt.plot(values[3][0],values[3][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
  plt.plot(values[3][0],values[3][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel(r'$\rho (fm^{-3})$')
  plt.title("Variation of the density for the COULOMB energy ")
  
  plt.subplot(2,3,5)
  plt.plot(values[4][0],values[4][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
  plt.plot(values[4][0],values[4][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel(r'$\rho (fm^{-3})$')
  plt.title("Variation of the density for the MOMENTUM energy ")
  
  plt.subplot(2,3,6)
  plt.plot(values[5][0],values[5][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
  plt.plot(values[5][0],values[5][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
  plt.grid()
  plt.xlabel('time step (fm)')
  plt.ylabel(r'$\rho (fm^{-3})$')
  plt.title("Variation of the density for the ASYMMETRY energy ")

