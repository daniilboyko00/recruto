from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest, *args, **kwargs):
    name = request.GET.get('name')
    message = request.GET.get('message')
    context = {
        'name':name,
        'message':message
    }
    return HttpResponse(content=f'Hello {name}! {message} ')
