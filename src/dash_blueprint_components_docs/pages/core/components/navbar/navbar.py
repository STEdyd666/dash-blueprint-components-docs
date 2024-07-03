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
        html.H1(parse_docstring(dbpc.Navbar)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Navbar)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Navbar(
                            children=[
                                dbpc.NavbarGroup(
                                    id='navbar-group',
                                    children=[
                                        dbpc.NavbarHeading('Blueprint'),
                                        dbpc.NavbarDivider(),
                                        dbpc.Button(
                                            icon='home',
                                            text='Home',
                                            minimal=True
                                        ),
                                        dbpc.Button(
                                            icon='document',
                                            text='Files',
                                            minimal=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='navbar-align',
                            children='Align right'
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='navbar-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H1('Usage'),
        html.P('The Navbar API includes four stateless React components:'),
        html.Ul(
            children=[
                html.Li('Navbar'),
                html.Li('NavbarGroup'),
                html.Li('NavbarHeading'),
                html.Li('NavbarDivider'),
            ],
            className='bp5-list'
        ),
        html.P('These components are simple containers for their children.'),
        html.H2('Fixed to viewport top'),
        html.P(
            inspect.cleandoc('''
                Enable the fixedToTop prop to attach a navbar to the top of the viewport using position: fixed; top: 0;. 
                This is so-called "sticky" behavior: the navbar stays at the top of the screen as the user scrolls through the document.
            '''
            )
        ),
        html.P('This modifier is not illustrated here because it breaks the document flow.'),
        dbpc.Callout(
            title='Body padding required',
            intent='danger',
            children='The fixed navbar will lie on top of your other content unless you add padding to the top of the <body> element equal to the height of the navbar. Use the $pt-navbar-height Sass variable.'
        ),
        html.H2('Props interface'),
        html.H4('Navbar'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Navbar)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H4('Navbar group'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.NavbarGroup)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H4('Navbar heading'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.NavbarHeading)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H4('Navbar divider'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.NavbarDivider)['props'])
                )
            ],
            className='bp5-html-table'
        ),
    ]
)


@callback(
    Output('navbar-group', 'align'),
    Input('navbar-align', 'checked')
)
def change(value):
    if value:
        return 'right'
    else:
        return 'left'

@callback(
    Output('navbar-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href