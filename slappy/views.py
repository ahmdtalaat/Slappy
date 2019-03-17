from django.shortcuts import render


def home(request):
    return render(request, "slappy/slappy.html")


# def fetch(request):
#     from slackclient import SlackClient
#     import os
#     import time
#     state = True
#     token = os.environ.get('SLACKBOT_TOKEN')
#     slack = SlackClient(token)
#     bot = 'Hello from Ahmed Go! :tada:'
#     if slack.rtm_connect():
#         while state:
#             events = slack.rtm_read()
#             for event in events:
#                 if ('channel' in event and 'text' in event and event.get('type') == 'message'):
#                     text = event['text']
#                     channel = event['channel']
#                     if 'go' in text.lower() and bot not in text:
#                         slack.api_call(
#                             'chat.postMessage',
#                             channel=channel,
#                             text=bot,
#                             as_user='true:'

#                         )
