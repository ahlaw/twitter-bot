#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tweet_textfile.py: Takes a text file as a second command line
	line argument and periodically tweets it line by line."""

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


def tweet(text_file):
	""" 
	Tweets a line from a text file every 2 hours.
	Filename is stated after script name.
	"""
	my_file = str(sys.argv[1])

	with open(text_file, 'r') as f:
		file_lines = f.readlines()

	for line in file_lines:
		try:
			if line != '\n':
				api.update_status(line)
				time.sleep(7200)
		except tweepy.TweepError as e:
			print(e.reason)
			time.sleep(2)


def main():
	""" 
	Passes filename stated after scriptname to tweet(text_file)
	"""
	filename = str(sys.argv[1])
	tweet(filename)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Program stopped")
		quit()