from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import json
from .tweet import Tweet

TWITTER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMwQGgAAAAAAdnpTrBeudQ5M7kDsWAgL3TFG2wY%3DDq1CGmrmniuKt7tuexvvyR3jc1mPnpL4doIa7xOkKZZsmkaRGm'


def search(query):
    query_params = urllib.parse.urlencode({
        'result_type': 'recent',
        'q': query
    })

    req = urllib.request.Request(
        'https://api.twitter.com/1.1/search/tweets.json?{0}'.format(query_params))
    req.add_header('Authorization', 'Bearer {0}'.format(TWITTER_TOKEN))
    response = urllib.request.urlopen(req)
    body = json.load(response)

    return [Tweet(t) for t in body['statuses']]
