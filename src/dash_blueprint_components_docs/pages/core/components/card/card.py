import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Card)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Card)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Card(
                            id='card',
                            children=[
                                html.H4('Analytical applications', className='bp5-heading'),
                                html.P('User interfaces that enable people to interact smoothly with data, ask better questions, and make better decisions.'),
                                dbpc.Button(children='Explore products')
                            ],
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        dbpc.Switch(
                            id='interactive',
                            children='Interactive',
                            checked=False
                        ),
                        dbpc.Switch(
                            id='compact',
                            children='Compact'
                        ),
                        html.P('Elevation'),
                        dbpc.Slider(
                            id='slider',
                            max=4,
                            showTrackFill=False,
                        )  
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='card-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H2('Props interface'),
        html.Table(
            children=[
                html.Thead(
                    children=[
                        html.Tr(
                            children=[
                                html.Th(children='Props'),
                                html.Th(children='Description')
                            ]
                        )
                    ]
                ),
                html.Tbody(
                    children=get_tablebody_from_props(parse_docstring(dbpc.Card)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('card', 'elevation'),
    Input('slider', 'value')
)
def change(value):
    return value

@callback(
    Output('card', 'compact'),
    Input('compact', 'checked')
)
def change(value):
    return value

@callback(
    Output('card', 'interactive'),
    Input('interactive', 'checked')
)
def change(value):
    return value

@callback(
    Output('card-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href