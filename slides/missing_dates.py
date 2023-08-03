from dash import html, dcc, Input, Output, State, dash_table
from server import app
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



df = pd.read_csv('data/missing_dates.csv')
md_text = """
**Issues in reporting statute name: from commercial disputes dataset**
* most cases report only the procedural law and not the substantive law
* statutes not related to commercial disputes are also reported: HMA, DVA   


"""
content = html.Div(children=[
    html.H1('Missing dates',
                                        style={'textAlign': 'center'}),
                    html.P(id='table_out'),
            html.Div(style={'width':'50%','align':'center','margin':'auto','padding':'10px'},
                     children=[dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} 
                 for i in df.columns],
        data=df.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="white"),
        filter_action="native",
        sort_action='native',
    filter_options={"placeholder_text": "Filter column..."},
    )]), 
    

])
