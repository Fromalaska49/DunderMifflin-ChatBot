from django.views.generic import ListView
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
from ChatBot.views.util.EmailUtil import send_welcome_email, send_admin_verification_email
from ChatBot.views.util.RegistrationUtil import validate_reg_form, create_admin_user, create_cb_user
from django.utils.crypto import get_random_string
from django.http import HttpResponse
import json


# Class-based view (Django calls handlers views)
class Forgot(ListView):

    # Post Request Handler
    def post(self, request):

        return render(request, "forgot.html")
    
    # Get Request Handler
    def get(self, request):

        return render(request, "forgot.html")

