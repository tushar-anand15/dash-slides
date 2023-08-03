# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app

# custom imports
# ...

image_path = 'assets/out0.jpg'
content = html.Div(
    style=dict(textAlign="center"),
    children=[
        #html.H1("A Slide for a Picture"),
        html.Img(src=image_path),
    ],
)



# @app.callback(Output("intro-div", "children"), [Input("intro-button", "n_clicks")])
# def create_template_graph(n):
    # return "Button has been clicked {} times.".format(n)
