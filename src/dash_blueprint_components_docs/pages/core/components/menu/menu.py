import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output, clientside_callback
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os
import inspect

from utils import parse_docstring, get_tablebody_from_props


component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Menu)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Menu)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dbpc.Menu(
                                    id='menu-1',
                                    children=[
                                        dbpc.MenuItem(
                                            icon='new-text-box',
                                            text='New text box'
                                        ),
                                        dbpc.MenuItem(
                                            icon='new-object',
                                            text='New object'
                                        ),
                                        dbpc.MenuItem(
                                            icon='new-link',
                                            text='New link'
                                        ),
                                        dbpc.MenuDivider(),
                                        dbpc.MenuItem(
                                            icon='cog',
                                            labelElement=html.Span(className="bp5-icon-standard bp5-icon-share"),
                                            text='Settings',
                                            intent='primary'
                                        )
                                    ],
                                    className='bp5-elevation-1'
                                )
                            ],
                            style={
                                'margin-right': '10px'
                            }  
                        ),
                        html.Div(
                            children=[
                                dbpc.Menu(
                                    id='menu-2',
                                    children=[
                                        dbpc.MenuDivider(title='Edit'),
                                        dbpc.MenuItem(
                                            icon='cut',
                                            text='Cut',
                                            label='⌘X'
                                        ),
                                        dbpc.MenuItem(
                                            icon='duplicate',
                                            text='Copy',
                                            label='⌘C'
                                        ),
                                        dbpc.MenuItem(
                                            icon='clipboard',
                                            text='Paste',
                                            label='⌘V',
                                            disabled=True
                                        ),
                                        dbpc.MenuDivider(title='Text'),
                                        dbpc.MenuItem(
                                            children=[
                                                dbpc.MenuItem(
                                                    icon='align-left',
                                                    text='Left'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='align-center',
                                                    text='Center'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='align-right',
                                                    text='Right'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='align-justify',
                                                    text='Justify'
                                                )
                                            ],
                                            icon='align-left',
                                            text='Alignment',
                                            disabled=True
                                        ),
                                        dbpc.MenuItem(
                                            children=[
                                                dbpc.MenuItem(
                                                    icon='bold',
                                                    text='Bold'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='italic',
                                                    text='Italic'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='underline',
                                                    text='Underline'
                                                )
                                            ],
                                            icon='style',
                                            text='Style',
                                        ),
                                        dbpc.MenuItem(
                                            children=[
                                                dbpc.MenuItem(
                                                    icon='badge',
                                                    text='Badge'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='book',
                                                    text='Long items will truncate when they reach max-width'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='more',
                                                    text='Look in here for even more items',
                                                    children=[
                                                        dbpc.MenuItem(
                                                            icon='briefcase',
                                                            text='Briefcase'
                                                        ),
                                                        dbpc.MenuItem(
                                                            icon='calculator',
                                                            text='Calculator'
                                                        ),
                                                        dbpc.MenuItem(
                                                            icon='dollar',
                                                            text='Dollar'
                                                        ),
                                                        dbpc.MenuItem(
                                                            icon='dot',
                                                            text='Shapes',
                                                            children=[
                                                                dbpc.MenuItem(
                                                                    icon='full-circle',
                                                                    text='Full circle'
                                                                ),
                                                                dbpc.MenuItem(
                                                                    icon='heart',
                                                                    text='Heart'
                                                                ),
                                                                dbpc.MenuItem(
                                                                    icon='ring',
                                                                    text='Ring'
                                                                ),
                                                                dbpc.MenuItem(
                                                                    icon='square',
                                                                    text='Square'
                                                                ),
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            ],
                                            icon='style',
                                            text='Style',
                                        ),
                                    ],
                                    className='bp5-elevation-1'
                                )
                            ]
                        )
                    ],
                    className='bp5-docs-page-example centered',
                    style={
                        'display': 'flex'
                    }
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        html.P(children='Size'),
                        dbpc.SegmentedControl(
                            id='menu-segmented-control',
                            options=[
                                {'label': 'Small', 'value': 'small'},
                                {'label': 'Regular', 'value': 'regular'},
                                {'label': 'Large', 'value': 'large'}
                            ],
                            value='regular'
                        )
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='menu-source',
            text='</> View source on GitHub',
            fill=True,
            minimal=True,
            intent='primary',
            className='bp5-source-button',
        ),
        html.H1('Usage'),
        html.P("Blueprint's Menu API includes three React components:"),
        html.Ul(
            children=[
                html.Li('Menu'),
                html.Li('MenuItem'),
                html.Li('MenuDivider'),
            ],
            className='bp5-list'
        ),
        html.Pre(
            children=[
                html.Code(
                    children=inspect.cleandoc('''<Menu>
                        <MenuItem icon="new-text-box" onClick={handleClick} text="New text box" />
                        <MenuItem icon="new-object" onClick={handleClick} text="New object" />
                        <MenuItem icon="new-link" onClick={handleClick} text="New link" />
                        <MenuDivider />
                        <MenuItem text="Settings..." icon="cog" intent="primary">
                            <MenuItem icon="tick" text="Save on edit" />
                            <MenuItem icon="blank" text="Compile on edit" />
                        </MenuItem>
                    </Menu>
                    '''),
                    style={
                        'font-size': '13px',
                    }
                )
            ],
            className='bp5-code-block language-jsx',
        ),
        html.P(children="<Menu> renders a <ul> container element for menu items and dividers."),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Menu)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H1('Menu item'),
        html.P("MenuItem is a single interactive item in a Menu."),
        html.P("This component renders an <li> containing an <a>. You can make the MenuItem interactive by defining the href, target, and onClick props as necessary."),
        html.P("Create submenus by nesting MenuItem elements inside each other as children. Remember to use the required text prop to define MenuItem content."),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dbpc.Menu(
                                    children=[
                                        dbpc.MenuItem(
                                            id='menu-item',
                                            icon='applications',
                                            text='Applications',
                                            children=[
                                                dbpc.MenuItem(
                                                    icon='add',
                                                    text='Add new application'
                                                ),
                                                dbpc.MenuItem(
                                                    icon='remove',
                                                    text='Remove application'
                                                )
                                            ]
                                        ),
                                    ],
                                    className='bp5-elevation-1'
                                )
                            ] 
                        )
                    ],
                    className='bp5-docs-page-example centered',
                    style={
                        'display': 'flex'
                    }
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='menu-item-active',
                            children='Active'
                        ),
                        dbpc.Switch(
                            id='menu-item-disabled',
                            children='Disabled'
                        ),
                        html.P(children='Selected'),
                        dbpc.SegmentedControl(
                            id='menu-item-segmented-control-1',
                            options=[
                                {'label': 'undefined', 'value': 'undefined'},
                                {'label': 'true', 'value': True},
                                {'label': 'false', 'value': False},
                            ],
                            value='undefined'
                        ),
                        html.P(children='Intent'),
                        dbpc.HTMLSelect(
                            id='menu-item-select',
                            options=[
                                {'label': 'None', 'value': 'none'},
                                {'label': 'Primary', 'value': 'primary'},
                                {'label': 'Success', 'value': 'success'},
                                {'label': 'Warning', 'value': 'warning'},
                                {'label': 'Danger', 'value': 'danger'}
                            ],
                            fill=True
                        ),
                        html.P(children='Role structure'),
                        dbpc.SegmentedControl(
                            id='menu-item-segmented-control-2',
                            options=[
                                {'label': 'menuitem', 'value': 'menuitem'},
                                {'label': 'listoption', 'value': 'listoption'},
                            ],
                            value='menuitem'
                        )
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.MenuItem)['props'])
                )
            ],
            className='bp5-html-table'
        ),
        html.H1('Menu divider'),
        html.P("MenuDivider is a decorative component used to group sets of items into sections which may optionally have a title."),
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.MenuDivider)['props'])
                )
            ],
            className='bp5-html-table'
        ),
    ]
)

clientside_callback(
    """
    function(_) {
        Prism.highlightAll()
        return dash_clientside.no_update
    }
    """,
    Output('menu-segmented-control', 'className'),
    Input('menu-segmented-control', 'id')
)

@callback(
    Output('menu-1', 'large'),
    Output('menu-1', 'small'),
    Output('menu-2', 'large'),
    Output('menu-2', 'small'),
    Input('menu-segmented-control', 'value')
)
def change(value):

    if value == 'large':
        return True, False, True, False
    elif value == 'small':
        return False, True, False, True
    else:
        return False, False, False, False

@callback(
    Output('menu-item', 'active'),
    Input('menu-item-active', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('menu-item', 'disabled'),
    Input('menu-item-disabled', 'checked')
)
def change(checked):
    return checked

@callback(
    Output('menu-item', 'selected'),
    Input('menu-item-segmented-control-1', 'value')
)
def change(value):
    return value

@callback(
    Output('menu-item', 'intent'),
    Input('menu-item-select', 'value')
)
def change(value):
    return value

@callback(
    Output('menu-item', 'roleStructure'),
    Input('menu-item-segmented-control-2', 'value')
)
def change(value):

    return value

@callback(
    Output('menu-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href