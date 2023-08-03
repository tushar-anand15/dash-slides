from dash import html, dcc, Input, Output, State
from server import app
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
#import json


# df = pd.read_csv('data/state_act_count.csv')
# gdf = gpd.read_file('data/states_shapefile.json')
# df.loc[df['State']=='DNH at Silvasa',['State']] = 'Dadra and Nagar Haveli and Daman and Diu'
# df.loc[df['State']=='Orissa',['State']] = 'Odisha'
# df.loc[df['State']=='Jammu and Kashmir',['State']] = 'Jammu & Kashmir'
# gdf = gdf.merge(df,left_on='ST_NM',right_on='State',how='outer')
gdf =  gpd.read_file('data/states_shapefile_act_count.json')
gdf.set_index('ST_NM',inplace=True)
gdf['none_values'] = gdf['none_values'].astype(int)
options = ['AC-Act', 'IC-Act', 'NI-Act',
        'SR-Act', 'TP-Act']




fig = px.choropleth(gdf,
            geojson=gdf.geometry,
            locations=gdf.index,
            color=gdf['none_values'].astype(str),
            projection="mercator",
            hover_name = gdf.index,
            hover_data=options,
            color_discrete_map = {"0":"lightgreen",   
                                    "1":"cyan" ,  
                                    "-1":"lightgrey"   ,  
                                    "2":"orange"   , 
                                    "4":"darkred" ,   
                                    "3":"red" },
                labels={'ST_NM':'State/UT','color':'Acts with no cases'},
                category_orders={'color':['-1','0','1','2','3','4']}

                
                )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    width=1600,height=800,
    #title_text = 'Statewise number of cases filed under each act',
legend=dict(
        title="No. of acts with zero cases"
    ))
        #paper_bgcolor="LightSteelBlue",
        #margin=dict(l=20, r=20, t=20, b=20))





 # html.Div(children=[dcc.Dropdown(id='site-dropdown',options = options, value='All',clearable=False,searchable=True)],style={'width':'25%'})
content = html.Div(
    children=[html.H1('Statewise distribution of cases under each selected act',
                                        style={'textAlign': 'center'}),
           
            
            html.Br(),
            html.Div(dcc.Graph(figure=fig)),

    ]
    )

# @app.callback(Output(component_id ='act-dist-choro',component_property='figure'),
    #  Input(component_id = 'site-dropdown',component_property = 'value'))
# def display_choropleth(value):
    # if value=='All':
        # fig = px.choropleth(gdf,
                    # geojson=gdf.geometry,
                    # locations=gdf.index,
                    # color=gdf['none_values'].astype(str),
                    # projection="mercator",
                    # hover_name = gdf.index,
                    # text=gdf['text'],
                    # color_discrete_map = {"0":"lightgreen",   
                                            # "1":"cyan" ,  
                                            # "-1":"lightgrey"   ,  
                                            # "2":"orange"   , 
                                            # "4":"darkred" ,   
                                            # "3":"red" },
                        # labels={'ST_NM':'State/UT','color':'Acts with no cases'}
                        # 
                        # )
        # fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(
            # title_text = 'Statewise number of cases filed under each act')
    # else:
        # fig = px.choropleth(gdf,
                    # geojson=gdf.geometry,
                    # locations=gdf.index,
                    # color=gdf['none_values'].astype(str),
                    # projection="mercator",
                    # hover_name = gdf.index,
                    # 
                    # color_discrete_map = {"0":"lightgreen",   
                                            # "1":"cyan" ,  
                                            # "-1":"lightgrey"   ,  
                                            # "2":"orange"   , 
                                            # "4":"darkred" ,   
                                            # "3":"red" },
                        # labels={'ST_NM':'State/UT','color':'Acts with no cases'}
                        # 
                        # )
        # fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(
            # title_text = f'Statewise number of cases filed under {value}')
        # 
    # return fig
# 
# 
# 
# def make_hover_text(row):
    # col_vals = ["AC-Act",  "IC-Act",    "NI-Act" ,  "SR-Act" , "TP-Act"]
    # if row['none_values'] ==-1:
        # text = 'Data not available'
    # else:
        # null_cols = [i for i in col_vals if row[i]==-1 ]
        # text ="No cases for :" +  ",".join(null_cols) 
    # return text