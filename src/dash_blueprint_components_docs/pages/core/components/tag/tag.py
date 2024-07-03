import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Tag)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Tag)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(dbpc.Tag(id='tag-1', children='London'), style={'margin': '10px', 'width': '100%', 'text-align': 'center'}),
                        html.Div(dbpc.Tag(id='tag-2', children='New York'), style={'margin': '10px', 'width': '100%', 'text-align': 'center'}),
                        html.Div(dbpc.Tag(id='tag-3', children='San Francisco'), style={'margin': '10px', 'width': '100%', 'text-align': 'center'}),
                        html.Div(dbpc.Tag(id='tag-4', children='Seattle'), style={'margin': '10px', 'width': '100%', 'text-align': 'center'})
                    ],
                    className='bp5-docs-page-example centered',
                    style={'flex-direction': 'column'}
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='tag-fill',
                            label='Fill',
                        ),
                        dbpc.Switch(
                            id='tag-large',
                            label='Large',
                        ),
                        dbpc.Switch(
                            id='tag-minimal',
                            label='Minimal',
                        ),
                        dbpc.Switch(
                            id='tag-interactive',
                            label='Interactive',
                        ),
                        dbpc.Switch(
                            id='tag-removable',
                            label='Removable',
                        ),
                        dbpc.Switch(
                            id='tag-round',
                            label='Round',
                        ),
                        dbpc.Switch(
                            id='tag-left-icon',
                            label='Left icon',
                        ),
                        dbpc.Switch(
                            id='tag-right-icon',
                            label='Right icon',
                        ),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='tag-intent',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ]
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='tag-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Tag)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('tag-1', 'fill'),
    Output('tag-2', 'fill'),
    Output('tag-3', 'fill'),
    Output('tag-4', 'fill'),
    Input('tag-fill', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('tag-1', 'large'),
    Output('tag-2', 'large'),
    Output('tag-3', 'large'),
    Output('tag-4', 'large'),
    Input('tag-large', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('tag-1', 'minimal'),
    Output('tag-2', 'minimal'),
    Output('tag-3', 'minimal'),
    Output('tag-4', 'minimal'),
    Input('tag-minimal', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('tag-1', 'interactive'),
    Output('tag-2', 'interactive'),
    Output('tag-3', 'interactive'),
    Output('tag-4', 'interactive'),
    Input('tag-interactive', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('tag-1', 'removable'),
    Output('tag-2', 'removable'),
    Output('tag-3', 'removable'),
    Output('tag-4', 'removable'),
    Input('tag-removable', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('tag-1', 'round'),
    Output('tag-2', 'round'),
    Output('tag-3', 'round'),
    Output('tag-4', 'round'),
    Input('tag-round', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('tag-1', 'icon'),
    Output('tag-2', 'icon'),
    Output('tag-3', 'icon'),
    Output('tag-4', 'icon'),
    Input('tag-left-icon', 'checked')
)
def change(value):

    if value:
        return 'home', 'home', 'home', 'home'
    else:
        return None, None, None, None

@callback(
    Output('tag-1', 'rightIcon'),
    Output('tag-2', 'rightIcon'),
    Output('tag-3', 'rightIcon'),
    Output('tag-4', 'rightIcon'),
    Input('tag-right-icon', 'checked')
)
def change(value):
    
    if value:
        return 'map', 'map', 'map', 'map'
    else:
        return None, None, None, None

@callback(
    Output('tag-1', 'intent'),
    Output('tag-2', 'intent'),
    Output('tag-3', 'intent'),
    Output('tag-4', 'intent'),
    Input('tag-intent', 'value')
)
def change(value):
    return value, value, value, value

@callback(
    Output('tag-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href