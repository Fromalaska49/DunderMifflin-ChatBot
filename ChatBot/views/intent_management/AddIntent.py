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
        return_data = {}
        return_data[ERROR] = False

        intent_name = request.POST[INTENT_NAME] #Returns str
        intent_user_says = request.POST[INTENT_USER_SAYS].split('\n') #Returns str
        intent_response = request.POST[INTENT_RESPONSE] #str

        logger.debug("Attempting to create intent: %s\n", intent_name)

        # Prepare the JSON body
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
        body += '],' \
                '"webhookForSlotFilling": false,' \
                '"webhookUsed": false}'

        response = requests.post(API_URL + '/' + API_URL_TAIL, body, headers=API_HEADER)
        response_string = ''
        for line in response:
            response_string += line
        response_json = json.loads(response_string)
        return_data[MSG] = response_json['status']['errorType']

        if return_data[MSG] == 'Success':
            logger.info("Successfully created intent: %s\n", intent_name)
        else:
            logger.error("Failed to create intent: %s, Error Message: %s\n", intent_name, return_data[MSG])

        return HttpResponse(json.dumps(return_data), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        if request.user.is_authenticated and request.user.is_staff:
            return render(request, 'admin/add_intent.html')