from dash import html


component = html.Div(
    children=[
        html.H1('Core', className='bp5-heading docs-title'),
        html.P("""
        The @blueprintjs/core NPM package is the basis of any Blueprint app. It includes many (30+) React components 
        covering all the basic bases, from buttons to form controls to tooltips and trees. It also includes CSS styles 
        for every component and an elegant color palette.
        """             
        )
    ],
)
