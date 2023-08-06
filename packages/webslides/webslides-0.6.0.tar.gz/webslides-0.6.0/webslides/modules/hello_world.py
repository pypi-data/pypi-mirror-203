# imports
import main as ws
import plotly.graph_objects as go

# title page
title_page = {
    'img_url': '',
    'title': 'Title of Title Page',
    'summary': {'Summary item 1': 'item text 1', 'Summary item 2': 'item text 2'},
    'footer': ['- use custom title image via the img_url parameter', '- footer2']
}


# simple plotly fig
def simple_fig():
    x = list(range(1, 11))
    y1 = [2 * i for i in x]
    y2 = [3 * i for i in x]
    trace1 = go.Scatter(x=x, y=y1, mode='markers+lines', name='Line 1')
    trace2 = go.Scatter(x=x, y=y2, mode='markers+lines', name='Line 2')
    fig = go.Figure()
    fig.add_trace(trace1)
    fig.add_trace(trace2)
    fig.update_layout(title='Simple Plotly Line Figure with Two Lines')
    return fig


# content pages
content = {
    'Topcat A': {
        'Subcat X': [
            {
                'title': 'Page Title 1 - HTML body',
                'highlights': ['- highlight 1', '- highlight 2'],
                'body': 'Content 1: this is a <b>HTML string</b>',
                'footer': ['- footer 1a', '- <i>italic footer 1b</i>'],
                'show': True},
            {
                'title': 'Page Title 2 - No highlights',
                'body': 'Content 2: this is a <b>HTML string</b>',
                'footer': ['- Note: No highlights, so no lightbulb in the index page', '- <i>italic footer 2b</i>'],
                'show': True}
        ],
        'Subcat Y': [
            {
                'title': 'Page Title 3 - Plotly fig !',
                'highlights': ['- highlight 3', '- note: no footer on this page'],
                'body': simple_fig(),
                'show': True}
        ]
    },
    'Topcat B': {
        'Subcat Z': [
            {
                'title': 'Page Title 4 - Different topcat',
                'highlights': ['- highlight 5', '- highlight 6'],
                'body': 'Content 3',
                'footer': ['- footer 4a', '- footer 4b'],
                'show': True}
        ]
    }
}

# MAIN
ws.create(content=content
          , title_page=title_page
          , fname='webslides_hello_world.html'
          , open_in_browser=True
          , show_index_page=True
          , show_topcat=True
          , show_subcat=True
          , show_highlights_page=True
          , show_highlights_only=False)
