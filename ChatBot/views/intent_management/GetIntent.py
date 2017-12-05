from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
import json
import logging
import requests

logger = logging.getLogger(__name__)


class GetIntent(LoginRequiredMixin, ListView):
    def post(self, request):
        """ Standard post function. """
        return_data = {}
        return_data[ERROR] = False
        intent_data = ''

        # Get all intents
        intents = requests.get(API_URL + '/' + API_URL_TAIL, headers=API_HEADER)
        for intent in intents:
            intent_data += intent
        intent_json = json.loads(intent_data)
        intent_output = []
        for intent in intent_json:
            templates = []
            if 'id' in intent and 'name' in intent:
                intent_id = intent['id']
                intent_name = intent['name']
            else:
                continue

            intent_info = requests.get(API_URL + '/' + intent_id + '/' + API_URL_TAIL, headers=API_HEADER)
            intent_info_data = ''
            for line in intent_info:
                intent_info_data += line
            intent_info_json = json.loads(intent_info_data)
            if 'responses' in intent_info_json and 'messages' in intent_info_json['responses'][0]:
                response = intent_info_json['responses'][0]['messages'][0]['speech']
                user_says = intent_info_json['userSays']
                for statement in user_says:
                    if(len(statement['data']) > 0):
                        template = {'id': statement['id'], 'text': statement['data'][0]['text']}
                        templates.append(template)
            else:
                response = ''
            temp = {'id': intent_id,
                    'name': intent_name,
                    'response': response,
                    'templates': templates}
            intent_output.append(temp)

        return_data[MSG] = intent_data

        return HttpResponse(json.dumps(intent_output), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        if request.user.is_authenticated and request.user.is_staff:
            return render(request, 'admin/intents.html')
        else:
            pass