import dash_blueprint_components as dbpc
from dash import html, callback, Input, Output
from dash.exceptions import PreventUpdate
from flask import current_app
import json
import os

from utils import parse_docstring, get_tablebody_from_props


films = [
    { 'label': "The Shawshank Redemption", 'rightLabel': 1994 },
    { 'label': "The Godfather", 'rightLabel': 1972 },
    { 'label': "The Godfather: Part II", 'rightLabel': 1974 },
    { 'label': "The Dark Knight", 'rightLabel': 2008 },
    { 'label': "12 Angry Men", 'rightLabel': 1957 },
    { 'label': "Schindler's List", 'rightLabel': 1993 },
    { 'label': "Pulp Fiction", 'rightLabel': 1994 },
    { 'label': "The Lord of the Rings: The Return of the King", 'rightLabel': 2003 },
    { 'label': "The Good, the Bad and the Ugly", 'rightLabel': 1966 },
    { 'label': "Fight Club", 'rightLabel': 1999 },
    { 'label': "The Lord of the Rings: The Fellowship of the Ring", 'rightLabel': 2001 },
    { 'label': "Star Wars: Episode V - The Empire Strikes Back", 'rightLabel': 1980 },
    { 'label': "Forrest Gump", 'rightLabel': 1994 },
    { 'label': "Inception", 'rightLabel': 2010 },
    { 'label': "The Lord of the Rings: The Two Towers", 'rightLabel': 2002 },
    { 'label': "One Flew Over the Cuckoo's Nest", 'rightLabel': 1975 },
    { 'label': "Goodfellas", 'rightLabel': 1990 },
    { 'label': "The Matrix", 'rightLabel': 1999 },
    { 'label': "Seven Samurai", 'rightLabel': 1954 },
    { 'label': "Star Wars: Episode IV - A New Hope", 'rightLabel': 1977 },
    { 'label': "City of God", 'rightLabel': 2002 },
    { 'label': "Se7en", 'rightLabel': 1995 },
    { 'label': "The Silence of the Lambs", 'rightLabel': 1991 },
    { 'label': "It's a Wonderful Life", 'rightLabel': 1946 },
    { 'label': "Life Is Beautiful", 'rightLabel': 1997 },
    { 'label': "The Usual Suspects", 'rightLabel': 1995 },
    { 'label': "Léon: The Professional", 'rightLabel': 1994 },
    { 'label': "Spirited Away", 'rightLabel': 2001 },
    { 'label': "Saving Private Ryan", 'rightLabel': 1998 },
    { 'label': "Once Upon a Time in the West", 'rightLabel': 1968 },
    { 'label': "American History X", 'rightLabel': 1998 },
    { 'label': "Interstellar", 'rightLabel': 2014 },
    { 'label': "Casablanca", 'rightLabel': 1942 },
    { 'label': "City Lights", 'rightLabel': 1931 },
    { 'label': "Psycho", 'rightLabel': 1960 },
    { 'label': "The Green Mile", 'rightLabel': 1999 },
    { 'label': "The Intouchables", 'rightLabel': 2011 },
    { 'label': "Modern Times", 'rightLabel': 1936 },
    { 'label': "Raiders of the Lost Ark", 'rightLabel': 1981 },
    { 'label': "Rear Window", 'rightLabel': 1954 },
    { 'label': "The Pianist", 'rightLabel': 2002 },
    { 'label': "The Departed", 'rightLabel': 2006 },
    { 'label': "Terminator 2: Judgment Day", 'rightLabel': 1991 },
    { 'label': "Back to the Future", 'rightLabel': 1985 },
    { 'label': "Whiplash", 'rightLabel': 2014 },
    { 'label': "Gladiator", 'rightLabel': 2000 },
    { 'label': "Memento", 'rightLabel': 2000 },
    { 'label': "The Prestige", 'rightLabel': 2006 },
    { 'label': "The Lion King", 'rightLabel': 1994 },
    { 'label': "Apocalypse Now", 'rightLabel': 1979 },
    { 'label': "Alien", 'rightLabel': 1979 },
    { 'label': "Sunset Boulevard", 'rightLabel': 1950 },
    { 'label': "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", 'rightLabel': 1964 },
    { 'label': "The Great Dictator", 'rightLabel': 1940 },
    { 'label': "Cinema Paradiso", 'rightLabel': 1988 },
    { 'label': "The Lives of Others", 'rightLabel': 2006 },
    { 'label': "Grave of the Fireflies", 'rightLabel': 1988 },
    { 'label': "Paths of Glory", 'rightLabel': 1957 },
    { 'label': "Django Unchained", 'rightLabel': 2012 },
    { 'label': "The Shining", 'rightLabel': 1980 },
    { 'label': "WALL·E", 'rightLabel': 2008 },
    { 'label': "American Beauty", 'rightLabel': 1999 },
    { 'label': "The Dark Knight Rises", 'rightLabel': 2012 },
    { 'label': "Princess Mononoke", 'rightLabel': 1997 },
    { 'label': "Aliens", 'rightLabel': 1986 },
    { 'label': "Oldboy", 'rightLabel': 2003 },
    { 'label': "Once Upon a Time in America", 'rightLabel': 1984 },
    { 'label': "Witness for the Prosecution", 'rightLabel': 1957 },
    { 'label': "Das Boot", 'rightLabel': 1981 },
    { 'label': "Citizen Kane", 'rightLabel': 1941 },
    { 'label': "North by Northwest", 'rightLabel': 1959 },
    { 'label': "Vertigo", 'rightLabel': 1958 },
    { 'label': "Star Wars: Episode VI - Return of the Jedi", 'rightLabel': 1983 },
    { 'label': "Reservoir Dogs", 'rightLabel': 1992 },
    { 'label': "Braveheart", 'rightLabel': 1995 },
    { 'label': "M", 'rightLabel': 1931 },
    { 'label': "Requiem for a Dream", 'rightLabel': 2000 },
    { 'label': "Amélie", 'rightLabel': 2001 },
    { 'label': "A Clockwork Orange", 'rightLabel': 1971 },
    { 'label': "Like Stars on Earth", 'rightLabel': 2007 },
    { 'label': "Taxi Driver", 'rightLabel': 1976 },
    { 'label': "Lawrence of Arabia", 'rightLabel': 1962 },
    { 'label': "Double Indemnity", 'rightLabel': 1944 },
    { 'label': "Eternal Sunshine of the Spotless Mind", 'rightLabel': 2004 },
    { 'label': "Amadeus", 'rightLabel': 1984 },
    { 'label': "To Kill a Mockingbird", 'rightLabel': 1962 },
    { 'label': "Toy Story 3", 'rightLabel': 2010 },
    { 'label': "Logan", 'rightLabel': 2017 },
    { 'label': "Full Metal Jacket", 'rightLabel': 1987 },
    { 'label': "Dangal", 'rightLabel': 2016 },
    { 'label': "The Sting", 'rightLabel': 1973 },
    { 'label': "2001: A Space Odyssey", 'rightLabel': 1968 },
    { 'label': "Singin' in the Rain", 'rightLabel': 1952 },
    { 'label': "Toy Story", 'rightLabel': 1995 },
    { 'label': "Bicycle Thieves", 'rightLabel': 1948 },
    { 'label': "The Kid", 'rightLabel': 1921 },
    { 'label': "Inglourious Basterds", 'rightLabel': 2009 },
    { 'label': "Snatch", 'rightLabel': 2000 },
    { 'label': "3 Idiots", 'rightLabel': 2009 },
    { 'label': "Monty Python and the Holy Grail", 'rightLabel': 1975 },
]

component = html.Div(
    children=[
        html.H1(parse_docstring(dbpc.Select)['name'], className='bp5-heading docs-title'),
        html.P(parse_docstring(dbpc.Select)['description']),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbpc.Select(
                            id='select',
                            items=films
                        )
                    ],
                    className='bp5-docs-page-example centered',
                ),
                html.Div(
                    children=[
                        html.H4('Props'),
                        dbpc.Switch(
                            id='select-filter',
                            children='Filterable',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='select-resetclose',
                            children='Reset on close',
                        ),
                        dbpc.Switch(
                            id='select-resetquery',
                            children='Reset on query',
                            defaultChecked=True
                        ),
                        dbpc.Switch(
                            id='select-resetselect',
                            children='Reset on select',
                        ),
                        dbpc.Switch(
                            id='select-useinitial',
                            children='Use initial content'
                        ),
                        html.H4('Appearance props'),
                        dbpc.Switch(
                            id='select-disabled',
                            children='Disabled'
                        ),
                        dbpc.Switch(
                            id='select-fill',
                            children='Fill container width'
                        ),
                        html.H4('Popover props'),
                        dbpc.Switch(
                            id='select-matchwidth',
                            children='Match target width'
                        ),
                        dbpc.Switch(
                            id='select-minimalpopover',
                            children='Minimal popover style',
                        ),
                    ],
                    className='bp5-docs-page-example-props',
                ),
            ],
            className='bp5-docs-page-example-container'
        ),
        dbpc.AnchorButton(
            id='select-source',
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
                    children=get_tablebody_from_props(parse_docstring(dbpc.Select)['props'])
                )
            ],
            className='bp5-html-table'
        )
    ]
)


@callback(
    Output('select', 'filterable'),
    Input('select-filter', 'checked')  
)
def change(value):

    return not value

@callback(
    Output('select', 'resetOnClose'),
    Input('select-resetclose', 'checked')  
)
def change(value):

    return value

@callback(
    Output('select', 'resetOnQuery'),
    Input('select-resetquery', 'checked')  
)
def change(value):

    return not value

@callback(
    Output('select', 'resetOnSelect'),
    Input('select-resetselect', 'checked')  
)
def change(value):

    return value

@callback(
    Output('select', 'initialContent'),
    Input('select-useinitial', 'checked')  
)
def change(value):
    if value:
        return html.Ul(
            children=dbpc.MenuItem(
                disabled=True,
                text='100 items loaded',
                roleStructure='listoption'
            ), 
            role='listbox', 
            className='bp5-menu'
        )
    else:
        return None

@callback(
    Output('select', 'disabled'),
    Input('select-disabled', 'checked')  
)
def change(value):

    return value

@callback(
    Output('select', 'fill'),
    Input('select-fill', 'checked')  
)
def change(value):

    return value

@callback(
    Output('select', 'matchTargetWidth'),
    Input('select-matchwidth', 'checked')  
)
def change(value):

    return value

@callback(
    Output('select', 'minimal'),
    Input('select-minimalpopover', 'checked')  
)
def change(value):

    return value

@callback(
    Output('select-source', 'href'),
    Input('navbar', 'route')
)
def sethref(route):
    if route is None:
        raise PreventUpdate
    repo = current_app.config['GITHUB']
    basename = os.path.basename(route)
    href = f'{repo}{route}/{basename}.py'
    return href