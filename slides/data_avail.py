from dash import html, dcc, Input, Output, State
from server import app
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data/data_availability_year.csv')

options = ['Count','Percentage']

content = html.Div(
    children=[html.H1('Data availability per year',
                                        style={'textAlign': 'center'}),
            html.Div(children=[dcc.Dropdown(id='site-dropdown',options = options, value='Percentage',clearable=False,searchable=True)],style={'width':'25%'})
            ,
            html.Br(),
            html.Div(dcc.Graph(id='data-avail-chart')),

    ]
    )

@app.callback(Output(component_id ='data-avail-chart',component_property='figure'),
     Input(component_id = 'site-dropdown',component_property = 'value'))
def display_bar_chart(value):
    if value=='Percentage':
        
        fig = go.Figure([go.Bar(
        name = "Pending",
        y = df['Pending_Percentage'],
        x = df['Year of filing'],
        #text = class_values['hovertext'],
        hovertemplate = "%{label} <br> % Pending cases: %{y}"
        ),
         go.Bar(
        name = "Disposed",
        y = df['Disposed_Percentage'],
        x = df['Year of filing'],
        #text = class_values['hovertext'],
        hovertemplate = "%{label} <br> % Disposed cases: %{y}" )])
        fig.update_layout(
            barmode='stack',
            title = dict(text = f"Distribution of cases filed in each year",x=0.5),
            xaxis_title = 'Time (Years)',
            yaxis_title = 'Percentage', 
            legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.30
        ))
    if value=='Count':
        fig = go.Figure([go.Bar(
        name = "Pending",
        y = df['Pending cases'],
        x = df['Year of filing'],
        #text = class_values['hovertext'],
        hovertemplate = "%{label} <br> % Pending cases: %{y}"
        ),
        go.Bar(
        name = "Disposed",
        y = df['Disposed cases'],
        x = df['Year of filing'],
        #text = class_values['hovertext'],
        hovertemplate = "%{label} <br> % Disposed cases: %{y}" )])

        fig.update_layout(
            barmode='stack',
            title = dict(text = f"Count of cases filed in each year",x=0.5),
            xaxis_title = 'Time (Years)',
            yaxis_title = 'Count', 
            legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.30
        ))
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return fig