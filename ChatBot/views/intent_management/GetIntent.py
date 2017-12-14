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
        response = []
        templates = []

        intent_id = request.POST[INTENT_ID]
        intent_name = 'hello'

        intent = requests.get(API_URL + '/' + intent_id + '/' + API_URL_TAIL, headers=API_HEADER)
        intent_info = ''

        for line in intent:
            intent_info += line
        intent_info_json = json.loads(intent_info)

        if 'responses' in intent_info_json and 'messages' in intent_info_json['responses'][0]:
            res = intent_info_json['responses'][0]['messages'][0]['speech']
            user_says = intent_info_json['userSays']
            for statement in user_says:
                if len(statement['data']) > 0:
                    template = {'id': statement['id'], 'text': statement['data'][0]['text']}
                    templates.append(template)
        else:
            res = ''

        temp = {'id': intent_id,
                'name': intent_name,
                'response': res,
                'templates': templates}
        response.append(temp)

        return HttpResponse(json.dumps(response), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        if request.user.is_authenticated and request.user.is_staff:
            return render(request, 'admin/intents.html')
        else:
            pass