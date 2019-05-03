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
from tools.import_methods import *

nnuc = 394.
def plotting_position(time,x,y,z,iso,static):
  rms_p_table= []
  rms_t_table= []
#  for j in range(len(time)):
  for j in range(1):
    print(j)
#    progress(j,len(time),'Generating PNGs')
    position = np.zeros(len(time[j]), dtype=[('x',float,1),
                                             ('y',float,1),
                                             ('z',float,1),
					     ('iso',float,1)])

#    position =  np.dtype([('x',float,len(time[j])),
#                       ('y',float,len(time[j])),
#                       ('z',float,len(time[j])),
#	               ('iso',float,len(time[j]))])

#    print(position)
#    print(len(position))
#    print(len(time[j]))
    for i in range(len(time[j])):
      position['x'][i] = x[j][i]
      position['y'][i] = y[j][i]
      position['z'][i] = z[j][i]
      position['iso'][i] = iso[j][i]
#    print(position)
#    print(len(position))

    particles = np.dtype([('x',float,len(time[j])),
		       ('y',float,len(time[j])),
		       ('z',float,len(time[j]))])


#    particles = np.dtype([('x',float,(len(time[j]),1)),
#			    ('y',float,(len(time[j]),1)),
#			    ('z',float,(len(time[j]),1))])


    single_particle = np.dtype([('x',float,1),
		                ('y',float,1),
		                ('z',float,1)])
                                   
    center = np.zeros(1,dtype = [('target',single_particle),
                                 ('projectile',single_particle)])
                                  
    target = np.zeros(1,dtype = [('neutron',particles),
        		         ('proton',particles)])

    projectile = np.zeros(1,dtype = [('neutron',particles),
		                     ('proton',particles)])

#    center = np.dtype([('target',single_particle),
#	               ('projectile',single_particle)])
#                                  
#    target = np.dtype([('neutron',particles),
#		       ('proton',particles)])
#
#    projectile = np.dtype([('neutron',particles),
#		        ('proton',particles)])

    time_rho = []
    rho_t = []
    rho_p = []

    PNTP_seperation(time,position,target,projectile)
    rms_t,rms_p =calculate_rms(time,center,position) 
    if(j != 0) : rms_t_table.append(rms_t)
    if(j != 0) :rms_p_table.append(rms_p)

    for i in range(j):
      time_rho.append(static[0][0][i])
      rho_t.append(static[0][7][i])
      rho_p.append(static[0][8][i])
#    print('TARGET NEUTRON X LEN : ')
#    print(target['neutron']['x'][0][0])
#    print(len(target['neutron']['x'][0]))
#    print(len(target['neutron']['y'][0]))
#    print(target['neutron']['z'][0][0])
########################################PLOTTING PART
    fig = plt.figure(j,figsize=(10.8,7.2), dpi=100)
    gs = gridspec.GridSpec(5,5,hspace=1)
    gs_target = gridspec.GridSpec(5,5,hspace=0)
    gs_projectile = gridspec.GridSpec(5,5,hspace=0)

    ax = fig.add_subplot(gs[:,:-1],projection='3d')
    sphere_t = ax.plot_wireframe(*sphere_on_center([center['target']['x'],
						    center['target']['y'],
						    center['target']['z']],rms_t), edgecolor="orange", alpha=0.2,linewidth=2)
#    print(target['neutron']['x'][0])
    target_n = ax.plot(target['neutron']['x'][0],
		       target['neutron']['y'][0],
		       target['neutron']['z'][0],color='red',linestyle='',marker='*',markersize=5,markeredgecolor='none',alpha=0.7,label='Target Neutron')
    target_p = ax.plot(target['proton']['x'][0],
		       target['proton']['y'][0],
		       target['proton']['z'][0],color='orange',linestyle='',marker='o',markersize=5,markeredgecolor='none',alpha=0.7,label='Target Proton')
    sphere_p = ax.plot_wireframe(*sphere_on_center([center['projectile']['x'],
						    center['projectile']['y'],
						    center['projectile']['z']],rms_p), edgecolor="purple", alpha=0.2)
    projectile_n = ax.plot(projectile['neutron']['x'][0],
			   projectile['neutron']['y'][0],
			   projectile['neutron']['z'][0],color='magenta',linestyle='',marker='*',markersize=5,markeredgecolor='none',alpha=0.7,label='Projectile Neutron')
    projectile_p = ax.plot(projectile['proton']['x'][0],
			   projectile['proton']['y'][0],
			   projectile['proton']['z'][0],color='purple',linestyle='',marker='o',markersize=5,markeredgecolor='none',alpha=0.7,label='Projectile Proton')
    ax.legend(loc='upper left')
    ax.view_init(14,78)
    ax.set_xlim3d(-30,30)
    ax.set_ylim3d(-30,30)
    ax.set_zlim3d(-30,30)


    ax2 = fig.add_subplot(gs_target[0,4]) 
    ax2.set_ylabel(r'$\rho (fm^{-3})$')
    ax2.set_xlim(0,120)
    ax2.set_ylim(0.08,0.2)
    ax2.grid()
    plt.tick_params(axis='x',bottom=False,labelbottom=False) 
    plot_rho_t = ax2.plot(time_rho,rho_p,color='orange',label='Target')
    ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=7)


    ax5 = fig.add_subplot(gs_target[1,4]) 
    ax5.set_xlabel('time step (fm)')
    ax5.set_ylabel(r'$rms (fm)$')
    ax5.set_xlim(0,120)
    ax5.set_ylim(6,14)
    ax5.grid()
    plt.tick_params(axis='x',bottom=False,labelbottom=False) 
    plot_rms_t = ax5.plot(time_rho,rms_t_table,color='orange')

    ax3 = fig.add_subplot(gs_projectile[2,4]) 
    ax3.set_ylabel(r'$\rho (fm^{-3})$')
    ax3.set_xlim(0,120)
    ax3.set_ylim(0.08,0.2)
    ax3.grid()
    plt.tick_params(axis='x',bottom=False,labelbottom=False) 
    plot_rho_p = ax3.plot(time_rho,rho_p,color ='purple',label='Projectile')
    ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=7)


    plt.tick_params(axis='x',bottom=True,labelbottom=False) 
    ax4 = fig.add_subplot(gs_projectile[3,4]) 
    ax4.set_xlabel('time step (fm)')
    ax4.set_ylabel(r'$rms (fm)$')
    ax4.set_xlim(0,120)
    ax4.set_ylim(6,14)
    ax4.grid()
    plot_rms_p = ax4.plot(time_rho,rms_p_table,color='purple',label='Projectile')

    fig.suptitle('T= '+  str(round(time[j][0],2)))
    if(j %10 ==0) : plt.savefig('output_graphs_python/position/position00'+str(j)+'.png')
    plt.close()




def sphere_on_center(centre_s,radius):
         u, v = np.mgrid[0:2*np.pi:10*1j, 0:np.pi:10*1j]
         sphere_x = centre_s[0] + radius * np.cos(u) * np.sin(v)
	 sphere_y = centre_s[1] + radius * np.sin(u) * np.sin(v)
	 sphere_z = centre_s[2] + radius * np.cos(v)
	 return sphere_x, sphere_y, sphere_z


def progress(count, total, status=''):
      bar_len = 60
      filled_len = int(round(bar_len * count / float(total)))
      percents = round(100.0 * count / float(total), 1)
      bar = '#' * filled_len + '-' * (bar_len - filled_len)

      sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))
      sys.stdout.flush()



def calculate_center(time,position,center):
      for i in range(int(nnuc)):
	if(i <= 196):
#	  if(i==0) :print(position['x'][i])
	  center['target']['x'] += position['x'][i]
	  center['target']['y'] += position['y'][i]
	  center['target']['z'] += position['z'][i]
#	  print('xm {0} then xi {1}'.format(center['target']['x'],position['x'][i]))
	else:
	  center['projectile']['x'] += position['x'][i]
	  center['projectile']['y'] += position['y'][i]
	  center['projectile']['z'] += position['z'][i]

      center['target']['x'] /=float(nnuc*0.5)
      center['target']['y'] /=float(nnuc*0.5)
      center['target']['z'] /=float(nnuc*0.5)

      center['projectile']['x'] /=float(nnuc*0.5)
      center['projectile']['y'] /=float(nnuc*0.5)
      center['projectile']['z'] /=float(nnuc*0.5)

def PNTP_seperation(time,position,target,projectile):
    tn_counter = 0
    tp_counter = 0
    pn_counter = 0
    pp_counter = 0
    xt_n = []
    yt_n = []
    zt_n = []

    xt_p = []
    yt_p = []
    zt_p = []
    xp_n = []
    yp_n = []
    zp_n = []

    xp_p = []
    yp_p = []
    zp_p = []
    for i in range(int(nnuc)):
	if(i <= 196) :
	  if(position['iso'][i] == 0) :
	    tn_counter += 1
	    xt_n.append(position['x'][i])
	    yt_n.append(position['y'][i])
	    zt_n.append(position['z'][i])
	  else :
	    tp_counter +=1
	    xt_p.append(position['x'][i])
	    yt_p.append(position['y'][i])
	    zt_p.append(position['z'][i])
	else:
	  if(position['iso'][i] ==0) :
	    pn_counter +=1
	    xp_n.append(position['x'][i])
	    yp_n.append(position['y'][i])
	    zp_n.append(position['z'][i])
	  else:
	    pp_counter +=1
	    xp_p.append(position['x'][i])
	    yp_p.append(position['y'][i])
	    zp_p.append(position['z'][i])
      
    rt = [[xt_n,yt_n,zt_n],[xt_p,yt_p,zt_p]]
    rp = [[xp_n,yp_n,zp_n],[xp_p,yp_p,zp_p]]
    return rt,rp,tn_counter,tp_counter,pn_counter,pp_counter
def calculate_rms(time,center,position):

    calculate_center(time,position,center)
#    print(center['target']['x'])
#    print(center['target']['y'])
#    print(center['target']['z'])
    rms_t = 0.
    rms_p = 0.
    for i in range(int(nnuc)):
      if(i <= 196):
       rms_t += np.array((position['x'][i]-center['target']['x'])**2
       +(position['y'][i]-center['target']['y'])**2
       +(position['z'][i]-center['target']['z'])**2,dtype=float)
      if(i>196) :
       rms_p += np.array((position['x'][i]-center['projectile']['x'])**2
       +(position['y'][i]-center['projectile']['y'])**2
       +(position['z'][i]-center['projectile']['z'])**2,dtype=float)
     
    rms_t = 5./3.*np.sqrt(rms_t/nnuc)
    rms_p = 5./3.*np.sqrt(rms_p/nnuc)
    return rms_t,rms_p
