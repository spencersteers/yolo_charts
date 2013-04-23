import sys
import json
import os
from pprint import pprint


twitter_auth_json = open('twitter/management/commands/twitter-auth.json')

data = json.load(twitter_auth_json)

CONSUMER_KEY = data['consumer_key']
CONSUMER_SECRET = data['consumer_secret']
ACCESS_TOKEN = data['access_token']
ACCESS_TOKEN_SECRET = data['access_token_secret']

twitter_auth_json.close()