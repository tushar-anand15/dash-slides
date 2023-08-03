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
# #gdf = gdf.merge(df,left_on='ST_NM',right_on='State',how='outer')
gdf =  gpd.read_file('data/states_shapefile_disposed_cases.json')
gdf.set_index('ST_NM',inplace=True)
gdf['Percentage'] = gdf['Percentage'].astype(float)
#gdf['Percentage_text'] = gdf['Percentage'] * 100
options = ['Cases with final orders','Total disposed cases']
gdf.fillna(-1,inplace=True)

gdf['Percentage'] = gdf['Percentage'].astype(float)
options = ['Cases with final orders','Total disposed cases']
gdf.fillna(-100,inplace=True)
gdf['Percentage'] = gdf['Percentage'].replace(-1,-100)


fig = px.choropleth(gdf,
            geojson=gdf.geometry,
            locations=gdf.index,
            color=gdf['Percentage'],
            projection="mercator",
            hover_name = gdf.index,
            hover_data=options,
            color_continuous_scale='Aggrnyl',
            color_continuous_midpoint=0,
            range_color=(-100, 100),
            # #color_continuous_scale = [(-1, 'grey'),(-1,'grey'),
            #                           (0, 'brown'),(15,'brown'),
            #                           (15, 'red'),(30,'red'),
            #                           (30, 'orange'),(45,'orange'),
            #                           (45, 'yellow'),(60,'yellow'),
            #                           (60, 'cyan'),(75,'cyan'),
            #                           (75, 'lightblue'),(90,'lightblue'),
            #                           (90, 'blue'), (100,'blue')]

)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    width=1600,height=800,
    #title_text = 'Statewise number of cases filed under each act',
legend=dict(
        title="Distribution of availability of final orders"
    ))
        #paper_bgcolor="LightSteelBlue",
        #margin=dict(l=20, r=20, t=20, b=20))

#fig.show()


 # html.Div(children=[dcc.Dropdown(id='site-dropdown',options = options, value='All',clearable=False,searchable=True)],style={'width':'25%'})
content = html.Div(
    children=[html.H1('Availability of final orders across states',
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