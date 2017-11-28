from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.http import Http404, HttpResponseRedirect


from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from ChatBot.views.util.EmailUtil import send_account_locked_email
from ChatBot.views.util.AuthenticationUtil import *
from ChatBot.views.misc.Constants import *
from django.utils.crypto import get_random_string
from django.utils import timezone
import json


class DeleteUser(DeleteView):

    @login_required
    def post(self, request):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise Http404
            # or return HttpResponse('404_url')

        # Get Request Handler
    def get(self, request):
        # Serve registration registration. give path relative to templates folder
        return render(request, "delete/delete_user.html")
