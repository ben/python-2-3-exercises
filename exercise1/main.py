import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, json

TWITTER_TOKEN='AAAAAAAAAAAAAAAAAAAAAMwQGgAAAAAAdnpTrBeudQ5M7kDsWAgL3TFG2wY%3DDq1CGmrmniuKt7tuexvvyR3jc1mPnpL4doIa7xOkKZZsmkaRGm'

print('Hello! What would you like to search Twitter for?')
query = input()
print("Okay, searching for '{0}'...".format(query))

query_params = urllib.parse.urlencode({
  'result_type': 'recent',
  'q': query
})

req = urllib.request.Request('https://api.twitter.com/1.1/search/tweets.json?{0}'.format(query_params))
req.add_header('Authorization', 'Bearer {0}'.format(TWITTER_TOKEN))
response = urllib.request.urlopen(req)

body = json.loads(response.read().decode('utf-8'))
for tweet in body['statuses']:
  print('@{0} at {1}: '.format(
    tweet['user']['screen_name'],
    tweet['created_at']
  ), tweet['text'])
