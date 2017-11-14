import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from ChatBot.views.misc.Constants import *
from ChatBot.views.state_handlers.chatbot_machine.LoginStateHandler import handle_login_state
from ChatBot.views.state_handlers.chatbot_machine.InitialStateHandler import handle_initial_state


class ChatBotHandler(ListView):

    def post(self, request):
        response_data = {}

        chatbot_state = request.session.get(CHATBOT_MACHINE_STATE)

        if chatbot_state == INITIAL_STATE:
            response_data = handle_initial_state(request)

        elif chatbot_state == LOGIN_STATE:
            response_data = handle_login_state(request)

        elif chatbot_state == ACCOUNT_RECOVERY_STATE:
            pass

        elif chatbot_state == INQUIRE_STATE:
            pass

        elif chatbot_state == INQUIRY_VERIFICATION_STATE:
            pass

        elif chatbot_state == AUTHENTICATION_STATE:
            pass

        elif chatbot_state == EMAIL_UPDATE_STATE:
            pass

        elif chatbot_state == NAME_UPDATE_STATE:
            pass

        elif chatbot_state == PASSWORD_UPDATE_STATE:
            pass

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    def get(self, request):
        request.session[LOGIN_MACHINE_STATE] = NULL_STATE       # Temporary
        request.session[CHATBOT_MACHINE_STATE] = INITIAL_STATE  # Temporary
        return render(request, "chatbot.html")
