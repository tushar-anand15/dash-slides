from dash import html, dcc, Input, Output, State
from server import app
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data/missing_orders_year.csv')
df['Percentage_without'] = 100 - df['Percentage']
df['count_without'] = df['Total disposed cases'] - df['Cases with final orders']

options = ['Count','Percentage']

content = html.Div(
    children=[html.H1('Final orders availability per year',
                                        style={'textAlign': 'center'}),
            html.Div(children=[dcc.Dropdown(id='site-dropdown',options = options, value='Percentage',clearable=False,searchable=True)],style={'width':'25%'})
            ,
            html.Br(),
            html.Div(dcc.Graph(id='orders-avail-chart')),

    ]
    )

@app.callback(Output(component_id ='orders-avail-chart',component_property='figure'),
     Input(component_id = 'site-dropdown',component_property = 'value'))
def display_bar_chart(value):
    if value=='Percentage':
        
        fig = go.Figure([go.Bar(
        name = "Available",
        y = df['Percentage'],
        x = df['Year of filing'],
        #text = class_values['hovertext'],
        hovertemplate = "%{label} <br>Final orders present: %{y}"
         ),
        go.Bar(
        name = "Not available",
        y = df['Percentage_without'],
        x = df['Year of filing'],
        #text = class_values['hovertext'],
        hovertemplate = "%{label} <br>Final orders NA: %{y}" )])
        fig.update_layout(
            barmode='stack',
            title = dict(text = f"Final order availability",x=0.5),
            legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.30
         ))
    if value=='Count':
            fig = go.Figure([go.Bar(
    name = "Available",
    y = df['Cases with final orders'],
    x = df['Year of filing'],
    #text = class_values['hovertext'],
    hovertemplate = "%{label} <br>Final orders present: %{y}"
),
 go.Bar(
    name = "Not available",
    y = df['count_without'],
    x = df['Year of filing'],
    #text = class_values['hovertext'],
    hovertemplate = "%{label} <br>Final orders NA: %{y}" )])
    fig.update_layout(
        barmode='stack',
        title = dict(text = f"Final order availability",x=0.5),
        legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.30
))
    return fig
        
        
        
        
        
        

        
        
        
        
        
        
        
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    return fig