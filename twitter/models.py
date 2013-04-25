from django.db import models

# Create your models here.

class Hashtag(models.Model):
    """Represents a twitter hastag."""
    
    text = models.CharField(max_length=140)

    """Appends '#' to the hashtag text"""
    def text_with_hashtag(self):
        return '#' + self.text

    def __unicode__(self):
        return self.text

class User(models.Model):
    """Represents a twitter user."""
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    screen_name = models.CharField(max_length=64)
    profile_url = models.URLField()
    profile_image_url = models.URLField()
    hashtags = models.ManyToManyField(Hashtag, blank=True, null=True)

    def __unicode__(self):
        return self.screen_name

class Tweet(models.Model):
    """Represents a twitter tweet"""
    
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    text = models.TextField()
    created_at = models.DateTimeField()
    url = models.URLField()
    hashtags = models.ManyToManyField(Hashtag, blank=True, null=True)

    def __unicode__(self):
        return self.text