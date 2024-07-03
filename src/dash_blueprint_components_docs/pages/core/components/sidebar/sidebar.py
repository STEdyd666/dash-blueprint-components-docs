import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


items=[
    {
        "route": "/blueprintexample",
        "path": "pages.blueprint.blueprint",
        "level": 1,
        "title": "Blueprint",
        "isSection": False,
        "icon": "home",
        "content": [
            {
            "route": "/blueprintexample/quickstart",
            "path": "pages.blueprint.quickstart.quickstart",
            "level": 2,
            "title": "Quickstart",
            "isSection": False,
            "content": []
            }
        ]
    },
    {
        "route": "/coreexample",
        "path": "pages.core.core",
        "level": 1,
        "title": "Core",
        "isSection": False,
        "icon": "cube",
        "content": [
            {
                "route": "/coreexample/components",
                "path": "pages.core.components.components",
                "level": 2,
                "title": "Components",
                "isSection": True,
                "content": [
                    {
                        "route": "/coreexample/components/breadcrumb",
                        "path": "pages.core.components.breadcrumb.breadcrumb",
                        "level": 2,
                        "title": "Breadcrumb",
                        "isSection": False,
                        "content": []
                    },
                    {
                        "route": "/coreexample/components/buttons",
                        "path": "pages.core.components.buttons.buttons",
                        "level": 2,
                        "title": "Buttons",
                        "isSection": False,
                        "content": []
                    },
                ]
            }
        ]
    }
]


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.SideBar)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.SideBar)['description']),
        dbpc.Callout(
            children="""
                This component is not part of official set of React Blueprint components. It has been created starting from the component "NavMenuItem"
                of the official package "docs-theme", to build the Dash Blueprint documentation.
            """,
            intent='danger'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.SideBar(
                            items=items
                        ),
                    ],
                    className='bp5-docs-page-example-no-props',
                )
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='sidebar-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H2('Usage'),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.SideBar)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)

@callback(
    Output('sidebar-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href