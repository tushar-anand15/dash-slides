# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app

# custom imports
# ...

image_path = 'assets/out7.jpg'
content = html.Div(
    style=dict(textAlign="center"),
    children=[
        #html.H1("A Slide for a Picture"),
        html.Img(src=image_path),
    ],
)
















