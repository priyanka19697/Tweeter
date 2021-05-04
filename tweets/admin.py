from django.contrib import admin
from .models import Tweet
# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']

    # def __str__(self):
    #     return self.content

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)
