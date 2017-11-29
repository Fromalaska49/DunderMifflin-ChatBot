from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.chatbot_service.Intents import *
from textblob import TextBlob
import json
import logging
import apiai

logger = logging.getLogger(__name__)

class ChatBotHandler(ListView):

    def post(self, request):
        """ Standard post function. """
        ai = apiai.ApiAI(API_KEY)

        question = request.POST[QUESTION_TEXT]
        request = ai.text_request()
        request.query = question
        response = json.loads(request.getresponse().read())
        print(response)

        return_data = {}
        return_data[ERROR] = False
        return_data[MSG] = response['result']['fulfillment']['speech']

        return HttpResponse(json.dumps(return_data), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        return render(request, "chat/chat.html")