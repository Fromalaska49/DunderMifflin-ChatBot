from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
from ChatBot.views.chatbot_service.Intents import *
from textblob import TextBlob
import json
import logging

class ChatBotHandler(ListView):

    """
    Interprets user question to return an appropriate response.
    """
    def post(self, request):
        question = request.POST[QUESTION_TEXT]
        question = TextBlob(str(question))
        question = question.correct()
        return_data = {}
        return_data[ERROR] = False

        logging.debug('Processing question: %s\n', question)

        response = None
        max_count = 0

        for intent in intents:
            keywords = intent.get(KEYWORDS)
            count = self.check_sentence_for_keywords(question, keywords)
            if max_count < count:
                max_count = count
                response = intent.get(RESPONSE)

        if max_count == 0:
            logging.debug('Could not find suitable response.')
            return HttpResponse(json.dumps(UNKNOWN_REQUEST), content_type="application/json")

        logging.debug('Responding with: %s\n', response)

        return_data[MSG] = response
        return HttpResponse(json.dumps(return_data), content_type="application/json")

    """
    Standard get function.
    """
    def get(self, request):
        return render(request, "chat/chat.html")

    """
    Returns a count of keywords in a sentence.
    """
    def check_sentence_for_keywords(self, sentence, keywords):
        count = 0
        for word in sentence.words:
            if word.lower() in keywords:
                count += 1
        return count
