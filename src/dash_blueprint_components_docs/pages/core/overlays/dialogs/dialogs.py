import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output, ctx
from dash.exceptions import PreventUpdate
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props

selectpanel = dbpc.DialogBody(
    children=[
        html.P('Use this dialog to divide content into multiple sequential steps.'),
        html.P('Select one of the options below in order to proceed to the next step:'),
        dbpc.RadioGroup(
            options=[
                {'label': 'Option A', 'value': 'A'},
                {'label': 'Option B', 'value': 'B'},
                {'label': 'Option C', 'value': 'C'}
            ]
        )
    ]
)

confirmpanel = dbpc.DialogBody(
    children=[
        html.P('To make changes, click the "Back" button or click on the "Select" step. Otherwise, click "Close" to completey our selection.')
    ]
)

component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Dialog)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Dialog)['description']),
        dbpc.Callout(
            title='Terminology note',
            intent='primary',
            children=inspect.cleandoc("""
                The term "modal" is sometimes used to mean "dialog," but this is a misnomer. Modal is an 
                adjective that describes parts of a UI. An element is considered to be "modal" if it blocks 
                interaction with the rest of the application. We use the term "dialog" in Blueprint to avoid 
                confusion with the adjective.
            """)
        ),
        html.P('Blueprint provides two types of dialogs:', style={'margin-top': '20px'}),
        html.Ol(
            children=[
                html.Li('Standard dialog: show single view using the <Dialog> component'),
                html.Li('Multi-step dialog: show multiple sequential views using the <MultistepDialog> component.')
            ],
            className='bp5-list'
        ),
        html.H2('Dialog'),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Button(
                            id='dialog-button',
                            text='Show dialog with title and footer'
                        ),
                        dbpc.Dialog(
                            id='dialog',
                            children=[
                                dbpc.DialogBody(
                                    children=[
                                        html.P(
                                            children=inspect.cleandoc("""
                                                Data integration is the seminal problem of the digital age. For over ten years, we’ve helped
                                                the world’s premier organizations rise to the challenge.
                                            """)
                                        ),
                                        html.P(
                                            children=inspect.cleandoc("""
                                                Palantir Foundry radically reimagines the way enterprises interact with data by amplifying and
                                                extending the power of data integration. With Foundry, anyone can source, fuse, and transform
                                                data into any shape they desire. Business analysts become data engineers — and leaders in their
                                                organization’s data revolution.
                                            """)
                                        ),
                                        html.P(
                                            children=inspect.cleandoc("""
                                                Foundry’s back end includes a suite of best-in-class data integration capabilities: data
                                                provenance, git-style versioning semantics, granular access controls, branching, transformation
                                                authoring, and more. But these powers are not limited to the back-end IT shop.
                                            """)
                                        ),
                                        html.P(
                                            children=inspect.cleandoc("""
                                                In Foundry, tables, applications, reports, presentations, and spreadsheets operate as data
                                                integrations in their own right. Access controls, transformation logic, and data quality flow
                                                from original data source to intermediate analysis to presentation in real time. Every end
                                                product created in Foundry becomes a new data source that other users can build upon. And the
                                                enterprise data foundation goes where the business drives it.
                                            """)
                                        ),
                                        html.P('Start the revolution. Unleash the power of data integration with Palantir Foundry.')
                                    ]
                                ),
                                dbpc.DialogFooter(
                                    actions=[
                                        dbpc.Button(
                                            id='closedialog',
                                            children='Close'
                                        )
                                    ],
                                    children='All checks passed'
                                )
                            ],
                            title='Palantir Foundry',
                            icon='info-sign',
                            isCloseButtonShown=True
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='dialog-escape',
                            children='Can escape key cancel',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='dialog-outside',
                            children='Can outside click cancel',
                            defaultChecked=True
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='dialogs-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H2('Dialog props'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Dialog)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2('Dialog body props'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.DialogBody)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2('Dialog footer props'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.DialogFooter)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2(parse_docstring(dbpc.MultistepDialog)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.MultistepDialog)['description']),
        html.P(inspect.cleandoc("""
            This component expects <DialogStep> child elements: each "step" is rendered in order and its panel is shown 
            as the dialog body content when the corresponding step is selected in the navigation panel.
        """)),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Button(
                            id='multistepdialog-button',
                            text='Show dialog'
                        ),
                        dbpc.MultistepDialog(
                            id='multistepdialog',
                            children=[
                                dbpc.DialogStep(panel=selectpanel, title='Select'),
                                dbpc.DialogStep(panel=confirmpanel, title='Confirm')
                            ],
                            title='Multistep dialog',
                            icon='info-sign'
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='multistepdialog-escape',
                            children='Escape key to close',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='multistepdialog-outside',
                            children='Click outside to close',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='multistepdialog-showbutton',
                            children='Show close button',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='multistepdialog-showfooterbutton',
                            children='Show footer close button',
                            defaultChecked=True
                        ),
                        dbpc.Divider(),
                        html.Div(
                            children=dbpc.SegmentedControl(
                                id='multistepdialog-position',
                                options=[
                                    {'label': 'Left', 'value': 'left'},
                                    {'label': 'Top', 'value': 'top'},
                                    {'label': 'Right', 'value': 'right'}
                                ],
                                value='left'
                            ),
                            style={'max-width': 'fit-content'}
                        ),
                        dbpc.NumericInput(
                            id='multistepdialog-index',
                            value=0,
                            min=-1,
                            max=2
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        html.H2('Multistep dialog props'),
        html.P('MultistepDialog is a wrapper around Dialog that displays a dialog with multiple steps. Each step has a corresponding panel.'),
        html.P('This component expects <DialogStep> child elements: each "step" is rendered in order and its panel is shown as the dialog body content when the corresponding step is selected in the navigation panel.'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.MultistepDialog)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2('DialogStep props'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.DialogStep)['props'])
                )
            ],
            className='bp5-html-table'
        ),
    ]
)


@callback(
    Output('dialog', 'isOpen'),
    Input('dialog-button', 'n_clicks'),
    Input('closedialog', 'n_clicks')
)
def change(n_clicks_1, n_clicks_2):

    if ctx.triggered_id == 'dialog-button':
        if n_clicks_1 is not None:
            return True
    elif ctx.triggered_id == 'closedialog':
        if n_clicks_2 is not None:
            return False

@callback(
    Output('dialog', 'canEscapeKeyClose'),
    Input('dialog-escape', 'checked')
)
def change(value):

    return value

@callback(
    Output('dialog', 'canOutsideClickClose'),
    Input('dialog-outside', 'checked')
)
def change(value):

    return value

@callback(
    Output('multistepdialog', 'isOpen'),
    Input('multistepdialog-button', 'n_clicks'),
)
def change(n_clicks):

    if n_clicks is not None:
        return True

@callback(
    Output('multistepdialog', 'isCloseButtonShown'),
    Input('multistepdialog-showbutton', 'checked')
)
def change(value):
    return not value

@callback(
    Output('multistepdialog', 'showCloseButtonInFooter'),
    Input('multistepdialog-showfooterbutton', 'checked')
)
def change(value):
    return not value

@callback(
    Output('multistepdialog', 'navigationPosition'),
    Input('multistepdialog-position', 'value')
)
def change(value):
    return value

@callback(
    Output('multistepdialog', 'initialStepIndex'),
    Input('multistepdialog-index', 'value')
)
def change(value):
    return value

@callback(
    Output('multistepdialog', 'canEscapeKeyClose'),
    Input('multistepdialog-escape', 'checked')
)
def change(value):
    return not value

@callback(
    Output('multistepdialog', 'canOutsideClickClose'),
    Input('multistepdialog-outside', 'checked')
)
def change(value):
    return not value

@callback(
    Output('dialogs-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href