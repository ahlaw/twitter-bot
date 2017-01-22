#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""manage_follows.py: Follows new followers every day and unfollows
	friends who have not followed you back every week."""

import credentials
import time
import tweepy

USER_ID = credentials.keys['user_id']
CONSUMER_KEY = credentials.keys['consumer_key']
CONSUMER_SECRET = credentials.keys['consumer_secret']
ACCESS_TOKEN = credentials.keys['access_token']
ACCESS_SECRET = credentials.keys['access_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


def follow_back():
	"""
	Follows new followers.
	"""
	for follower in tweepy.Cursor(api.followers).items():
		try:
			follower.follow()
		except tweepy.TweepError as e:
			print(e.reason)
			time.sleep(2)


def unfollow():
	"""
	Unfollows users that do not follow you back.
	"""
	for friend in api.friends_ids(user_id=USER_ID):
		print(friend)
		if friend not in api.followers_ids(user_id=USER_ID):
			try:
				api.destroy_friendship(user_id=friend)
			except tweepy.TweepError as e:
				print(e.reason)
				time.sleep(2)


def main():
	"""
	Follows daily and unfollows weekly.
	"""
	while True:
		follow_back()
		unfollow()
		time.sleep(86400) # 24 hours
		for i in range(6):
			follow_back()
			time.sleep(86400)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Program stopped")
		quit()