import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.ProgressBar)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.ProgressBar)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.ProgressBar(
                            id='progress-bar',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='progress-bar-intent',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ]
                        ),
                        dbpc.Switch(
                            label='Known value',
                            id='progress-bar-slider-disabled',
                        ),
                        dbpc.Slider(
                            id='progress-bar-slider',
                            disabled=True,
                            min=0.0,
                            max=1.0,
                            stepSize=0.1,
                            showTrackFill=False,
                            labelPrecision=1
                        )  
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='progressbar-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.ProgressBar)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('progress-bar', 'intent'),
    Input('progress-bar-intent', 'value')
)
def change(value):
    return value

@callback(
    Output('progress-bar-slider', 'disabled'),
    Input('progress-bar-slider-disabled', 'checked')
)
def change(value):

    return not value

@callback(
    Output('progress-bar', 'value'),
    Input('progress-bar-slider', 'value')
)
def change(value):

    return value

@callback(
    Output('progressbar-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href