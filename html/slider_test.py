import plotly.plotly as py
import numpy as np
import plotly.offline
import plotly.graph_objs as go


t=np.linspace(-1,1,100)
x=t+t**2
y=t-t**2
xm=np.min(x)-1.5
xM=np.max(x)+1.5
ym=np.min(y)-1.5
yM=np.max(y)+1.5
N=50
s=np.linspace(-1,1,N)
xx=s+s**2
yy=s-s**2


data=[dict(x=x, y=y, 
           mode='lines', 
           line=dict(width=2, color='blue')
          ),
      dict(x=x, y=y, 
           mode='lines', 
           line=dict(width=2, color='blue')
          )
    ]

layout=dict(xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title='Kinematic Generation of a Planar Curve', hovermode='closest',
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]}]}])

frames=[dict(data=[dict(x=[xx[k]], 
                        y=[yy[k]], 
                        mode='markers', 
                        marker=dict(color='red', size=10)
                        )
                  ]) for k in range(N)]    
          
figure=dict(data=data, layout=layout, frames=frames)   	

plotly.offline.plot(figure, filename = 'animation_test.html')
