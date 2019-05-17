import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.animation as animation
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
print mpl.__version__
from mpl_toolkits.mplot3d import axes3d, Axes3D  
import matplotlib.gridspec as gridspec
from tools.nuclei import *

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

def energy_plot(runs):
 for k in range(len(runs[0].runs)):
  print(k)
#  print(runs[0].runs[0])
  nucleus = [runs[0].runs[k],runs[1].runs[k]]
#  nucleus = [runs[0].runs[k]]
  fig = plt.figure(figsize=(19.2,10.8), dpi=100)                                                                                                                                              
  plt.suptitle(nucleus[0].sup_title) 
  gs = gridspec.GridSpec(2,3,hspace=0.4,wspace=0.3)          
  cols = 3
  for j in range(len(nucleus)): 
   for i in range(len(nucleus[j].energies)):
        row = (i // cols)
        col = i % cols
        ax = fig.add_subplot(gs[row,col]) 
        ax.grid()
        ax.set_title(nucleus[j].titles[i])
        ax.set_xlabel(nucleus[j].time_label)
        ax.set_ylabel(nucleus[j].energy_label)
        ax.plot(nucleus[j].time,nucleus[j].energies[i],label = nucleus[j].plot_aspect.label ,
          				      color = nucleus[j].plot_aspect.color, 
          				      marker = nucleus[j].plot_aspect.marker, 
          				      linestyle = nucleus[j].plot_aspect.linestyle,
         				      markevery = nucleus[j].plot_aspect.markevery)
        if(i ==0) : ax.legend(loc='upper left',bbox_to_anchor=(-0.1,1.35))
    
  

  plt.savefig('output_graphs_python/testing/'+str(runs[0].names[k])+'.png')
  if(k ==6) :
      fig = plt.figure(figsize=(19.2,10.8), dpi=100) 
      plt.suptitle(nucleus[0].sup_title) 
      gs = gridspec.GridSpec(2,3,hspace=0.4,wspace=0.3)          
      cols = 3
      for l in range(len(nucleus[j].tpe)):
	nucleus[1].tmpe[l] = runs[1].runs[1].tpe[l] + nucleus[1].tme[l]
	nucleus[0].tpe[l] = runs[0].runs[0].tpe[l]
      for j in range(len(nucleus)): 
       for i in range(len(nucleus[j].energies)):
            row = (i // cols)
            col = i % cols
            ax = fig.add_subplot(gs[row,col]) 
            ax.grid()
            ax.set_title(nucleus[j].special_titles[i])
            ax.set_xlabel(nucleus[j].time_label)
            ax.set_ylabel(nucleus[j].energy_label)
            ax.plot(nucleus[j].time,nucleus[j].special_energies[i],label = nucleus[j].plot_aspect.label ,
              				      color = nucleus[j].plot_aspect.color, 
              				      marker = nucleus[j].plot_aspect.marker, 
              				      linestyle = nucleus[j].plot_aspect.linestyle,
             				      markevery = nucleus[j].plot_aspect.markevery)
            if(i ==0) : ax.legend(loc='upper left',bbox_to_anchor=(-0.1,1.35))
      plt.savefig('output_graphs_python/testing/'+str(runs[0].special_name)+'.png')

def density_plot(nucleus):
 fig = plt.figure(figsize=(19.2,10.8), dpi=100)
 plt.suptitle(nucleus[0].sup_title) 
 gs = gridspec.GridSpec(1,2)
 cols = 2
 for j in range(len(nucleus)):
   row = (j // cols)
   col = j % cols
   ax = fig.add_subplot(gs[row,col]) 
   ax.grid()
   for i in range(len(nucleus[j].densities)):
     ax.set_ylabel(nucleus[j].density_label)
     ax.set_xlabel(nucleus[j].time_label)
     ax.plot(nucleus[j].time,nucleus[j].densities[i],label = nucleus[j].plot_aspect.dlabel[i] ,
           				      color = nucleus[j].plot_aspect.dcolor[i], 
           				      marker = nucleus[j].plot_aspect.dmarker[i], 
           				      linestyle = nucleus[j].plot_aspect.dlinestyle[i],
  					      markevery = nucleus[j].plot_aspect.dmarkevery[i],
					      mfc = nucleus[j].plot_aspect.dmfc[i],
					      markeredgecolor=nucleus[j].plot_aspect.dmarkeredgecolor[i])
  
     ax.legend(loc='upper left',bbox_to_anchor=(-0.1,1.1))
 plt.savefig('density_test.png')

def wood_saxon(r):
  r = r
  RA = 1.125*197**(1/3)
  a = 0.534
  rho_0=0.1695
  ws_val = rho_0/(1+np.exp((r-RA)/a))

  return ws_val

def plot_density(r,rho,time_values,m_or_s,N):

 fig = plt.figure(figsize=(19.2,10.8), dpi=100)
 ws = []
 r_shift = []
 count = 0
 r_ws = np.arange(-1,10,0.01)
 for i in range(len(r_ws)):
   if(r_ws[i]< 4.3):
     ws.append(wood_saxon(r_ws[0]))
   else:
    count  = count + 1
    ws.append(wood_saxon(r_ws[count]))
#    print(count)
#   r_shift.append(r[i]+5.3)
 if(m_or_s == 'static') : v_color = tableau20[8]
 if(m_or_s == 'momentum') : v_color = tableau20[2]
 plt.plot(r,rho,label='For initial values',marker='o',linestyle='--',color=v_color)
 plt.plot(r_ws,ws,label='Wood saxon',marker='',linestyle='-',linewidth=4,color=tableau20[7])
 plt.xlabel(r'Radius $r(fm)$',fontsize=18)
 for tick in fig.xaxis.get_major_ticks():
  tick.label.set_fontsize(14) 
 plt.ylabel(r'$\rho(r)$ $(fm^{-3})$',fontsize=18)
 for tick in plt.yaxis.get_major_ticks():
  tick.label.set_fontsize(14) 
 if(time_values ==0 ): plt.title(str(m_or_s)+' Initial density distribution for N='+N+',b=20, TIME = 0',fontsize=20)
 if(time_values ==2 ): plt.title(str(m_or_s)+' Density distribution for N='+N+',b=20, TIME = 2',fontsize=20)
 if(time_values ==30 ): plt.title(str(m_or_s)+' Density distribution for N='+N+',b=20, TIME = 30',fontsize=20)
 plt.legend(loc='upper right',fontsize=15)
 if (time_values == 0) : plt.savefig('dens/'+m_or_s+'_ws_plot_0.pdf')
 if (time_values == 2) : plt.savefig('dens/'+m_or_s+'_ws_plot_1.pdf')
 if (time_values == 30) : plt.savefig('dens/'+m_or_s+'_ws_plot_30.pdf')

def import_density_first(fname):
	data = []
	rho = []
	r = []
	data = np.loadtxt(fname)
	print(len(data))
	for i in range(len(data)):
	    r.append(data[i][0])
	    rho.append(data[i][1])

	return r,rho


def sal_plot_rms(runs):
  fig = plt.figure(figsize=(19.2,10.8), dpi=100) 
  SAL = [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00]
#  for k in range(len(runs[0].runs)):
  for k in range(13):
      nucleus = [runs[0].runs[k],runs[1].runs[k]]
      plt.suptitle(nucleus[0].sup_title + "\n" + "FOR TARGET NUCLEUS") 
      gs = gridspec.GridSpec(4,4,hspace=0.4,wspace=0.3)          
      cols = 4
      row = (k // cols)
      col = k % cols
#      print('row {0}'.format(row))
#      print('col {0}'.format(col))
      print('k {0}'.format(k))
      ax = fig.add_subplot(gs[row,col]) 
      ax.grid()
      ax.set_xlabel('Time fm/c')
      ax.set_xlabel('RMS fm')
      for j in range(len(nucleus)):
	ax.set_title('SAL = ' + str(SAL[k]))
	ax.plot(nucleus[j].time,nucleus[j].rms_t,color = nucleus[j].plot_aspect.color,
						 label = nucleus[j].plot_aspect.label,
						 marker = nucleus[j].plot_aspect.marker,
						 linestyle = nucleus[j].plot_aspect.linestyle,
						 markevery = nucleus[j].plot_aspect.markevery)
      if(k ==0) : ax.legend(loc='upper left',bbox_to_anchor=(0,1.5))
  plt.savefig('output_graphs_python/sal/rms.pdf') 


def sal_plot_density(runs):
  fig = plt.figure(figsize=(19.2,10.8), dpi=100) 
  SAL = [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00]
#  for k in range(len(runs[0].runs)):
  for k in range(13):
      nucleus = [runs[0].runs[k],runs[1].runs[k]]
      plt.suptitle(nucleus[0].sup_title + "\n" + "FOR TARGET NUCLEUS") 
      gs = gridspec.GridSpec(4,4,hspace=0.4,wspace=0.3)          
      cols = 4
      row = (k // cols)
      col = k % cols
#      print('row {0}'.format(row))
#      print('col {0}'.format(col))
      print('k {0}'.format(k))
      ax = fig.add_subplot(gs[row,col]) 
      ax.grid()
      ax.set_xlabel('Time fm/c')
      ax.set_xlabel(r'$\rho$ $fm^{-3}$')
      for j in range(len(nucleus)):
	ax.set_title('SAL = ' + str(SAL[k]))
	ax.plot(nucleus[j].time,nucleus[j].rhom_t,color = nucleus[j].plot_aspect.color,
						 label = nucleus[j].plot_aspect.label,
						 marker = nucleus[j].plot_aspect.marker,
						 linestyle = nucleus[j].plot_aspect.linestyle,
						 markevery = nucleus[j].plot_aspect.markevery)
      if(k ==0) : ax.legend(loc='upper left',bbox_to_anchor=(0,1.5))
  plt.savefig('output_graphs_python/sal/density.pdf') 


def sal_plot_rms_alt(runs):
  fig = plt.figure(figsize=(19.2,10.8), dpi=100) 
  SAL = [4.00,4.25,4.50,4.75,5.00,5.25,5.50,5.75,6.00,6.25,6.50,6.75,7.00]
#  for k in range(len(runs[0].runs)):
  for k in range(13):
      nucleus = [runs[0].runs[k],runs[1].runs[k]]
      plt.suptitle(nucleus[0].sup_title + "\n" + "FOR TARGET NUCLEUS RMS ALT") 
      gs = gridspec.GridSpec(4,4,hspace=0.4,wspace=0.3)          
      cols = 4
      row = (k // cols)
      col = k % cols
#      print('row {0}'.format(row))
#      print('col {0}'.format(col))
      print('k {0}'.format(k))
      ax = fig.add_subplot(gs[row,col]) 
      ax.grid()
      ax.set_xlabel('Time fm/c')
      ax.set_xlabel('RMS fm')
      for j in range(len(nucleus)):
	ax.set_title('SAL = ' + str(SAL[k]))
	ax.plot(nucleus[j].time,nucleus[j].rms_t_alt,color = nucleus[j].plot_aspect.color,
						 label = nucleus[j].plot_aspect.label,
						 marker = nucleus[j].plot_aspect.marker,
						 linestyle = nucleus[j].plot_aspect.linestyle,
						 markevery = nucleus[j].plot_aspect.markevery)
      if(k ==0) : ax.legend(loc='upper left',bbox_to_anchor=(0,1.5))
  plt.savefig('output_graphs_python/sal/rms_alt.pdf') 
