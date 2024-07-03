import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Breadcrumb)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Breadcrumb)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Card(
                            id='breadcrumb-card',
                            children=[
                                dbpc.Breadcrumb(
                                    id='breadcrumb',
                                    items=[
                                        {'icon': "folder-close", 'text': "All files"},
                                        {'icon': "folder-close", 'text': "Users"},
                                        {'icon': "folder-close", 'text': "Janet"},
                                        {'href': "#", 'icon': "folder-close", 'text': "Photos"},
                                        {'href': "#", 'icon': "folder-close", 'text': "Wednesday"},
                                        {'icon': "document", 'text': "image.jpg", 'current': 'true'},
                                    ],
                                    collapseFrom='start',
                                    alwaysRenderOverflow=False,
                                )
                            ],
                            style={
                                'width': '50%'
                            }
                        )

                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        dbpc.Checkbox(
                            id='overflow-list',
                            children='Overflow list',
                            checked=False
                        ),
                        dbpc.RadioGroup(
                            id='radio',
                            label='Collapse from',
                            options=[
                                {'label': 'Start', 'value': 'start'},
                                {'label': 'end', 'value': 'end'}
                            ],
                            inline=True,
                            selectedValue='start'
                        ),
                        html.P('Width'),
                        dbpc.Slider(
                            id='slider',
                            labelStepSize=50,
                            max=100,
                            showTrackFill=False,
                            value=50,
                            format='percentage'
                        )                  
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='breadcrumb-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Breadcrumb)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('breadcrumb-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href

@callback(
    Output('breadcrumb', 'alwaysRenderOverflow'),
    Input('overflow-list', 'checked')
)
def change(value):
    return value

@callback(
    Output('breadcrumb', 'collapseFrom'),
    Input('radio', 'selectedValue')
)
def change(value):
    return value

@callback(
    Output('breadcrumb-card', 'style'),
    Input('slider', 'value')
)
def change(value):
    return {'width': f'{value}%'}