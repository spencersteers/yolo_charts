from django.contrib import admin
from twitter.models import Hashtag, User, Tweet

admin.site.register(Hashtag)
admin.site.register(User)
admin.site.register(Tweet)