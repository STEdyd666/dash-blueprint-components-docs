import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.DateInput)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.DateInput)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=dbpc.DateInput(
                                id='dateinput',
                            ),
                            className='centered'
                        ),
                        html.Div(
                            children=dbpc.Tag(
                                children='none',
                                id='dateinput-output',
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
                        html.H4('Behaviour props'),
                        dbpc.Switch(
                            id='dateinput-closeselection',
                            children='Close on selection'
                        ),
                        html.H4('Date picker props'),
                        dbpc.Switch(
                            id='dateinput-shortcuts',
                            children='Show shortcuts'
                        ),
                        dbpc.Switch(
                            id='dateinput-actionsbar',
                            children='Show actions bar'
                        ),
                        dbpc.Switch(
                            id='dateinput-reversemonthyear',
                            children='Reverse month and year menus'
                        ),
                        html.H4('Input appearance props'),
                        dbpc.Switch(
                            id='dateinput-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='dateinput-fill',
                            children='Fill container width'
                        ),
                        dbpc.Switch(
                            id='dateinput-showright',
                            children='Show right element'
                        ),
                        html.H4('date-fns format'),
                        dbpc.RadioGroup(
                            id='dateinput-datefns',
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
                            id='dateinput-timeprecision',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': 'Minute', 'value': 'minute'},
                                {'label': 'Second', 'value': 'second'},
                                {'label': 'Millisecond', 'value': 'millisecond'},
                            ]
                        ),
                        dbpc.Switch(
                            id='dateinput-timearrows',
                            children='Show time picker arrows'
                        ),
                        dbpc.Switch(
                            id='dateinput-ampm',
                            children='Use AM/PM time'
                        ),
                        html.H4('Timezone select props'),
                        dbpc.Switch(
                            id='dateinput-timezoneselect',
                            children='Show timezone select',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='dateinput-disabletimezone',
                            children='Disable timezone select'
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='dateinput-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.DateInput)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('dateinput', 'closeOnSelection'),
    Input('dateinput-closeselection', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'shortcuts'),
    Input('dateinput-shortcuts', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'showActionsBar'),
    Input('dateinput-actionsbar', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'reverseMonthAndYearMenus'),
    Input('dateinput-reversemonthyear', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'disabled'),
    Input('dateinput-disabled', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'fill'),
    Input('dateinput-fill', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'rightElement'),
    Input('dateinput-showright', 'checked')
)
def change(value):
    
    if value:
        rightElement=html.Span(
            style={
                'padding': '7px 5px',
            },
            className='bp5-icon-globe'
        )
    else:
        rightElement = None

    return rightElement

@callback(
    Output('dateinput', 'dateFnsFormat'),
    Input('dateinput-datefns', 'selectedValue')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'timePrecision'),
    Input('dateinput-timeprecision', 'value')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'showTimeArrowButtons'),
    Input('dateinput-timearrows', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'useAmPm'),
    Input('dateinput-ampm', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput', 'showTimezoneSelect'),
    Input('dateinput-timezoneselect', 'checked')
)
def change(value):

    return not value

@callback(
    Output('dateinput', 'disableTimezoneSelect'),
    Input('dateinput-disabletimezone', 'checked')
)
def change(value):

    return value

@callback(
    Output('dateinput-output', 'children'),
    Input('dateinput', 'date')
)
def change(value):

    if value:
        return value
    else:
        return 'none'

@callback(
    Output('dateinput-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href