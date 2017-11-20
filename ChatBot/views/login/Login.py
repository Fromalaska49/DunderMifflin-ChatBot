from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.util.EmailUtil import send_account_locked_email
from ChatBot.views.util.AuthenticationUtil import *
from ChatBot.views.misc.Constants import *
from django.utils.crypto import get_random_string
import json


class Login(ListView):

    def post(self, request):
        email = request.POST[EMAIL]
        password = request.POST[PASSWORD]
        return_data = {}
        return_data[ERROR] = True
        user = authenticate(request, username=email, password=password)

        if account_is_locked(email):
            return_data[MSG] = ACCOUNT_IS_LOCKED

        elif user is None:
            increment_login_attempts(request.session, email)
            return_data[MSG] = COMBINATION_INVALID

            if login_attempts_exceeded(request.session, email):
                # lock account if it exists. Otherwise, pretend to lock to not give away DB info
                if user_exists(email):
                    token = get_random_string()
                    user = User.objects.get(username=email)
                    user.is_locked = True
                    user.acct_locked_token = token
                    user.save()
                    send_account_locked_email(email, request.META[HTTP_HOST], token)

                return_data[MSG] = ATTEMPTS_EXCEEDED

        else:
            reset_login_attempts(request.session, email)
            return_data[ERROR] = False

            if user.is_active:
                login(request, user)
                return_data[MSG] = LOGIN_SUCCESS

            else:
                return_data[RET_CODE] = ACCOUNT_INACTIVE

        return HttpResponse(json.dumps(return_data), content_type="application/json")

        # Get Request Handler
    def get(self, request):
        # Serve registration registration. give path relative to templates folder
        return render(request, "login.html")

