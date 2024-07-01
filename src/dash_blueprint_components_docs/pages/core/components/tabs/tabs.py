import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Tabs)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Tabs)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Tabs(
                            id='tabs',
                            defaultSelectedTabId='react',
                            animate=True,
                            children=[
                                dbpc.Tab(
                                    id='react',
                                    panel=html.Div(
                                        children=[
                                            html.H5('Example panel: React'),
                                            html.P("""
                                                Lots of people use React as the V in MVC. Since React makes no assumptions about 
                                                the rest of your technology stack, it's easy to try it out on a small feature in an existing 
                                                project.
                                            """)
                                        ]
                                    ),
                                    title='React'
                                ),
                                dbpc.Tab(
                                    id='angular',
                                    panel=html.Div(
                                        children=[
                                            html.H5('Example panel: Angular'),
                                            html.P("""
                                                HTML is great for declaring static documents, but it falters when we try to use it for declaring 
                                                dynamic views in web-applications. AngularJS lets you extend HTML vocabulary for your application. 
                                                The resulting environment is extraordinarily expressive, readable, and quick to develop.
                                            """)
                                        ],
                                    ),
                                    title='Angular'
                                )
                            ],
                        )
                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='tabs-vertical',
                            label='Vertical',
                        ),
                        dbpc.Switch(
                            id='tabs-large',
                            label='Large size',
                        ),
                        dbpc.Switch(
                            id='tabs-animate',
                            label='Animate tab indicator',
                            defaultChecked=True
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='tabs-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H1('Usage'),
        html.P(inspect.cleandoc("""
            Tab selection is managed by id. This is more reliable than using a numeric index as it does not require 
            translating between arbitrary indices and tab names. It does, however, require that every <Tab> have a 
            locally unique id value.
        """)),
        html.P('Arbitrary elements are supported in the tab list, and order is respected. Yes, you can even insert things between <Tab> elements.'),
        html.H2('Props interface'),
        html.H4('Tabs'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Tabs)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H4('Tab'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Tab)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('tabs', 'vertical'),
    Input('tabs-vertical', 'checked')
)
def change(value):

    return value

@callback(
    Output('tabs', 'large'),
    Input('tabs-large', 'checked')
)
def change(value):

    return value

@callback(
    Output('tabs', 'animate'),
    Input('tabs-animate', 'checked')
)
def change(value):
    
    return not value

@callback(
    Output('tabs-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href