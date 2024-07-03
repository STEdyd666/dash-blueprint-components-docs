import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.ContextMenu)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.ContextMenu)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.ContextMenu(
                            id='contextmenu',
                            content=dbpc.Menu(
                                children=[
                                    dbpc.MenuItem(
                                        icon='search-around',
                                        text='Search around'
                                    ),
                                    dbpc.MenuItem(
                                        icon='search',
                                        text='Object viewer'
                                    ),
                                    dbpc.MenuItem(
                                        icon='graph-remove',
                                        text='Remove'
                                    ),
                                    dbpc.MenuItem(
                                        icon='group-objects',
                                        text='Group'
                                    ),
                                    dbpc.MenuDivider(),
                                    dbpc.MenuItem(
                                        disabled=True,
                                        text='Clicked on node'
                                    ),
                                ]
                            ),
                            children=html.Div(
                                id='contextmenubutton',
                                children="Right click me!",
                                style={
                                    'border': 'solid 2px',
                                    'padding': '15px'
                                }
                            )
                        ),
                    ],
                    className='bp5-docs-page-example centered',
                )
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='contextmenu-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.ContextMenu)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('contextmenubutton', 'style'),
    Input('contextmenu', 'isOpen')
)
def change_intent(value):

    if value:
        style={
            'border': 'solid 4px red',
            'padding': '15px'
        }
        return style
    else:
        style={
            'border': 'solid 2px',
            'padding': '15px'
        }
        return style

@callback(
    Output('contextmenu-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href