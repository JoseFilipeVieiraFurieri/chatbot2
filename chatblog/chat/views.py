from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import format_html

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatblog', read_only=False,
              
 
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[
          {
          "import_path": "chatterbot.logic.BestMatch",
          "default_response": "Sorry, i have no response to that answer",
          "maximum_similarity_threshold": 0.95
          }
        ],
        database_uri='sqlite:///database.sqlite3')


corpus = ChatterBotCorpusTrainer(bot)
corpus.train('chatterbot.corpus.english')



def index(request):
    return render(request, "chat/index.html")


def getResponse(request):
    userMessage = request.GET.get("userMessage")
    ChatBot = str(bot.get_response(userMessage))
    return HttpResponse(ChatBot)
