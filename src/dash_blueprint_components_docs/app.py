
import importlib
from importlib_resources import files
import os
import dash
from dash import Dash, html, page_container, dcc, clientside_callback, Output, Input, State
import dash_blueprint_components as dbpc
import json


app = Dash(
    __name__, 
    use_pages=True,
    external_scripts=[
        'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js'
    ],
    external_stylesheets=[
        'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css'
    ],
    title='DBPC',
)

# set app config
githubroot = os.environ.get('GITHUBROOT')
app.server.config['GITHUB'] = githubroot

# load source file
jsondata = files('dash_blueprint_components_docs.src').joinpath('src.json').read_text()
src = json.loads(jsondata)

for d in src:
    for subdir in d['content']:
        for subsubdir in subdir['content']:                
            # get layout
            imported = importlib.import_module(subsubdir['path'])
            layout = html.Div(getattr(imported, "component"))

            # register with dash
            dash.register_page(
                subsubdir['module'],
                path=subsubdir['route'],
                name=subsubdir['name'],
                title=subsubdir['title'],
                description=subsubdir['description'],
                section=subsubdir['section'],
                layout=layout,
            )

        # get layout
        imported = importlib.import_module(subdir['path'])
        layout = html.Div(getattr(imported, "component"))

        # register with dash
        dash.register_page(
            subdir['module'],
            path=subdir['route'],
            name=subdir['name'],
            title=subdir['title'],
            description=subdir['description'],
            section=subdir['section'],
            layout=layout,
        )
    
    # get layout
    imported = importlib.import_module(d['path'])
    layout = html.Div(getattr(imported, "component"))

    # register with dash
    dash.register_page(
        d['module'],
        path=d['route'],
        name=d['name'],
        title=d['title'],
        description=d['description'],
        section=d['section'],
        layout=layout
    )

navbar = dbpc.SideBar(
	id='navbar',
    items=src
)

sidebartitle = html.Div(
    children='Dash Blueprint Components',
    className='bp5-navbar-heading',
    style={
        'font-size': '24px',
        'font-weight': '600',
        'margin-top': '20px',
        'margin-bottom': '30px',
    }
)

switchtheme = dbpc.Button(
    id='switch-theme',
    text='Dark theme',
    className='bp5-text-muted',
    minimal=True,
    outlined=False,
    fill=True,
    icon='flash',
    alignText='left',
)

layout = html.Div(
	children=[
		dcc.Location(id="url", refresh="callback-nav"),
        html.Div(
            children=[
                sidebartitle,
                dbpc.Divider(),
                switchtheme,
                dbpc.Divider(),
                html.Div(
                    children=navbar, 
                    style={
                        'margin-top': '20px'
                    }
                )
            ],
            className='bp5-sidebar'
        ),
        html.Div(
            children=page_container, 
            className='bp5-docs-page bp5-fill bp5-text-large'
        )
    ],
    className='bp5-docs-root',
    style={
        'padding-top': '40px'
    }
)

banner = html.Div(
    children=html.A(
        children='Click here to view the official Blueprint documentation!',
        href='https://blueprintjs.com/docs/'
    ),
    className='docs-banner bp5-intent-primary'
) 

layout = html.Div(
    id='main-div',
    children=html.Div(
        children=[
            banner,
            layout
        ], 
        className='bp5-html'
    ),
    className='bp5-dark'
)

app.layout = layout

clientside_callback(
    """
    function(value) {
        if (value) {
            return value
        }
    }
    """,
    Output("navbar", "initialRoute"),
    Input("url", "pathname"),
)

clientside_callback(
    """
    function(value, pathname) {
        console.log(pathname)
        if (value) {
            return value
        }

        if (pathname === "/") {
            return "/blueprint"
        } else {
            return pathname
        }
    }
    """,
    Output("url", "pathname"),
    Input("navbar", "route"),
    State("url", "pathname")
)

clientside_callback(
    """
    function(_, currentTheme) {
        if (currentTheme === "bp5-dark") {
            return ["", "Light theme", "flash"]
        } else {
            return ["bp5-dark", "Dark theme", "moon"]
        }
    }
    """,
    Output("main-div", "className"),
    Output("switch-theme", "text"),
    Output("switch-theme", "icon"),
    Input("switch-theme", "n_clicks"),
    State("main-div", "className"),
)

if __name__ == '__main__':
	app.run(debug=False)