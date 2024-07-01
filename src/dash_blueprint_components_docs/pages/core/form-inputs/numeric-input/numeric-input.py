import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.NumericInput)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.NumericInput)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.NumericInput(
                            id='numericinput',
                            placeholder='Enter a number',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='numericinput-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='numericinput-fill',
                            children='Fill'
                        ),
                        dbpc.Switch(
                            id='numericinput-large',
                            children='Large'
                        ),
                        dbpc.Switch(
                            id='numericinput-small',
                            children='Small'
                        ),
                        dbpc.Switch(
                            id='numericinput-lefticon',
                            children='Left icon'
                        ),
                        dbpc.Switch(
                            id='numericinput-leftele',
                            children='Left element'
                        ),
                        dbpc.Switch(
                            id='numericinput-onlynumeric',
                            children='Numeric characters only'
                        ),
                        dbpc.Divider(),
                        html.P(children='Button position'),
                        dbpc.HTMLSelect(
                            id='numericinput-selectbutton',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Right', 'value': 'right'},
                                {'label': 'Left', 'value': 'left'},
                            ],
                            value='right'
                        ),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='numericinput-selectintent',
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
            id='numericinput-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.NumericInput)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('numericinput', 'disabled'),
    Input('numericinput-disabled', 'checked')
)
def change(value):
    return value

@callback(
    Output('numericinput', 'fill'),
    Input('numericinput-fill', 'checked')
)
def change(value):

    return value

@callback(
    Output('numericinput', 'large'),
    Output('numericinput', 'small'),
    Output('numericinput-large', 'disabled'),
    Output('numericinput-small', 'disabled'),
    Input('numericinput-large', 'checked'),
    Input('numericinput-small', 'checked')
)
def change(islarge, issmall):
    if islarge:
        return islarge, not islarge, False, True
    elif issmall:
        return not issmall, issmall, True, False
    else:
        return False, False, False, False

@callback(
    Output('numericinput', 'leftIcon'),
    Input('numericinput-lefticon', 'checked')
)
def change(value):
    if value:
        return 'dollar'
    else:
        return None

@callback(
    Output('numericinput', 'leftElement'),
    Input('numericinput-leftele', 'checked')
)
def change(value):
    if value:
        button = dbpc.Button(
            icon='filter'
        )
        return button
    else:
        return None

@callback(
    Output('numericinput', 'allowNumericCharactersOnly'),
    Input('numericinput-onlynumeric', 'checked')
)
def change(value):

    return value

@callback(
    Output('numericinput', 'buttonPosition'),
    Input('numericinput-selectbutton', 'value')
)
def change(value):

    return value

@callback(
    Output('numericinput', 'intent'),
    Input('numericinput-selectintent', 'value')
)
def change(value):

    return value

@callback(
    Output('numericinput-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href