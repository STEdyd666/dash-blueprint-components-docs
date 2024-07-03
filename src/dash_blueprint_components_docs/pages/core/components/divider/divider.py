import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Divider)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Divider)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.ButtonGroup(
                            id='divider-buttongroup',
                            children=[
                                dbpc.Button(text='File'),
                                dbpc.Button(text='Edit'),
                                dbpc.Divider(),
                                dbpc.Button(text='Delete'),
                                dbpc.Button(text='Create'),
                                dbpc.Divider(),
                                dbpc.Button(icon='add'),
                                dbpc.Button(icon='remove')
                            ],
                            minimal=True
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='divider-vertical',
                            children='Vertical',
                            checked=False
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='divider-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Divider)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('divider-buttongroup', 'vertical'),
    Input('divider-vertical', 'checked')
)
def change(value):

    return value

@callback(
    Output('divider-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href