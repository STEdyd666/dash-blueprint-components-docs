import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.DatePicker)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.DatePicker)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=dbpc.DatePicker(
                                id='datepicker',
                            ),
                            className='centered',
                        ),
                        html.Div(
                            children=dbpc.Tag(
                                children='none',
                                id='datepicker-output',
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
                            id='datepicker-shortcuts',
                            children='Show shortcuts'
                        ),
                        dbpc.Switch(
                            id='datepicker-actionsbar',
                            children='Show actions bar'
                        ),
                        dbpc.Switch(
                            id='datepicker-currentday',
                            children='Highlight current day'
                        ),
                        dbpc.Switch(
                            id='datepicker-reversemonthyear',
                            children='Reverse month and year menus'
                        ),
                        dbpc.Switch(
                            id='datepicker-footer',
                            children='Show custom footer element'
                        ),
                        html.P(children='Minimum date'),
                        dbpc.HTMLSelect(
                            id='datepicker-min',
                        ),
                        html.P(children='Maximum date'),
                        dbpc.HTMLSelect(
                            id='datepicker-max',
                        ),
                        dbpc.Switch(
                            id='datepicker-weeknumbers',
                            children='Show week numbers'
                        ),
                        dbpc.Switch(
                            id='datepicker-outsidedays',
                            children='Show outside days'
                        ),
                        html.H4('Time picker props'),
                        html.P(children='Time precision'),
                        dbpc.HTMLSelect(
                            id='datepicker-timeprecision',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': 'Minute', 'value': 'minute'},
                                {'label': 'Second', 'value': 'second'},
                                {'label': 'Millisecond', 'value': 'millisecond'},
                            ]
                        ),
                        dbpc.Switch(
                            id='datepicker-timearrows',
                            children='Show time picker arrows'
                        ),
                        dbpc.Switch(
                            id='datepicker-ampm',
                            children='Use AM/PM time'
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='datepicker-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.DatePicker)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)

@callback(
    Output('datepicker', 'shortcuts'),
    Input('datepicker-shortcuts', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'showActionsBar'),
    Input('datepicker-actionsbar', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'highlightCurrentDay'),
    Input('datepicker-currentday', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'reverseMonthAndYearMenus'),
    Input('datepicker-reversemonthyear', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'footerElement'),
    Input('datepicker-footer', 'checked')
)
def change(value):
    if value:
        return dbpc.Callout(
            'This additional footer component can be displayed below the date picker'
        )
    else:
        return None 

@callback(
    Output('datepicker-min', 'options'),
    Input('datepicker', 'id')
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
    Output('datepicker', 'minDate'),
    Input('datepicker-min', 'value')
)
def change(value):

    return value

@callback(
    Output('datepicker-max', 'options'),
    Input('datepicker', 'id')
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
    Output('datepicker', 'maxDate'),
    Input('datepicker-max', 'value')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'showWeekNumber'),
    Input('datepicker-weeknumbers', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'showOutsideDays'),
    Input('datepicker-outsidedays', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'timePrecision'),
    Input('datepicker-timeprecision', 'value')
)
def change(value):
    
    return value

@callback(
    Output('datepicker', 'showTimeArrowButtons'),
    Input('datepicker-timearrows', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker', 'useAmPm'),
    Input('datepicker-ampm', 'checked')
)
def change(value):

    return value

@callback(
    Output('datepicker-output', 'children'),
    Input('datepicker', 'date')
)
def change(value):
    
    if value:
        return value
    else:
        return 'none'

@callback(
    Output('datepicker-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href