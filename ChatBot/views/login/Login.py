from __future__ import print_function
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from ChatBot.views.util.EmailUtil import send_account_locked_email
from ChatBot.views.util.AuthenticationUtil import *
from ChatBot.views.misc.Constants import *
from django.utils.crypto import get_random_string
from django.utils import timezone
import json


class Login(ListView):
    def post(self, request):
        email = request.POST[EMAIL]
        password = request.POST[PASSWORD]
        return_data = {}
        return_data[ERROR] = True
        return_data[ACCOUNT_TYPE] = USER
        user = authenticate(request, username=email, password=password)

        if account_is_locked(email):
            return_data[MSG] = ATTEMPTS_EXCEEDED

        elif user is None:
            increment_login_attempts(request.session, email)
            return_data[MSG] = COMBINATION_INVALID

            if login_attempts_exceeded(request.session, email):
                # lock account if it exists and is active. Otherwise, pretend to lock to not give away DB info
                if user_exists(email):
                    user = User.objects.get(username=email)
                    # lock account at DB level only if account is active
                    if user.is_active:
                        token = get_random_string()
                        user.is_locked = True
                        user.acct_locked_token = token
                        user.acct_locked_token_stamp = timezone.now()
                        user.save()
                        send_account_locked_email(email, request.META[HTTP_HOST], token)

                return_data[MSG] = ATTEMPTS_EXCEEDED
        else:
            reset_login_attempts(request.session, email)

            if account_is_active(email):
                return_data[ERROR] = False
                login(request, user)
                return_data[MSG] = LOGIN_SUCCESS

                if user.is_staff:
                    return_data[ACCOUNT_TYPE] = ADMIN

                redirect_to = reverse("chatbot_handler")
                '''
                # redirect should be handled by JS on successful login
                return HttpResponseRedirect(redirect_to)
                '''

            else:
                return_data[ERROR] = True
                return_data[MSG] = ACCOUNT_NOT_VERIFIED
        return HttpResponse(json.dumps(return_data), content_type="application/json")

    def get(self, request):
        if request.user.is_authenticated:

            if request.user.is_staff:
                return HttpResponseRedirect("/admin")

            return HttpResponseRedirect("/chatbot")
        return render(request, "admin/login.html")
