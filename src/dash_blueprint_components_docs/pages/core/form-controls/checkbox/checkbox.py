import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Checkbox)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Checkbox)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.FormGroup(
                            id='checkbox',
                            label='Lunch special',
                            children=[
                                dbpc.Checkbox(
                                    id='checkbox-1',
                                    label='Soup',
                                    defaultIndeterminate=True
                                ),
                                dbpc.Checkbox(
                                    id='checkbox-2',
                                    label='Salad',
                                ),
                                dbpc.Checkbox(
                                    id='checkbox-3',
                                    label='Sandwich',
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
                            id='checkbox-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='checkbox-inline',
                            children='Inline'
                        ),
                        dbpc.Switch(
                            id='checkbox-large',
                            children='Large'
                        ),
                        html.P(children='Align indicator'),
                        html.Div(
                            children=dbpc.SegmentedControl(
                                id='checkbox-segmented-control',
                                options=[
                                    {'label': 'Left', 'value': 'left'},
                                    {'label': 'Right', 'value': 'right'}
                                ],
                                defaultValue='left',
                            ),
                            style={'max-width': 'fit-content'}
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='checkbox-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Checkbox)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('checkbox-1', 'disabled'),
    Output('checkbox-2', 'disabled'),
    Output('checkbox-3', 'disabled'),
    Input('checkbox-disabled', 'checked')
)
def change(value):

    return value, value, value

@callback(
    Output('checkbox-1', 'inline'),
    Output('checkbox-2', 'inline'),
    Output('checkbox-3', 'inline'),
    Input('checkbox-inline', 'checked')
)
def change(value):

    return value, value, value

@callback(
    Output('checkbox-1', 'large'),
    Output('checkbox-2', 'large'),
    Output('checkbox-3', 'large'),
    Input('checkbox-large', 'checked')
)
def change(value):

    return value, value, value

@callback(
    Output('checkbox-1', 'alignIndicator'),
    Output('checkbox-2', 'alignIndicator'),
    Output('checkbox-3', 'alignIndicator'),
    Input('checkbox-segmented-control', 'value')
)
def change(value):
    return value, value, value

@callback(
    Output('checkbox-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href