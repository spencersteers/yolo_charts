from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from twitter.models import Hashtag, User, Tweet
from pprint import pprint
from spencer.twitter import api


class Command(BaseCommand):
    """updates, creates, twitter models"""


    auth_file = 'twitter/management/commands/auth.json'
    option_list = BaseCommand.option_list + (
        make_option('-u', '--users',
            dest='users',
            type='int',
            help='Number of "#yolo" statuses to search through'),
        ),
        #make_option('-t', '--tweets',
        #    dest='tweets',
        #    type='int',
        #    help='Number of tweets to search for each user'),
        #)

    def handle(self, *args, **options):
        if options['users']:
            api.auth_from_file(file_path=self.auth_file)
            url_params = {'q' : '#yolo', 'count' : options['users']}
            self.fetch_new_users(p=url_params)
        if options['tweets']:
            

    def fetch_new_users(self, p):
        statuses = api.search_to_statuses(parameters=p)
        users = []
        tweets = []
        hashtags = []
        for status in statuses:
            user_dict = api.status_to_user_dict(status)
            tweet_dict = api.status_to_tweet_dict(status)
            u, created = User.objects.get_or_create(id=user_dict['id'],
                                                    name=user_dict['name'],
                                                    screen_name=user_dict['screen_name'],
                                                    profile_url=user_dict['profile_url'],
                                                    profile_image_url=user_dict['profile_image_url'],)
            t, created = Tweet.objects.get_or_create(id=tweet_dict['id'],
                                                    user=u,
                                                    text=tweet_dict['text'],
                                                    created_at=tweet_dict['created_at'],
                                                    url=tweet_dict['url'],)
            
            hashtag_list = api.status_to_hashtags(status)

            htags = []
            for hashtag in hashtag_list:
                h, created = Hashtag.objects.get_or_create(text=hashtag)
                h.save()
                htags.append(h)

            for h in htags:
                t.hashtags.add(h)

            users.append(u)
            tweets.append(t)

        for u in users:
            u.save()

        for t in tweets:
            t.save()




