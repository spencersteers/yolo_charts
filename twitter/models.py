from django.db import models

# Create your models here.

""" Represents a twitter hastag """
class Hashtag(models.Model):
    text = models.CharField(max_length=140)

    def text_with_hash(self):
        return '#' + text
    
    def __unicode__(self):
        return self.text

""" Represents a twitter user """
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    my_id = models.AutoField()
    name = models.CharField(max_length=64)
    screen_name = models.CharField(max_length=64)
    profile_url = models.URLField()
    profile_avatar_url = models.URLField()
    hashtags = models.ManyToManyField(Hashtag, blank=True, null=True)

    def __unicode__(self):
        return self.screen_name

""" Represents a twitter tweet """
class Tweet(models.Model):
    id = models.IntegerField(primary_key=True)
    my_id = models.AutoField()
    user = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField()
    tweet_url = models.URLField()
    hashtags = models.ManyToManyField(Hashtag)

    def __unicode__(self):
        return self.text