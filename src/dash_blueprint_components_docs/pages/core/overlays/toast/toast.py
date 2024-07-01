import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output, ctx
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Toast)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Toast)['description']),
        html.P('Toasts can be configured to appear at either the top or the bottom of an application window. It is possible to show more than one toast on-screen at a time.'),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Button(
                            id='button-toaster-1',
                            text='Procure toast',
                            intent='primary',
                            style={
                                'margin': '10px'
                            }
                        ),
                        dbpc.Button(
                            id='button-toaster-2',
                            text='Move files',
                            intent='success',
                            style={
                                'margin': '10px'
                            }
                        ),
                        dbpc.Button(
                            id='button-toaster-3',
                            text='Delete root',
                            intent='danger',
                            style={
                                'margin': '10px'
                            }
                        ),
                        dbpc.OverlayToaster(
                            id='toaster',
                            position='bottom_left',
                        ),
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        html.P(children='position'),
                        dbpc.HTMLSelect(
                            id='toast-position',
                            options=[
                                {'label': 'top-left', 'value': 'top-left'},
                                {'label': 'top', 'value': 'top'},
                                {'label': 'top-right', 'value': 'top-right'},
                                {'label': 'bottom-left', 'value': 'bottom-left'},
                                {'label': 'bottom', 'value': 'bottom'},
                                {'label': 'bottom-right', 'value': 'bottom-right'}, 
                            ],
                            value='top',
                        ),
                        html.P(children='Maximum active toasts'),
                        dbpc.NumericInput(
                            id='toast-max',
                            placeholder='No maximum!',
                            fill=True,
                            min=1
                        ),
                        dbpc.Switch(
                            id='toast-escape',
                            children='Can escape key clear',
                            defaultChecked=True
                        ), 
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='toast-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H1('Usage'),
        html.H2('Toast'),
        html.P(inspect.cleandoc("""
            Toasts have a built-in timeout of five seconds. Users can also dismiss them manually by clicking 
            the × button. overing the cursor over a toast prevents it from disappearing. When the cursor leaves the toast, 
            the toast's timeout restarts. Similarly, focussing the toast DOM element (for example, by hitting the tab key) halts 
            the timeout, and blurring restarts the timeout.
            """
        )), 
        html.P(inspect.cleandoc("""
            You may also apply the same visual intents to Toasts as other core components like Buttons.
            """
        )),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Toast)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2('OverlayToaster'),
        html.P(inspect.cleandoc("""
            The OverlayToaster component (previously named Toaster) is a stateful container for a single list of toasts. 
            Internally, it uses Overlay2 to manage children and transitions. It can be vertically aligned along the top or 
            bottom edge of its container (new toasts will slide in from that edge) and horizontally aligned along the left 
            edge, center, or right edge of its container.
            """
        )),
        dbpc.Callout(
            title="Working with multiple toasters",
            children=[
                html.P(inspect.cleandoc("""You can have multiple toasters in a single application, but you must ensure that each has a 
                unique position to prevent overlap.
                """))
            ],
            intent='primary',
            icon='info-sign'
        ),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.OverlayToaster)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('toaster', 'toasts'),
    Input('button-toaster-1', 'n_clicks'),
    Input('button-toaster-2', 'n_clicks'),
    Input('button-toaster-3', 'n_clicks'),
)
def change(_1, _2, _3):
    
    button_clicked = ctx.triggered_id
    if button_clicked == 'button-toaster-1':
        toasts=[
                dbpc.Toast(
                    message='One toast created.',
                    intent='primary',
                )
            ]
    elif button_clicked == 'button-toaster-2':
        toasts=[
                dbpc.Toast(
                    message='Moved 6 files.',
                    intent='success',
                    icon='tick'
                )
            ]
    elif button_clicked == 'button-toaster-3':
        toasts=[
                dbpc.Toast(
                    message=inspect.cleandoc("""
                        You do not have permissions to perform this action.
                        Please contact your system administrator to request the appropriate access rights.
                    """),
                    intent='danger',
                    icon='warning-sign'
                )
            ]
    else:
        raise PreventUpdate()

    return toasts

@callback(
    Output('toaster', 'position'),
    Input('toast-position', 'value'),
)
def change(value):
    
    return value

@callback(
    Output('toaster', 'maxToasts'),
    Input('toast-max', 'value'),
)
def change(value):
    
    if value is None:
        raise PreventUpdate
    
    if not value:
        return None

    return int(value)

@callback(
    Output('toaster', 'canEscapeKeyClear'),
    Input('toast-escape', 'checked'),
)
def change(value):
    return value

@callback(
    Output('toast-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href