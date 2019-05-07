import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.animation as animation
import matplotlib as mpl
mpl.use('Agg')
print mpl.__version__
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import axes3d, Axes3D
from tools.import_methods import *
from tools.nuclei import *
nnuc = 394.
def plotting_position(time,x,y,z,iso,static):
  rms_p_table= []
  rms_t_table= []
  rotation_addition = 50
#  for j in range(len(time)):
  for j in tqdm(range(len(time)),desc='Generating PNGs'):
#  for j in range(20):
#    print(j)
#    progress(j,len(time),'Generating PNGs')
                                  

    time_rho = []
    rho_t = []
    rho_p = []
    target = nuclei() 
    projectile = nuclei()
    attribution(j,x,y,z,iso,target,projectile)
    target.calc_center()
    target.calc_rms()
    projectile.calc_center()
    projectile.calc_rms()
    if(j != 0) : rms_t_table.append(target.rms)
    if(j != 0) :rms_p_table.append(projectile.rms)

    for i in range(j):
      time_rho.append(static[0][0][i])
      rho_t.append(static[0][7][i])
      rho_p.append(static[0][8][i])

    if(j %10 ==0) : 
########################################PLOTTING PART
      fig = plt.figure(j,figsize=(10.8,7.2), dpi=100)
      gs = gridspec.GridSpec(5,5,hspace=1)
      gs_target = gridspec.GridSpec(5,5,hspace=0)
      gs_projectile = gridspec.GridSpec(5,5,hspace=0)

      ax = fig.add_subplot(gs[:,:-1],projection='3d')
      if (time[j][0] <= 41):
        sphere_t = ax.plot_wireframe(*sphere_on_center([target.xc,
          					      target.yc,
          					      target.zc],target.rms), edgecolor="orange", alpha=0.2,linewidth=2)
      else:
        alpha_value = 0.2/(float(time[j][0]-40.)*0.4)
        if(alpha_value < 0.05): alpha_value = 0.0
        sphere_t = ax.plot_wireframe(*sphere_on_center([target.xc,
          					      target.yc,
          					      target.zc],target.rms), edgecolor="orange", alpha=alpha_value,linewidth=2)
      target_n = ax.plot(target.neutrons.x,
          	       target.neutrons.y,
          	       target.neutrons.z,color='red',linestyle='',marker='*',markersize=5,markeredgecolor='none',alpha=0.7,label='Target Neutron')
      target_p = ax.plot(target.protons.x,
          	       target.protons.y,
          	       target.protons.z,color='orange',linestyle='',marker='o',markersize=5,markeredgecolor='none',alpha=0.7,label='Target Proton')

      if (time[j][0] <= 41):
        sphere_p = ax.plot_wireframe(*sphere_on_center([projectile.xc,
          					      projectile.yc,
          					      projectile.zc],projectile.rms), edgecolor="purple", alpha=0.2)
      else:
        sphere_p = ax.plot_wireframe(*sphere_on_center([projectile.xc,
          					      projectile.yc,
          					      projectile.zc],projectile.rms), edgecolor="purple", alpha=alpha_value)
      projectile_n = ax.plot(projectile.neutrons.x,
          		   projectile.neutrons.y,
          		   projectile.neutrons.z,color='magenta',linestyle='',marker='*',markersize=5,markeredgecolor='none',alpha=0.7,label='Projectile Neutron')
      projectile_p = ax.plot(projectile.protons.x,
          		   projectile.protons.y,
          		   projectile.protons.z,color='purple',linestyle='',marker='o',markersize=5,markeredgecolor='none',alpha=0.7,label='Projectile Proton')

      ax.legend(loc='upper left')
      ax.view_init(14,78)
      ax.set_xlim3d(-30,30)
      ax.set_ylim3d(-30,30)
      ax.set_zlim3d(-30,30)

      end_time = 160
      ax2 = fig.add_subplot(gs_target[0,4]) 
      ax2.set_ylabel(r'$\rho (fm^{-3})$')
      ax2.set_xlim(0,end_time)
      ax2.set_yscale('log')
      ax2.grid()
      plt.tick_params(axis='x',bottom=False,labelbottom=False) 
      plot_rho_t = ax2.plot(time_rho,rho_p,color='orange',label='Target')
      ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=7)


      ax5 = fig.add_subplot(gs_target[1,4]) 
      ax5.set_xlabel('time step (fm)')
      ax5.set_ylabel(r'$rms (fm)$')
      ax5.set_xlim(0,end_time)
      ax5.set_yscale('log')
      ax5.grid()
      plt.tick_params(axis='x',bottom=False,labelbottom=False) 
      plot_rms_t = ax5.plot(time_rho,rms_t_table,color='orange')

      ax3 = fig.add_subplot(gs_projectile[2,4]) 
      ax3.set_ylabel(r'$\rho (fm^{-3})$')
      ax3.set_xlim(0,end_time)
      ax3.set_yscale('log')
      ax3.grid()
      plt.tick_params(axis='x',bottom=False,labelbottom=False) 
      plot_rho_p = ax3.plot(time_rho,rho_p,color ='purple',label='Projectile')
      ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=7)


      plt.tick_params(axis='x',bottom=True,labelbottom=False) 
      ax4 = fig.add_subplot(gs_projectile[3,4]) 
      ax4.set_xlabel('time step (fm)')
      ax4.set_ylabel(r'$rms (fm)$')
      ax4.set_xlim(0,end_time)
      ax4.set_yscale('log')
      ax4.grid()
      plot_rms_p = ax4.plot(time_rho,rms_p_table,color='purple',label='Projectile')

      fig.suptitle('T= '+  str(round(time[j][0],2)))
      stop_time = 120
      if(j <stop_time )  : plt.savefig('../animation_out/position/position00'+str(j)+'.png')
      if( j == stop_time) :
          for i in tqdm(range(5),desc='Dramatic Pause'):
         	plt.savefig('../animation_out/position/position00'+str(j+i)+'.png')
		ax_w_b = ax.w_zaxis.line.get_lw()
		ax_tcks_b = ax.get_zticks()
          for i in tqdm(range(10,rotation_addition),desc='Rotating PNGs'):
		ax.w_zaxis.line.set_lw(0.)
		ax.set_zticks([])
          	ax.set_xlim3d(-30,30)
      		ax.set_ylim3d(-30,30)
      		ax.set_zlim3d(-30,30)
                ax.view_init(14,78+9*i)
                plt.savefig('../animation_out/position/position00'+str(j+i)+'.png')
	  ax.w_zaxis.line.set_lw(ax_w_b)
	  ax.set_zticks(ax_tcks_b)
      if(j>stop_time) :  plt.savefig('../animation_out/position/position00'+str(j+rotation_addition)+'.png')
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



def attribution(j,x,y,z,iso,target,projectile):
    for i in range(int(target.nucleons)):
        if(i <= 196):
            if(iso[j][i] == 0) :
                target.neutrons.x.append(x[j][i]) 
                target.neutrons.y.append(y[j][i]) 
                target.neutrons.z.append(z[j][i]) 
            else : 
                target.protons.x.append(x[j][i]) 
                target.protons.y.append(y[j][i]) 
                target.protons.z.append(z[j][i]) 
        else:
            if(iso[j][i] == 0) :
                projectile.neutrons.x.append(x[j][i]) 
                projectile.neutrons.y.append(y[j][i]) 
                projectile.neutrons.z.append(z[j][i]) 
            else : 
                projectile.protons.x.append(x[j][i]) 
                projectile.protons.y.append(y[j][i]) 
                projectile.protons.z.append(z[j][i]) 
