from celery import shared_task


@shared_task
def go_listener():
    from slackclient import SlackClient
    import os
    import time
    import twitter
    from slappy.models import Tweets
    slack = SlackClient(os.environ.get('SLACKBOT_TOKEN'))
    bot_msg = 'Hello from Ahmed Go! :tada:'
    screen_name = 'FictionFone'
    api = twitter.Api(consumer_key=os.environ.get('CONKEY'), consumer_secret=os.environ.get(
        'CONSEC'), access_token_key=os.environ.get('ACCTOK'), access_token_secret=os.environ.get('ACCSEC'))
    if slack.rtm_connect():
        while True:
            events = slack.rtm_read()
            for event in events:
                if ('channel' in event and 'text' in event and event.get('type') == 'message'):
                    text = event['text']
                    if 'go' in text.lower() and bot_msg not in text:
                        statuses = api.GetUserTimeline(screen_name=screen_name)
                        if statuses:
                            for status in statuses:
                                if not Tweets.objects.filter(tw_id=status.id):
                                    Tweets.create_from_fetches(status)
