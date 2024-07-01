from dash import html, dcc


component = html.Div(
    children=[
        html.H1('Datetime', className='bp5-heading docs-title'),
        dcc.Markdown("""
        Dash components for interacting with dates and times:

        - [DatePicker](/datetime/date-picker) for selecting a single date (day, month, year).

        - [DateRangePicker](/datetime/date-range-picker) for selecting date ranges.

        - [DateInput](/datetime/date-input), which composes a text input with a DatePicker in a Popover, for use in forms.

        - [DateRangeInput](/datetime/date-range-input) , which composes two text inputs with a DateRangePicker in a Popover, for use in forms.
        
        - [TimePicker](/datetime/time-picker) for selecting a time (hour, minute, second, millisecond).

        """             
        )
    ]
)
