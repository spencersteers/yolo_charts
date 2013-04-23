from django.contrib import admin
from twitter.models import Hashtag, User, Tweet

class HashtagAdmin(admin.ModelAdmin):
    list_display = (text_with_tag)
    list_display_links = (text_with_tag)

    fields = ('text')

class UserHashtagsInline(admin.TabularInline):
    model = User.hashtags.through

class UserAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'profile_url',)
    list_display_links = ('screen_name',)

    fields = (('screen_name', 'name',), 'profile_url', 'profile_avatar_url',)
    inlines = [UserHashtagsInline,]

    exclude = ('hashtags',)

class TweetInline(admin.StackedInline)
    date_hierarchy = 'date'
    fields = ('tweet_url', 'hashtags', ('tweet',),)


admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(User, UserAdmin)