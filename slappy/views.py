from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from slappy.models import Tweets
from slappy.serializers import TweetSerializer
from rest_framework import viewsets


def home(request):
    tweets = Tweets.objects.all()
    context = {
        'tweets': tweets
    }
    return render(request, "slappy/slappy.html", context)


@csrf_exempt
def get_data(request):
    data = Tweets.objects.all()
    if request.method == "GET":
        serializer = TweetSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
