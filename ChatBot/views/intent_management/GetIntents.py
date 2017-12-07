from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
import json
import logging
import requests

logger = logging.getLogger(__name__)


class GetIntents(LoginRequiredMixin, ListView):
    def post(self, request):
        """ Standard post function. """
        response = ''

        # Get all intents
        intents = requests.get(API_URL + '/' + API_URL_TAIL, headers=API_HEADER)
        for intent in intents:
            response += intent

        return HttpResponse(json.dumps(response), content_type="application/json")

    def get(self, request):
        """ Standard get function. """
        if request.user.is_authenticated and request.user.is_staff:
            return render(request, 'admin/intents.html')
        else:
            pass