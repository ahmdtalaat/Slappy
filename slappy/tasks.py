from celery import shared_task


@shared_task
def go_listener():
    from slackclient import SlackClient
    import os
    import time
    slack = SlackClient(os.environ.get('SLACKBOT_TOKEN'))
    bot_msg = 'Hello from Ahmed Go! :tada:'
    if slack.rtm_connect():
        while True:
            events = slack.rtm_read()
            for event in events:
                if ('channel' in event and 'text' in event and event.get('type') == 'message'):
                    text = event['text']
                    channel = event['channel']
                    if 'go' in text.lower() and bot_msg not in text:
                        slack.api_call(
                            'chat.postMessage',
                            channel=channel,
                            text=bot_msg,
                            as_user='true:')
