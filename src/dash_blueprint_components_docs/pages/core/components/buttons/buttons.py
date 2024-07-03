import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output, dcc, clientside_callback
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1('Buttons', className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Button)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Button(
                            id='button',
                            children='Button',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props', className='bp5-heading'),
                        dbpc.Switch(
                            id='active',
                            children='Active'
                        ),
                        dbpc.Switch(
                            id='disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='loading',
                            children='Loading'
                        ),
                        dbpc.Switch(
                            id='minimal',
                            children='Minimal'
                        ),
                        dbpc.Switch(
                            id='outlined',
                            children='Outlined'
                        ),
                        dbpc.Switch(
                            id='fill',
                            children='Fill'
                        ),
                        dbpc.Switch(
                            id='button-icon',
                            children='Icon'
                        ),
                        html.P(children='Size'),
                        html.Div(
                            dbpc.SegmentedControl(
                                id='segmented-control',
                                options=[
                                    {'label': 'Small', 'value': 'small'},
                                    {'label': 'Regular', 'value': 'regular'},
                                    {'label': 'Large', 'value': 'large'}
                                ],
                                defaultValue='regular',
                            ),
                            style={'max-width': 'fit-content'}
                        ),
                        html.P(children='Intent'),
                        dbpc.HTMLSelect(
                            id='button-select',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ],
                            fill=True
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='buttons-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H1('AnchorButton vs Button'),
        html.P(
        """
        The two button components generate different HTML tags. They each look the same, but they have different 
        semantic behaviors according to the HTML spec.
        """
        ),
        html.Pre(
            children=[
                html.Code(
                    children='<AnchorButton text="Click" />',
                    style={
                        'font-size': '13px',
                    }
                )
            ],
            className='bp5-code-block language-jsx',
        ),
        html.Pre(
            children=[
                html.Code(
                    children='<a class="bp5-button" role="button" tabindex={0}>Click</a>',
                    style={
                        'font-size': '13px',
                    }
                )
            ],
            className='bp5-code-block language-jsx',
        ),
        html.Hr(
            style={
                'margin': '20px 0',
                'border': 'none',
                'border-bottom': '1px solid rgba(17,20,24,.15)',
            },
        ),
        html.Pre(
            children=[
                html.Code(
                    children='<Button icon="refresh" />',
                    style={
                        'font-size': '13px',
                    }
                )
            ],
            className='bp5-code-block language-jsx',
        ),
        html.Pre(
            children=[
                html.Code(
                    children='<button class="bp5-button" type="button"><svg class="bp5-icon">...</svg></button>',
                    style={
                        'font-size': '13px',
                    }
                )
            ],
            className='bp5-code-block language-jsx',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Button)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('buttons-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href

@callback(
    Output('button', 'active'),
    Input('active', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('button', 'disabled'),
    Input('disabled', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('button', 'loading'),
    Input('loading', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('button', 'minimal'),
    Input('minimal', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('button', 'outlined'),
    Input('outlined', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('button', 'fill'),
    Input('fill', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('button', 'icon'),
    Input('button-icon', 'checked')
)
def change(checked):

    if checked:
        return 'refresh'
    else:
        return False

@callback(
    Output('button', 'intent'),
    Input('button-select', 'value')
)
def change(value):
    return value

@callback(
    Output('button', 'large'),
    Output('button', 'small'),
    Input('segmented-control', 'value')
)
def change(value):

    if value == 'large':
        return True, False
    elif value == 'small':
        return False, True
    else:
        return False, False

clientside_callback(
    """
    function(_) {
        Prism.highlightAll()
        return dash_clientside.no_update
    }
    """,
    Output('button', 'children'),
    Input('button', 'id')
)