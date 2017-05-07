import urllib
import urllib2
import json
from tweet import Tweet

TWITTER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMwQGgAAAAAAdnpTrBeudQ5M7kDsWAgL3TFG2wY%3DDq1CGmrmniuKt7tuexvvyR3jc1mPnpL4doIa7xOkKZZsmkaRGm'


def search(query):
    query_params = urllib.urlencode({
        'result_type': 'recent',
        'q': query
    })

    req = urllib2.Request(
        'https://api.twitter.com/1.1/search/tweets.json?{0}'.format(query_params))
    req.add_header('Authorization', 'Bearer {0}'.format(TWITTER_TOKEN))
    response = urllib2.urlopen(req)
    body = json.load(response)

    return [Tweet(t) for t in body['statuses']]
