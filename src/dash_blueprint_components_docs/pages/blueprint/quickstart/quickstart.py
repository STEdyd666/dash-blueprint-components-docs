from dash import html, Input, Output, clientside_callback
import inspect


component = html.Div(
    children=[
        html.H1('Quickstart', className='bp5-heading docs-title'),
        html.P('Install the Dash Blueprint Components package using pip and import the library.'),
        html.Pre(
            children=[
                html.Code(
                    id='quickstart-code',
                    children=inspect.cleandoc("""
                        from dash import Dash, html, callback, Input, Output
                        import dash_blueprint_components as dbpc


                        app = Dash(
                            __name__,
                        )

                        app.layout = html.Div(
                            children=[
                                dbpc.Button(
                                    id='button',
                                    text='Click me!'
                                ),
                                html.Div(
                                    id='output'
                                )
                            ]
                        )

                        @callback(
                            Output('output', 'children'),
                            Input('button', 'n_clicks')
                        )
                        def click(n_clicks):
                            if n_clicks is not None:
                                return n_clicks

                        if __name__ == "__main__":
                            app.run_server()
                    """),
                    style={
                        'font-size': '13px',
                    }
                )
            ],
            className='bp5-code-block language-python',
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
    Output('quickstart-code', 'style'),
    Input('quickstart-code', 'id')
)