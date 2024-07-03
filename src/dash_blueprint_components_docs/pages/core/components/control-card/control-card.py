import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1('Control card', className='bp5-heading docs-title'),
        html.P(inspect.cleandoc("""
            A control card is an interactive Card with an embedded form control. 
            There are a few supported form controls, each has a corresponding component API:
        """)),
        html.Ul(
            children=[
                html.Li('SwitchCard'),
                html.Li('CheckboxCard'),
                html.Li('RadioCard'),
            ],
            className='bp5-list'
        ),
        html.P('Users may click anywhere inside the card to toggle the control state.'),
        html.H2(parse_docstring(dbpc.SwitchCard)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.SwitchCard)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            dbpc.SwitchCard(
                                id='controlcard-switch-1',
                                label='Wifi',
                            )
                        ),
                        html.Div(
                            dbpc.SwitchCard(
                                id='controlcard-switch-2',
                                label='Bluetooth'
                            )
                        ),
                        html.Div(
                            dbpc.SwitchCard(
                                id='controlcard-switch-3',
                                label='VPN'
                            )
                        )
                    ],
                    className='bp5-docs-page-example centered',
                    style={
                        'flex-wrap': 'wrap',
                        'gap': '10px',
                        'justify-content': 'center'
                    }
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        dbpc.Switch(
                            id='controlcard-switch-compact',
                            children='Compact',
                        ),
                        dbpc.Switch(
                            id='controlcard-switch-disabled',
                            children='Disabled'
                        ),
                        dbpc.Divider(),
                        html.P(children='Align control indicator'),
                        html.Div(
                            children=dbpc.SegmentedControl(
                                id='controlcard-switch-align',
                                options=[
                                    {'label': 'Left', 'value': 'left'},
                                    {'label': 'Right', 'value': 'right'}
                                ],
                                defaultValue='right',
                                value='right'
                            ),
                            style={'max-width': 'fit-content'}
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='controlcard-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H2(parse_docstring(dbpc.CheckboxCard)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.CheckboxCard)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            dbpc.CheckboxCard(
                                id='controlcard-checkbox-1',
                                label='Wifi',
                            )
                        ),
                        html.Div(
                            dbpc.CheckboxCard(
                                id='controlcard-checkbox-2',
                                label='Bluetooth'
                            )
                        ),
                        html.Div(
                            dbpc.CheckboxCard(
                                id='controlcard-checkbox-3',
                                label='VPN'
                            )
                        )
                    ],
                    className='bp5-docs-page-example centered',
                    style={
                        'flex-wrap': 'wrap',
                        'gap': '10px',
                        'justify-content': 'center'
                    }
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        dbpc.Switch(
                            id='controlcard-checkbox-compact',
                            children='Compact',
                        ),
                        dbpc.Switch(
                            id='controlcard-checkbox-disabled',
                            children='Disabled'
                        ),
                        dbpc.Divider(),
                        html.P(children='Align control indicator'),
                        html.Div(
                            children=dbpc.SegmentedControl(
                                id='controlcard-checkbox-align',
                                options=[
                                    {'label': 'Left', 'value': 'left'},
                                    {'label': 'Right', 'value': 'right'}
                                ],
                                defaultValue='right',
                                value='right'
                            ),
                            style={'max-width': 'fit-content'}
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        html.H2(parse_docstring(dbpc.RadioCard)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.RadioCard)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.RadioGroup(
                            asCard=True,
                            children=[
                                dbpc.RadioCard(
                                    id='controlcard-radio-1',
                                    label='Soup',
                                    value='soup',
                                ),
                                dbpc.RadioCard(
                                    id='controlcard-radio-2',
                                    label='Salad',
                                    value='salad'
                                ),
                                dbpc.RadioCard(
                                    id='controlcard-radio-3',
                                    label='Sandwich',
                                    value='sandwich'
                                )
                            ],
                            className='radio-flex'
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        dbpc.Switch(
                            id='controlcard-radio-compact',
                            children='Compact',
                        ),
                        dbpc.Switch(
                            id='controlcard-radio-disabled',
                            children='Disabled'
                        ),
                        dbpc.Divider(),
                        html.P(children='Align control indicator'),
                        html.Div(
                            children=dbpc.SegmentedControl(
                                id='controlcard-radio-align',
                                options=[
                                    {'label': 'Left', 'value': 'left'},
                                    {'label': 'Right', 'value': 'right'}
                                ],
                                defaultValue='right',
                                value='right'
                            ),
                            style={'max-width': 'fit-content'}
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.SwitchCard)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('controlcard-switch-1', 'compact'),
    Output('controlcard-switch-2', 'compact'),
    Output('controlcard-switch-3', 'compact'),
    Input('controlcard-switch-compact', 'checked')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-switch-1', 'disabled'),
    Output('controlcard-switch-2', 'disabled'),
    Output('controlcard-switch-3', 'disabled'),
    Input('controlcard-switch-disabled', 'checked')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-switch-1', 'alignIndicator'),
    Output('controlcard-switch-2', 'alignIndicator'),
    Output('controlcard-switch-3', 'alignIndicator'),
    Input('controlcard-switch-align', 'value')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-checkbox-1', 'compact'),
    Output('controlcard-checkbox-2', 'compact'),
    Output('controlcard-checkbox-3', 'compact'),
    Input('controlcard-checkbox-compact', 'checked')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-checkbox-1', 'disabled'),
    Output('controlcard-checkbox-2', 'disabled'),
    Output('controlcard-checkbox-3', 'disabled'),
    Input('controlcard-checkbox-disabled', 'checked')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-checkbox-1', 'alignIndicator'),
    Output('controlcard-checkbox-2', 'alignIndicator'),
    Output('controlcard-checkbox-3', 'alignIndicator'),
    Input('controlcard-checkbox-align', 'value')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-radio-1', 'compact'),
    Output('controlcard-radio-2', 'compact'),
    Output('controlcard-radio-3', 'compact'),
    Input('controlcard-radio-compact', 'checked')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-radio-1', 'disabled'),
    Output('controlcard-radio-2', 'disabled'),
    Output('controlcard-radio-3', 'disabled'),
    Input('controlcard-radio-disabled', 'checked')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-radio-1', 'alignIndicator'),
    Output('controlcard-radio-2', 'alignIndicator'),
    Output('controlcard-radio-3', 'alignIndicator'),
    Input('controlcard-radio-align', 'value')
)
def change(value):
    return value, value, value

@callback(
    Output('controlcard-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href