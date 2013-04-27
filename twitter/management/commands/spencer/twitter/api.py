import sys
import json
import os
import time
import requests
from requests_oauthlib import OAuth1

__OAUTH__ = None
URL = 'https://api.twitter.com/1.1/search/tweets.json'

def auth_from_file(file_path):
    global __OAUTH__
    if __OAUTH__ is None:
        file = open(file_path)
        raw = json.load(file)
        __OAUTH__ = OAuth1(client_key=raw['consumer_key'],
                           client_secret=raw['consumer_secret'],
                           resource_owner_key=raw['access_token'],
                           resource_owner_secret=raw['access_token_secret'])

def auth(consumer_key, consumer_secret, access_token, access_token_secret):
    global __OAUTH__
    if __OAUTH__ is None:
        __OAUTH__ = OAuth1(client_key=consumer_key,
                       client_secret=consumer_secret,
                       resource_owner_key=access_token,
                       resource_owner_secret=access_token_secret)

def search_to_statuses(parameters, url="https://api.twitter.com/1.1/search/tweets.json"):
    global __OAUTH__
    raw = (requests.get(url=url, auth=__OAUTH__, params=parameters)).json()
    return raw['statuses']

def status_to_user_dict(status):
    raw = status['user']
    id = raw['id']
    name = raw['name']
    screen_name = raw['screen_name']
    profile_url = 'https://twitter.com/' + screen_name
    profile_image_url = raw['profile_image_url']
    return dict(id=id, name=name, screen_name=screen_name, profile_url=profile_url, profile_image_url=profile_image_url)

def status_to_tweet_dict(status):
    id = status['id']
    text = status['text']
    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
    url = 'https://twitter.com/' + status['user']['screen_name'] + '/status/' + str(id)
    return dict(id=id, text=text, created_at=created_at, url=url)

def status_to_hashtags(status):
    hashtags = status['entities']['hashtags']
    hashtags_text = []
    for hashtag in hashtags:
        hashtags_text.append(hashtag['text'])
    return hashtags_text

def main():
    pass



if __name__ == "__main__":
    main()