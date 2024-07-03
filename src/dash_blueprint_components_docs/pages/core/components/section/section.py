import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output, clientside_callback
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Section)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Section)['description']),
        html.P('It makes use of some concepts from other more atomic Blueprint components:'),
        html.Ul(
            children=[
                html.Li('The overall appearance looks like a Card (with limited elevation options)'),
                html.Li('Contents may be collapsible like the Collapse component'),
            ],
            className='bp5-list'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Section(
                            id='section',
                            children=[
                                dbpc.SectionCard(
                                    children=inspect.cleandoc("""
                                        Ocimum basilicum, also called great basil, is a culinary herb of the family Lamiaceae (mints). It \
                                        is a tender plant, and is used in cuisines worldwide. In Western cuisine, the generic term "basil" \
                                        refers to the variety also known as sweet basil or Genovese basil. Basil is native to tropical regions \
                                        from Central Africa to Southeast Asia.
                                    """
                                    )
                                ),
                                dbpc.SectionCard(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.Span('Kingdom', className='bp5-text-muted'),
                                                        'Plantae'
                                                    ],
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'space-between',
                                                    }
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Span('Clade', className='bp5-text-muted'),
                                                        'Tracheophytes'
                                                    ],
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'space-between',
                                                    }
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Span('Family', className='bp5-text-muted'),
                                                        'Lamiaceae'
                                                    ],
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'space-between',
                                                    }
                                                ),
                                            ],
                                            style={
                                                'display': 'flex',
                                                'flex-direction': 'column',
                                                'gap': '10px'
                                            }
                                        )
                                    ]
                                ),
                            ],
                            title='Basil'
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='section-compact',
                            label='Compact',
                        ),
                        dbpc.Switch(
                            id='section-icon',
                            label='Icon',
                        ),
                        dbpc.Switch(
                            id='section-subtitle',
                            label='Sub-title',
                        ),
                        dbpc.Switch(
                            id='section-collapsible',
                            label='Collapsible',
                        ),
                        dbpc.Switch(
                            id='section-defaultopen',
                            label='Default is open',
                        ),
                        html.P('Elevation'),
                        dbpc.Slider(
                            id='section-elevation',
                            max=1,
                            min=0,
                            showTrackFill=False,
                        ) 
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='section-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Section)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2('Section Card'),
        html.P(inspect.cleandoc("""
            Multiple SectionCard child components can be added under one Section, they will be stacked vertically. 
            This layout can be used to further group information.
        """)
        ),
        html.Pre(
            children=[
                html.Code(
                    children=inspect.cleandoc("""
                    <Section>
                        <SectionCard>{/* ... */}</SectionCard>
                        <SectionCard>{/* ... */}</SectionCard>
                    </Section>"""),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.SectionCard)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)

clientside_callback(
    """
    function(_) {
        Prism.highlightAll()
        return dash_clientside.no_update
    }
    """,
    Output('section', 'children'),
    Input('section', 'id')
)

@callback(
    Output('section', 'compact'),
    Input('section-compact', 'checked')
)
def change(value):
    return value

@callback(
    Output('section', 'icon'),
    Input('section-icon', 'checked')
)
def change(value):
    if value:
        return 'book'
    
    return None

@callback(
    Output('section', 'subtitle'),
    Input('section-subtitle', 'checked')
)
def change(value):
    if value:
        return 'Ocimum basilicum'

    return None

@callback(
    Output('section', 'collapsible'),
    Input('section-collapsible', 'checked')
)
def change(value):
    return value

@callback(
    Output('section', 'elevation'),
    Input('section-elevation', 'value')
)
def change(value):
    return value

@callback(
    Output('section', 'defaultIsOpen'),
    Input('section-defaultopen', 'checked')
)
def change(value):
    return value

@callback(
    Output('section-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href