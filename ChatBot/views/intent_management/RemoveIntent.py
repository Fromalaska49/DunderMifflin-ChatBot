from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
import json
import logging
import requests

logger = logging.getLogger(__name__)

class RemoveIntent(LoginRequiredMixin, ListView):
    def post(self, request):
        """ Standard post function. """
        return_data = {}
        return_data[ERROR] = False

        intent_id = request.POST[INTENT_ID]

        logger.debug("Attempting to delete intent: %s\n", intent_id)

        response = requests.delete(API_URL + '/' + intent_id + '/' + API_URL_TAIL, headers=API_HEADER)
        response_string = ''
        for line in response:
            response_string += line
        response_json = json.loads(response_string)
        return_data[MSG] = response_json['status']['errorType']

        # Log error
        if return_data[MSG] == 'Success':
            logger.info("Successfully deleted intent: %s\n", intent_id)
        else:
            logger.error("Failed to delete intent: %s, Error Message: %s\n", intent_id, return_data[MSG])

        return HttpResponse(json.dumps(return_data), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        pass

