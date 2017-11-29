from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
from ChatBot.views.chatbot_service.Intents import *
from textblob import TextBlob
import json
import logging

logger = logging.getLogger(__name__)

class ChatBotHandler(ListView):

    def post(self, request):
        """ Standard post function. """
        question = self.preprocess_text(request)
        return self.do_frequency_analysis(question)

    def get(self, request):
        """ Standard get function. """
        return render(request, "chat/chat.html")

    @staticmethod
    def preprocess_text(request):
        """ Prepares the user question for interpretation. """
        question = request.POST[QUESTION_TEXT]
        question = TextBlob(str(question))
        logger.info("Original request: %s\n", question)
        question = question.correct().lower()
        logger.info("Processed request: %s\n", question)
        return question

    @staticmethod
    def check_sentence_for_keywords(sentence, keywords):
        """ Returns a count of keywords in a sentence. """
        count = 0
        for word in sentence.words:
            if word in keywords:
                count += 1
        return count

    def do_frequency_analysis(self, question):
        """ Interprets user question to return an appropriate response. """
        return_data = {}
        return_data[ERROR] = False

        response = None
        max_count = 0

        for intent in intents:
            keywords = intent.get(KEYWORDS)
            count = self.check_sentence_for_keywords(question, keywords)
            if max_count < count:
                max_count = count
                response = intent.get(RESPONSE)

        if max_count == 0:
            logger.info('Could not find suitable response.')
            return_data[MSG] = UNKNOWN_REQUEST
            return HttpResponse(json.dumps(return_data), content_type="application/json")

        logger.info('Responding with: %s\n', response)

        return_data[MSG] = response
        return HttpResponse(json.dumps(return_data), content_type="application/json")