import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.ControlGroup)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.ControlGroup)['description']),
        dbpc.Callout(
            title="Control group vs. input group",
            children=[
                html.P("Both components group multiple elements into a single unit, but their usage patterns are quite different."),
                html.P("Think of ControlGroup as a parent with multiple children, with each one a separate control."),
                html.P(inspect.cleandoc("""Conversely, an InputGroup is a single control, and should behave like so. A button inside of an input group should 
                    only affect that input; if its reach is further, then it should be promoted to live in a control group.
                """))
            ],
            intent='success',
            icon='comparison'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.ControlGroup(
                            id='control-group',
                            children=[
                                dbpc.HTMLSelect(
                                    options=[
                                        "Filter", "Name - ascending", "Name - descending", "Price - ascending", "Price - descending"
                                    ]
                                ),
                                dbpc.InputGroup(placeholder='Find filters...'),
                                dbpc.Button(icon='arrow-right')
                            ],
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='control-group-fill',
                            children='Fill'
                        ),
                        dbpc.Switch(
                            id='control-group-vertical',
                            children='Vertical'
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='controlgroup-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H2('Flex layout'),
        html.P('ControlGroup is a CSS inline flex row (or column if vertical) and provides some modifer props for common flexbox patterns:'),
        html.Ul(
            children=[
                html.Li('Enable the fill prop on a control group to make all controls expand equally to fill the available space.'),
                html.Ul(
                    children=[
                        html.Li('Controls will expand horizontally by default, or vertically if the vertical prop is enabled.'),
                        html.Li('Add the class Classes.FIXED to individual controls to revert them to their initial sizes.'),
                    ],
                    className='bp5-list'
                ),
                html.Li('In addition, you may enable the fill prop on specific controls inside the group to expand them fill more space while other controls retain their original sizes.'),
            ],
            className='bp5-list'
        ),
        html.P('You can adjust the specific size of a control with the flex-basis or width CSS properties.'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.ControlGroup)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('control-group', 'fill'),
    Input('control-group-fill', 'checked')
)
def change(value):

    return value

@callback(
    Output('control-group', 'vertical'),
    Input('control-group-vertical', 'checked')
)
def change(value):
    
    return value

@callback(
    Output('controlgroup-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href