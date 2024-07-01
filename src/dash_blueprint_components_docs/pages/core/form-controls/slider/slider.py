import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from flask import current_app
import json
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Slider)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Slider)['description']),
        html.P(inspect.cleandoc("""
            To adjust a slider value, the user clicks and drags a handle or clicks the axis to move the nearest 
            handle to that spot. Users can also use arrow keys on the keyboard to adjust individual handles.
        """)),
        html.P(inspect.cleandoc("""
            Use Slider for choosing a single value, RangeSlider for choosing two values, and MultiSlider for more advanced use cases.
        """)),
        html.H2('Slider'),
        html.P(inspect.cleandoc("""
            Use Slider to choose a single value on a number line. It is a controlled component, so the value prop determines its current 
            appearance. Provide an onChange handler to receive updates and an onRelease handler to determine when the user has stopped 
            interacting with the slider.
        """)),
        html.Div(
            children=[
                html.Div(
                    id='slider-className',
                    children=[
                        html.Div(
                            children=dbpc.Slider(
                                id='slider-1',
                                min=0,
                                max=10,
                                stepSize=0.1,
                                labelStepSize=10
                            ),
                            style={
                                'margin': '35px'
                            }
                        ),
                        html.Div(
                            children=dbpc.Slider(
                                id='slider-2',
                                min=0,
                                max=0.7,
                                stepSize=0.01,
                                labelStepSize=0.14
                            ),
                            style={
                                'margin': '35px',
                            }
                        ),
                        html.Div(
                            children=dbpc.Slider(
                                id='slider-3',
                                min=-12,
                                max=48,
                                stepSize=6,
                                labelStepSize=10,
                                showTrackFill=False,
                                format={
                                    'before': '€'
                                }
                            ),
                            style={
                                'margin': '35px'
                            }
                        ),
                    ],
                    className='bp5-docs-page-example',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='slider-vertical',
                            label='Vertical',
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='slider-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Slider)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2('Range slider'),
        html.P(inspect.cleandoc("""
            Use RangeSlider to choose a range between upper and lower bounds. The component functions identically to 
            Slider with the addition of a second handle. It exposes its selected value as [number, number]: a two-element 
            array with minimum and maximum range bounds.
        """)),
        html.Div(
            children=[
                html.Div(
                    children=dbpc.RangeSlider(
                        id='range-slider',
                        min=0,
                        max=100,
                        stepSize=2,
                        labelStepSize=20
                    ),
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='range-slider-vertical',
                            label='Vertical',
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.RangeSlider)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H2('Multi slider'),
        html.P(inspect.cleandoc("""
            MultiSlider is a flexible solution for picking arbitrary values on a number line. It powers both 
            Slider and RangeSlider internally and can be used for implementing more advanced use cases 
            than one or two numbers.
        """)),
        html.Div(
            children=[
                html.Div(
                    children=dbpc.MultiSlider(
                        id='multi-slider',
                        min=0,
                        max=100,
                        stepSize=2,
                        labelStepSize=20,
                        handles=[
                            dbpc.Handle(
                                value=12,
                                type='start',
                                intentBefore='danger',
                                intentAfter='warning'
                            ),
                            dbpc.Handle(
                                value=36,
                                type='start',
                                intentBefore='warning',
                                intentAfter='success'
                            ),
                            dbpc.Handle(
                                value=72,
                                type='end',
                                intentBefore='success',
                                intentAfter='warning'
                            ),
                            dbpc.Handle(
                                value=90,
                                type='end',
                                intentBefore='warning',
                                intentAfter='danger'
                            )
                        ]
                    ),
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='multi-slider-vertical',
                            label='Vertical',
                        ),
                        dbpc.Switch(
                            id='multi-slider-track',
                            label='Show track fill',
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        html.H2('Props interface'),
        html.H3('Multi slider'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.MultiSlider)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H3('Handle'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Handle)['props'])
                )
            ],
            className='bp5-html-table'
        ),
    ]
)


@callback(
    Output('slider-1', 'vertical'),
    Output('slider-2', 'vertical'),
    Output('slider-3', 'vertical'),
    Output('slider-className', 'className'),
    Input('slider-vertical', 'checked')
)
def change(value):
    if value:
        return value, value, value, 'bp5-docs-page-example centered'
    else:
        return value, value, value, 'bp5-docs-page-example'

@callback(
    Output('range-slider', 'vertical'),
    Input('range-slider-vertical', 'checked')
)
def change(value):
    return value

@callback(
    Output('multi-slider', 'vertical'),
    Input('multi-slider-vertical', 'checked')
)
def change(value):
    return value

@callback(
    Output('multi-slider', 'showTrackFill'),
    Input('multi-slider-track', 'checked')
)
def change(value):
    return value

@callback(
    Output('multi-slider', 'className'),
    Input('multi-slider', 'handles')
)
def change(value):
    return value

@callback(
    Output('slider-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    repo = current_app.config['GITHUB']
    href = f'{repo}{route}'
    return href
