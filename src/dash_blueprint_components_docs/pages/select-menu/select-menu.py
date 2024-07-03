from dash import html, dcc


component = html.Div(
    children=[
        html.H1('Select', className='bp5-heading docs-title'),
        dcc.Markdown("""
        Dash components for selecting items from a list:

        - [Select](/select-menu/select) for selecting items in a list.

        - [Suggest](/select-menu/suggest) for selecting items in a list, from a text input.

        - [MultiSelect](/select-menu/multi-select) for selecting multiple items in a list.

        - [Omnibar](/select-menu/omnibar), a macOS spotlight-style typeahead component.

        """             
        )
    ]
)