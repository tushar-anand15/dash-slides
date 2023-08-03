from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import os
import importlib

layout = html.Div(
    children=[
        html.Div(id="page-content"),
        dcc.Location(id="url", refresh=False),
    html.Div(
        style = {},
        children = [
            dbc.Container(
                 fluid=True,
            children=[html.Div(id="current-slide", style=dict(display="none", children="")),
                # nav div
                dbc.Row(
                    style=dict(height="auto", position="sticky", margin="10px",align='baseline'),
                    children=[
                        # logo
                        #dbc.Col(width=2, style=nav_style, children=[get_logo()]),
                        # previous
                        dbc.Col(
                            width=2,
                            style=nav_style,
                            children=[
                                dcc.Link(
                                    id="previous-link",
                                    href="",
                                    children=nav_button_div("<<"),
                                ),
                            ],
                        ),  # end previous
                        # slide count
                        dbc.Col(
                            width=2,
                            style=nav_style,
                            children=[
                                dbc.DropdownMenu(
                                    id="slide-count",
                                    size="sm",
                                    color='secondary',
                                    
                                    children=[
                                        dbc.DropdownMenuItem(
                                            s,
                                            href="/" + s,
                                        )
                                        for s in slide_order
                                    ],
                                )
                            ],
                        ),  # end slide count
                        # next
                        dbc.Col(
                            width=2,
                            style=nav_style,
                            children=[
                                dcc.Link(
                                    id="next-link",
                                    href="",
                                    children=nav_button_div(">>"),
                                ),
                            ],
                        ),  # end next
                    ],
                ),

            ]

            )
        ]
    )

    ]




)