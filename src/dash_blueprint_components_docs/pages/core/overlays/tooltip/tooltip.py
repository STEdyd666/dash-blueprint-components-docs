import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Tooltip)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Tooltip)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.P('Inline text with '),
                                dbpc.Tooltip(
                                    children='a tooltip.',
                                    content='This tooltip contains a div element.',
                                    className='bp5-tooltip-indicator'
                                )
                            ],
                            style={
                                'display': '-webkit-box',
                                'white-space': 'pre-wrap',
                                'height': '35px'
                            }
                        ),
                        html.Div(
                            dbpc.Tooltip(
                                children='Or, hover anywhere over this whole line.',
                                content='In facilisis scelerisque dui vel dignissim. Sed nunc orci, ultricies congue vehicula quis, facilisis a orci.'
                            ),
                            style={
                                'height': '35px'
                            }
                        ),
                        html.Div(
                            children=[
                                html.P("This line's tooltip  "),
                                dbpc.Tooltip(
                                    children='is disabled.',
                                    disabled=True,
                                    className='bp5-tooltip-indicator'
                                )
                            ],
                            style={
                                'display': '-webkit-box',
                                'white-space': 'pre-wrap',
                                'height': '35px'
                            }
                        ),
                        html.Div(
                            children=[
                                html.P("This line's tooltip  "),
                                dbpc.Tooltip(
                                    children='is minimal.',
                                    minimal=True,
                                    content='This tooltip has the minimal style applied!',
                                    className='bp5-tooltip-indicator'
                                )
                            ],
                            style={
                                'display': '-webkit-box',
                                'white-space': 'pre-wrap',
                                'height': '35px'
                            }
                        ),
                        html.Div(
                            children=[
                                dbpc.Tooltip(
                                    children='Available ',
                                    intent='primary',
                                    content='primary',
                                    className='bp5-tooltip-indicator'
                                ),
                                dbpc.Tooltip(
                                    children='in the full ',
                                    intent='success',
                                    content='success',
                                    className='bp5-tooltip-indicator'
                                ),
                                dbpc.Tooltip(
                                    children='range of ',
                                    intent='warning',
                                    content='warning',
                                    className='bp5-tooltip-indicator'
                                ),
                                dbpc.Tooltip(
                                    children='visual intents!',
                                    intent='danger',
                                    content='danger',
                                    className='bp5-tooltip-indicator'
                                )
                            ],
                            style={
                                'display': '-webkit-box',
                                'white-space': 'pre-wrap',
                                'height': '35px'
                            }
                        ),
                        html.Div(
                            children=dbpc.Popover(
                                content=html.Div(
                                    children='Popover!',
                                    style={
                                       'padding': '20px'
                                    }
                                ),
                                placement='right',
                                children=dbpc.Tooltip(
                                    content='This button also has a popover!',
                                    openOnTargetFocus=False,
                                    placement='right',
                                    children=dbpc.Button(
                                        intent='success',
                                        text='Hover and click me'
                                    )
                                )
                            ),
                            style={
                                'margin': '15px'
                            }
                        ),
                        html.Div(
                            children=dbpc.ButtonGroup(
                                children=[
                                    dbpc.Tooltip(
                                        content='Each',
                                        placement='bottom',
                                        children=dbpc.Button(
                                            intent='primary',
                                            text='Group'
                                        )
                                    ),
                                    dbpc.Tooltip(
                                        content='has',
                                        placement='bottom',
                                        children=dbpc.Button(
                                            intent='primary',
                                            text='of'
                                        )
                                    ),
                                    dbpc.Tooltip(
                                        content='a tooltip',
                                        placement='bottom',
                                        children=dbpc.Button(
                                            intent='primary',
                                            text='buttons'
                                        )
                                    )
                                ]
                            ),
                            style={
                                'margin': '15px'
                            }
                        )
                    ],
                    className='bp5-docs-page-example-no-props centered',
                    style={
                        'flex-direction': 'column'
                    }
                )
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='tooltip-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Tooltip)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('tooltip-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href