import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.TimePicker)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.TimePicker)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            dbpc.TimePicker(
                                id='timepicker',
                            ),
                            className='centered'
                        ),
                        html.Div(
                            children=dbpc.Tag(
                                children='none',
                                id='timepicker-output',
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
                            id='timepicker-selectfocus',
                            children='Select all on focus'
                        ),
                        dbpc.Switch(
                            id='timepicker-timearrows',
                            children='Show arrow buttons'
                        ),
                        dbpc.Switch(
                            id='timepicker-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='timepicker-ampm',
                            children='Use AM/PM'
                        ),
                        dbpc.Switch(
                            id='timepicker-autofocus',
                            children='Auto focus',
                            defaultChecked=True
                        ),
                        html.P(children='precision'),
                        dbpc.HTMLSelect(
                            id='timepicker-precision',
                            options=[
                                {'label': 'Minute', 'value': 'minute'},
                                {'label': 'Second', 'value': 'second'},
                                {'label': 'Millisecond', 'value': 'millisecond'},
                            ]
                        ),
                        html.P(children='Minimum time'),
                        dbpc.HTMLSelect(
                            id='timepicker-min',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': '6pm (18:00)', 'value': '1970-01-01T18:00:00'},
                            ]
                        ),
                        html.P(children='Maximum time'),
                        dbpc.HTMLSelect(
                            id='timepicker-max',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': '6pm (18:00)', 'value': '1970-01-01T18:00:00'},
                                {'label': '9pm (21:00)', 'value': '1970-01-01T21:00:00'},
                                {'label': '2am (02:00)', 'value': '1970-01-01T02:00:00'},
                            ]
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='timepicker-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.TimePicker)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('timepicker', 'selectAllOnFocus'),
    Input('timepicker-selectfocus', 'checked')
)
def change(value):

    return value

@callback(
    Output('timepicker', 'showArrowButtons'),
    Input('timepicker-timearrows', 'checked')
)
def change(value):

    return value

@callback(
    Output('timepicker', 'disabled'),
    Input('timepicker-disabled', 'checked')
)
def change(value):

    return value

@callback(
    Output('timepicker', 'useAmPm'),
    Input('timepicker-ampm', 'checked')
)
def change(value):

    return value

@callback(
    Output('timepicker', 'autoFocus'),
    Input('timepicker-autofocus', 'checked')
)
def change(value):

    return not value

@callback(
    Output('timepicker', 'precision'),
    Input('timepicker-precision', 'value')
)
def change(value):

    return value

@callback(
    Output('timepicker', 'minTime'),
    Input('timepicker-min', 'value')
)
def change(value):

    return value

@callback(
    Output('timepicker', 'maxTime'),
    Input('timepicker-max', 'value')
)
def change(value):

    return value

@callback(
    Output('timepicker-output', 'children'),
    Input('timepicker', 'value')
)
def change(value):

    if value:
        return value
    else:
        return 'none'

@callback(
    Output('timepicker-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href