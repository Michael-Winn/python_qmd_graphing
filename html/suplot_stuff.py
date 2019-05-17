import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline

# Top left
trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis data',
    )
trace2 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis2 data',
    yaxis='y2'
    )

# Top right
trace3 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis3 data',
    xaxis='x2',
    yaxis='y3'
    )
trace4 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis4 data',
    xaxis='x2',
    yaxis='y4'
    )

# Bottom left
trace5 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis5 data',
    xaxis='x3',
    yaxis='y5'
    )
trace6 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis6 data',
    xaxis='x3',
    yaxis='y6'
    )

# Bottom right
trace7 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis7 data',
    xaxis='x4',
    yaxis='y7'
    )
trace8 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis8 data',
    xaxis='x4',
    yaxis='y8'
    )


data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
layout = go.Layout(
    title='Double Y Axis Example',
    legend={'x': 1.1},
    width=1000,
    height=500,
    # Top left
    xaxis=dict(
      title='xaxis title',
      domain=[0, 1.0]
      ),
    yaxis=dict(
      title='yaxis title',
      type='log',
      domain=[0.6, 1.0],
      anchor='x'
      ),
    yaxis2=dict(
      title='yaxis2 title',
      overlaying='y',
      side='right'
      ),

    # Top right
    xaxis2=dict(
      title='xaxis2 title',
      domain=[0.6, 1.0],
      anchor='y3'
      ),
    yaxis3=dict(
      type='log',
      title='yaxis3 title',
      domain=[0.6, 1.0],
      anchor='x2'
      ),
    yaxis4=dict(
      title='yaxis4 title',
      domain=[0.6, 1.0],
      overlaying='y3',
      side='right',
      anchor='x2'
      ),

    # Bottom left
    xaxis3=dict(
      title='xaxis3 title',
      domain=[0, 0.4],
      anchor='y5'
      ),
    yaxis5=dict(
      type='log',
      title='yaxis5 title',
      domain=[0, 0.4],
      anchor='x3'
      ),
    yaxis6=dict(
	title='yaxis6 title',
	domain=[0, 0.4],
	overlaying='y5',
	side='right',
	anchor='x3'
	),

    # Bottom right
    xaxis4=dict(
	title='xaxis4, title',
	domain=[0.6, 1.0],
	anchor='y7'
	),
    yaxis7=dict(
	type='log',
	title='yaxis7 title',
	domain=[0, 0.4],
	anchor='x4'
	),
    yaxis8=dict(
	title='yaxis8 title',
	domain=[0, 0.4],
	overlaying='y7',
	side='right',
	anchor='x4'
	)
    )
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename = 'sub_test.html')
