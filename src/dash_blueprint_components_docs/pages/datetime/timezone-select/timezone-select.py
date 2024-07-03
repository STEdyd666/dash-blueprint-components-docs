import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.TimezoneSelect)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.TimezoneSelect)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            dbpc.TimezoneSelect(
                                id='timezone',
                            ),
                            className='centered'
                        ),
                        html.Div(
                            children=dbpc.Tag(
                                children='none',
                                id='timezone-output',
                                intent='primary',
                            ),
                            className='centered',
                            style={
                                'margin-top': '10px'
                            }
                        )
                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='timezone-showtz',
                            children='Show local timezone'
                        ),
                        dbpc.Switch(
                            id='timezone-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='timezone-fill',
                            children='Fill container width'
                        ),
                        html.P(children='Display format'),
                        dbpc.RadioGroup(
                            id='timezone-format',
                            options=[
                                {'label': 'Composite', 'value': 'composite' },
                                {'label': 'Abbreviation', 'value': 'abbreviation' },
                                {'label': 'Long Name', 'value': 'long name' },
                                {'label': 'IANA Code', 'value': 'code' },
                                {'label': 'Offset', 'value': 'offset' },
                            ],
                            selectedValue='composite'
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='timezoneselect-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.TimezoneSelect)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)

@callback(
    Output('timezone', 'showLocalTimezone'),
    Input('timezone-showtz', 'checked')
)
def change_intent(value):

    return value

@callback(
    Output('timezone', 'disabled'),
    Input('timezone-disabled', 'checked')
)
def change_intent(value):
    return value

@callback(
    Output('timezone', 'fill'),
    Input('timezone-fill', 'checked')
)
def change_intent(value):

    return value

@callback(
    Output('timezone', 'valueDisplayFormat'),
    Input('timezone-format', 'selectedValue')
)
def change_intent(value):

    return value

@callback(
    Output('timezone-output', 'children'),
    Input('timezone', 'value')
)
def change(value):

    if value:
        return value
    else:
        return 'none'

@callback(
    Output('timezoneselect-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href