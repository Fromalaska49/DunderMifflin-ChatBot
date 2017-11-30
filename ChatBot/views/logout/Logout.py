from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ChatBot.views.util.EmailUtil import send_account_locked_email
from ChatBot.views.util.AuthenticationUtil import *
from ChatBot.views.misc.Constants import *
from django.utils.crypto import get_random_string
from django.utils import timezone
import json


class Login(ListView):
    def post(self, request):
        
        logout(user)

        # Get Request Handler

    def get(self, request):
        # Serve registration registration. give path relative to templates folder
        logout(user)
        return render(request, "admin/logout.html")
