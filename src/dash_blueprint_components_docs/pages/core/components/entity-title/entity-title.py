import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.EntityTitle)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.EntityTitle)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            id='entitytitle-div',
                            children=dbpc.EntityTitle(
                                id='entitytitle',
                                title='Buy groceries on my way home',
                            ),
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        html.P(children='heading'),
                        dbpc.HTMLSelect(
                            id='entitytitle-heading',
                            options=[
                                {'label': 'Text', 'value': 'Text'},
                                {'label': 'H1', 'value': 'H1'},
                                {'label': 'H2', 'value': 'H2'},
                                {'label': 'H3', 'value': 'H3'},
                                {'label': 'H4', 'value': 'H4'},
                                {'label': 'H5', 'value': 'H5'},
                                {'label': 'H6', 'value': 'H6'},
                            ],
                            value='H4'
                        ),
                        dbpc.Switch(
                            id='entitytitle-ellipsize',
                            children='Ellipsize',
                        ),
                        dbpc.Switch(
                            id='entitytitle-icon',
                            children='Display icon',
                            defaultChecked=True
                        ), 
                        dbpc.Switch(
                            id='entitytitle-loading',
                            children='Loading',
                        ), 
                        dbpc.Switch(
                            id='entitytitle-subtitle',
                            children='Display subtitle',
                        ),
                        dbpc.Switch(
                            id='entitytitle-tag',
                            children='Display tag',
                        ),                      
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='entitytitle-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.EntityTitle)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('entitytitle', 'heading'),
    Input('entitytitle-heading', 'value')
)
def change(value):
    return value

@callback(
    Output('entitytitle', 'ellipsize'),
    Output('entitytitle-div', 'style'),
    Input('entitytitle-ellipsize', 'checked')
)
def change(value):
    if value:
        return value, {'width': '225px'}
    
    return value, {}

@callback(
    Output('entitytitle', 'icon'),
    Input('entitytitle-icon', 'checked')
)
def change(value):
    if not value:
        return 'shop'
    return None

@callback(
    Output('entitytitle', 'loading'),
    Input('entitytitle-loading', 'checked')
)
def change(value):
    return value

@callback(
    Output('entitytitle', 'subtitle'),
    Input('entitytitle-subtitle', 'checked')
)
def change(value):
    if value:
        return "Reminder set for today at 6:00 PM"
    return None

@callback(
    Output('entitytitle', 'tags'),
    Input('entitytitle-tag', 'checked')
)
def change(value):
    if value:
        tag = dbpc.Tag(
            intent='danger',
            minimal=True,
            children='Due today'
        )
        return tag

    return None

@callback(
    Output('entitytitle-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href