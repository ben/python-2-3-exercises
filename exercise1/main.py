import urllib, urllib2, json

TWITTER_TOKEN='AAAAAAAAAAAAAAAAAAAAAMwQGgAAAAAAdnpTrBeudQ5M7kDsWAgL3TFG2wY%3DDq1CGmrmniuKt7tuexvvyR3jc1mPnpL4doIa7xOkKZZsmkaRGm'

print 'Hello! What would you like to search Twitter for?'
query = raw_input()
print "Okay, searching for '{0}'...".format(query)

query_params = urllib.urlencode({
  'result_type': 'recent',
  'q': query
})

req = urllib2.Request('https://api.twitter.com/1.1/search/tweets.json?{0}'.format(query_params))
req.add_header('Authorization', 'Bearer {0}'.format(TWITTER_TOKEN))
response = urllib2.urlopen(req)

body = json.load(response)
for tweet in body['statuses']:
  print '@{0} at {1}: '.format(
    tweet['user']['screen_name'],
    tweet['created_at']
  ), tweet['text']
