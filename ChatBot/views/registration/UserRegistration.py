from django.views.generic import ListView
from django.shortcuts import render
from ChatBot.models import User
from ChatBot.views.misc.Constants import *
from ChatBot.views.util.EmailUtil import send_welcome_email
from ChatBot.views.util.RegistrationUtil import validate_credentials
from django.http import HttpResponse
import json


# Class-based view (Django calls handlers views)
class UserRegistration(ListView):

    # Post Request Handler
    def post(self, request):
        response_data = {}
        email = request.POST[EMAIL]
        password = request.POST[PASSWORD]
        password_conf = request.POST[CONFIRM_PASSWORD]

        password_val = validate_credentials(email, password, password_conf)

        if password_val[ERROR]:
            response_data = password_val

        else:
            user = User.objects.create_user(
                                            first_name=request.POST[FIRST_NAME],
                                            last_name=request.POST[LAST_NAME],
                                            email=email,
                                            password=password,
                                            username=email              #Django default user table requires username
                                            )

            user.save()
            send_welcome_email(email)
            response_data[ERROR] = False
            response_data[MSG] = ACCOUNT_CREATED_USER

        return HttpResponse(json.dumps(response_data), content_type="application/json")


    #Get Request Handler
    def get(self, request):

        # Serve registration registration. give path relative to templates folder
        return render(request, "registration/registration.html")

