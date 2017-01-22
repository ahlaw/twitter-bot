#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""hashtag_follow.py: Follows and retweets others based on query.
	Number of users followed is taken from second command line argument.
	Query is taken from command line arguments after the number.
	Queried user must have over 10000 followers."""

import credentials
import time
import tweepy
import sys

CONSUMER_KEY = credentials.keys['consumer_key']
CONSUMER_SECRET = credentials.keys['consumer_secret']
ACCESS_TOKEN = credentials.keys['access_token']
ACCESS_SECRET = credentials.keys['access_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


def main():
	tag = ["#"+item for item in sys.argv[2:]]
	query = " OR ".join(tag)

	for tweet in tweepy.Cursor(api.search, q=query).items(int(sys.argv[1])):
		try:
			if not tweet.user.following and \
			tweet.user.followers_count > 10000:
				tweet.user.follow()
				tweet.favorite()

		except tweepy.TweepError as e:
			print(e.reason)

		except StopIteration:
			break


if __name__ == "__main__":
	main()