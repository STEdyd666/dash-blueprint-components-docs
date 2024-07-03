import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.FileInput)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.FileInput)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.FileInput(
                            id='fileinput',
                            text='Choose file...',
                            buttonText='Browse'
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='fileinput-large',
                            label='Large',
                        ),
                        dbpc.Switch(
                            id='fileinput-small',
                            label='Small',
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='fileinput-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.FileInput)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('fileinput', 'large'),
    Output('fileinput', 'small'),
    Output('fileinput-large', 'disabled'),
    Output('fileinput-small', 'disabled'),
    Input('fileinput-large', 'checked'),
    Input('fileinput-small', 'checked')
)
def change(islarge, issmall):
    if islarge:
        return islarge, not islarge, False, True
    elif issmall:
        return not issmall, issmall, True, False
    else:
        return False, False, False, False

@callback(
    Output('fileinput-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href