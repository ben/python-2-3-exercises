#!/usr/bin/env python

from __future__ import print_function
from builtins import input
import io
from twitter import api, template

print('Hello! What would you like to search Twitter for?')
query = input()
print("Okay, searching for '{0}'...".format(query))

tweets = api.search(query)
html = template.render(query, sorted(tweets))
with io.open('/tmp/tweets.html', 'w') as F:
    F.write(html)
print('Done! Open file:///tmp/tweets.html to see the results!')
