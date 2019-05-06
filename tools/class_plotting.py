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
 fig = plt.figure(figsize=(10.8,7.2), dpi=100)                                                                                                                                              
 plt.suptitle(nucleus.sup_title) 
 gs = gridspec.GridSpec(2,3)          
 cols = 3
 
 for i in range(len(nucleus.energies)):
      row = (i // cols)
      col = i % cols
      ax = fig.add_subplot(gs[row,col]) 
      ax.grid()
      ax.set_xlabel(nucleus.time_label)
      ax.set_ylabel(nucleus.energy_label)
      ax.plot(nucleus.time,nucleus.energies[i],label = nucleus.plot_aspect.label ,
					      color = nucleus.plot_aspect.color, 
					      marker = nucleus.plot_aspect.marker, 
					      linestyle = nucleus.plot_aspect.linestyle)
 plt.savefig('test.png')
