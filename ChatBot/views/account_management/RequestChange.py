from django.views.generic import ListView
from ChatBot.models import User
from django.http import HttpResponse
from django.http import Http404
from django.utils.crypto import get_random_string
from ChatBot.views.misc.Constants import *
from ChatBot.views.util.EmailUtil import send_pass_reset_email
from ChatBot.views.util.RegistrationUtil import validate_email
import json


# only handles password reset for now, but will handle requests for updating all information later
class RequestChange(ListView):

    def post(self, request):

        return_data = {}
        return_data[ERROR] = False
        return_data[MSG] = PASS_RESET_REQ_SUCCESS
        change_type = request.POST.get(CHANGE_TYPE)  # will also handle regular info updates later. Psswd only for now.
        email = request.POST.get(EMAIL)
        token = get_random_string()

        if change_type is None or change_type != PASSWORD:
            return_data[ERROR] = True
            return_data[MSG] = INCORRECT_PARAMETERS

        elif not validate_email(email):
            return_data[ERROR] = True
            return_data[MSG] = EMAIL_INVALID_ERROR

        elif User.objects.filter(username=email).exists():
            user = User.objects.get(username=email)
            user.pass_reset_token = token
            user.save()
            send_pass_reset_email(email, request.META[HTTP_HOST], token)

        return HttpResponse(json.dumps(return_data), content_type="application/json")

