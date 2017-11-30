from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
import json
import logging
import apiai

logger = logging.getLogger(__name__)

class ChatBotHandler(LoginRequiredMixin, ListView):
    #only works for admin atm
    #restricts chatbot usage to only logged in users

    login_url = 'login_handler'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        """ Standard post function. """
        ai = apiai.ApiAI(API_CLIENT_KEY)

        question = request.POST[QUESTION_TEXT]
        logger.info("Processing question: %s\n", question)

        request = ai.text_request()
        request.query = question
        response = json.loads(request.getresponse().read())

        return_data = {}
        return_data[ERROR] = False
        return_data[MSG] = response['result']['fulfillment']['speech']

        logger.info("Anwsering with: %s\n", return_data[MSG])

        return HttpResponse(json.dumps(return_data), content_type="application/json")

    def get(self, request):
        # type: (object) -> object
        """ Standard get function. """
        return render(request, "chat/chat.html")