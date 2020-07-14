from random import randint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, Http404

from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse('Hello World')
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    """
    Fetches all the tweets
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": randint(0, 199)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript
    return json data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
        # data["image_path"] = obj.image.url
    except:
        data['message'] = "Not found"
        status = 404
        # raise Http404
    
    # return HttpResponse(f'<h1>Hello{tweet_id} - {obj.content}</h1>')
    return JsonResponse(data, status=status)