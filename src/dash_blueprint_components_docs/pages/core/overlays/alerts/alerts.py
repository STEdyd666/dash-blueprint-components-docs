import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Alert)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Alert)['description']),
        html.P(inspect.cleandoc("""
            Although similar to Dialog, an alert is more restrictive and should only be used for important information. 
            By default, the user can only exit the alert by clicking one of the confirmation buttons; clicking the overlay 
            or pressing the esc key will not close the alert. These interactions can be enabled via props.
        """)),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Button(
                            id='alert-button',
                            text="Open file deletion alert"
                        ),
                        dbpc.Alert(
                            id='alert',
                            children='Are you sure you want to move <b>filename</b> to Trash? You will be able to restore it later, but it will become private to you.',
                            cancelButtonText='Cancel',
                            confirmButtonText='Move to Trash',
                            icon='trash',
                            intent='danger'
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='alert-escape',
                            children='Can escape key cancel'
                        ),
                        dbpc.Switch(
                            id='alert-outside',
                            children='Can outside click cancel'
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='alerts-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Alert)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('alert', 'isOpen'),
    Input('alert-button', 'n_clicks')
)
def change(n_clicks):

    if n_clicks is None:
        raise PreventUpdate

    return True

@callback(
    Output('alert', 'canEscapeKeyCancel'),
    Input('alert-escape', 'checked')
)
def change(value):

    return value

@callback(
    Output('alert', 'canOutsideClickCancel'),
    Input('alert-outside', 'checked')
)
def change(value):

    return value

@callback(
    Output('alerts-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href