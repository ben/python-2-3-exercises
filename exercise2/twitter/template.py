template = None
import os.path


def load_template():
    global template
    if template == None:
        basepath = os.path.dirname(__file__)
        with open(os.path.join(basepath, 'template.html'), 'r') as F:
            template = F.read()
    return template


def render(query, tweets):
    return load_template() \
        .replace('{{QUERY}}', query) \
        .replace('{{TWEETS}}', '<hr/>'.join(unicode(t) for t in tweets))
