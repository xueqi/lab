from django import template

register = template.Library()
@register.inclusion_tag('notebook/show_one_article_html.html')
def show_one_article_html(article):
    return {"article" : article}

@register.inclusion_tag('notebook/show_one_forum_div.html')
def show_one_forum_div(forum):
    return {"forum" : forum}

@register.filter(name="highlight")
def highlight_content(content):
    '''
        highlight content
    '''
    from pygments.formatters import HtmlFormatter
    from pygments import highlight
    from pygments.lexers import PythonLexer
    import re
    highlighted = ""
    l = content.find('&lt;py&gt;')
    print "l = ", l
    if l < 0:
        highlighted = content
    r = 0
    while l >= 0:
        highlighted += content[r:l]
        l+=10
        print r, l
        r = content.find('&lt;/py&gt;', l)
        print r, l
        if r > 0:
            highlighted += "<div class=\"highlight\">%s</div>" % highlight(re.sub("<[^>]+>", "", content[l:r]).replace("&nbsp;", " "), PythonLexer(), HtmlFormatter(linenos = "table"))
            r+=11
        else:
            highlighted += content[l:]
            break
        l = content.find('&lt;py&gt;', r)
        if l < 0:
            highlighted += content[r:]
    return highlighted
