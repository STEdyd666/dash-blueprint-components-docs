import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


radiooptions = [
    {'label': 'Soup', 'value': 'one', 'disabled': True},
    {'label': 'Salad', 'value': 'two'},
    {'label': 'Sandwich', 'value': 'three'}
]

component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.RadioGroup)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.RadioGroup)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.RadioGroup(
                            id='radio',
                            options=radiooptions,
                            label="Determine lunch"
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='radio-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='radio-inline',
                            children='Inline'
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='radio-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.RadioGroup)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('radio', 'disabled'),
    Input('radio-disabled', 'checked')
)
def change(value):

    return value

@callback(
    Output('radio', 'inline'),
    Input('radio-inline', 'checked')
)
def change(value):

    return value

@callback(
    Output('radio-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href