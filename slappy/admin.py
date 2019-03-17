from django.contrib import admin
from slappy.models import Tweets
# Register your models here.


class TweetsAdmin(admin.ModelAdmin):
    list_display = ['tw_text', 'tw_date']

    def get_ordering(self, request):
        return [('-tw_date')]


admin.site.register(Tweets, TweetsAdmin)
