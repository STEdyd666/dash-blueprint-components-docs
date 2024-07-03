import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.TagInput)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.TagInput)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.TagInput(
                            id='taginput',
                            placeholder='Separate values with commas...',
                            values=[
                                'Albert',
                                'Bartholomew',
                                'Casper'
                            ],
                            leftIcon='user',
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Appearance props'),
                        dbpc.Switch(
                            id='taginput-large',
                            children='Large'
                        ),
                        dbpc.Switch(
                            id='taginput-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='taginput-lefticon',
                            children='Left icon',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='taginput-fill',
                            children='Fill'
                        ),
                        dbpc.Divider(),
                        html.P(children='intent'),
                        dbpc.HTMLSelect(
                            id='taginput-selectintent',
                            options=[
                                {'label': 'None', 'value': None},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ]
                        ),
                        html.H4('Behaviour props'),
                        dbpc.Switch(
                            id='taginput-addonblur',
                            children='Add on blur'
                        ),
                        dbpc.Switch(
                            id='taginput-addonpaste',
                            children='Add on paste',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='taginput-autoresize',
                            children='Auto resize',
                        ),
                        html.H4('Tag props'),
                        dbpc.Switch(
                            id='taginput-minimal',
                            children='Use minimal tags'
                        ),
                        dbpc.Switch(
                            id='taginput-cycleintents',
                            children='Cycle through intents'
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.Callout(
            title='Looking for a dropdown menu?',
            intent='success',
            icon='info-sign',
            children='The MultiSelect component in the @blueprintjs/select package composes this component with a dropdown menu.'
        ),
        dbpc.AnchorButton(
            id='taginput-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H1('Usage'),
        html.P(inspect.cleandoc("""
            Typing in the input and pressing Enter will add new items by invoking callbacks. If addOnBlur is set to true, 
            clicking outside of the component will also trigger the callback to add new items. A separator prop is supported 
            to allow multiple items to be added at once; the default splits on commas and newlines.
        """)),
        html.P(inspect.cleandoc("""
            Tags may be removed by clicking their  buttons or by pressing either backspace or delete repeatedly. Pressing delete 
            mimics the behavior of deleting in a text editor, where trying to delete at the end of the line will do nothing. Arrow 
            keys can also be used to focus on a particular tag before removing it. The cursor must be at the beginning of the text 
            input for these interactions.
        """)),
        html.P(inspect.cleandoc("""
            Tags may be removed by clicking their  buttons or by pressing either backspace or delete repeatedly. Pressing delete 
            mimics the behavior of deleting in a text editor, where trying to delete at the end of the line will do nothing. Arrow 
            keys can also be used to focus on a particular tag before removing it. The cursor must be at the beginning of the text 
            input for these interactions.
        """)),
        dbpc.Callout(
            title='Handling long words',
            intent='primary',
            children=inspect.cleandoc("""
                Set an explicit width on the container element to cause long tags to wrap onto multiple lines. Either supply a specific 
                pixel value, or use <TagInput className={Classes.FILL}> to fill its container's width (try this in the example above).
            """)
        ),
        dbpc.Callout(
            title='Disabling a tag input',
            intent='primary',
            children=inspect.cleandoc("""
                Disabling this component requires setting the disabled prop to true and separately disabling the component's rightElement 
                as appropriate (because TagInput accepts any React.JSX.Element as its rightElement).
            """)
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.TagInput)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('taginput', 'large'),
    Input('taginput-large', 'checked')
)
def change(value):

    return value

@callback(
    Output('taginput', 'disabled'),
    Input('taginput-disabled', 'checked')
)
def change(value):

    return value

@callback(
    Output('taginput', 'leftIcon'),
    Input('taginput-lefticon', 'checked')
)
def change(value):
    if not value:
        return 'user'
    else:
        return None

@callback(
    Output('taginput', 'fill'),
    Input('taginput-fill', 'checked')
)
def change(value):

    return value

@callback(
    Output('taginput', 'intent'),
    Input('taginput-selectintent', 'value')
)
def change(value):

    return value

@callback(
    Output('taginput', 'addOnBlur'),
    Input('taginput-addonblur', 'checked')
)
def change(value):

    return value

@callback(
    Output('taginput', 'addOnPaste'),
    Input('taginput-addonpaste', 'checked')
)
def change(value):

    return value

@callback(
    Output('taginput', 'autoResize'),
    Input('taginput-autoresize', 'checked')
)
def change(value):

    return value

@callback(
    Output('taginput', 'tagMinimal'),
    Input('taginput-minimal', 'checked')
)
def change(value):

    return value

@callback(
    Output('taginput', 'tagIntents'),
    Input('taginput-cycleintents', 'checked')
)
def change(value):
    return value

@callback(
    Output('taginput-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href