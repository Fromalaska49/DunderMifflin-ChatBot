import datetime

from django.contrib import auth
from django.contrib.auth.views import logout, login
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from ChatBot import settings


class AutoLogout(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return
        try:
            if (datetime.datetime.now() - request.session['last_touch']).seconds > settings.SESSION_IDLE_TIMEOUT:
                auth.logout(request)
                del request.session['last_touch']
                return render(request, "admin/login.html")
        except KeyError:
            pass
        request.session['last_touch'] = datetime.datetime.now()
