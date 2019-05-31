import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.animation as animation
import matplotlib as mpl
mpl.use('Agg')
print mpl.__version__
from tqdm import tqdm
import matplotlib.pyplot as plt,mpld3
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import axes3d, Axes3D
from tools.import_methods import *
from tools.nuclei import *
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline
from plotly import tools
import random
nnuc = 394.
def plotting_position(time,x,y,z,iso,static):
  rms_p_table= []
  rms_t_table= []
  rotation_addition = 50
#  for j in tqdm(range(len(time)),desc='Generating PNGs'):
  for j in [251,376,502,626,757]:
#  for j in range(1):
#  for k in range(1):
#    j = 300
#    print(j)
#    progress(j,len(time),'Generating PNGs')
                                  
    times = ['50','75','100','125','150']
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

#    if(j %10 ==0) : 
    if(j >0) : 
########################################PLOTTING PART
      lines = []
      sphere = sphere_lines([target.xc,target.yc,target.zc],target.rms)
      line_marker = dict(color='#0066FF', width=2)
      

      trace1 = go.Scatter3d(x=target.neutrons.x,y=target.neutrons.y,z=target.neutrons.z,mode='markers',name = 'Target neutrons',marker=dict(color='rgb(214,39,40)',size=3,symbol='diamond'))
      trace2 = go.Scatter3d(x=target.protons.x,y=target.protons.y,z=target.protons.z,mode='markers',name = 'Target protons',marker=dict(color='rgb(255,127,14)',size=3,symbol='circle'))

      trace3 = go.Scatter3d(x=projectile.neutrons.x,y=projectile.neutrons.y,z=projectile.neutrons.z,mode='markers',name='Projecile neutrons',marker=dict(color='rgb(220,95,186)',size=3,symbol='diamond'))
      trace4 = go.Scatter3d(x=projectile.protons.x,y=projectile.protons.y,z=projectile.protons.z,mode='markers',name='Projectile protons',marker=dict(color='rgb(148,103,189)',size=3,symbol='circle'))
      trace5 = go.Scatter(x=time_rho,y=rho_t,name='Rho(t)',xaxis='x',yaxis='y' ,mode = 'lines',line = dict(color='rgb(255,127,14)'),showlegend=False)
      trace6 = go.Scatter(x=time_rho,y=rho_p,name='Rho(t)',xaxis='x2',yaxis='y2' ,mode = 'lines',line = dict(color='rgb(148,103,189)'),showlegend=False)
      trace7 = go.Scatter(x=time_rho,y=rms_t_table,name='RMS(t)',xaxis='x3',yaxis='y3' ,mode = 'lines',line = dict(color='rgb(255,127,14)'),showlegend=False)
      trace8 = go.Scatter(x=time_rho,y=rms_p_table,name='RMS(t)',xaxis='x4',yaxis='y4' ,mode = 'lines',line = dict(color='rgb(148,103,189)'),showlegend=False)


      lines.append(trace1)
      lines.append(trace2)
      lines.append(trace3)
      lines.append(trace4)
      lines.append(trace5)
      lines.append(trace6)
      lines.append(trace7)
      lines.append(trace8)

      data = lines
      layout = go.Layout(
	  xaxis = dict(domain=[0.8,1.0]),
	  yaxis = dict(domain=[0.75,1.0],anchor='x',title=r'$ \rho fm^{-3}$'),
	  xaxis2 = dict(domain=[0.8,1],anchor='y2',
	    title='Time (fm/c)'),
	  yaxis2 = dict(domain=[0.5,0.75],anchor='x2',title=r'$ \rho fm^{-3}$'),
	  xaxis3 = dict(domain=[0.8,1.0],anchor='y3'),
	  yaxis3 = dict(domain=[0.25,0.45],anchor='x3',title=r'rms'),
	  xaxis4 = dict(domain=[0.8,1.0],anchor='y4',title='Time (fm/c)'),
	  yaxis4 = dict(domain=[0.0,0.25],anchor='x4',title=r'rms'),
	  title = go.layout.Title(
	    text = 'Bene = 0.6 Mev, b = 12 fm/c , T = '+str(round(time[j][0],2)),
	    xref = 'paper',
	    x=0.5,
	    y = 0.95
	    ),
          margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
            ),
	  legend=dict(x=-.1, y=1.0)
          )

      if(j==251 or j==376 or j ==502 or j ==626 or j == 752): 
#	 print(j)
         fig = go.Figure(data=data, layout=layout)
         plotly.offline.plot(fig, filename = str(j)+'.html',auto_open=False)



def sphere_on_center(centre_s,radius):
         u, v = np.mgrid[0:2*np.pi:10*1j, 0:np.pi:10*1j]
         sphere_x = centre_s[0] + radius * np.cos(u) * np.sin(v)
	 sphere_y = centre_s[1] + radius * np.sin(u) * np.sin(v)
	 sphere_z = centre_s[2] + radius * np.cos(v)
	 return sphere_x, sphere_y, sphere_z

def sphere_lines(center,radius):
  x = []
  y = []
  z = []
  i_range = 10.
  nb_per_circle = 200
  for i in range(int(i_range)):
    z_val = (1-i/i_range)*radius
    temp_x = []
    temp_y = []
    temp_z = []
    r = i/i_range * radius
    for j in range(nb_per_circle):
      angle = random.uniform(0, 1)*3.14159265*2
      temp_x.append(np.cos(angle)*r+center[0])
      temp_y.append(np.sin(angle)*r+center[1])
      temp_z.append(z_val+center[2])
    x.append(temp_x)
    y.append(temp_y)
    z.append(temp_z)
  for i in range(1,int(i_range)):
    temp_x = []
    temp_y = []
    temp_z = []
    for j in range(nb_per_circle):
      temp_x.append(x[int(10-i)][j])
      temp_y.append(y[int(10-i)][j])
      temp_z.append(-z[int(10-i)][j])
    x.append(temp_x)
    y.append(temp_y)
    z.append(temp_z)
  return [x,y,z]

def progress(count, total, status=''):
      bar_len = 60
      filled_len = int(round(bar_len * count / float(total)))
      percents = round(100.0 * count / float(total), 1)
      bar = '#' * filled_len + '-' * (bar_len - filled_len)

      sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))
      sys.stdout.flush()

def testing():
  fig = plt.figure(figsize=(10.8,7.2), dpi=100)
  plt.grid()
  plt.xlabel('x label')
  plt.ylabel('y label')
  mpld3.save_html(fig,'../html_out/test.html')

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

def animation_alt(time,x,y,z,iso,static):

      import numpy as np
#      from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot
#      init_notebook_mode(connected=True)

#  for j in [251,376,502,626,757]:
      coords = []
      times = ['25','50','75','100','125','150']
      rms_t_table = []
      rms_p_table = []
#      print(time[126])
      for j in range(len(time)):
#      for j in [125,251,376,502,626,757]:
#	print(j)
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
        if(j == 125 or j == 251 or j == 376 or j == 502 or j == 626 or j == 575):
	  tn = [target.neutrons.x,target.neutrons.y,target.neutrons.z]
	  tp = [target.protons.x,target.protons.y,target.protons.z]
	  pn = [projectile.neutrons.x,projectile.neutrons.y,projectile.neutrons.z]
	  pp = [projectile.protons.x,projectile.protons.y,projectile.protons.z]
	  coords.append([tn,tp,pn,pp])
#      print(coords[0][0][0]) 
      fig = dict (
	      layout=dict(width=1400, height=1000,
	      title  = 'Static values',
	      margin = {'t': 50, 'b': 50, 'l': 50, 'r': 50},
	),
      data = [
	  {'type':'scatter3d', # This is the target neutrons 
	    'name':'Target Neutrons',
	    'x':np.asarray(coords[0][0][0]),
	    'y':np.asarray(coords[0][0][1]),
	    'z':np.asarray(coords[0][0][2]),
	    'mode':'markers',
	    'marker':{'symbol':'diamond','size': 3,'color':'rgb(214,39,40)'},
	    },
	  {'type':'scatter3d', # This is the target protons 
	    'name':'Target Protons',
	    'x':np.asarray(coords[0][1][0]),
	    'y':np.asarray(coords[0][1][1]),
	    'z':np.asarray(coords[0][1][2]),
	    'mode':'markers',
	    'marker':{'symbol':'circle','size': 3,'color':'rgb(255,127,14)'},
	    },

	  {'type':'scatter3d', # This is the Projectile neutrons 
	    'name':'Projectile Neutrons',
	    'x':np.asarray(coords[0][2][0]),
	    'y':np.asarray(coords[0][2][1]),
	    'z':np.asarray(coords[0][2][2]),
	    'mode':'markers',
	    'marker':{'symbol':'diamond','size': 3,'color':'rgb(220,95,186)'},
	    },
	  {'type':'scatter3d', # This is the Projectile protons 
	    'name':'Projectile Protons',
	    'x':np.asarray(coords[0][3][0]),
	    'y':np.asarray(coords[0][3][1]),
	    'z':np.asarray(coords[0][3][2]),
	    'mode':'markers',
	    'marker':{'symbol':'circle','size': 3,'color':'rgb(148,103,186)'},
	    },
	  ]
        )



      frames = [dict(name=k,
		      data=[
			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][0][0]),
			  'y' : np.asarray(coords[k][0][1]),
			  'z' : np.asarray(coords[k][0][2]),
			  },

			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][1][0]),
			  'y' : np.asarray(coords[k][1][1]),
			  'z' : np.asarray(coords[k][1][2]),
			  },

			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][2][0]),
			  'y' : np.asarray(coords[k][2][1]),
			  'z' : np.asarray(coords[k][2][2]),
			  },

			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][3][0]),
			  'y' : np.asarray(coords[k][3][1]),
			  'z' : np.asarray(coords[k][3][2]),
			  },
			  ],	
			traces=[0,1,2,3]) for k in range(6)]

      sliders = [{'yanchor': 'top',
            'xanchor': 'left', 
            'currentvalue': {'font': {'size': 16}, 'prefix': 'Time: ', 'visible': True, 'xanchor': 'right'},
            'transition': {'duration': 500.0, 'easing': 'linear'},
            'pad': {'b': 10, 't': 50}, 
            'len': 0.9, 'x': 0.1, 'y': 0, 
	    'steps': [{'args': [[k], {'frame': {'duration': 500.0, 'easing': 'linear', 'redraw': False},'mode':'immediate',
                                      'transition': {'duration': 0, 'easing': 'linear'}}], 
                       'label': times[k], 'method': 'animate'} for k in range(6)      
                    ]}]

      fig.update(frames=frames)
      fig['layout'].update(sliders=sliders)
      plotly.offline.plot(fig, filename = 'static.html')

def animation_alt2(time,x,y,z,iso,static):

      import numpy as np
#      from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot
#      init_notebook_mode(connected=True)

#  for j in [251,376,502,626,757]:
      coords = []
#      times = ['25','50','75','100','125','150']
      times = []
      rms_t_table = []
      rms_p_table = []
#      print(time[126])
      for j in range(len(time)):
#      for j in range(50):
#      for j in [125,251,376,502,626,757]:
#	print(j)
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
#        if(j == 125 or j == 251 or j == 376 or j == 502 or j == 626 or j == 575):
	if(j%10 ==0) :
#	if(j>0):
	  tn = [target.neutrons.x,target.neutrons.y,target.neutrons.z]
	  tp = [target.protons.x,target.protons.y,target.protons.z]
	  pn = [projectile.neutrons.x,projectile.neutrons.y,projectile.neutrons.z]
	  pp = [projectile.protons.x,projectile.protons.y,projectile.protons.z]
	  coords.append([tn,tp,pn,pp])
	  times.append(time[j][0])
#      print(coords[0][0][0]) 
      slider_range = len(coords)
      print(len(coords))
      fig = dict (
	      layout=dict(width=1400, height=1000,
	      title  = 'Static values',
	      margin = {'t': 50, 'b': 50, 'l': 50, 'r': 50},
#	      updatemenus = [{'type':'buttons',
#			      'buttons':[{'label':'Play', 'method':'animate','args':[None]}]}]
	),
      data = [
	  {'type':'scatter3d', # This is the target neutrons 
	    'name':'Target Neutrons',
	    'x':np.asarray(coords[0][0][0]),
	    'y':np.asarray(coords[0][0][1]),
	    'z':np.asarray(coords[0][0][2]),
	    'mode':'markers',
	    'marker':{'symbol':'diamond','size': 3,'color':'rgb(214,39,40)'},
	    },
	  {'type':'scatter3d', # This is the target protons 
	    'name':'Target Protons',
	    'x':np.asarray(coords[0][1][0]),
	    'y':np.asarray(coords[0][1][1]),
	    'z':np.asarray(coords[0][1][2]),
	    'mode':'markers',
	    'marker':{'symbol':'circle','size': 3,'color':'rgb(255,127,14)'},
	    },

	  {'type':'scatter3d', # This is the Projectile neutrons 
	    'name':'Projectile Neutrons',
	    'x':np.asarray(coords[0][2][0]),
	    'y':np.asarray(coords[0][2][1]),
	    'z':np.asarray(coords[0][2][2]),
	    'mode':'markers',
	    'marker':{'symbol':'diamond','size': 3,'color':'rgb(220,95,186)'},
	    },
	  {'type':'scatter3d', # This is the Projectile protons 
	    'name':'Projectile Protons',
	    'x':np.asarray(coords[0][3][0]),
	    'y':np.asarray(coords[0][3][1]),
	    'z':np.asarray(coords[0][3][2]),
	    'mode':'markers',
	    'marker':{'symbol':'circle','size': 3,'color':'rgb(148,103,186)'},
	    },
	  ]
        )

      fig['layout']['updatemenus'] = [
	  {
	    'buttons': [
	      {
		'args': [None, {'frame': {'duration': 10, 'redraw': False},
		  'fromcurrent': True, 'transition': {'duration': 10, 'easing': 'quadratic-in-out'}}],
		'label': 'Play',
		'method': 'animate'
		},
	      {
		'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
		  'transition': {'duration': 0}}],
		'label': 'Pause',
		'method': 'animate'
		}
	      ],
	    'direction': 'left',
	    'pad': {'r': 10, 't': 87},
	    'showactive': False,
	    'type': 'buttons',
	    'x': 0.1,
	    'xanchor': 'right',
	    'y': 0,
	    'yanchor': 'top'
	    }
	  ]


      frames = [dict(name=k,
		      data=[
			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][0][0]),
			  'y' : np.asarray(coords[k][0][1]),
			  'z' : np.asarray(coords[k][0][2]),
			  },

			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][1][0]),
			  'y' : np.asarray(coords[k][1][1]),
			  'z' : np.asarray(coords[k][1][2]),
			  },

			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][2][0]),
			  'y' : np.asarray(coords[k][2][1]),
			  'z' : np.asarray(coords[k][2][2]),
			  },

			{'type' : 'scatter3d',
			  'x' : np.asarray(coords[k][3][0]),
			  'y' : np.asarray(coords[k][3][1]),
			  'z' : np.asarray(coords[k][3][2]),
			  },
			  ],	
			traces=[0,1,2,3]) for k in range(slider_range)]

      sliders = [{'yanchor': 'top',
            'xanchor': 'left', 
            'currentvalue': {'font': {'size': 16}, 'prefix': 'Time: ', 'visible': True, 'xanchor': 'right'},
	    'transition': {'duration': 0.0},
            'pad': {'b': 10, 't': 50}, 
            'len': 0.9, 'x': 0.1, 'y': 0, 
#            'steps': [{'args': [[k], {'frame': {'duration': 100, 'easing': 'elastic', 'redraw': False},
	    'steps': [{"args": [[k], {"frame": {"duration": 0.0,"easing" : "linear",'redraw': False},
#                                      'transition': {'duration': 0, 'easing': 'elastic'},
				      'transition': {"easing": " linear" ,'duration': 0},
				      'mode' : 'immediate'}], 
				      'label': round(times[k],2), 'method': 'animate','visible': (k%20 ==0)} for k in range(slider_range)]      
#                       'label': times[k]} for k in range(slider_range)      
                    }]

      fig.update(frames=frames)
      fig['layout'].update(sliders=sliders)
      plotly.offline.plot(fig, filename = 'static_sal.html',auto_open=False,auto_play=False)