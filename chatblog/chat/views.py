from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


from chatterbot import ChatBot
from django.contrib.auth import authenticate, login
from .chat_adapters import Login_User
from chatterbot.conversation import Statement
import logging


bot = ChatBot('chatblog', read_only=False,
              
 
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[


        ],
        database_uri='sqlite:///database.sqlite3')

print('Type something to begin...')

# The following loop will execute each time the user enters input






userAdapter = Login_User(bot)

bot.logic_adapters.append(userAdapter)

print(bot.logic_adapters)

def index(request):
    return render(request, "chat/index.html")


def getResponse(request):
    userMessage = request.GET.get("userMessage")
    ChatBot = str(bot.get_response(userMessage))
    return HttpResponse(ChatBot)
