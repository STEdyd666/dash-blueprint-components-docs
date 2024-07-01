import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.CompoundTag)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.CompoundTag)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            dbpc.CompoundTag(
                                id='compoundtag-1', 
                                children='London',
                                leftContent='city'
                            ),
                            style={'width': '100%', 'text-align': 'center'}
                        ),
                        html.Div(
                            dbpc.CompoundTag(
                                id='compoundtag-2', 
                                children='New York',
                                leftContent='city'
                            ),
                            style={'width': '100%', 'text-align': 'center'}
                        ),
                        html.Div(
                            dbpc.CompoundTag(
                                id='compoundtag-3', 
                                children='San Francisco',
                                leftContent='city'
                            ),
                            style={'width': '100%', 'text-align': 'center'}
                        ),
                        html.Div(
                            dbpc.CompoundTag(
                                id='compoundtag-4', 
                                children='Seattle',
                                leftContent='city'
                            ),
                            style={'width': '100%', 'text-align': 'center'}
                        )
                    ],
                    className='bp5-docs-page-example centered',
                    style={
                        'flex-direction': 'column',
                        'gap': '15px'
                    }
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='compoundtag-fill',
                            label='Fill',
                        ),
                        dbpc.Switch(
                            id='compoundtag-large',
                            label='Large',
                        ),
                        dbpc.Switch(
                            id='compoundtag-minimal',
                            label='Minimal',
                        ),
                        dbpc.Switch(
                            id='compoundtag-interactive',
                            label='Interactive',
                        ),
                        dbpc.Switch(
                            id='compoundtag-removable',
                            label='Removable',
                        ),
                        dbpc.Switch(
                            id='compoundtag-round',
                            label='Round',
                        ),
                        dbpc.Switch(
                            id='compoundtag-left-icon',
                            label='Left icon',
                        ),
                        dbpc.Switch(
                            id='compoundtag-right-icon',
                            label='Right icon',
                        ),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='compoundtag-intent',
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
            id='compoundtag-source',
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
    Output('compoundtag-1', 'fill'),
    Output('compoundtag-2', 'fill'),
    Output('compoundtag-3', 'fill'),
    Output('compoundtag-4', 'fill'),
    Input('compoundtag-fill', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('compoundtag-1', 'large'),
    Output('compoundtag-2', 'large'),
    Output('compoundtag-3', 'large'),
    Output('compoundtag-4', 'large'),
    Input('compoundtag-large', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('compoundtag-1', 'minimal'),
    Output('compoundtag-2', 'minimal'),
    Output('compoundtag-3', 'minimal'),
    Output('compoundtag-4', 'minimal'),
    Input('compoundtag-minimal', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('compoundtag-1', 'interactive'),
    Output('compoundtag-2', 'interactive'),
    Output('compoundtag-3', 'interactive'),
    Output('compoundtag-4', 'interactive'),
    Input('compoundtag-interactive', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('compoundtag-1', 'removable'),
    Output('compoundtag-2', 'removable'),
    Output('compoundtag-3', 'removable'),
    Output('compoundtag-4', 'removable'),
    Input('compoundtag-removable', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('compoundtag-1', 'round'),
    Output('compoundtag-2', 'round'),
    Output('compoundtag-3', 'round'),
    Output('compoundtag-4', 'round'),
    Input('compoundtag-round', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('compoundtag-1', 'icon'),
    Output('compoundtag-2', 'icon'),
    Output('compoundtag-3', 'icon'),
    Output('compoundtag-4', 'icon'),
    Input('compoundtag-left-icon', 'checked')
)
def change(value):

    if value:
        return 'home', 'home', 'home', 'home'
    else:
        return None, None, None, None

@callback(
    Output('compoundtag-1', 'rightIcon'),
    Output('compoundtag-2', 'rightIcon'),
    Output('compoundtag-3', 'rightIcon'),
    Output('compoundtag-4', 'rightIcon'),
    Input('compoundtag-right-icon', 'checked')
)
def change(value):
    
    if value:
        return 'map', 'map', 'map', 'map'
    else:
        return None, None, None, None

@callback(
    Output('compoundtag-1', 'intent'),
    Output('compoundtag-2', 'intent'),
    Output('compoundtag-3', 'intent'),
    Output('compoundtag-4', 'intent'),
    Input('compoundtag-intent', 'value')
)
def change(value):
    return value, value, value, value

@callback(
    Output('compoundtag-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href