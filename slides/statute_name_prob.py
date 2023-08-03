from dash import html, dcc, Input, Output, State, dash_table
from server import app
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



df = pd.read_csv('data/statute_name_table.csv')
md_text = """
**Issues in reporting statute name: from commercial disputes dataset**
* most cases report only the procedural law and not the substantive law
* statutes not related to commercial disputes are also reported: HMA, DVA   


"""
content = html.Div(children=[
    html.H1('Issues in reporting statute name: commercial disputes dataset',
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


# @app.callback(
#     Output('table_out', 'children'), 
#     Input('table', 'active_cell'))
# def update_graphs(active_cell):
#     if active_cell:
#         cell_data = df.iloc[active_cell['row']][active_cell['column_id']]
#         return f"Data: \"{cell_data}\" from table cell: {active_cell}"
#     return "Click the table"


