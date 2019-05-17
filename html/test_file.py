import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline

import numpy as np

# Creating the data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
xGrid, yGrid = np.meshgrid(y, x)
R = np.sqrt(xGrid ** 2 + yGrid ** 2)
z = np.sin(R)

# Creating the plot
lines = []
line_marker = dict(color='#0066FF', width=2)
for i, j, k in zip(xGrid, yGrid, z):
  print('x : {0}'.format(i))
  print('y : {0}'.format(j))
  print('z : {0}'.format(k))
  lines.append(go.Scatter3d(x=i, y=j, z=k, mode='lines', line=line_marker))

layout = go.Layout(
    title='Wireframe Plot',
    showlegend=False,
    )
fig = go.Figure(data=lines, layout=layout)
plotly.offline.plot(fig, filename = 'wire_test.html')
