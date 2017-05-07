import unittest
import random
import datetime
import re
from twitter.tweet import Tweet
from twitter import template


def tweet(screen_name, text, followers=None, created=None):
    if followers == None:
        followers = random.randint(1, 200)
    if created == None:
        created = str(datetime.datetime.now())
    return Tweet({
        'created_at': created,
        'text': text,
        'user': {
            'screen_name': screen_name,
            'followers_count': followers
        }
    })


class TestTweet(unittest.TestCase):
    def test_sorting(self):
        # More popular tweeters come first
        less = tweet('abc', 'something', 20)
        more = tweet('def', 'something', 30)
        [first, second] = sorted([less, more])
        self.assertEqual(first, more)
        self.assertEqual(second, less)

    def test_stringify(self):
        t = str(tweet('abc', 'something'))
        self.assertRegexpMatches(t, '@abc')
        self.assertRegexpMatches(t, 'something')


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.tweets = [tweet('user%d' % i, 'message %d' % i)
                       for i in range(100)]
        self.rendered = template.render('xyz', self.tweets)

    def test_separators(self):
        self.assertEqual(len(re.findall('<hr', self.rendered)), 99)

    def test_query_mentioned(self):
        self.assertRegexpMatches(self.rendered, 'xyz')

if __name__ == '__main__':
    unittest.main()
