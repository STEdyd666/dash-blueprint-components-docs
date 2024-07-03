import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.FormGroup)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.FormGroup)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=dbpc.FormGroup(
                                id='form-group-1',
                                children=[
                                    dbpc.InputGroup(
                                        id='form-group-1-input-group',
                                        placeholder='Placeholder text',
                                    )
                                ],
                            ),
                            className='centered'
                        ),
                        html.Div(
                            children=dbpc.FormGroup(
                                id='form-group-2',
                                children=[
                                    dbpc.Switch(
                                        id='form-group-2-switch-1',
                                        label='Engage the hyperdrive',
                                    ),
                                    dbpc.Switch(
                                        id='form-group-2-switch-2',
                                        label='Initiate thrusters',
                                    )
                                ],
                            ),
                            className='centered'
                        )

                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='checkbox-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='checkbox-inline',
                            children='Inline'
                        ),
                        dbpc.Switch(
                            id='checkbox-helper-text',
                            children='Show helper text'
                        ),
                        dbpc.Switch(
                            id='checkbox-label',
                            children='Show label',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='checkbox-label-info',
                            children='Show label info',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='checkbox-sub-label',
                            children='Show sub label'
                        ),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='form-group-intent',
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
            id='formgroup-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.FormGroup)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('form-group-1-input-group', 'intent'),
    Output('form-group-1', 'intent'),
    Output('form-group-2', 'intent'),
    Input('form-group-intent', 'value')
)
def change(value):

    return value, value, value

@callback(
    Output('form-group-1', 'label'),
    Output('form-group-2', 'label'),
    Input('checkbox-label', 'checked')
)
def change(value):
    if value:
        return None, None
    else:
        return 'label', 'label'

@callback(
    Output('form-group-1', 'labelInfo'),
    Output('form-group-2', 'labelInfo'),
    Input('checkbox-label-info', 'checked')
)
def change(value):
    if value:
        return None, None        
    else:
        return '(required)', '(required)'

@callback(
    Output('form-group-1', 'helperText'),
    Output('form-group-2', 'helperText'),
    Input('checkbox-helper-text', 'checked')
)
def change(value):
    if value:
        return 'Helper text with details...', 'Helper text with details...'
    else:
        return None, None        

@callback(
    Output('form-group-1', 'inline'),
    Output('form-group-2', 'inline'),
    Input('checkbox-inline', 'checked')
)
def change(value):
    if value:
        return True, True
    else:
        return False, False

@callback(
    Output('form-group-1', 'disabled'),
    Output('form-group-2', 'disabled'),
    Output('form-group-1-input-group', 'disabled'),
    Output('form-group-2-switch-1', 'disabled'),
    Output('form-group-2-switch-2', 'disabled'),
    Input('checkbox-disabled', 'checked')
)
def change(value):
    if value:
        return True, True, True, True, True
    else:
        return False, False, False, False, False

@callback(
    Output('form-group-1', 'subLabel'),
    Output('form-group-2', 'subLabel'),
    Input('checkbox-sub-label', 'checked')
)
def change(value):
    if value:
        return 'Label helper text with details...', 'Label helper text with details...'
    else:
        return None, None

@callback(
    Output('formgroup-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href