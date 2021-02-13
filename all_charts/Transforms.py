
# coding: utf-8

# In[1]:


import plotly.io as pio

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'filter',
    target = 'y',
    operation = '>',
    value = 4
  )]
)]

layout = dict(
    title = 'Scores > 4'
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)


# In[ ]:


import plotly.io as pio

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'groupby',
    groups = subject,
    styles = [
        dict(target = 'Moe', value = dict(marker = dict(color = 'blue'))),
        dict(target = 'Larry', value = dict(marker = dict(color = 'red'))),
        dict(target = 'Curly', value = dict(marker = dict(color = 'black')))
    ]
  )]
)]

fig_dict = dict(data=data)
pio.show(fig_dict, validate=False)


# In[ ]:


import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://plotly.com/~public.health/17.csv")

data = [dict(
  x = df['date'],
  autobinx = False,
  autobiny = True,
  marker = dict(color = 'rgb(68, 68, 68)'),
  name = 'date',
  type = 'histogram',
  xbins = dict(
    end = '2016-12-31 12:00',
    size = 'M1',
    start = '1983-12-31 12:00'
  )
)]

layout = dict(
  paper_bgcolor = 'rgb(240, 240, 240)',
  plot_bgcolor = 'rgb(240, 240, 240)',
  title = '<b>Shooting Incidents</b>',
  xaxis = dict(
    title = '',
    type = 'date'
  ),
  yaxis = dict(
    title = 'Shootings Incidents',
    type = 'linear'
  ),
  updatemenus = [dict(
        x = 0.1,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,
        buttons = [
        dict(
            args = ['xbins.size', 'D1'],
            label = 'Day',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M1'],
            label = 'Month',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M3'],
            label = 'Quater',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M6'],
            label = 'Half Year',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M12'],
            label = 'Year',
            method = 'restyle',
        )]
  )]
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)


# In[2]:


import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/worldhappiness.csv")

aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)

data = [dict(
  type = 'choropleth',
  locationmode = 'country names',
  locations = df['Country'],
  z = df['HappinessScore'],
  autocolorscale = False,
  colorscale = 'Portland',
  reversescale = True,
  transforms = [dict(
    type = 'aggregate',
    groups = df['Country'],
    aggregations = [dict(
        target = 'z', func = 'sum', enabled = True)
    ]
  )]
)]

layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation',
  xaxis = dict(title = 'Subject'),
  yaxis = dict(title = 'Score', range = [0,22]),
  height = 600,
  width = 900,
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)


# In[ ]:


import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

colors = ['blue', 'orange', 'green', 'red', 'purple']

opt = []
opts = []
for i in range(0, len(colors)):
    opt = dict(
        target = df['continent'][[i]].unique(), value = dict(marker = dict(color = colors[i]))
    )
    opts.append(opt)

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'groupby',
        groups = df['continent'],
        styles = opts
    )]
)]

layout = dict(
    yaxis = dict(
        type = 'log'
    )
)

fig_dict = dict(data=data, layout=layout)
pio.show(fig_dict, validate=False)


# In[ ]:


import plotly.io as pio
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'aggregate',
        groups = df['continent'],
        aggregations = [
            dict(target = 'x', func = 'avg'),
            dict(target = 'y', func = 'avg'),
            dict(target = 'marker.size', func = 'sum')
        ]
      )]
)]

layout = dict(
    yaxis = dict(
        type = 'log'
    )
)


fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)


# In[ ]:


import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

colors = ['blue', 'orange', 'green', 'red', 'purple']

opt = []
opts = []
for i in range(0, len(colors)):
    opt = dict(
        target = df['continent'][[i]].unique(), value = dict(marker = dict(color = colors[i]))
    )
    opts.append(opt)

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'groupby',
        groups = df['continent'],
        styles = opts
      ),
      dict(
        type = 'aggregate',
        groups = df['continent'],
        aggregations = [
            dict(target = 'x', func = 'avg'),
            dict(target = 'y', func = 'avg'),
            dict(target = 'marker.size', func = 'sum')
        ]
      )]
)]

layout = dict(
    title = '<b>Gapminder</b><br>2007 Average GDP Per Cap & Life Exp. by Continent',
    yaxis = dict(
        type = 'log'
    )
)

fig_dict = dict(data=data, layout=layout)
pio.show(fig_dict, validate=False)

