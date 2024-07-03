import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Spinner)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Spinner)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Spinner(
                            id='spinner',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='spinner-intent',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ]
                        ),
                        html.P(children='Size'),
                        dbpc.Slider(
                            id='spinner-slider-size',
                            min=0,
                            max=200,
                            stepSize=50,
                            showTrackFill=False,
                            labelStepSize=50
                        ),
                        dbpc.Switch(
                            id='slider-value-disabled',
                            label='Known value',
                        ),
                        dbpc.Slider(
                            id='spinner-slider-value',
                            disabled=True,
                            min=0.0,
                            max=1.0,
                            stepSize=0.1,
                            showTrackFill=False,
                        ) 
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='spinner-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Spinner)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)



@callback(
    Output('spinner', 'intent'),
    Input('spinner-intent', 'value')
)
def change(value):
    return value

@callback(
    Output('spinner-slider-value', 'disabled'),
    Input('slider-value-disabled', 'checked')
)
def change(value):

    return not value

@callback(
    Output('spinner', 'size'),
    Input('spinner-slider-size', 'value')
)
def change(value):

    return value

@callback(
    Output('spinner', 'value'),
    Input('spinner-slider-value', 'value'),
    Input('slider-value-disabled', 'checked')
)
def change(value, checked):

    if checked:
        return value
    else:
        return None

@callback(
    Output('spinner-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href