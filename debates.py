# Adapted from:
# http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html
# http://docs.tweepy.org/en/v3.4.0/auth_tutorial.html#auth-tutorial
# https://github.com/tweepy/examples/blob/master/streamwatcher.py


import tweepy
from keys import consumer_key, consumer_secret, access_token, access_token_secret


class DebateListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status)


if __name__ == '__main__':

	auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, DebateListener(), timeout=None)

	stream.filter(track=['#debates','#debates2016'], async=True)