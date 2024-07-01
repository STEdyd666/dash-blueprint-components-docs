import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.HTMLSelect)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.HTMLSelect)['description']),
        dbpc.Callout(
            children=inspect.cleandoc("""The Select component in the @blueprintjs/select package provides a more full-features 
            alternative to the native HTML <select> tag. Notably, it supports custom filtering logic and item rendering.
            """),
            intent='success',
            icon='info-sign'
        ),
        html.H2('Usage'),
        html.P(
            inspect.cleandoc("""
                Use HTMLSelect exactly like you would use a native <select> with value (or defaultValue). 
                Options can be passed as <option> children for full flexibility or via the options prop for simple shorthand.
            """
            )
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.HTMLSelect(
                            id='html-select',
                            options=[
                                'One',
                                'Two',
                                'Three',
                                'Four'
                            ],
                            iconName='double-caret-vertical',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='html-select-fill',
                            children='Fill'
                        ),
                        dbpc.Switch(
                            id='html-select-large',
                            children='Large'
                        ),
                        dbpc.Switch(
                            id='html-select-minimal',
                            children='Minimal'
                        ),
                        dbpc.Switch(
                            id='html-select-disabled',
                            children='Disabled'
                        ),
                        html.P(children='icon'),
                        dbpc.HTMLSelect(
                            id='html-select-icon',
                            options=[
                                {'label': 'double-caret-vertical', 'value': 'double-caret-vertical'},
                                {'label': 'caret-down', 'value': 'caret-down'},
                            ],
                            value='double-caret-vertical'
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='htmlselect-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.HTMLSelect)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('html-select', 'fill'),
    Input('html-select-fill', 'checked')
)
def change(value):

    return value

@callback(
    Output('html-select', 'large'),
    Input('html-select-large', 'checked')
)
def change(value):

    return value

@callback(
    Output('html-select', 'minimal'),
    Input('html-select-minimal', 'checked')
)
def change(value):

    return value

@callback(
    Output('html-select', 'disabled'),
    Input('html-select-disabled', 'checked')
)
def change(value):

    return value

@callback(
    Output('html-select', 'iconName'),
    Input('html-select-icon', 'value')
)
def change(value):

    return value

@callback(
    Output('htmlselect-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href