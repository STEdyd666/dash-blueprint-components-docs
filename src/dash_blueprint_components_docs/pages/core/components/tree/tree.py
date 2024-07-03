import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


treecontent = [
    {
        'id': 0,
        'hasCaret': True,
        'icon': "folder-close",
        'label': 'Folder 0'
    },
    {
        'id': 1,
        'hasCaret': True,
        'icon': "folder-close",
        'label': 'Folder 1',
        'isExpanded': True,
        'childNodes': [
            {
                'id': 2,
                'icon': "document",
                'label': 'Item 0',
            },
            {
                'id': 2,
                'icon': 'tag',
                'label': 'Item 0',
            },
            {
                'id': 3,
                'hasCaret': True,
                'icon': "folder-close",
                'label': 'Folder 2',
                'childNodes': [
                    {
                        'id': 4, 
                        'label': "No-Icon item"
                    },
                    {
                        'id': 5,
                        'icon': 'tag',
                        'label': 'Item 1',
                    },
                    {
                        'id': 6,
                        'hasCaret': True,
                        'icon': "folder-close",
                        'label': 'Folder 3',
                        'childNodes': [
                            {
                                'id': 7, 
                                'label': "Item 0"
                            },
                            {
                                'id': 8,
                                'icon': 'tag',
                                'label': 'Item 1',
                            }
                        ]
                    }
                ]
            },
        ]
    },
    {
        'id': 9,
        'hasCaret': True,
        'icon': "folder-close",
        'label': 'Super secret files',
        'disabled': True
    }
]

component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Tree)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Tree)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Tree(
                            id='tree',
                            contents=treecontent
                        ),
                    ],
                    className='bp5-docs-page-example-no-props',
                )
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='tree-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Tree)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)

@callback(
    Output('tree-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href