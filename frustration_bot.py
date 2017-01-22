#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""frustation_bot.py: Searches for tweets that mispell
 	"frustrating" as "fustrating" and corrects the user."""

import credentials
import time
import tweepy

CONSUMER_KEY = credentials.keys['consumer_key']
CONSUMER_SECRET = credentials.keys['consumer_secret']
ACCESS_TOKEN = credentials.keys['access_token']
ACCESS_SECRET = credentials.keys['access_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


def main():	
	for s in api.search(q="fustrating"):
		try:
			sn = s.user.screen_name
			m = "@{} I'm sorry to correct you, but I think you " \
			 	"meant the word \"frustrating\"".format(sn)
			api.update_status(m, s.id)
			time.sleep(86400) # 24 hours

		except tweepy.TweepError as e:
			print(e.reason)
			time.sleep(2)


if __name__ == "__main__":
	main()