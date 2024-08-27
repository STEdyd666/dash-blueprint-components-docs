import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Switch)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Switch)['description']),
        html.P('Its whole label is interactive and it supports a few visual modifiers for different UI layouts.'),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.FormGroup(
                            label='Privacy settings',
                            children=[
                                dbpc.Switch(
                                    id='switch-1',
                                    labelElement=html.Strong('Enabled')
                                ),
                                dbpc.Switch(
                                    id='switch-2',
                                    labelElement=html.Em('Public')
                                ),
                                dbpc.Switch(
                                    id='switch-3',
                                    labelElement=html.U('Cooperative')
                                ),
                                dbpc.Switch(
                                    id='switch-4',
                                    labelElement='Containing text'
                                )
                            ],
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='switch-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='switch-inline',
                            children='Inline'
                        ),
                        dbpc.Switch(
                            id='switch-large',
                            children='Large'
                        ),
                        html.P(children='Align indicator'),
                        html.Div(
                        dbpc.SegmentedControl(
                            id='switch-segmented-control',
                            options=[
                                {'label': 'Left', 'value': 'left'},
                                {'label': 'Right', 'value': 'right'}
                            ],
                            value='left',
                        ),
                        style={'max-width': 'fit-content'})
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='switch-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Switch)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('switch-1', 'disabled'),
    Output('switch-2', 'disabled'),
    Output('switch-3', 'disabled'),
    Output('switch-4', 'disabled'),
    Input('switch-disabled', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('switch-1', 'inline'),
    Output('switch-2', 'inline'),
    Output('switch-3', 'inline'),
    Output('switch-4', 'inline'),
    Input('switch-inline', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('switch-1', 'large'),
    Output('switch-2', 'large'),
    Output('switch-3', 'large'),
    Output('switch-4', 'large'),
    Input('switch-large', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('switch-1', 'alignIndicator'),
    Output('switch-2', 'alignIndicator'),
    Output('switch-3', 'alignIndicator'),
    Output('switch-4', 'alignIndicator'),
    Input('switch-segmented-control', 'value')
)
def change(value):
    return value, value, value, value

@callback(
    Output('switch-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href