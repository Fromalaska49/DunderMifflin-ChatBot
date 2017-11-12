from ChatBot.views.authentication.Login import login
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.ChatBotStates import *
from ChatBot.views.misc.GlobalDictKeys import CHATBOT_MACHINE_STATE
from ChatBot.views.authentication.Authentication import LOGIN_MACHINE_STATE, NULL_STATE
import json

class ChatBotHandler(ListView):

    def post(self, request):
        response_data = {}
        chatbot_state = request.POST.get(CHATBOT_MACHINE_STATE)

        if chatbot_state == INITIAL_AUTH_STATE:
            response_data = login(request)
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif chatbot_state == LOGGED_IN_AUTH_STATE:
            pass
        elif chatbot_state == AUTHENTICATED_INPUT_STATE:
            pass
        elif chatbot_state == ANSWER_VERIFICATION_STATE:
            pass

    def get(self, request):
        request.session[LOGIN_MACHINE_STATE] = NULL_STATE
        return render(request, "chatbot.html")
