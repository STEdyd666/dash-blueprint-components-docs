import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.EditableText)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.EditableText)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H1(
                            children=[
                                dbpc.EditableText(
                                    id='editabletext-title',
                                    placeholder='Edit title...'
                                )
                            ]
                        ),
                        dbpc.EditableText(
                            id='editabletext-content',
                            placeholder='Edit report... (multiline)',
                            minLines=3,
                            maxLines=12,
                            multiline=True
                        )
                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        html.Label(children='intent', className='bp5-label'),
                        dbpc.HTMLSelect(
                            id='editabletext-select',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ],
                        ),
                        html.Label(children='Max length', className='bp5-label'),
                        dbpc.NumericInput(
                            id='editabletext-numeric',
                            placeholder='Unlimited',
                            fill=True,
                            max=300,
                            min=0
                        ),
                        dbpc.Switch(
                            id='editabletext-disabled',
                            children='Disabled',
                        ),
                        dbpc.Switch(
                            id='editabletext-selectonfocus',
                            children='Select on focus',
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='editabletext-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.EditableText)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('editabletext-title', 'intent'),
    Output('editabletext-content', 'intent'),
    Input('editabletext-select', 'value')
)
def change(value):
    return value, value

@callback(
    Output('editabletext-title', 'maxLength'),
    Output('editabletext-content', 'maxLength'),
    Input('editabletext-numeric', 'value')
)
def change(value):

    if value is None:
        return None, None
        
    return value, value

@callback(
    Output('editabletext-title', 'disabled'),
    Output('editabletext-content', 'disabled'),
    Input('editabletext-disabled', 'checked')
)
def change(value):
    return value, value

@callback(
    Output('editabletext-title', 'selectAllOnFocus'),
    Output('editabletext-content', 'selectAllOnFocus'),
    Input('editabletext-selectonfocus', 'checked')
)
def change(value):
    return value, value

@callback(
    Output('editabletext-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href