from dash import html
import dash_blueprint_components as dbpc


component = html.Div(
    children=[
        html.H1('Dash Blueprint Components', className='bp5-heading docs-title'),
        html.P('Dash Blueprint Components (DBPC) is the porting for dash plotly of the blueprintjs React-based UI toolkit for the web.'),
        html.P('It is optimized for building complex data-dense interfaces for desktop applications.'),
        html.P("""
        This documentation is a replica of the official BlueprintJS website created using solely dash components. All the rights belongs 
        to BlueprintJS team.
        """),
        html.Div(
            children=[
                html.A(
                    href='https://blueprintjs.com/docs',
                    children=dbpc.Card(
                        children=[
                            html.Div(
                                className='bp5-icon-link',
                                style={
                                    'margin-top': '15px',
                                    'margin-bottom': '15px',
                                    'font-size': '50px',
                                    'color': '#5f6b7c',
                                }
                            ),
                            html.H4('Official documentation')
                        ],
                        interactive=True
                    ),
                    style={
                        'text-decoration': 'none',
                    }
                ),
                html.A(
                    href='https://github.com/palantir/blueprint',
                    children=dbpc.Card(
                        children=[
                            html.Div(
                                className='bp5-icon-git-repo',
                                style={
                                    'margin-top': '15px',
                                    'margin-bottom': '15px',
                                    'font-size': '50px',
                                    'color': '#5f6b7c'
                                }
                            ),
                            html.H4('Official git repository')
                        ],
                        interactive=True
                    ),
                    style={'text-decoration': 'none'}
                ),
                html.A(
                    href="https://github.com/STEdyd666/dash-blueprint-components",
                    children=dbpc.Card(
                        children=[
                            html.Div(
                                className='bp5-icon-git-repo',
                                style={
                                    'margin-top': '15px',
                                    'margin-bottom': '15px',
                                    'font-size': '50px',
                                    'color': '#5f6b7c'
                                }
                            ),
                            html.H4('Dash git repository')
                        ],
                        interactive=True
                    ),
                    style={'text-decoration': 'none'}
                ),
                html.A(
                    href='/blueprint/quickstart',
                    children=dbpc.Card(
                        children=[
                            html.Div(
                                className='bp5-icon-star',
                                style={
                                    'margin-top': '15px',
                                    'margin-bottom': '15px',
                                    'font-size': '50px',
                                    'color': '#5f6b7c'
                                }
                            ),
                            html.H4('Getting started')
                        ],
                        interactive=True
                    ),
                    style={'text-decoration': 'none'}
                )
            ],
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'justify-content': 'space-between',
                'margin-top': '50px',
                'text-align': 'center',
                'gap': '20px'
            }
        )
    ]
)
