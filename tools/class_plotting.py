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


def energy_plot(nucleus):
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

 plt.savefig('energy_test.png')


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
