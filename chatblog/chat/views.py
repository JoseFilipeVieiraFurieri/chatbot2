from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from django.contrib.auth import authenticate, login


ChatBot('chatblog', read_only=False, 
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[

])


def index(request):
    return render(request, "chat/index.html")

def getResponse(request):
    UserMessage = request.GET.get('userMessage')
    return HttpResponse(UserMessage)

def authenticate(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return HttpResponse('invalid Login')


