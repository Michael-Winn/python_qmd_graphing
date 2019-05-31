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
    
  

  plt.savefig('output_graphs_python/testing/impact_b/'+str(runs[0].names[k])+'_'+str(nucleus[j].impact_para)+'.png')
#  if(k ==6) :
#      fig = plt.figure(figsize=(19.2,10.8), dpi=100) 
#      plt.suptitle(nucleus[0].sup_title) 
#      gs = gridspec.GridSpec(2,3,hspace=0.4,wspace=0.3)          
#      cols = 3
#      for l in range(len(nucleus[j].tpe)):
#	nucleus[1].tmpe[l] = runs[1].runs[1].tpe[l] + nucleus[1].tme[l]
#	nucleus[0].tpe[l] = runs[0].runs[1].tpe[l]
#	nucleus[0].te[l] = runs[0].runs[1].te[l]
#      for j in range(len(nucleus)): 
#       for i in range(len(nucleus[j].energies)):
#            row = (i // cols)
#            col = i % cols
#            ax = fig.add_subplot(gs[row,col]) 
#            ax.grid()
#            ax.set_title(nucleus[j].special_titles[i])
#            ax.set_xlabel(nucleus[j].time_label)
#            ax.set_ylabel(nucleus[j].energy_label)
#	    if(j ==1) :
#	      ax.plot(nucleus[j].time,nucleus[j].special_energies[i],label = nucleus[j].plot_aspect.label ,
#                				      color = nucleus[j].plot_aspect.color, 
#                				      marker = nucleus[j].plot_aspect.marker, 
#                				      linestyle = nucleus[j].plot_aspect.linestyle,
#               				              markevery = nucleus[j].plot_aspect.markevery)
#	    if(j ==0) :
#	      ax.plot(nucleus[j].time,nucleus[j].energies[i],label = nucleus[j].plot_aspect.label ,
#                				      color = nucleus[j].plot_aspect.color, 
#                				      marker = nucleus[j].plot_aspect.marker, 
#                				      linestyle = nucleus[j].plot_aspect.linestyle,
#               				              markevery = nucleus[j].plot_aspect.markevery)
#            if(i ==0) : ax.legend(loc='upper left',bbox_to_anchor=(-0.1,1.35))
#      plt.savefig('output_graphs_python/testing/'+str(runs[0].special_name)+'.png')

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
 if(m_or_s == 'static soft') : v_color = tableau20[8]
 if(m_or_s == 'static hard') : v_color = tableau20[12]
 if(m_or_s == 'momentum') : v_color = tableau20[2]
 plt.plot(r,rho,label='For initial values',marker='o',linestyle='--',color=v_color)
 plt.plot(r_ws,ws,label='Wood saxon',marker='',linestyle='-',linewidth=4,color=tableau20[7])
 plt.xlabel(r'Radius $r(fm)$',fontsize=18)
# for tick in fig.xaxis.get_major_ticks():
#  tick.label.set_fontsize(14) 
 plt.ylabel(r'$\rho(r)$ $(fm^{-3})$',fontsize=18)
# for tick in plt.yaxis.get_major_ticks():
#  tick.label.set_fontsize(14) 
 if(time_values ==0 ): plt.title(str(m_or_s)+' Initial density distribution for N='+N+',b=20, TIME = 0',fontsize=20)
 if(time_values ==40 ): plt.title(str(m_or_s)+' Density distribution for N='+N+',b=20, TIME = 40',fontsize=20)
 if(time_values ==80 ): plt.title(str(m_or_s)+' Density distribution for N='+N+',b=20, TIME = 80',fontsize=20)
 plt.legend(loc='upper right',fontsize=15)
 if (time_values == 0) : plt.savefig('dens/'+m_or_s+'_ws_plot_0.pdf')
 if (time_values == 40) : plt.savefig('dens/'+m_or_s+'_ws_plot_40.pdf')
 if (time_values == 80) : plt.savefig('dens/'+m_or_s+'_ws_plot_80.pdf')




def plot_density_sub(r,rho,time_values,m_or_s,N,sal):
 fig = plt.figure(figsize=(19.2,10.8), dpi=100)
 gs = gridspec.GridSpec(1,3,hspace=0.4,wspace=0.3)          
 cols = 3
 ws = []
 r_shift = []
 count = 0
 r_ws = np.arange(-1,10,0.01)
 marker = ['o','o','o','s','s','s']
 for i in range(len(r_ws)):
   if(r_ws[i]< 4.3):
     ws.append(wood_saxon(r_ws[0]))
   else:
    count  = count + 1
    ws.append(wood_saxon(r_ws[count]))
 for i in range(len(r)):
   row =0
#   col = i % cols
   print(i)
   if( i == 0 or i == 3 ) : col = 0
   if( i == 1 or i == 4 ) : col = 1
   if( i == 2 or i == 5 ) : col = 2
   ax = fig.add_subplot(gs[row,col]) 
   print(' Type : {0} , place {1}, SAL {2}'.format(m_or_s,col,sal))
   if(m_or_s == 'static soft' and sal[i] == '5.25') : v_color = tableau20[8]
   if(m_or_s == 'static soft' and sal[i] == '6.25') : v_color = tableau20[9]
   if(m_or_s == 'static hard' and sal[i] == '5.25') : v_color = tableau20[12]
   if(m_or_s == 'static hard' and sal[i] == '6.25') : v_color = tableau20[13]
   if(m_or_s == 'momentum' and sal[i] == '5.00') : v_color = tableau20[2]
   if(m_or_s == 'momentum' and sal[i] == '6.25') : v_color = tableau20[3]
#   ax.plot(r[i],rho[i],label=r'$\rho(r)$ SAL = ' + sal[i],marker=marker[i],linestyle='',color=v_color,markevery = 5)
   ax.plot(r[i],rho[i],label=r'$\rho(r)$ SAL = ' + sal[i],marker=marker[i],linestyle='',color=v_color)
   if(i %2 != 0 ) : ax.plot(r_ws,ws,label='Wood saxon',marker='',linestyle='-',linewidth=4,color=tableau20[7])
#   if(i == 0 ) : ax.plot(r_ws,ws,label='Wood saxon',marker='',linestyle='-',linewidth=4,color=tableau20[7])
   ax.set_ylim(0,0.6)
   ax.set_xlabel(r'Radius $r(fm)$',fontsize=18)
   ax.set_ylabel(r'$\rho(r)$ $(fm^{-3})$',fontsize=18)
   ax.set_title("Time = " + str(time_values[i]))
   ax.legend(loc='upper right',fontsize=15)
 plt.suptitle(str(m_or_s)+' Density distribution for N='+N+',b=20',fontsize=20)
 plt.savefig('dens/'+m_or_s+'_ws_plot_'+str(time_values)+'.pdf')





def import_density_alone(fname):
	data = []
	rho = []
	data = np.loadtxt(fname)
#	print(len(data))
#	for i in range(len(data)):
#	    rho.append(data[0][0])
	rho = data
#	print(rho)
	return rho




def import_density_first(fname):
	data = []
	rho = []
	r = []
	data = np.loadtxt(fname)
#	print(len(data))
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





def plot_density_histo_old(rho,m_or_s):
    print("CHANGE RHO 0 VALUE ")
    rho_0 = 1.0
    rho_first_sal = []
    rho_second_sal = []
    fig = plt.figure(figsize=(19.2,10.8), dpi=100) 
    cols = 3
    gs = gridspec.GridSpec(1,3,hspace=0.4,wspace=0.3)          
#    SAL = [5.25,5.25,5.25,6.25,6.25,6.25]*10
    print(SAL)
    time = [0,40,80]*20
    name = ["SAL = 5.25","SAL = 5.25 ","SAL = 5.25","SAL = 6.25","SAL = 6.25","SAL = 6.25"]*10
    handles = []
    if(m_or_s == 'static soft') : v_color = [tableau20[0],tableau20[0],tableau20[0],tableau20[9],tableau20[9],tableau20[9]]*10 
    if(m_or_s == 'static hard') : v_color = [tableau20[3],tableau20[3],tableau20[3],tableau20[13],tableau20[13],tableau20[13]]*10 
    if(m_or_s == 'momentum') : v_color = [tableau20[5],tableau20[5],tableau20[5],tableau20[19],tableau20[19],tableau20[19]]*10 
    for i in range(120):
      if(i<60):
	rho_first_sal.append(rho[i]*0.17)
      if(i>= 60):
	rho_second_sal.append(rho[i]*0.17)
    count = 0
    for i in range(60):
      if(count ==0) : 
	col = 0
	count = count +1
	print(count)
      elif(count ==1) : 
	col = 1
	count = count +1
	print(count)
      else:
	col = 2
	count = 0
	print(count)
      row = 0
      ax = fig.add_subplot(gs[row,col]) 
#     if( i < 3 ) : ax.hist(rho[i],bins=100,alpha=0.3,edgecolor=v_color[i])
      ax.hist(rho[i],bins=25,alpha=0.7,edgecolor=v_color[i],color = v_color[i],label = name[i])
#     if(i >= 3 ) : ax.hist(rho[i],bins=100,alpha=0.3,fc = 'none',edgecolor=v_color[i])
#     ax.set_xlabel(r'$\rho / \rho_0$')
      ax.set_xlabel(r'$\rho / \rho_0$')
      ax.set_ylabel('number')
      ax.set_title("Time  = " + str(time[i]))
#    plt.legend(["sal_1_0","sal_2_0"],['SAL = 5.25','SAL = 6.25'],loc="upper right")
    plt.legend(loc="upper right")
    if(m_or_s == 'static soft' ) :plt.suptitle("Num = 5 ,  b = 20.00 , E = 0.6 Mev, STATIC SOFT")
    if(m_or_s == 'static hard' ) : plt.suptitle("Num = 5 ,  b = 20.00 , E = 0.6 Mev, STATIC hard")
    if(m_or_s == 'momentum') : plt.suptitle("Num = 5 ,  b = 20.00 , E = 0.6 Mev, momentum SOFT")
    if(m_or_s == 'static soft' ) : plt.savefig('output/static_soft_sal_rho_histo.png')
    if(m_or_s == 'static hard' ) : plt.savefig('output/static_hard_sal_rho_histo.png')
    if(m_or_s == 'momentum' ) : plt.savefig('output/momentum_sal_rho_histo.png')

def plot_density_histo(rho_0,rho_40,rho_80,m_or_s):
#    print("CHANGE RHO 0 VALUE 0.17 ")
    from matplotlib.ticker import PercentFormatter
    temp = []
    fact_rho_0 = 0.168
    rho_fh_sal = []
    rho_sh_sal = []

    fig = plt.figure(figsize=(19.2,10.8), dpi=100) 
    cols = 3
    gs = gridspec.GridSpec(1,3,hspace=0.4,wspace=0.3)          
    SAL = [5.25,5.25,5.25,6.25,6.25,6.25]*100
#    print(SAL)
    time = [0,40,80]*100
    name = ["SAL = 5.25","SAL = 5.25 ","SAL = 5.25","SAL = 6.25","SAL = 6.25","SAL = 6.25"]*100
    handles = []
    if(m_or_s == 'static soft') : v_color = [tableau20[0],tableau20[0],tableau20[0],tableau20[9],tableau20[9],tableau20[9]]*100 
    if(m_or_s == 'static hard') : v_color = [tableau20[3],tableau20[3],tableau20[3],tableau20[13],tableau20[13],tableau20[13]]*100 
    if(m_or_s == 'momentum') : v_color = [tableau20[5],tableau20[5],tableau20[5],tableau20[19],tableau20[19],tableau20[19]]*100 
    temp_1_f = []
    temp_2_f = []
    temp_3_f = []

    temp_1_s = []
    temp_2_s = []
    temp_3_s = []

    for i in range(len(rho_0)):
      if(i<len(rho_0)/2):
#	print("HERE")
#	print(len(rho_0[i]))
	for j in range(len(rho_0[i])):
	    temp_1_f.append(rho_0[i][j]*fact_rho_0)

	for j in range(len(rho_40[i])):
	    temp_2_f.append(rho_40[i][j]*fact_rho_0)

	for j in range(len(rho_80[i])):
	    temp_3_f.append(rho_80[i][j]*fact_rho_0)
      if(i>= len(rho_0)/2):
	for j in range(len(rho_0[i])):
	    temp_1_s.append(rho_0[i][j]*fact_rho_0)

	for j in range(len(rho_40[i])):
	    temp_2_s.append(rho_40[i][j]*fact_rho_0)

	for j in range(len(rho_80[i])):
	    temp_3_s.append(rho_80[i][j]*fact_rho_0)

    rho_fh_sal = [temp_1_f,temp_2_f,temp_3_f]
    rho_sh_sal = [temp_1_s,temp_2_s,temp_3_s]

#    print("************************************************************")
#    print("Lenght of rho_fh_sal[0] {0}".format(len(rho_fh_sal[0])))
#    print("Lenght of rho_fh_sal[1] {0}".format(len(rho_fh_sal[1])))
#    print("Lenght of rho_fh_sal[2] {0}".format(len(rho_fh_sal[2])))
#    print("************************************************************")
#    print("Lenght of rho_sh_sal[0] {0}".format(len(rho_sh_sal[0])))
#    print("Lenght of rho_sh_sal[1] {0}".format(len(rho_sh_sal[1])))
#    print("Lenght of rho_sh_sal[2] {0}".format(len(rho_sh_sal[2])))
#    print("************************************************************")

    print('State : {0} , value sal 1 : {1}, value sal 2 {2}'.format(m_or_s,rho_fh_sal[0][50],rho_sh_sal[0][50]))
    count = 0
    for i in range(6):
      if(count ==0) : 
	col = 0
	count = count +1
#	print(count)
      elif(count ==1) : 
	col = 1
	count = count +1
#	print(count)
      else:
	col = 2
	count = 0
#	print(count)
      row = 0
      ax = fig.add_subplot(gs[row,col]) 
#     if( i < 3 ) : ax.hist(rho[i],bins=100,alpha=0.3,edgecolor=v_color[i])
      if(i < 3) : ax.hist(rho_fh_sal[col],bins=25,alpha=0.7,edgecolor=v_color[i],color = v_color[i],label = name[i],weights=np.ones(len(rho_fh_sal[col])) / len(rho_fh_sal[col]))
      if(i >= 3) : ax.hist(rho_sh_sal[col],bins=25,alpha=0.7,edgecolor=v_color[i],color = v_color[i],label = name[i],weights=np.ones(len(rho_sh_sal[col])) / len(rho_sh_sal[col]))
      plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
#     if(i >= 3 ) : ax.hist(rho[i],bins=100,alpha=0.3,fc = 'none',edgecolor=v_color[i])
#     ax.set_xlabel(r'$\rho / \rho_0$')
      ax.set_xlabel(r'$\rho / \rho_0$')
      ax.set_ylabel('Percentage of total number of denisties N = ' + str(len(rho_fh_sal[0]))+' = 20*394')
      ax.set_title("Time  = " + str(time[i]))
      ax.set_ylim(0,0.10)
      ax.set_xlim(0,1.8)
#    plt.legend(["sal_1_0","sal_2_0"],['SAL = 5.25','SAL = 6.25'],loc="upper right")
    plt.legend(loc="upper right")
    if(m_or_s == 'static soft' ) :plt.suptitle("Runs = 20, Num = 1 ,  b = 20.00 , E = 0.6 Mev, STATIC SOFT")
    if(m_or_s == 'static hard' ) : plt.suptitle("Runs = 20, Num = 1 ,  b = 20.00 , E = 0.6 Mev, STATIC hard")
    if(m_or_s == 'momentum') : plt.suptitle("Runs = 20, Num = 1 ,  b = 20.00 , E = 0.6 Mev, momentum SOFT")
    if(m_or_s == 'static soft' ) : plt.savefig('output/static_soft_sal_rho_histo.pdf')
    if(m_or_s == 'static hard' ) : plt.savefig('output/static_hard_sal_rho_histo.pdf')
    if(m_or_s == 'momentum' ) : plt.savefig('output/momentum_sal_rho_histo.pdf')

