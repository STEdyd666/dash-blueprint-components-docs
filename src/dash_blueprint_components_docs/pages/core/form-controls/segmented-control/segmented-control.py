import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


options=[
    {
        'label': 'List',
        'value': 'list',
    },
    {
        'label': 'Grid',
        'value': 'grid',
    },
    {
        'label': 'Gallery',
        'value': 'gallery',
    },
    {
        'disabled': True,
        'label': 'Disabled',
        'value': 'disabled',
    },
]

component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.SegmentedControl)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.SegmentedControl)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.SegmentedControl(
                            id='segmented-control',
                            options=options,
                            defaultValue='list',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='segmented-control-inline',
                            children='Inline'
                        ),
                        dbpc.Switch(
                            id='segmented-control-fill',
                            children='Fill'
                        ),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='segmented-control-intent-primary',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                            ]
                        ),
                        html.P(children='size'),
                        dbpc.SegmentedControl(
                            id='segmented-control-size',
                            options=[
                                {'label': 'Small', 'value': 'small'},
                                {'label': 'Regular', 'value': 'regular'},
                                {'label': 'Large', 'value': 'large'}
                            ],
                            defaultValue='regular'
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='segmentedcontrol-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.SegmentedControl)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('segmented-control', 'inline'),
    Input('segmented-control-inline', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('segmented-control', 'fill'),
    Input('segmented-control-fill', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('segmented-control', 'intent'),
    Input('segmented-control-intent-primary', 'value')
)
def change(value):
    return value

@callback(
    Output('segmented-control', 'large'),
    Output('segmented-control', 'small'),
    Input('segmented-control-size', 'value')
)
def change(value):

    if value == 'large':
        return True, False
    elif value == 'small':
        return False, True
    else:
        return False, False

@callback(
    Output('segmentedcontrol-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href