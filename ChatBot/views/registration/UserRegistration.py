from django.views.generic import ListView
from django.shortcuts import render
from ChatBot.views.misc.Constants import *
from ChatBot.views.util.EmailUtil import send_welcome_email, send_admin_verification_email
from ChatBot.views.util.RegistrationUtil import validate_reg_form, create_admin_user, create_cb_user
from django.utils.crypto import get_random_string
from django.http import HttpResponse
import json


# Class-based view (Django calls handlers views)
class UserRegistration(ListView):

    # Post Request Handler
    def post(self, request):
        response_data = {}
        response_data[ERROR] = True
        fname = request.POST.get(FIRST_NAME)
        lname = request.POST.get(LAST_NAME)
        email = request.POST[EMAIL]
        password = request.POST[PASSWORD]
        password_conf = request.POST[CONFIRM_PASSWORD]

        val_object = validate_reg_form(email, password, password_conf, fname, lname)

        if val_object[ERROR]:
            response_data = val_object

        else:
            token = get_random_string()
            acct_type = request.POST.get(ACCOUNT_TYPE)

            if acct_type is None or acct_type != ADMIN:
                create_cb_user(fname, lname, email, password, token)
                send_welcome_email(email, request.META.get(HTTP_HOST, LOCALHOST), token)
                response_data[ERROR] = False
                response_data[MSG] = CREATED_USER

            else:
                create_admin_user(fname, lname, email, password, token)
                send_admin_verification_email(fname, lname, email, request.META.get(HTTP_HOST, LOCALHOST), token)
                response_data[ERROR] = False
                response_data[MSG] = CREATED_ADMIN

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # Get Request Handler
    def get(self, request):

        # Serve registration registration. give path relative to templates folder
        return render(request, "registration/registration.html")

