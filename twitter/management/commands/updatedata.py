from __init__ import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

import sys
import json
import requests

from requests_oauthlib import OAuth1
from pprint import pprint
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from twitter.models import Hashtag, User, Tweet


class RawHashtag:
    def __init__(self, text):
        self.text = text
        self.count = 0

class RawUser:
    def __init__(self, name, screen_name):
        self.name = name
        self.screen_name = screen_name

class RawTweet:
    def __init__(self, text, date):
        self.text = text
        self.date = date

class Command(BaseCommand):

    SEARCH_QUERY = '#YOLO'
    SEARCH_COUNT = 1

    URL = 'https://api.twitter.com/1.1/search/tweets.json'

    OAUTH = OAuth1(client_key=CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=ACCESS_TOKEN,
                   resource_owner_secret=ACCESS_TOKEN_SECRET)

    def handle(self, *args, **options):
        url_params = {'q' : self.SEARCH_QUERY, 'count' : self.SEARCH_COUNT}
        result = requests.get(url=self.URL, auth=self.OAUTH, params=url_params)
        json_result = result.json()
        pprint(json_result)
        for status in json_result['statuses']:
            for hashtag in status['entities']['hashtags']:
                if hashtag['text'].upper() == 'YOLO':
                    self.is_yolo(status)
                    break

    def is_yolo(self, json):
        user_json = json['user']
        tweet_json = json
        hashtags_json = json['entities']['hashtags']

        hs = self.get_hashtags_info(hashtags_json=hashtags_json)
        u = self.get_user_info(user_json=user_json, hashtags=hs)
        t = self.get_tweet_info(tweet_json=tweet_json, user=u)

        for h in hs:
            h.save()

        u.save()
        t.save()

    def get_user_info(self, user_json, hashtags):
        user_id = user_json['id']
        user_name = user_json['name']
        user_screen_name = user_json['screen_name']
        
        u, created = User.objects.get_or_create(id=user_id, name=user_name, screen_name=user_screen_name)
        
        for hashtag in hashtags:
            u.hashtags.add(hashtag)

        print("USER INFO: ", user_id, user_name, user_screen_name)
        return u

    def get_tweet_info(self, tweet_json, user):
        tweet_id = tweet_json['id']
        tweet_text = tweet_json['text']
        tweet_date = tweet_json['created_at']
        t, created = Tweet.objects.get_or_create(id=tweet_id, user=user, text=tweet_text, date=datetime.now())
        print("TWEET INFO: ", tweet_id, tweet_text, tweet_date)
        return t

    def get_hashtags_info(self, hashtags_json):
        hashtag_texts = []
        hashtags = []
        for hashtag in hashtags_json:
            hashtag_texts.append(hashtag['text'])
            htag, created = Hashtag.objects.get_or_create(text=hashtag['text'])
            hashtags.append(htag)

        print("HASHTAG INFO: ", hashtag_texts)
        return hashtags

if __name__ == "__main__":
    Command().handle()