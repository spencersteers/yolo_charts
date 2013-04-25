import sys
import json
import requests
import time
from requests_oauthlib import OAuth1

CONSUMER_KEY = "Z67KnzNnx8PQCpPKhK5TA"
CONSUMER_SECRET = "Y1GG4iVHEJnx656a3XL9Vzd1j2BOz3o4u9kLhyXjoIs"
ACCESS_TOKEN = "158526890-y3gnw94g75mqaVZSbfh3IuDop7KJiWUQQxQwzwU6"
ACCESS_TOKEN_SECRET = "gw3ESNps8qCabcFbjKSKMyBxpgKmH7AwGLJRxS2Zw"

URL = 'https://api.twitter.com/1.1/search/tweets.json'

OAUTH = OAuth1(client_key=CONSUMER_KEY,
               client_secret=CONSUMER_SECRET,
               resource_owner_key=ACCESS_TOKEN,
               resource_owner_secret=ACCESS_TOKEN_SECRET)

def twitter_search_to_statuses(parameters, url="https://api.twitter.com/1.1/search/tweets.json", auth=OAUTH,):
    raw = (requests.get(url=url, auth=auth, params=parameters)).json()
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
    created_at = ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
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