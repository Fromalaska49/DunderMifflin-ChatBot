from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
import json
import logging
import apiai

logger = logging.getLogger(__name__)

class AddIntent(LoginRequiredMixin, ListView):
    def post(self, request):
        """ Standard post function. """
        pass

    def get(self, request):
        """ Standard get function. """
        pass