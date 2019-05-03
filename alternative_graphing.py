import plotly.offline
from plotly import tools
import plotly.graph_objs as go 
import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
#import matplotlib.pyplot as plt
#Made modules import
from tools.function_with_time import *
from tools.graph_names import *
from tools.output_methods import *
############################################################KEY

#time = the timestep of the for of lenght the energy [0]
#tse = total system energy [1]
#tpe  = total potential energy [2]
#tke = total kinetic energy [3]
#tce = total coulomb energy [4]
#tme = total momentum energy [5]
#tae = total system asymetry energy [6]

########################################################### COMMON VARIABLES
current_working_dir = '../altered_version_v11'
static_dir_nb = 1
momentum_dir_nb = 2
number_of_files_to_import =1
static = []
momentum = []
############# STATIC [0]  OR MOMENTUM [1] OF BOTH [2]
wtp =2
########################################################### PLOTTING LEGEND ARGUMENTS
plot_info_static = []
plot_info_momentum = []
plot_info_density_static = []
plot_info_density_momentum = []
plot_info_rms_static = []
plot_info_rms_momentum = []
plot_info_old = []
plot_info_new = []

plot_info_static = graph_settings_static(number_of_files_to_import*number_of_files_to_import)
plot_info_momentum = graph_settings_momentum(number_of_files_to_import*number_of_files_to_import)
plot_info_density_static = graph_settings_density_static()
plot_info_density_momentum = graph_settings_density_momentum()
plot_info_rms_static = graph_settings_rms_static()
plot_info_rms_momentum = graph_settings_rms_momentum()

plot_info_old = graph_settings_momentum_comparing_old(number_of_files_to_import)
plot_info_new = graph_settings_momentum_comparing_new(number_of_files_to_import)
###########################################################  IMPORTS
if(wtp==0) : print('WTP = {0}, so only static values will be plotted'.format(wtp))
if(wtp==1) : print('WTP = {0}, so only momentum values will be plotted'.format(wtp))
if(wtp==2) : print('WTP = {0}, momentum and static values will be plotted'.format(wtp))
for i in range(number_of_files_to_import) :
#STATIC IMPORT
    if(wtp ==0 or wtp ==2) :
        if(i==0) : print('STATIC import files they number : {0}'.format(number_of_files_to_import))
	static_dir = current_working_dir + '/xxx'+str(static_dir_nb)+'/xxx'+str(static_dir_nb)+'-'+str(i)+'/xxx1-'+str(i)+'-5.25/prop_out_'+str(i)+'.dat'
    	time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(static_dir)
    	static.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])
#MOMENTUM IMPORT
for i in range(number_of_files_to_import) :
    if(wtp ==1 or wtp ==2) :
        if(i==0) : print('MOMENTUM import files they number : {0}'.format(number_of_files_to_import))
	momentum_dir = current_working_dir + '/xxx'+str(momentum_dir_nb)+'/xxx'+str(momentum_dir_nb)+'-'+str(i)+'/xxx2-'+str(i)+'-5.25/prop_out_'+str(i)+'.dat'
    	time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p = import_energies(momentum_dir)
    	momentum.append([time,tse,tpe,tke,tce,tme,tae,rhom_t,rhom_p,rms_t,rms_p])


tse_s = go.Scatter(
    x = static[0][0],
    y = static[0][1],
    name = 'Static',
    line = dict(color = ('rgb(148,103,189)')))

tsp_s = go.Scatter(
    x = static[0][0],
    y = static[0][2],
    showlegend=False,
    line = dict(color = ('rgb(148,103,189)')))

tsk_s = go.Scatter(
    x = static[0][0],
    y = static[0][3],
    showlegend=False,
    line = dict(color = ('rgb(148,103,189)')))

tsc_s = go.Scatter(
    x = static[0][0],
    y = static[0][4],
    showlegend=False,
    line = dict(color = ('rgb(148,103,189)')))

tsm_s = go.Scatter(
    x = static[0][0],
    y = static[0][5],
    showlegend=False,
    line = dict(color = ('rgb(148,103,189)')))

tsa_s = go.Scatter(
    x = static[0][0],
    y = static[0][6],
    showlegend=False,
    line = dict(color = ('rgb(148,103,189)')))

tse_m = go.Scatter(
    x = momentum[0][0],
    y = momentum[0][1],
    name = 'Momentum',
    mode = 'markers',
    line = dict(color = ('rgb(255,193,86)')))

tsp_m = go.Scatter(
    x = momentum[0][0],
    y = momentum[0][2],
    showlegend=False,
    mode = 'markers',
    line = dict(color = ('rgb(255,193,86)')))

tsk_m = go.Scatter(
    x = momentum[0][0],
    y = momentum[0][3],
    showlegend=False,
    mode = 'markers',
    line = dict(color = ('rgb(255,193,86)')))

tsc_m = go.Scatter(
    x = momentum[0][0],
    y = momentum[0][4],
    showlegend=False,
    mode = 'markers',
    line = dict(color = ('rgb(255,193,86)')))

tsm_m = go.Scatter(
    x = momentum[0][0],
    y = momentum[0][5],
    showlegend=False,
    mode = 'markers',
    line = dict(color = ('rgb(255,193,86)')))

tsa_m = go.Scatter(
    x = momentum[0][0],
    y = momentum[0][6],
    showlegend=False,
    mode = 'markers',
    line = dict(color = ('rgb(255,193,86)')))



fig = tools.make_subplots(rows =2, cols = 3,subplot_titles=('Variation of total energy',
							    'Variation of Potential energy',
							    'Variation of Kinetic energy',
							    'Variation of Coulomb energy',
							    'Variation of momentum energy',
							    'Variation of asymmetry energy'))

fig.append_trace(tse_s,1,1)
fig.append_trace(tsp_s,1,2)
fig.append_trace(tsk_s,1,3)
fig.append_trace(tsc_s,2,1)
fig.append_trace(tsm_s,2,2)
fig.append_trace(tsa_s,2,3)


fig.append_trace(tse_m,1,1)
fig.append_trace(tsp_m,1,2)
fig.append_trace(tsk_m,1,3)
fig.append_trace(tsc_m,2,1)
fig.append_trace(tsm_m,2,2)
fig.append_trace(tsa_m,2,3)

fig['layout'].update(title='Energy variations for static calculation')
#plotly.io.write_image(fig, 'fig1.pdf')
plotly.offline.plot(fig,filename='static_energy_plot.html')
