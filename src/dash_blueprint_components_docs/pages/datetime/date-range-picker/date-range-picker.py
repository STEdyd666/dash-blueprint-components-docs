import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.DateRangePicker)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.DateRangePicker)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=dbpc.DateRangePicker(
                                id='daterangepicker',
                            ),
                            className='centered'
                        ),
                        html.Div(
                            children=[
                                dbpc.Tag(
                                    children='none',
                                    id='daterangepicker-output-start',
                                    intent='primary',
                                ),
                                dbpc.Tag(
                                    children='none',
                                    id='daterangepicker-output-end',
                                    intent='primary',
                                ),
                            ],
                            className='centered',
                            style={
                                'margin-top': '10px',
                                'display': 'flex'
                            }
                        )
                    ],
                    className='bp5-docs-page-example',
                    style={
                        'width': '785px',
                        'max-width': '785px'
                    }
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dbpc.Switch(
                                    id='daterangepicker-shortcuts',
                                    children='Show shortcuts',
                                    defaultChecked=True
                                ),
                                dbpc.Switch(
                                    id='daterangepicker-singleday',
                                    children='Allow single day range'
                                ),
                                dbpc.Switch(
                                    id='daterangepicker-singlemonth',
                                    children='Single month only'
                                ),
                                dbpc.Switch(
                                    id='daterangepicker-contiguousmonth',
                                    children='Constrain calendar to contiguous months',
                                    defaultChecked=True
                                ),
                                dbpc.Switch(
                                    id='daterangepicker-reversemonthyear',
                                    children='Reverse month and year menus'
                                ),
                            ],
                            style={
                                'margin': '10px'
                            }
                        ),
                        html.Div(
                            children=[
                                html.P(children='Minimum date'),
                                dbpc.HTMLSelect(
                                    id='daterangepicker-min',
                                    style={
                                        'margin-bottom': '10px'
                                    }
                                ),
                                html.P(children='Maximum date'),
                                dbpc.HTMLSelect(
                                    id='daterangepicker-max',
                                ),
                            ],
                            style={
                                'margin': '10px'
                            }
                        ),
                        html.Div(
                            children=[
                                html.P(children='Time precision'),
                                dbpc.HTMLSelect(
                                    id='daterangepicker-timeprecision',
                                    options=[
                                        {'label': 'None', 'value': 'none'},
                                        {'label': 'Minute', 'value': 'minute'},
                                        {'label': 'Second', 'value': 'second'},
                                        {'label': 'Millisecond', 'value': 'millisecond'},
                                    ],
                                    style={
                                        'margin-bottom': '10px'
                                    }
                                ),
                                dbpc.Switch(
                                    id='daterangepicker-timearrows',
                                    children='Show time picker arrows'
                                ),
                                dbpc.Switch(
                                    id='daterangepicker-ampm',
                                    children='Use AM/PM time'
                                ),
                            ],
                            style={
                                'margin': '10px'
                            }
                        )
                    ],
                    className='bp5-docs-page-example-props',
                    style={
                        'display': 'flex',
                        'justify-content': 'center'
                    }
                ),
            ],
            style={
                'margin-bottom': '20px'
            }
        ),
        dbpc.AnchorButton(
            id='daterangepicker-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.DateRangePicker)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('daterangepicker', 'shortcuts'),
    Input('daterangepicker-shortcuts', 'checked')
)
def change(value):

    return not value

@callback(
    Output('daterangepicker', 'allowSingleDayRange'),
    Input('daterangepicker-singleday', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangepicker', 'singleMonthOnly'),
    Input('daterangepicker-singlemonth', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangepicker', 'contiguousCalendarMonths'),
    Input('daterangepicker-contiguousmonth', 'checked')
)
def change(value):

    return not value

@callback(
    Output('daterangepicker', 'reverseMonthAndYearMenus'),
    Input('daterangepicker-reversemonthyear', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangepicker-min', 'options'),
    Input('daterangepicker', 'id')
)
def change(_):

    options=[
        {'label': 'Default (20 years ago)', 'value': 'none'},
        {'label': '1 week ago', 'value': datetime.today() - timedelta(weeks=1)},
        {'label': '4 months ago', 'value': datetime.today() - relativedelta(months=4)},
        {'label': '1 year ago', 'value': datetime.today() - relativedelta(year=1)},
    ]

    return options

@callback(
    Output('daterangepicker', 'minDate'),
    Input('daterangepicker-min', 'value')
)
def change(value):

    return value

@callback(
    Output('daterangepicker-max', 'options'),
    Input('daterangepicker', 'id')
)
def change(_):

    options=[
        {'label': 'Default (6 months from now)', 'value': 'none'},
        {'label': 'Today', 'value': datetime.today()},
        {'label': '1 week ago', 'value': datetime.today() + timedelta(weeks=1)},
        {'label': '4 months ago', 'value': datetime.today() + relativedelta(months=4)},
        {'label': '1 year ago', 'value': datetime.today() + relativedelta(year=1)},
    ]

    return options

@callback(
    Output('daterangepicker', 'maxDate'),
    Input('daterangepicker-max', 'value')
)
def change(value):

    return value

@callback(
    Output('daterangepicker', 'timePrecision'),
    Input('daterangepicker-timeprecision', 'value')
)
def change(value):

    return value

@callback(
    Output('daterangepicker', 'showTimeArrowButtons'),
    Input('daterangepicker-timearrows', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangepicker', 'useAmPm'),
    Input('daterangepicker-ampm', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangepicker-output-start', 'children'),
    Output('daterangepicker-output-end', 'children'),
    Input('daterangepicker', 'range')
)
def change(value):
    if isinstance(value, list):
        if value[0] and value[1]:
            return value[0], value[1]
        elif value[0]:
            return value[0], 'none'
        elif value[1]:
            return 'none', value[1]
        else:
            return 'none', 'none'
    else:
        return 'none', 'none'
    
@callback(
    Output('daterangepicker-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href