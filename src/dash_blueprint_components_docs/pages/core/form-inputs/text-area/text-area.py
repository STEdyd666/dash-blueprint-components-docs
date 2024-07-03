import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.TextArea)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.TextArea)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.TextArea(
                            id='textarea',
                            placeholder='Type something...'
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Appearance props'),
                        dbpc.Switch(
                            id='textarea-large',
                            children='Large'
                        ),
                        dbpc.Switch(
                            id='textarea-small',
                            children='Small',
                        ),
                        dbpc.Divider(),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='textarea-selectintent',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ]
                        ),
                        html.H4('Behaviour props'),
                        dbpc.Switch(
                            id='textarea-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='textarea-readonly',
                            children='Read-only'
                        ),
                        dbpc.Switch(
                            id='textarea-autoresize',
                            children='Auto resize',
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='textarea-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.TextArea)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('textarea', 'large'),
    Output('textarea', 'small'),
    Output('textarea-large', 'disabled'),
    Output('textarea-small', 'disabled'),
    Input('textarea-large', 'checked'),
    Input('textarea-small', 'checked')
)
def change(islarge, issmall):
    if islarge:
        return islarge, not islarge, False, True
    elif issmall:
        return not issmall, issmall, True, False
    else:
        return False, False, False, False

@callback(
    Output('textarea', 'intent'),
    Input('textarea-selectintent', 'value')
)
def change(value):

    return value

@callback(
    Output('textarea', 'disabled'),
    Input('textarea-disabled', 'checked')
)
def change(value):

    return value

@callback(
    Output('textarea', 'readOnly'),
    Input('textarea-readonly', 'checked')
)
def change(value):

    return value

@callback(
    Output('textarea', 'autoResize'),
    Input('textarea-autoresize', 'checked')
)
def change(value):

    return value

@callback(
    Output('textarea-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href


