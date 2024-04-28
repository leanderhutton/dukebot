#!/usr/bin/python
# Simple Twitter bot in python.  I'm sure there are better ones out there.
# Requires python-twitter: http://code.google.com/p/python-twitter/

import twitter
import logging
from random import choice


# User definable variables
consumer_key = ''
consumer_secret=''
access_token_key=''
access_token_secret=''
logfile='dukebot.log'
api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

logging.basicConfig(filename=logfile,level=logging.DEBUG)

# Duke's vocabulary of one liners
vocab = ["Bitchin!", "Blow it out your ass!", "Damn... I'm looking good!", "Oh...your ass is grass and I've got the weed-whacker.", "Shake it, baby!", "You're an inspiration for birth control.", "Your face, your ass, what's the difference?", "Let's rock!", "My name is Duke Nukem", "I've got balls of steel", "BALLS BALLS BALLS", "What? Did you think I was gone forever?", "Hail to the King, baby!", "My job is to kick ass, not make small talk.", "Looks like those alien bastards drank all my beer.", "Oh yeah! I'm bringing sexy back", "Take your pills...er...vitamins every day and you might grow up to be as awesome as me.", "Huh, I was expecting a monkey", "Pucker up, buttercup!", "Life is like a box of ammo.", "I like big guns, and I cannot lie.", "Get back to work, you slacker!", "Go ahead, make my day. ", "Damn, you're ugly", "Come get some!"]

def makeReply():

	replies = api.GetReplies()
	if len(replies) == 0:
		jerks = []
		for r in replies:
			screenname = r.user.screen_name
			jerks.append(screenname)

		poorBastard = choice(jerks)
		oneLiner = choice(vocab)
	
		tweet = "@"+poorBastard+ " "+oneLiner
		return tweet

	else:
		# Get a list of possible targets
		friends = api.GetFollowers()
		# Randomly select the poor person
		poorBastard = choice(friends)
		# Randomly select a one liner
		oneLiner = choice(vocab)
		# assemble the tweset
		tweet = "@"+poorBastard.screen_name+" "+oneLiner
		return tweet


def makeRandomTweet():
		# Get a list of possible targets
		friends = api.GetFollowers()
		# Randomly select the poor person
		poorBastard = choice(friends)
		# Randomly select a one liner
		oneLiner = choice(vocab)
		# assemble the tweset
		tweet = "@"+poorBastard.screen_name+" "+oneLiner
		return tweet
	
numTweets = 0
while (numTweets < 4):
	if numTweets%2==0:
		tweet = makeRandomTweet()
		logging.info(tweet)

	else:
		tweet = makeReply()
		logging.info(tweet)
	numTweets = numTweets + 1
	
api.PostUpdate(tweet)

