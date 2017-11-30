from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
import json
import logging
import apiai
import requests

logger = logging.getLogger(__name__)

class AddIntent(LoginRequiredMixin, ListView):

    def post(self, request):
        """ Standard post function. """
        intent_name = request.POST[INTENT_NAME]
        intent_user_says = request.POST[INTENT_USER_SAYS]
        intent_response = request.POST[INTENT_RESPONSE]

        body = '"{contexts": [],' \
               '"events": [],' \
               '"fallbackIntent": false,' \
               '"name": "' + intent_name + '",' \
               '"priority": 50000,' \
               '"responses": [{"messages": '\
               '[{"speech": "' + intent_response + '",' \
               '"type": 0}],' \
               '"resetContexts": false}],'

        templates = '"templates": ['

        length = len(intent_user_says)
        for i in range(0, length):
            if i != length - 1:
                templates += '"' + intent_user_says[i] + '",'
            else:
                templates += '"' + intent_user_says[i] + '"'

        body += templates
        body += '],'
        body += '"webhookForSlotFilling": false,' \
                '"webhookUsed": false}'


    def get(self, request):
        """ Standard get function. """
        pass