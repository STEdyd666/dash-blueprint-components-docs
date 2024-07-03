import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output, State
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


text = ("""[11:53:30] Finished 'typescript-bundle-blueprint'
[11:53:30] Starting 'typescript-typings-blueprint'...
[11:53:30] Finished 'typescript-typings-blueprint'
[11:53:30] write ./blueprint.css
[11:53:30] Finished 'sass-compile-blueprint'
""")

component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Collapse)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Collapse)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dbpc.Button(
                                    id='open-collapse',
                                    children='Show build logs'
                                ),
                                dbpc.Collapse(
                                    id='collapse',
                                    children=html.Pre(text),
                                    className='bp5-code-block'
                                )
                            ]
                        )
                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='select',
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
            id='collapse-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Collapse)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('collapse', 'isOpen'),
    Input('open-collapse', 'n_clicks'),
    State('collapse', 'isOpen'),
)
def change_intent(_, isOpen):
    if isOpen:
        return False
    else:
        return True

@callback(
    Output('collapse-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href