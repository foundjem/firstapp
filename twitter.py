#!/usr/bin/env python3

import json
import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'DVB03IhBVN8GBPv2Xllu95Bqy'
consumer_secret = 'tjxVCsVmUvvXx6V31pVnPXKNDop52tWSofOiysKVQwiPmQwlGY'
access_token = '151284278-3yBILdBKPJKoV7fSfIRJODmiDvcI9lgnPTwWVnSJ'
access_secret = 'DGmMyt9J3NHZNYTz9kJrzwcq1dzasgZ9oufSkqar783r1'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(110):
    # Process a single status
    print(status.text) 

def process_or_store(tweet):
    #The function process_or_store() is a place-holder for your custom implementation. 
    #In the simplest form, you could just print out the JSON, one tweet per line:
    print(json.dumps(tweet))

    
for status in tweepy.Cursor(api.home_timeline).items(110):
    # Process a single status
    process_or_store(status._json) 

for friend in tweepy.Cursor(api.friends).items():
    #What if we want to have a list of all our followers
    process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    #And how about a list of all our tweets
    process_or_store(tweet._json)



