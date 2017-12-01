from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
import json
import logging
import requests

logger = logging.getLogger(__name__)

class AddIntent(LoginRequiredMixin, ListView):
    def post(self, request):
        """ Standard post function. """
        return_data = {}
        return_data[ERROR] = False

        intent_id = None
        intent_name = request.POST[INTENT_NAME]

        logger.debug("Attempting to delete intent: %s\n", intent_name)

        # Get all intents
        intents = requests.get(API_URL + '/' + API_URL_TAIL, headers=API_HEADER)

        # Get the intent id for the input intent name
        for intent in intents:
            if intent['name'] == intent_name:
                intent_id = intent['id']
                break

        # Delete the intent if the input intent name is valid
        if intent_id is None:
            logger.error("Intent does not exist: $s\n", intent_name)
            return_data[ERROR] = True
        else:
            response = requests.delete(API_URL + '/' + intent_id + '/' + API_URL_TAIL)
            return_data[MSG] = response['status']['errorType']

        # Log error
        if return_data[MSG] == 'Success':
            logger.info("Successfully deleted intent: %s\n", intent_name)
        else:
            logger.error("Failed to delete intent: %s, Error Message: %s\n", intent_name, return_data[MSG])

        return HttpResponse(json.dumps(return_data), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        pass

