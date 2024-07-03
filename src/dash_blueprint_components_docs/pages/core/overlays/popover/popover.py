import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Popover)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Popover)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                         dbpc.Popover(
                                            id='popover',
                                            children = dbpc.Button(
                                                id='popover-button',
                                                intent='primary', 
                                                text='Popover target'
                                            ),
                                            content=html.Div(
                                                children=[
                                                    html.Div('Confirm deletion', className='bp5-heading'),
                                                    html.P("Are you sure you want to delete these items? You won't be able to recover them."),
                                                    html.Div(
                                                        children=[
                                                            dbpc.Button(
                                                                children='Cancel',
                                                                style={
                                                                    'margin-right': 10
                                                                },
                                                                className='bp5-popover-dismiss'
                                                            ),
                                                            dbpc.Button(
                                                                children='Delete',
                                                                intent='danger',
                                                                className='bp5-popover-dismiss'
                                                            )
                                                        ],
                                                        style={
                                                            'display': 'flex',
                                                            'justify-content': 'flex-end',
                                                            'margin-top': 15
                                                        }
                                                    )
                                                ],
                                                style={
                                                    'padding': '20px'
                                                }
                                            )
                                        ),
                                        html.Div(
                                            children='Scroll around this container to experiment with flip and preventOverflow modifiers.',
                                            style={
                                                'width': '200px',
                                                'margin-top': '10px'
                                            }
                                        )
                                    ],
                                    style={
                                        'align-items': 'center',
                                        'display': 'flex',
                                        'flex-direction': 'column',
                                        'height': '1700px',
                                        'justify-content': 'center',
                                        'width': '1600px',
                                        'margin': 0
                                    }
                                )
                            ],
                            style={
                                'display': 'block',
                                'position': 'relative',
                                'max-height': '785px',
                                'overflow': 'scroll',
                                'padding': 0
                            }
                        ),
                    ],
                    className='bp5-docs-page-example centered',
                    style={
                        'padding': 0
                    }
                ),
                html.Div(
                    children=[
                        html.H4('Appearance'),
                        html.P(children='Position when opened'),  
                        dbpc.HTMLSelect(
                            id='popover-position',
                            options=[
                                {'label': 'top', 'value': 'top'},
                                {'label': 'top-start', 'value': 'top-start'},
                                {'label': 'top-end', 'value': 'top-end'},
                                {'label': 'bottom', 'value': 'bottom'},
                                {'label': 'bottom-start', 'value': 'bottom-start'},
                                {'label': 'bottom-end', 'value': 'bottom-end'},
                                {'label': 'right', 'value': 'right'},
                                {'label': 'right-start', 'value': 'right-start'},
                                {'label': 'right-end', 'value': 'right-end'},
                                {'label': 'left', 'value': 'left'},
                                {'label': 'left-start', 'value': 'left-start'},
                                {'label': 'left-end', 'value': 'left-end'},
                                {'label': 'auto', 'value': 'auto'},
                                {'label': 'auto-start', 'value': 'auto-start'},
                                {'label': 'auto-end', 'value': 'auto-end'},
                            ],
                            value='auto'
                        ),
                        dbpc.Switch(
                            id='popover-minimal',
                            children='Minimal appearance',
                        ),
                        html.H4('Interactions'),
                        html.P(children='Interaction kind'),
                        dbpc.RadioGroup(
                            id='popover-interaction',
                            options=[
                                {'label': 'Click', 'value': 'click' },
                                {'label': 'Click (target only)', 'value': 'click-target' },
                                {'label': 'Hover', 'value': 'hover' },
                                {'label': 'Hover (target only)', 'value': 'hover-target' },
                            ],
                            selectedValue='click'
                        ),
                        dbpc.Divider(),
                        dbpc.Switch(
                            id='popover-escape',
                            children='Can escape key close',
                            defaultChecked=True
                        ),
                        html.H4('Modifiers'),
                        dbpc.Switch(
                            id='popover-match-width',
                            children='Match target width',
                            defaultChecked=False
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='popover-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Popover)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('popover', 'position'),
    Input('popover-position', 'value')
)
def change(value):

    return value

@callback(
    Output('popover', 'minimal'),
    Input('popover-minimal', 'checked')
)
def change(value):

    return value

@callback(
    Output('popover', 'interactionKind'),
    Input('popover-interaction', 'selectedValue')
)
def change(value):

    return value

@callback(
    Output('popover', 'canEscapeKeyClose'),
    Input('popover-escape', 'checked')
)
def change(value):
    return not value

@callback(
    Output('popover', 'matchTargetWidth'),
    Output('popover-button', 'text'),
    Input('popover-match-width', 'checked')
)
def change(value):
    if value:
        return value, '(Slightly wider) popover target'
    else:
        return value, 'Popover target'

@callback(
    Output('popover-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href