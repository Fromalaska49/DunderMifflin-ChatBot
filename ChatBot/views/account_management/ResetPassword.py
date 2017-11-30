from django.views.generic import ListView
from ChatBot.models import User
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.util.RegistrationUtil import validate_password
from ChatBot.views.util.AuthenticationUtil import reset_login_attempts
from django.http import Http404
from ChatBot.views.misc.Constants import *
import json


class ResetPassword(ListView):

    def post(self, request):
        return_data = {}
        return_data[ERROR] = True
        password = request.POST.get(PASSWORD)
        password_conf = request.POST.get(CONFIRM_PASSWORD)
        val_object = validate_password(password)
        token = request.session.get(PASS_RESET_TOKEN)

        if token is None:
            raise Http404()

        elif password != password_conf:
            return_data[MSG] = PASS_MATCH_ERROR

        elif val_object[ERROR]:
            return_data = val_object

        else:
            user = User.objects.get(pass_reset_token=token)
            user.set_password(password)
            user.pass_reset_token = ''
            user.save()
            return_data[ERROR] = False
            return_data[MSG] = PASS_RESET_SUCCESS

        return HttpResponse(json.dumps(return_data), content_type="application/json")


    def get(self, request, token):
        # type: (object, object) -> object

        if token is None:
            raise Http404()

        if User.objects.filter(pass_reset_token=token).exists():
            request.session[PASS_RESET_TOKEN] = token
            return render(request, 'reset_password.html')

        else:
            raise Http404()
