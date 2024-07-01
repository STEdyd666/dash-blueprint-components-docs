from dash import html


def parse_docstring(component) -> dict:
    """Parse component docstring"""
    docstring = dict()

    # get name
    docstring['name'] = component.__name__
    
    # split content
    content = component.__doc__.split('\n\n')
    
    # get component description
    rawdescription = content[0]
    description = rawdescription.split('\n', maxsplit=1)[1]
    docstring['description'] = description
    
    # loop over props
    rawprops = content[2:]
    props = list()
    for rawprop in rawprops:
        # split name/type and component description
        rawpropnametype, rawpropdescription = rawprop.split('):')

        # get name and type
        propnametype = rawpropnametype.split('-')[1].strip()
        rawpropname, rawproptype = propnametype.split('(')
        propname = rawpropname.strip()
        proptype = rawproptype.strip()

        # get description
        propdescription = ' '.join([v.strip() for v in rawpropdescription.split('\n')])

        # append new prop
        props.append({
            'name': propname,
            'type': proptype,
            'description': propdescription
        })

    docstring['props'] = props
    
    return docstring

def get_tablebody_from_props(props):
    """Create an html table starting from component props"""
    tr = list()
    for prop in props:
        row = html.Tr(
            children=[
                html.Td(
                    children=[
                        html.Div(
                            children=prop['name'],
                            className='bp5-code',
                            style={
                                'width': 'fit-content'
                            }
                        )
                    ]
                ),
                html.Td(
                    children=[
                        html.Div(
                            children=prop['type'],
                            className='docs-props-details'
                        ),
                        html.Div(children=prop['description'])
                    ]
                )
            ]
        )
        tr.append(row)

    return tr