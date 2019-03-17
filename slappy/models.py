from django.db import models
from datetime import datetime


class Tweets(models.Model):
    tw_id = models.CharField(max_length=255)
    tw_username = models.CharField(max_length=255)
    tw_lang = models.CharField(max_length=255)
    tw_date = models.DateTimeField()
    tw_text = models.TextField()

    @staticmethod
    def create_from_fetches(data):
        tw_id = data.id
        tw_username = data.user.screen_name
        tw_lang = data.lang
        tw_date = datetime.fromtimestamp(data.created_at_in_seconds)
        tw_text = data.text

        return Tweets.objects.create(tw_id=tw_id, tw_username=tw_username, tw_lang=tw_lang, tw_date=tw_date, tw_text=tw_text)

    def __str__(self):
        return self.tw_text
