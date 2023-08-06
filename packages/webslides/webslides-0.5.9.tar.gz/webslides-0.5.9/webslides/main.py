import os
import sys
import codecs
import webbrowser

from webslides.modules.tohtml import *
from webslides.modules.generate import *
from webslides.modules.pagination import *
from webslides.modules.input_validations import *

def create(content=None
           , title_page=None
           , fname='output.html'
           , open_in_browser=True
           , show_index_page=False
           , show_highlights_page=False
           , show_topcat=True
           , show_subcat=True
           , show_highlights_only=False):
    """
    param pd (pagedata): list of lists with html strings or plotly fig objects ie.
        [[titlepage],[hl_page_title,hl_page_content],
        [index_page_title,index_page_content],
        [content_page1_title,content_page1_comments,content_page1_fig],
        [content_page2_title,content_page2_comments,content_page2_fig]]
    param fname: str filename for output file. If not provided defaults to 'output.html')
    param write: bool, False will only output to screen, True will write file AND output to screen
    return: str html code
    """

    # INPUT VALIDATIONS
    if title_page:
        title_error = validate_title_page(title_page)
        if title_error:
            print(title_error)
            return

    if content:
        content_error = validate_content(content)
        if content_error:
            print(content_error)
            return
    else:
        print('content variable is mandatory')

    # create dataframe from pagedata list and enrich with pagination data
    df = pagination_data(content=content, show_highlights_only=show_highlights_only)

    #################
    ## CREATE HTML ##
    #################

    # page shadow css options: https://getcssscan.com/css-box-shadow-examples
    html = """
    <html>
    <head><meta charset="utf-8" />
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
    .page {padding:50px; margin:100px; box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;}
    body {font-family: "Arial";} a {text-decoration: none;}
    </style>
    </head>
    <body>
    <span></span>
    </body>
    </html>
    """

    # 1. title page
    if title_page:
        page = {'title': title_page.get('title', ''),
                'img_url': title_page.get('img_url', ''),
                'summary': title_page.get('summary', ''),
                'footer': title_page.get('footer', list())}

        # start new page
        html = html.replace('<span></span>', '<div class="page"><span></span></div>')

        # reuse contenpage_to_html function (normally used for contenslides)
        html = titlepage_to_html(html, page)

        # close page
        html = html.replace('<span></span></div>', '</div><span></span>')

    # 2. index page
    if show_index_page:
        # start new page
        html = html.replace('<span></span>', '<div class="page"><span></span></div>')

        indexpage_html = generate_index_page(df, show_topcat=show_topcat, show_subcat=show_subcat)
        html = html.replace('<span></span>', indexpage_html + '<span></span>')

        # close page
        html = html.replace('<span></span></div>', '</div><span></span>')

    # 3. highlights page
    if show_highlights_page:
        # start new page
        html = html.replace('<span></span>', '<div class="page"><span></span></div>')

        hlpage_html = generate_highlights_page(df, show_topcat=show_topcat, show_subcat=show_subcat)
        html = html.replace('<span></span>', hlpage_html + '<span></span>')

        # close page
        html = html.replace('<span></span></div>', '</div><span></span>')

    # 4. content pages
    for idx, page in df.iterrows():
        # start new page
        html = html.replace('<span></span>', '<div class="page"><span></span></div>')

        # insert content html
        html = content_to_html(html, page,
                               show_topcat=show_topcat,
                               show_subcat=show_subcat,
                               show_index_page=show_index_page,
                               show_highlights_page=show_highlights_page,
                               show_navi=True)

        # close page
        html = html.replace('<span></span></div>', '</div><span></span>')

    ###################
    ## HANDLE OUTPUT ##
    ###################

    # create output directory 'out' if not present
    current_working_dir = os.getcwd()
    # current_working_dir = os.path.abspath(__file__)
    fpath = os.path.join(current_working_dir, 'wsout')

    if not os.path.exists(fpath):
        os.makedirs(fpath)

    with codecs.open(f"{fpath}/{fname}", "w", encoding='utf-8') as f:
        f.write(html)
        print(f'output saved as {fname}')


    if open_in_browser:
        # open in browser to check result
        htmlfile = f"{fpath}/{fname}"
        webbrowser.open(htmlfile)
        print(f'opened in browser {fname}')

    return None

