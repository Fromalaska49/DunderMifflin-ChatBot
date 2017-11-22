import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView



class ChatBotHandler(ListView):

    def post(self, request):
        pass

    def get(self, request):
        pass
