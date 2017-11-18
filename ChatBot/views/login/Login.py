from django.views.generic import ListView
from ChatBot.views.misc.Constants import *
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.models import User
from ChatBot.views.util.EmailUtil import send_account_locked_email
from ChatBot.views.util.AuthenticationUtil import login_attempts_exceeded, increment_login_attempts, reset_login_attempts
import json


class Login(ListView):

    def post(self, request):
        email = request.POST[EMAIL]
        password = request.POST[PASSWORD]
        return_data = {}
        return_data[ERROR] = True
        user = authenticate(request, username=email, password=password)

        if login_attempts_exceeded(request.session, email):
            return_data[MSG] = ATTEMPTS_EXCEEDED

        elif user is None:
            increment_login_attempts(request.session, email)
            return_data[MSG] = COMBINATION_INVALID

            if login_attempts_exceeded(request.session, email):

                if User.objects.filter(username=email).exists():
                    user = User.objects.get(username=email)
                    user.is_locked = True
                    user.save()
                    send_account_locked_email(email)

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

