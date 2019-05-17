import pandas as pd
import numpy as np
import plotly.offline 

test_data=np.random.randint(25, 100, (24, 31))
ymin=test_data.min()
ymax=test_data.max()
ymax

#for k in range(31): print(test_data[:,k])

data=[dict(type='scatter',
          x=list(range(24)),
          y=test_data[:0],
     mode='markers',
     marker=dict(size=10, color='red'))
     ]

frames=[dict(data=[dict(y=test_data[:,k])],
             traces=[0],
             name=k+1) for k in range(31)]
#             name=f'{k+1}') for k in range(31)]

sliders=[dict(steps= [dict(method= 'animate',
                           args= [[k+1],
#                           args= [[ f'{k+1}'],
                                  dict(mode= 'immediate',
                                  frame= dict( duration=2000, redraw= False ),
                                           transition=dict( duration= 2000)
                                          )
                                    ],
                            label='day'+str(k+1)
#                            label=f'day {k+1}'
                             ) for k in range(31)], 
                transition= dict(duration= 2000 ),
                x=0,#slider starting position  
                y=0, 
                currentvalue=dict(font=dict(size=12), 
                                  prefix='Day: ', 
                                  visible=True, 
                                  xanchor= 'center'
                                 ),  
                len=1.0)#slider length)
           ]

axis_style=dict(showline=True,
               mirror=True,
               zeroline=False,
               ticklen=4)

layout=dict(title='Your title',
           width=900,
           height=600,
           autosize=False,
            xaxis=dict(axis_style, **dict(range=[0,24])),
            yaxis=dict(axis_style, **dict(range=[ymin-1, ymax+1], autorange=False)
           ),
             hovermode='closest',
            updatemenus=[dict(type='buttons', showactive=False,
                                y=0,
                                x=1.15,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=2000, 
                                                                    redraw=False),
                                                         transition=dict(duration=2000),
                                                         fromcurrent=True,
                                                         mode='immediate'
                                                        )
                                                   ]
                                             )
                                        ]
                               )
                          ],
              sliders=sliders
           )

fig=dict(data=data, frames=frames, layout=layout)
plotly.offline.plot(fig, filename = 'duration.html')
