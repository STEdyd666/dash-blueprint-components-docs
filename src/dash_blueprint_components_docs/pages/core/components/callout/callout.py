import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Callout)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Callout)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Callout(
                            id='callout',
                            children=(
                                'Long-form information about the important content'
                            ),
                            title='Visually important content',
                            intent='danger',
                            className='bp5-running-text'
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='callout-select',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ],
                            fill=True
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='callout-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Callout)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('callout', 'intent'),
    Input('callout-select', 'value')
)
def change_intent(value):

    return value

@callback(
    Output('callout-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href