import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.InputGroup)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.InputGroup)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=dbpc.InputGroup(
                                        id='input-group-1',
                                        leftIcon='filter',
                                        placeholder='Filter histogram...',
                                    ),
                                    style={
                                        'width': '200px',
                                        'margin': '25px'
                                    },
                                ),
                                html.Div(
                                    children=dbpc.InputGroup(
                                        id='input-group-2',
                                        type='password',
                                        rightElement=dbpc.Button(icon='lock', minimal=True)
                                    ),
                                    style={
                                        'width': '200px',
                                        'margin': '25px'
                                    },
                                ),
                                html.Div(
                                    children=dbpc.InputGroup(
                                        id='input-group-3',
                                        leftIcon='tag',
                                        rightElement=dbpc.Tag(children=10000)
                                    ),
                                    style={
                                        'width': '200px',
                                        'margin': '25px',
                                    }
                                ),
                                html.Div(
                                    children=dbpc.InputGroup(
                                        id='input-group-4',
                                        placeholder='Add people or groups...',
                                        rightElement=dbpc.Popover(
                                            content=[
                                                dbpc.Menu(
                                                    children=[
                                                        dbpc.MenuItem(
                                                            text='can edit'
                                                        ),
                                                        dbpc.MenuItem(
                                                            text='can view'
                                                        )
                                                    ]
                                                )
                                            ],
                                            children=dbpc.Button(
                                                children='can edit',
                                                minimal=True, 
                                                rightIcon='caret-down'
                                            )
                                        )
                                    ),
                                    style={
                                        'width': '300px',
                                        'margin': '25px',
                                    }
                                )
                            ],
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='input-group-disabled',
                            label='Disabled',
                        ),
                        dbpc.Switch(
                            id='input-group-large',
                            label='Large',
                        ),
                        dbpc.Switch(
                            id='input-group-small',
                            label='Small',
                        ),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='input-group-intent',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ]
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='inputgroup-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.InputGroup)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)

@callback(
    Output('input-group-1', 'disabled'),
    Output('input-group-2', 'disabled'),
    Output('input-group-3', 'disabled'),
    Output('input-group-4', 'disabled'),
    Input('input-group-disabled', 'checked')
)
def change(value):

    return value, value, value, value

@callback(
    Output('input-group-1', 'large'),
    Output('input-group-2', 'large'),
    Output('input-group-3', 'large'),
    Output('input-group-4', 'large'),
    Output('input-group-1', 'small'),
    Output('input-group-2', 'small'),
    Output('input-group-3', 'small'),
    Output('input-group-4', 'small'),
    Output('input-group-large', 'disabled'),
    Output('input-group-small', 'disabled'),
    Input('input-group-large', 'checked'),
    Input('input-group-small', 'checked')
)
def change(islarge, issmall):
    if islarge:
        return islarge, islarge, islarge, islarge, not islarge, not islarge, not islarge, not islarge, False, True
    elif issmall:
        return not issmall, not issmall, not issmall, not issmall, issmall, issmall, issmall, issmall, True, False
    else:
        return False, False, False, False, False, False, False, False, False, False

@callback(
    Output('input-group-1', 'intent'),
    Output('input-group-2', 'intent'),
    Output('input-group-3', 'intent'),
    Output('input-group-4', 'intent'),
    Input('input-group-intent', 'value')
)
def change(value):

    return value, value, value, value

@callback(
    Output('inputgroup-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href