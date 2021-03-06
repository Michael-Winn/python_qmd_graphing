import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.animation as animation
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#import matplotlib as mpl
print mpl.__version__
#mpl.use('agg')
#import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D  
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
    plt.suptitle('CONSTANT DT=0.2 B=20 NUM=5 100 mev ',fontsize=18,y=0.05)
    plt.subplot(2,2,1)
    plt.plot(momentum[5][0],momentum[5][1],label=plot_old[0][0][0],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    plt.plot(momentum[6][0],momentum[6][1],label=plot_new[0][0][0],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.title("Variation of the TOTAL energy ")
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    
    plt.subplot(2,2,2)
    plt.plot(momentum[1][0],momentum[1][2],label=plot_old[0][0][1],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    plt.plot(momentum[7][0],momentum[7][2],label=plot_new[0][0][1],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the POTENTIAL energy ")
    
    plt.subplot(2,2,3)
    plt.plot(momentum[5][0],momentum[5][5],label=plot_old[0][0][4],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    plt.plot(momentum[6][0],momentum[6][5],label=plot_new[0][0][4],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the MOMENTUM energy ")
    handles = [] 
    for i in range(len(momentum[1][5])):
      momentum[5][5][i] = momentum[5][5][i] + momentum[1][2][i]
      momentum[6][5][i] = momentum[6][5][i] + momentum[7][2][i]
    handles.append(0)
    handles.append(0)
    handles.append(0)
    plt.subplot(2,2,4)
    handles[0] = plt.plot(static[0][0],static[0][2],label=plot_static[0][0][2],color=plot_static[0][1],linestyle=plot_static[0][2],marker=plot_static[0][3],markevery=10)
    handles[1] = plt.plot(momentum[5][0],momentum[5][5],label=plot_old[0][0][4],color=plot_old[0][1],linestyle=plot_old[0][2],marker=plot_old[0][3],markevery=10)
    handles[2] = plt.plot(momentum[6][0],momentum[6][5],label=plot_new[0][0][4],color=plot_new[0][1],linestyle=plot_new[0][2],marker=plot_new[0][3],markevery=10)
    plt.grid()
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    plt.title("Variation of the MOMENTUM+POTENTIAL STATIC energy ")
    
    plt.legend(["POTENTIAL STATIC","POTENTIAL MOMENTUM OLD","POTENTIAL MOMENTUM OPTICAL"],loc='upper center', bbox_to_anchor=(-1, 2.5),ncol=1, fancybox=True, shadow=True)
    plt.savefig('output_graphs_python/constant/momentum_contribution.pdf')
#    plt.legend(handles[0],handles[1],handles[2],["POTENTIAL MOMENTUM OLD","POTENTIAL MOMENTUM OPTICAL","POTENTIAL STATIC"],loc='upper center', bbox_to_anchor=(-0.2, 2.6),ncol=1, fancybox=True, shadow=True)
#    plt.legend(handles,loc='upper center', bbox_to_anchor=(0, 2.6),ncol=1, fancybox=True, shadow=True)
#
    plt.subplots_adjust(top=0.8)
#    plt.show()


def upgraded_plotting_function(static,plot_static,momentum,plot_momentum,wtp):
  for i in range(len(momentum)):
    print(i)
    print(len(momentum))
    plt.figure(i,figsize=(19.2,10.8), dpi=100)
    plt.suptitle('CONSTANT DT=0.2 B=20 NUM=1 250 mev ',fontsize=18,y=0.05)
    plt.grid()
    if(wtp ==0 or wtp ==2):
      upgraded_plot_inner(i,static,plot_static)
      plt.savefig('output_graphs_python/constant/static/' + plot_static[0][4][i]+'.pdf')
      plt.clf()
    if(wtp==1 or wtp ==2):
      upgraded_plot_inner(i,momentum,plot_momentum)
      print("here")
      plt.savefig('output_graphs_python/constant/momentum/' + plot_momentum[0][4][i]+'.pdf')
    if(wtp==2) :  
      upgraded_plot_inner(i,static,plot_static)
      plt.legend(["MOMENTUM","STATIC"],loc='upper center', bbox_to_anchor=(-2.55,2.45),ncol=1, fancybox=True, shadow=True)
      plt.savefig('output_graphs_python/constant/' + plot_static[0][4][i]+'.pdf')
  plt.show()

def upgraded_plot_inner(i,values,info):
    plt.figure(i)
    plt.subplot(2,3,1)
    plt.grid()
    plt.plot(values[i][0],values[i][1],label=info[0][0][0],color=info[0][1],linestyle=info[0][2],marker=info[0][3],markevery=10)
    plt.title("Variation of the TOTAL energy ")
    plt.xlabel('time step (fm)')
    plt.ylabel('energy (MeV)')
    
#    plt.legend(loc='upper center', bbox_to_anchor=(1, 1.25),ncol=3, fancybox=True, shadow=True)
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

def import_position(fname) :

        data_set = []
	data = []
	counter = 0
	separated_data = []
	number_of_separate_particles = 394

	data = np.loadtxt(fname)
	temp_data_storage = []
	for i in range(len(data)):
		temp_data_storage.append(data[i])
	 	if ((i+1) % number_of_separate_particles == 0 and i != 0) :
			separated_data.append(temp_data_storage)
			temp_data_storage = []
	print(len(separated_data))
	time = []
	x = []
	y = []
	z = []
	iso = []
	for j in range(number_of_separate_particles):
		  temp_time = []
                  temp_x = []
		  temp_y = []
		  temp_z = []
		  temp_iso = []
		  for i in range(len(separated_data)):
			  temp_time.append(separated_data[i][j][0])
			  temp_x.append(separated_data[i][j][1])
			  temp_y.append(separated_data[i][j][2])
			  temp_z.append(separated_data[i][j][3])
			  temp_iso.append(separated_data[i][j][4])

		  time.append(temp_time)
		  x.append(temp_x)
		  y.append(temp_y)
		  z.append(temp_z)
		  iso.append(temp_iso)

	return time,x,y,z,iso

def plotting_position(time,x,y,z,iso,static):
  rms_p_table= []
  rms_t_table= []
#  for j in range(len(time[0])):
#    progress(j,len(time[0]),'Generating PNGs')
  for j in range(1):
    print(j)
    nnuc = 394.
    time_rho = []
    rho_t = []
    rho_p = []
    x0t_n = []
    y0t_n = []
    z0t_n = []
    x0t_p = []
    y0t_p = []
    z0t_p = []
    x0p_n = []
    y0p_n = []
    z0p_n = []
    x0p_p = []
    y0p_p = []
    z0p_p = []
    xm_t = 0. 
    ym_t = 0. 
    zm_t = 0. 
    xm_p = 0. 
    ym_p = 0. 
    zm_p = 0. 
    rms_t = 0.
    rms_p = 0.
    for i in range(len(time)):
     if(i <= 196):
       if(iso[i][j] ==0) :
        x0t_n.append(x[i][j])
        y0t_n.append(y[i][j])
        z0t_n.append(z[i][j])
       else:
        x0t_p.append(x[i][j])
        y0t_p.append(y[i][j])
        z0t_p.append(z[i][j])
     if(i>196) :
       if(iso[i][j] ==0) :
        x0p_n.append(x[i][j])
        y0p_n.append(y[i][j])
        z0p_n.append(z[i][j])
       else : 
        x0p_p.append(x[i][j])
        y0p_p.append(y[i][j])
        z0p_p.append(z[i][j])

    for i in range(len(x0t_n)):
      xm_t += x0t_n[i]
      ym_t += y0t_n[i]
      zm_t += z0t_n[i]

    for i in range(len(x0t_p)):
      xm_t += x0t_p[i]
      ym_t += y0t_p[i]
      zm_t += z0t_p[i]


    for i in range(len(x0p_n)):
      xm_p += x0p_n[i]
      ym_p += y0p_n[i]
      zm_p += z0p_n[i]

    for i in range(len(x0p_p)):
      xm_p += x0p_p[i]
      ym_p += y0p_p[i]
      zm_p += z0p_p[i]


    xm_t /= nnuc*0.5
    ym_t /= nnuc*0.5
    zm_t /= nnuc*0.5
    xm_p /= nnuc*0.5
    ym_p /= nnuc*0.5
    zm_p /= nnuc*0.5

    for i in range(len(time)):
      if(i <= 196):
       rms_t +=(x[i][j]-xm_t)*(x[i][j]-xm_t)+(y[i][j]-ym_t)*(y[i][j]-ym_t)+(z[i][j]-zm_t)*(z[i][j]-zm_t)
       print(rms_t,x[i][j],
	   (x[i][j]-xm_t)**2,
	   (y[i][j]-ym_t)**2,
	   (z[i][j]-zm_t)**2)
      if(i>196) :
       rms_p +=(x[i][j]-xm_p)*(x[i][j]-xm_p)+(y[i][j]-ym_p)*(y[i][j]-ym_p)+(z[i][j]-zm_p)*(z[i][j]-zm_p)
      
    print('RMS before division {0}'.format(rms_t)) 
    rms_t = 5./3.*np.sqrt(rms_t/nnuc)
    rms_p = 5./3.*np.sqrt(rms_p/nnuc)
    if(j != 0) : rms_t_table.append(rms_t)
    if(j != 0) :rms_p_table.append(rms_p)


    for i in range(j):
      time_rho.append(static[0][0][i])
      rho_t.append(static[0][7][i])
      rho_p.append(static[0][8][i])
#    print('-----------')
#    print(time_rho)
#    print(rms_t_table)
    fig = plt.figure(j,figsize=(10.8,7.2), dpi=100)
    gs = gridspec.GridSpec(5,5,hspace=1)
    gs_target = gridspec.GridSpec(5,5,hspace=0)
    gs_projectile = gridspec.GridSpec(5,5,hspace=0)

#    ax = plt.subplot2grid((5,5),(0,0), rowspan=5,colspan=4,projection='3d')
    ax = fig.add_subplot(gs[:,:-1],projection='3d')
    print('Center targert {0} {1} {2}'.format(xm_t,ym_t,zm_t))
    print('RMS_t {0}'.format(rms_t))
    sphere_t = ax.plot_wireframe(*sphere_on_center([xm_t,ym_t,zm_t],rms_t), edgecolor="orange", alpha=0.2,linewidth=2)
    target_n = ax.plot(x0t_n,y0t_n,z0t_n,color='red',linestyle='',marker='*',markersize=5,markeredgecolor='none',alpha=0.7,label='Target Neutron')
    target_p = ax.plot(x0t_p,y0t_p,z0t_p,color='orange',linestyle='',marker='o',markersize=5,markeredgecolor='none',alpha=0.7,label='Target Proton')
    sphere_p = ax.plot_wireframe(*sphere_on_center([xm_p,ym_p,zm_p],rms_p), edgecolor="purple", alpha=0.2)
    projectile_n = ax.plot(x0p_n,y0p_n,z0p_n,color='magenta',linestyle='',marker='*',markersize=5,markeredgecolor='none',alpha=0.7,label='Projectile Neutron')
    projectile_p = ax.plot(x0p_p,y0p_p,z0p_p,color='purple',linestyle='',marker='o',markersize=5,markeredgecolor='none',alpha=0.7,label='Projectile Proton')
    ax.legend(loc='upper left')
    ax.view_init(14,78)
    ax.set_xlim3d(-30,30)
    ax.set_ylim3d(-30,30)
    ax.set_zlim3d(-30,30)


#    ax2 = plt.subplot2grid((5,5),(0,4),hspace=0.4) 
    ax2 = fig.add_subplot(gs_target[0,4]) 
#    ax2.set_title('Target density')
#    ax2.set_title('Target')
#    ax2.set_xlabel('time step (fm)')
    ax2.set_ylabel(r'$\rho (fm^{-3})$')
    ax2.set_xlim(0,120)
    ax2.set_ylim(0.08,0.2)
    ax2.grid()
    plt.tick_params(axis='x',bottom=False,labelbottom=False) 
    plot_rho_t = ax2.plot(time_rho,rho_p,color='orange',label='Target')
    ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=7)


#    ax5 = plt.subplot2grid((5,5),(1,4)) 
    ax5 = fig.add_subplot(gs_target[1,4]) 
#    ax5.set_title('Target')
    ax5.set_xlabel('time step (fm)')
    ax5.set_ylabel(r'$rms (fm)$')
    ax5.set_xlim(0,120)
    ax5.set_ylim(6,14)
    ax5.grid()
#    ax5.legend()
    plt.tick_params(axis='x',bottom=False,labelbottom=False) 
    plot_rms_t = ax5.plot(time_rho,rms_t_table,color='orange')

#    ax3 = plt.subplot2grid((5,5),(3,4)) 
    ax3 = fig.add_subplot(gs_projectile[2,4]) 
#    ax3.set_title('Projectile')
#    ax3.set_xlabel('time step (fm)')
    ax3.set_ylabel(r'$\rho (fm^{-3})$')
    ax3.set_xlim(0,120)
    ax3.set_ylim(0.08,0.2)
    ax3.grid()
    plt.tick_params(axis='x',bottom=False,labelbottom=False) 
    plot_rho_p = ax3.plot(time_rho,rho_p,color ='purple',label='Projectile')
    ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=7)


#    ax4 = plt.subplot2grid((5,5),(2,4)) 
    plt.tick_params(axis='x',bottom=True,labelbottom=False) 
    ax4 = fig.add_subplot(gs_projectile[3,4]) 
#    ax4.set_title('Projectile rms')
    ax4.set_xlabel('time step (fm)')
    ax4.set_ylabel(r'$rms (fm)$')
    ax4.set_xlim(0,120)
    ax4.set_ylim(6,14)
    ax4.grid()
    plot_rms_p = ax4.plot(time_rho,rms_p_table,color='purple',label='Projectile')

    fig.suptitle('T= '+  str(round(time[0][j],2)))
#    plt.savefig('output_graphs_python/position/position00'+str(j)+'.png')
#    if(j %10 ==0) : plt.savefig('output_graphs_python/position/position00'+str(j)+'.png')
    plt.savefig('output_graphs_python/position/position00'+str(j)+'.png')
    plt.close()
#    plt.show()



def import_rms(fname) :

	data = []
	rms_mean_t = []
	rms_mean_p = []
	x_mean_t = []
	y_mean_t = []
	z_mean_t = []
	x_mean_p = []
	y_mean_p = []
	z_mean_p = []

	data = np.loadtxt(fname)
	print(len(data))
	for i in range(len(data)):
	  rms_mean_t.append(data[i][0])
	  rms_mean_p.append(data[i][1])
	  x_mean_t.append(data[i][2])
	  y_mean_t.append(data[i][3])
	  z_mean_t.append(data[i][4])
	  x_mean_p.append(data[i][5])
	  y_mean_p.append(data[i][6])
	  z_mean_p.append(data[i][7])

	return rms_mean_t,rms_mean_p,x_mean_t,y_mean_t,z_mean_t,x_mean_p,y_mean_p,z_mean_p

def sphere_on_center(centre,radius):
         u, v = np.mgrid[0:2*np.pi:10*1j, 0:np.pi:10*1j]
         sphere_x = centre[0] + radius * np.cos(u) * np.sin(v)
	 sphere_y = centre[1] + radius * np.sin(u) * np.sin(v)
	 sphere_z = centre[2] + radius * np.cos(v)
	 return sphere_x, sphere_y, sphere_z


def progress(count, total, status=''):
      bar_len = 60
      filled_len = int(round(bar_len * count / float(total)))
      percents = round(100.0 * count / float(total), 1)
      bar = '#' * filled_len + '-' * (bar_len - filled_len)

      sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))
      sys.stdout.flush()





def plotting_density_function(static,momentum):
    sal_value = []
    cols = 6
    for i in range(50,71):
      sal_value.append(float(i)/10.)
#      print(float(i)/10.)
    fig = plt.figure(0,figsize=(10.8,7.2), dpi=100)
    gs = gridspec.GridSpec(4,6)
    for i in range(len(static)):
      row = (i // cols)
      col = i % cols
      ax = fig.add_subplot(gs[row,col]) 
      ax.grid()
      ax.plot(static[i][0],static[i][7],label='Target static',marker='',linestyle = '-' , color = 'purple')
#      ax.plot(static[i][0],static[i][8],label='Projectile static',marker='',linestyle = '--' , color = 'purple')
      ax.plot(momentum[i][0],momentum[i][7],label='Target momentum',marker = 'o',linestyle = 'none' , color = 'orange',markevery=10)
#      ax.plot(momentum[i][0],momentum[i][8],label='Projectile momentum',marker = 'o', mfc='none',markeredgecolor = 'orange',linestyle = 'none' , color = 'orange',markevery=10)
      ax.set_title("SAL = "+str(sal_value[i]))
      if(i==0): ax.legend(loc='upper left')
    plt.savefig('output_graphs_python/density_sal.png')


#def plotting_density_r(values_0,values_30):
#def plotting_density_r(values_0):
#    sal_value = []
#    cols = 1
#    for i in range(53,70):
#      sal_value.append(float(i)/10.)
#    fig = plt.figure(0,figsize=(10.8,7.2), dpi=100)
#    gs = gridspec.GridSpec(1,1)
#    for i in range(len(values_0)):
#      sum_t_0 = 0
#      sum_p_0 = 0
#
#      sum_t_30 = 0
#      sum_p_30 = 0
#      for j in range(len(values_0[i][1])):
#	sum_t_0 += values_0[i][1][j]
#	sum_p_0 += values_0[i][2][j]
#
##      for j in range(len(values_30[i][1])):
##	sum_t_30 += values_30[i][1][j]
##	sum_p_30 += values_30[i][2][j]
#
#      row = (i // cols)
#      col = i % cols
#      ax = fig.add_subplot(gs[row,col]) 
#      ax1=ax.twinx()
#      ax1.axis('off')
#      ax.grid()
#      sum_d =0
#      temp = 0
#      print(len(np.arange(0,10,0.05)))
#      for k in range(len(values_0[i][3])):
#	if(np.isnan(values_0[i][3][k])):
#	      a =0  
#        else:
#	    sum_d += values_0[i][3][k]
#	    temp += 1
#
#      sum_d /= temp
#      print(temp)
#      print(sum_d)
##      for k in range(len(values_0[i][3])):
##	if(k != len(values_0[i][3])) :
##	  values_0[i][3][k] = values_0[i][3][k]/(4./3. * 3.14159265 * (values_0[i][0][k+1]**3- values_0[i][0][k]**3) ) 
##	  values_0[i][3][k] = (values_0[i][3][k])**(1./3.)
#      ws_val = []
#      for k in range(len(values_0[i][0])):
#	ws_val.append(wood_saxon(values_0[i][0][k]))
#
##	if(values_0[i][0][k] < 2) : values_0[i][3][k] = values_0[i][3][k]/(4./3. * 3.14159265 * 2**3)
##        if(values_0[i][0][k] > 2 and values_0[i][0][k] < 4) : values_0[i][3][k] = values_0[i][3][k]/(4./3. * 3.14159265 * 4**3-4./3. * 3.14159265 * 2**3 )
##	if(values_0[i][0][k] > 4 and values_0[i][0][k] < 6) : values_0[i][3][k] = values_0[i][3][k]/(4./3. * 3.14159265 * 6**3-4./3. * 3.14159265 * 4**3 )
##	if(values_0[i][0][k] > 6 and values_0[i][0][k] < 8) : values_0[i][3][k] = values_0[i][3][k]/(4./3. * 3.14159265 * 8**3-4./3. * 3.14159265 * 6**3 )
##	if(values_0[i][0][k] > 8 and values_0[i][0][k] < 10) : values_0[i][3][k] = values_0[i][3][k]/(4./3. * 3.14159265 * 10**3-4./3. * 3.14159265 * 8**3 )
##      n,bins,patches=ax1.hist(np.arange(0,10.05,0.05),bins=100,weights=values_0[i][1],alpha=0.2,edgecolor='green',color='green')
##      n,bins,patches=ax1.hist(np.arange(0,10.05,0.05),bins=100,weights=values_0[i][2],alpha=0.2,fc='none',edgecolor='green',color='green')
##      n,bins,patches=ax1.hist(np.arange(0,10.1,0.1),bins=100,weights=values_30[i][1],alpha=0.2,edgecolor = 'cyan',color='cyan')
##      values_0_t = values_0
##      values_0_p = values_0
##      for i in range(len(values_0[i][0])):
##	if(values_0_t[i][3][j] ==0): values_0_t.remove(values_0_t[i][3][j])
##	if(values_0_p[i][4][j] ==0): values_0_p.remove(values_0_p[i][3][j])
##	if(values_0_t[i][3][j] ==0): values_0_t.remove(values_0_t[i][3][j])
##	if(values_0_p[i][4][j] ==0): values_0_p.remove(values_0_p[i][3][j])
#      ax.plot(values_0[i][0],ws_val,color='blue',linestyle='-',label='Wood saxon')
#      ax.plot(values_0[i][0],values_0[i][3],label='TIME 0 targ',marker='o',linestyle = '' , color = 'green')
#      ax.plot(values_0[i][0],values_0[i][4],label='TIME 0 proj',marker='o',linestyle = '' ,mfc='none',markeredgecolor='green', color = 'green')
##      ax.plot(values_30[i][0],values_30[i][3],label='TIME 30 targ',marker='o',linestyle = 'none' , color = 'cyan')
##      ax.plot(values_30[i][0],values_30[i][4],label='TIME 30 proj',marker='o',linestyle = 'none',mfc='none',markeredgecolor='cyan' , color = 'cyan')
#      ax.set_xlabel('r (fm)')
#      ax.set_ylabel(r'$\rho(r) fm^{-3}$')
#      ax.set_title("SAL = 5.0 " +r' $\Sigma_t = $' + str(sum_t_0) + r' $\Sigma_p = $ '+str(sum_p_0) + r' $\bar{\rho}=$ ' +str(round(sum_d,2)))
#      if(i==0): ax.legend(loc='upper right')
#    plt.savefig('output_graphs_python/density_sal.png')


def wood_saxon(r):
  RA = 1.125*197**(1/3)
  a = 0.534
  rho_0=0.1695
  ws_val = rho_0/(1+np.exp((r-RA)/a))

  return ws_val




def plotting_density_r(values_0,*values_1):
# These are the "Tableau 20" colors as RGB.    
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
                  (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
                  (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
                  (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
                  (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
    for i in range(len(tableau20)):    
      r, g, b = tableau20[i]    
      tableau20[i] = (r / 255., g / 255., b / 255.)   

    sal_value = []
    for i in range(53,70):
      sal_value.append(float(i)/10.)
    fig = plt.figure(0,figsize=(19.2,10.8), dpi=100)
    gs = gridspec.GridSpec(1,2)
    for i in range(len(values_0)):
      sum_t_0 = 0
      sum_p_0 = 0

      sum_t_30 = 0
      sum_p_30 = 0
      for j in range(len(values_0[i][1])):
	sum_t_0 += values_0[i][1][j]
	sum_p_0 += values_0[i][2][j]
      if values_1:
	print(len(values_1[0][0][1]))
        for j in range(len(values_1[0][i][1])):
	 sum_t_30 += values_1[0][i][1][j]
  	 sum_p_30 += values_1[0][i][2][j]

      sum_d =0
      temp = 0
      print(len(np.arange(0,10,0.05)))
      for k in range(len(values_0[i][3])):
	if(np.isnan(values_0[i][3][k])):
	      a =0  
        else:
	    sum_d += values_0[i][3][k]
	    temp += 1

      sum_d /= temp
      print(temp)
      print(sum_d)
      ws_val = []
      for k in range(len(values_0[i][0])):
	ws_val.append(wood_saxon(values_0[i][0][k])*20)
      ax = fig.add_subplot(gs[0,0])
      ax1=ax.twinx()
      ax1.axis('off')
      ax.grid()
      n,bins,patches=ax1.hist(np.arange(0,10.05,0.05),bins=100,weights=values_0[i][1],alpha=0.3,edgecolor=tableau20[4],color=tableau20[4])
      n,bins,patches=ax1.hist(np.arange(0,10.05,0.05),bins=100,weights=values_0[i][2],alpha=0.3,fc='none',edgecolor=tableau20[4],color=tableau20[4])
      ax.plot(values_0[i][0],ws_val,color=tableau20[0],linestyle='-',label='Wood saxon')
      ax.plot(values_0[i][0],values_0[i][3],label='TIME 0 targ',marker='o',linestyle = '' , color = tableau20[4])
      ax.plot(values_0[i][0],values_0[i][4],label='TIME 0 proj',marker='o',linestyle = '' ,mfc='none',markeredgecolor=tableau20[4], color = tableau20[4])
      ax.set_xlabel('r (fm)')
      ax.set_ylabel(r'$\rho(r) fm^{-3}$')
      ax.set_title("TIME 30" + "\n" + "SAL = 5.0 " +r' $\Sigma_t = $' + str(sum_t_0) + r' $\Sigma_p = $ '+str(sum_p_0) + r' $\bar{\rho}=$ ' +str(round(sum_d,2)))
      if(i==0): ax.legend(loc='upper right')

      if values_1:

       ws_val = []
       for k in range(len(values_0[i][0])):
	ws_val.append(wood_saxon(values_0[i][0][k])*10)
       ax2 = fig.add_subplot(gs[0,1])
       ax3=ax2.twinx()
       ax3.axis('off')
       ax2.grid()
       n,bins,patches=ax3.hist(np.arange(0,10.05,0.05),bins=100,weights=values_0[i][1],alpha=0.3,edgecolor=tableau20[18],color=tableau20[19])
       n,bins,patches=ax3.hist(np.arange(0,10.05,0.05),bins=100,weights=values_0[i][2],alpha=0.3,fc='none',edgecolor=tableau20[18],color=tableau20[19])
       ax2.plot(values_1[0][i][0],ws_val,color=tableau20[0],linestyle='-',label='Wood saxon')
       ax2.plot(values_1[0][i][0],values_1[0][i][3],label='TIME 30 targ',marker='o',linestyle = 'none' , color = tableau20[18])
       ax2.plot(values_1[0][i][0],values_1[0][i][4],label='TIME 30 proj',marker='o',linestyle = 'none',mfc='none',markeredgecolor=tableau20[18] , color = tableau20[19])
       ax2.set_xlabel('r (fm)')
       ax2.set_ylabel(r'$\rho(r) fm^{-3}$')
       ax2.set_title("TIME 30 " + "\n" + "SAL = 5.0 " +r' $\Sigma_t = $' + str(sum_t_0) + r' $\Sigma_p = $ '+str(sum_p_0) + r' $\bar{\rho}=$ ' +str(round(sum_d,2)))
       if(i==0): ax2.legend(loc='upper right')
    plt.savefig('output_graphs_python/density_sal.png')



def upgraded_plotting_function_density_all_only(static,plot_static,momentum,plot_momentum,wtp):
###########################################RHOM
  plt.figure(figsize=(19.2,10.8), dpi=100)
  plt.suptitle('CONSTANT DT=0.2 B=20 NUM=5 100 MeV RHOM METHOD ',fontsize=18,y=0.05)
  if(wtp==0 or wtp ==2) : upgraded_density_inner_all(static,plot_static)
  if(wtp==1 or wtp ==2) : upgraded_density_inner_all(momentum,plot_momentum)
  plt.savefig('output_graphs_python/density/density.pdf')
#  plt.show()

def upgraded_density_inner_all(values,info):
  plt.plot(values[0][0],values[0][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
  plt.plot(values[0][0],values[0][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
  plt.grid()
  plt.title("Variation of the density for the TOTAL energy ")
  plt.xlabel('time step (fm)')
  plt.ylabel(r'$\rho (fm^{-3})$')
  
  plt.legend(loc='upper center')


def other_plotting_function_density_all_only(static,plot_static,momentum,plot_momentum,wtp):
###########################################RHOM
  print('gets here')
  print(len(momentum))
  fig = plt.figure(figsize=(19.2,10.8), dpi=100)
  plt.suptitle('CONSTANT DT=0.2 B=20 NUM=5 100 MeV RHOM METHOD ',fontsize=18,y=0.05)
  other_density_inner_all(fig,static,plot_static,momentum,plot_momentum)
#  plt.show()

def other_density_inner_all(fig,static,plot_static,momentum,plot_momentum):
  sal_values = []
  for i in np.arange(4.0,7.25,0.25) :
    sal_values.append(i)
  cols = 4
  gs = gridspec.GridSpec(4,4,hspace=0.5)
  for j in range(2) : 
    if(j ==0) :
      values = static
      info = plot_static

    if(j ==1) :
      values = momentum
      info = plot_momentum

    for i in range(len(values)):
        row = (i // cols)
        col = i % cols
        ax = fig.add_subplot(gs[row,col]) 
        ax.grid()
        ax.plot(values[i][0],values[i][7],label=info[0][0][0],color=info[0][1],markeredgecolor=info[0][5][0],linestyle=info[0][2][0],marker=info[0][3],markevery=10,mfc=info[0][4][0])
        ax.plot(values[i][0],values[i][8],label=info[0][0][1],color=info[0][1],markeredgecolor=info[0][5][1],linestyle=info[0][2][1],marker=info[0][3],markevery=10,mfc=info[0][4][1])
        ax.grid()
        ax.set_title(r"$\rho(t)$  $E_{tot}$  $SAL = $ "+str(sal_values[i]))
        ax.set_xlabel('time step (fm)')
        ax.set_ylabel(r'$\rho (fm^{-3})$')
        ax.legend(loc='upper center')
#        ax.set_ylim(0.07,0.22)
  plt.savefig('output_graphs_python/density/density_sal_momentum.pdf')

