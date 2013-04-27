from django.db import models

# Create your models here.

class Hashtag(models.Model):
    """Represents a twitter hastag."""
    
    text = models.CharField(max_length=140)

    def use_count(self):
        return self.tweet_set.all().count()

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

    def get_hashtags_count(self):
        """Returns the amount of times a user tweeted each hashtag"""
        tweets = self.tweet_set.all()
        values = tweets.values("hashtags", "hashtags__text")
        aggregate = values.annotate(models.Count("id")).order_by()
        
        h_list = []
        for info in aggregate:
            h = Hashtag.objects.get(pk=info['hashtags'])
            h_list.append({h: info['id__count']})
        return h_list

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