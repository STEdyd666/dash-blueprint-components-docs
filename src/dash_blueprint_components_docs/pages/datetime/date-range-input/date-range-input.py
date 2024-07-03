import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.DateRangeInput)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.DateRangeInput)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=dbpc.DateRangeInput(
                                id='daterangeinput',
                            ),
                            className='centered',
                        ),
                        html.Div(
                            children=[
                                dbpc.Tag(
                                    children='none',
                                    id='daterangeinput-output-start',
                                    intent='primary',
                                ),
                                dbpc.Tag(
                                    children='none',
                                    id='daterangeinput-output-end',
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
                ),
                html.Div(
                    children=[
                        html.H4('Behaviour props'),
                        dbpc.Switch(
                            id='daterangeinput-closeselection',
                            children='Close on selection'
                        ),
                        dbpc.Switch(
                            id='daterangeinput-selectfocus',
                            children='Select all text on input focus'
                        ),
                        html.H4('Date picker props'),
                        dbpc.Switch(
                            id='daterangeinput-shortcuts',
                            children='Show shortcuts'
                        ),
                        dbpc.Switch(
                            id='daterangeinput-singleday',
                            children='Allow single day range'
                        ),
                        dbpc.Switch(
                            id='daterangeinput-singlemonth',
                            children='Single month only'
                        ),
                        dbpc.Switch(
                            id='daterangeinput-contiguousmonth',
                            children='Constrain calendar to contiguous months',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='daterangeinput-reversemonthyear',
                            children='Reverse month and year menus'
                        ),
                        dbpc.Switch(
                            id='daterangeinput-footer',
                            children='Show custom footer element'
                        ),
                        html.H4('Input appearance props'),
                        dbpc.Switch(
                            id='daterangeinput-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='daterangeinput-fill',
                            children='Fill container width'
                        ),
                        html.H4('date-fns format'),
                        dbpc.RadioGroup(
                            id='daterangeinput-datefns',
                            options=[
                                {'label': 'MM/dd/yyyy', 'value': 'MM/dd/yyyy' },
                                {'label': 'yyyy-MM-dd', 'value': 'yyyy-MM-dd' },
                                {'label': 'yyyy-MM-dd HH:mm:ss', 'value': 'yyyy-MM-dd HH:mm:ss' },
                                {'label': "LLL do, yyyy 'at' K:mm a", 'value': "LLL do, yyyy 'at' K:mm a" },
                            ],
                            selectedValue='MM/dd/yyyy'
                        ),
                        html.H4('Time picker props'),
                        html.P(children='Time precision'),
                        dbpc.HTMLSelect(
                            id='daterangeinput-timeprecision',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': 'Minute', 'value': 'minute'},
                                {'label': 'Second', 'value': 'second'},
                                {'label': 'Millisecond', 'value': 'millisecond'},
                            ]
                        ),
                        dbpc.Switch(
                            id='daterangeinput-timearrows',
                            children='Show time picker arrows'
                        ),
                        dbpc.Switch(
                            id='daterangeinput-ampm',
                            children='Use AM/PM time'
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='daterangeinput-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.DateRangeInput)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)

@callback(
    Output('daterangeinput', 'closeOnSelection'),
    Input('daterangeinput-closeselection', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'selectAllOnFocus'),
    Input('daterangeinput-selectfocus', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'shortcuts'),
    Input('daterangeinput-shortcuts', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'allowSingleDayRange'),
    Input('daterangeinput-singleday', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'singleMonthOnly'),
    Input('daterangeinput-singlemonth', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'contiguousCalendarMonths'),
    Input('daterangeinput-contiguousmonth', 'checked')
)
def change(value):

    return not value

@callback(
    Output('daterangeinput', 'reverseMonthAndYearMenus'),
    Input('daterangeinput-reversemonthyear', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'footerElement'),
    Input('daterangeinput-footer', 'checked')
)
def change(value):
    if value:
        return dbpc.Callout(
            'This additional footer component can be displayed below the date picker'
        )
    else:
        return None 

@callback(
    Output('daterangeinput', 'disabled'),
    Input('daterangeinput-disabled', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'fill'),
    Input('daterangeinput-fill', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'dateFnsFormat'),
    Input('daterangeinput-datefns', 'selectedValue')
)
def change(value):

    return value

@callback(
    Output('daterangeinput-output-start', 'children'),
    Output('daterangeinput-output-end', 'children'),
    Input('daterangeinput', 'range')
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
    Output('daterangeinput', 'timePrecision'),
    Input('daterangeinput-timeprecision', 'value')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'showTimeArrowButtons'),
    Input('daterangeinput-timearrows', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput', 'useAmPm'),
    Input('daterangeinput-ampm', 'checked')
)
def change(value):

    return value

@callback(
    Output('daterangeinput-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href