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
        intent_data = []

        # Get all intents
        intents = requests.get(API_URL + '/' + API_URL_TAIL, headers=API_HEADER)

        for intent in intents:
            templates = []
            intent_id = intent['id']
            intent_name = intent['name']

            intent_info = requests.get(API_URL + '/' + intent_id + '/' + API_URL_TAIL, headers=API_HEADER)
            user_says = intent_info['userSays']
            for statement in user_says:
                template = {'id': statement['id'], 'text': statement['data']['text']}
                templates.append(template)

            temp = {'id': intent_id,
                    'name': intent_name,
                    'templates': templates}
            intent_data.append(temp)

        return_data[MSG] = intent_data

        return HttpResponse(json.dumps(return_data), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        pass