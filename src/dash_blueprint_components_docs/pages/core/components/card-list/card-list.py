import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.CardList)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.CardList)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.CardList(
                            id='cardlist',
                            children=[
                                dbpc.Card('Basil', interactive=True),
                                dbpc.Card('Olive oil', interactive=True),
                                dbpc.Card('Kosher salt', interactive=True),
                                dbpc.Card('Garlic', interactive=True),
                                dbpc.Card('Pine nuts', interactive=True),
                                dbpc.Card('Parmigiano reggiano', interactive=True)
                            ],
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        dbpc.Switch(
                            id='cardlist-bordered',
                            children='Bordered',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='cardlist-compact',
                            children='Compact'
                        ), 
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='cardlist-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.CardList)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('cardlist', 'bordered'),
    Input('cardlist-bordered', 'checked')
)
def change(value):
    return not value

@callback(
    Output('cardlist', 'compact'),
    Input('cardlist-compact', 'checked')
)
def change(value):
    return value

@callback(
    Output('cardlist-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href