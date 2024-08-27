import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Drawer)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Drawer)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Button(
                            id='drawer-button',
                            text='Show drawer'
                        ),
                        dbpc.Drawer(
                            id='drawer',
                            children=[
                                html.Div(
                                    children=[
                                        html.P(html.Strong(inspect.cleandoc("""
                                            Data integration is the seminal problem of the digital age. For over ten years,
                                            we’ve helped the world’s premier organizations rise to the challenge.
                                        """))),
                                        html.P(inspect.cleandoc("""
                                            Palantir Foundry radically reimagines the way enterprises interact with data by
                                            amplifying and extending the power of data integration. With Foundry, anyone can source,
                                            fuse, and transform data into any shape they desire. Business analysts become data
                                            engineers — and leaders in their organization’s data revolution.
                                        """)),
                                        html.P(inspect.cleandoc("""
                                            Foundry’s back end includes a suite of best-in-class data integration capabilities: data
                                            provenance, git-style versioning semantics, granular access controls, branching,
                                            transformation authoring, and more. But these powers are not limited to the back-end IT
                                            shop.
                                        """)),
                                        html.P(inspect.cleandoc("""
                                            In Foundry, tables, applications, reports, presentations, and spreadsheets operate as
                                            data integrations in their own right. Access controls, transformation logic, and data
                                            quality flow from original data source to intermediate analysis to presentation in real
                                            time. Every end product created in Foundry becomes a new data source that other users
                                            can build upon. And the enterprise data foundation goes where the business drives it.
                                        """)),
                                        html.P(inspect.cleandoc("""
                                            In Foundry, tables, applications, reports, presentations, and spreadsheets operate as
                                            data integrations in their own right. Access controls, transformation logic, and data
                                            quality flow from original data source to intermediate analysis to presentation in real
                                            time. Every end product created in Foundry becomes a new data source that other users
                                            can build upon. And the enterprise data foundation goes where the business drives it.
                                        """)),
                                        html.P('Start the revolution. Unleash the power of data integration with Palantir Foundry.'),
                                    ],
                                    className='bp5-drawer-body',
                                    style={'margin': '15px'}
                                ),
                                html.Div(
                                    children='Footer',
                                    className='bp5-drawer-footer'
                                )
                            ],
                            title='Palantir Foundry',
                            icon='info-sign',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        html.P(children='position'),
                        html.Div(
                            children=dbpc.SegmentedControl(
                                id='drawer-position',
                                options=[
                                    {'label': 'top', 'value': 'top'},
                                    {'label': 'right', 'value': 'right'},
                                    {'label': 'bottom', 'value': 'bottom'},
                                    {'label': 'left', 'value': 'left'},
                                ],
                                value='right'
                            ),
                            style={'max-width': 'fit-content'}
                        ),
                        html.P(children='size'),
                        dbpc.HTMLSelect(
                            id='drawer-size',
                            options=[
                                {'label': 'Default', 'value': 'default'},
                                {'label': 'Small', 'value': 'small'},
                                {'label': 'Standard', 'value': 'standard'},
                                {'label': 'Large', 'value': 'large'},
                                {'label': '72%', 'value': '72%'},
                                {'label': '560px', 'value': '560px'}
                            ]
                        ),
                        dbpc.Divider(),
                        dbpc.Switch(
                            id='drawer-backdrop',
                            children='Has backdrop',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='drawer-outside',
                            children='Can outside click cancel',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='drawer-escape',
                            children='Can escape key cancel',
                            defaultChecked=True
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='drawer-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Drawer)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('drawer', 'isOpen'),
    Input('drawer-button', 'n_clicks'),
)
def change(n_clicks):

    if n_clicks is not None:
        return True

@callback(
    Output('drawer', 'position'),
    Input('drawer-position', 'value'),
)
def change(value):

    return value

@callback(
    Output('drawer', 'size'),
    Input('drawer-size', 'value'),
)
def change(value):

    return value

@callback(
    Output('drawer', 'hasBackdrop'),
    Input('drawer-backdrop', 'checked')
)
def change(value):

    return not value

@callback(
    Output('drawer', 'canEscapeKeyClose'),
    Input('drawer-escape', 'checked')
)
def change(value):
    return not value

@callback(
    Output('drawer', 'canOutsideClickClose'),
    Input('drawer-outside', 'checked')
)
def change(value):
    return not value

@callback(
    Output('drawer-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href