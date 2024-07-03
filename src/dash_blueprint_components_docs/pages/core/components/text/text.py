import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Text)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Text)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Text(
                            id='text',
                            children=(
                                inspect.cleandoc("""
                                    You can change the text in the input below. Hover to see full text. " +
                                    "If the text is long enough, then the content will overflow. This is done by setting " +
                                    "ellipsize to true.
                                """
                                )
                            ),
                        )
                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='text-ellipsize',
                            label='Ellipsize',
                            defaultChecked=True
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='text-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Text)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('text', 'ellipsize'),
    Input('text-ellipsize', 'checked')
)
def change(value):
    return not value

@callback(
    Output('text-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href